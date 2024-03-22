using System.Collections;
using System.Security.Cryptography;
using MathNet.Numerics;
using MathNet.Numerics.Distributions;
using MathNet.Numerics.LinearAlgebra;
using MathNet.Numerics.LinearAlgebra.Factorization;
using MathNet.Numerics.Statistics;

Console.WriteLine("Hello, World!");

System.Console.WriteLine();

System.Console.WriteLine("--- Task 1:");

//Task 1
//1. Creat Arrays
//aI. ArrayList
ArrayList list_ArrayList = []; //hoesntly no idea how to use this (i never used it).

//or
//aII. List
List<double> list_DoubleList = []; //list, easy to work with with no hard limitations and has ready to use methods. can hold other types of arrays/lists.

//or
//aIII. Vector (Random Length)
Vector<double> vector_DoubleVector = Vector<double>.Build.Random(RandomNumberGenerator.GetInt32(3,9)); //vector, (psuedo-)random elements, (psuedo-)random length (length range: 3~9).

//b. 2D Matrix
Matrix<double> matrix_DoubleMatrix = Matrix<double>.Build.Dense(3,4); //matrix, 3rows x 4columns, dense as in same elements for all coordinations (default = 0).

//cI. 3D Matrix
Matrix<double>[] matrix_DoubleMatrixArray = new Matrix<double>[2]; //an array that holds type of Matrix<double>, size is 2 here.

Matrix<double> matrix2DBuilder_DoubleMatrix = Matrix<double>.Build.Dense(3,4,1); //matrix with "double" element type, 3rows x 4columns, dense as in same elements for all coordinations (element=1)

for (int i = 0; i < 2; i++)
{

    matrix_DoubleMatrixArray[i] = matrix2DBuilder_DoubleMatrix; //initializing our array with repeated matrices.
    
}

//OR
//cII. 3D Array
double[][][] array3D_DoubleArray3D = new double[2][][]; //could use a literal 3 dimensional array instead of matrix.

double[][] array2DBuilder_DoubleArray2D = [[1,1,1,1],[1,1,1,1],[1,1,1,1]]; //represents a 3x4 matrix with 1s as element.

for (int i = 0; i < 2; i++)
{

    array3D_DoubleArray3D[i] = array2DBuilder_DoubleArray2D; //initializing our 3d array with repeated 2d arrays.

}

//2. Inspection
//2a. Dimensions //self explanatory
System.Console.WriteLine($"2 Lists: {list_ArrayList.Count} & {list_DoubleList.Count} elements (has no elements; will throw exception while indexing)");

System.Console.WriteLine($"Vector:      {vector_DoubleVector.Count} elements ((psuedo-)random length ranging 3~9 with (psuedo-)randomized elements; will use this as 1D array)");

System.Console.WriteLine($"2D Matrix:   {matrix_DoubleMatrix.RowCount}x{matrix_DoubleMatrix.ColumnCount} | {matrix_DoubleMatrix.RowCount} rows & {matrix_DoubleMatrix.ColumnCount} columns");

System.Console.WriteLine($"3D Matrix: {matrix_DoubleMatrixArray.Length}x{matrix_DoubleMatrixArray[0].RowCount}x{matrix_DoubleMatrix.ColumnCount} | {matrix_DoubleMatrixArray.Length} matrices, {matrix_DoubleMatrixArray[0].RowCount} rows & {matrix_DoubleMatrixArray[0].ColumnCount} columns each");

System.Console.WriteLine($"3D Array:  {array3D_DoubleArray3D.Length}x{array3D_DoubleArray3D[0].Length}x{array3D_DoubleArray3D[0][0].Length} | {array3D_DoubleArray3D.Length} arrays, {array3D_DoubleArray3D[0].Length} rows & {array3D_DoubleArray3D[0][0].Length} columns each");

//END OF TASK 1 ----------------------------

//Task 2
//1. Indexing //self explanatory
//a. vector index 
System.Console.WriteLine();

System.Console.WriteLine("--- Task 2:");

System.Console.WriteLine($"value index[2] in our vector: {vector_DoubleVector[2]}");

//b. matrix index
System.Console.WriteLine($"value Of index[2,3] in 2D matrix: {matrix_DoubleMatrix[2,3]}");

//2. Slicing
//2d matrix upper left
Matrix<double> slicedMatrix_DoubleMatrix = matrix_DoubleMatrix.SubMatrix(0,2,0,2); //(1,2,3,4) -> 1=index of row we to cut, 2=how many rows to cut, 3=index of columns to cut, 4=how many columns to cut

System.Console.WriteLine($"Sub Matrix:   {slicedMatrix_DoubleMatrix.RowCount}x{slicedMatrix_DoubleMatrix.ColumnCount} | {slicedMatrix_DoubleMatrix.RowCount} rows & {slicedMatrix_DoubleMatrix.ColumnCount} columns");

//3. Iterating //self explanatory
int matrix_Int = 1;

int row_Int = 1;

System.Console.WriteLine();

System.Console.WriteLine("Matrices in our 3d array:");

System.Console.WriteLine();

foreach (Matrix<double> matrix in matrix_DoubleMatrixArray)
{

    System.Console.WriteLine($"   Matrix {matrix_Int}");

    matrix_Int++;

    System.Console.WriteLine(matrix.ToString());
    
}

//END OF TASK 2 ----------------------------

System.Console.WriteLine();

System.Console.WriteLine("Task 3:");
//Task 3
//1. Arithmetic //self explanatory
{

    System.Console.WriteLine("--- Task 3:");

    //a. addition
    System.Console.WriteLine("Addition: every element +5");

    Matrix<double> aMatrix_DoubleMatrix = matrix_DoubleMatrix.Add(5);

    System.Console.WriteLine(aMatrix_DoubleMatrix.ToString());

    //b. subtraction
    System.Console.WriteLine("Subtraction: every element -2");

    Matrix<double> bMatrix_DoubleMatrix = aMatrix_DoubleMatrix.Subtract(2);

    System.Console.WriteLine(bMatrix_DoubleMatrix.ToString());

    //c. nultiplication
    System.Console.WriteLine("Miltiplication: every element x5");

    Matrix<double> cMatrix_DoubleMatrix = bMatrix_DoubleMatrix.Multiply(5); //left or right does not matter here

    System.Console.WriteLine(cMatrix_DoubleMatrix.ToString());

    //d. division
    System.Console.WriteLine("Division: every element devided by 3");

    Matrix<double> dMatrix_DoubleMatrix = cMatrix_DoubleMatrix.Divide(3); //same for here

    System.Console.WriteLine(dMatrix_DoubleMatrix.ToString());

}

System.Console.WriteLine();

//2. Broadcast
{

    System.Console.WriteLine("Broadcast:");

    Vector<double> initialVector_DoubleVector = Vector<double>.Build.Dense(3,i=>3*i-2); //(psuedo-)random vector, where elements are equal to 3xindex-2

    System.Console.WriteLine("Vector:");

    System.Console.WriteLine(initialVector_DoubleVector.ToString());

    Matrix<double> destination_DoubleMatrix = Matrix<double>.Build.DenseOfMatrix(matrix_DoubleMatrix); //duplicating out first matrix which is all zero

    System.Console.WriteLine("Matrix:");

    System.Console.WriteLine(destination_DoubleMatrix.ToString());

    System.Console.WriteLine("Broadcasting:");

    for (int i = 0; i < destination_DoubleMatrix.ColumnCount; i++)
    {

        destination_DoubleMatrix.SetColumn(i,destination_DoubleMatrix.Column(i).Add(initialVector_DoubleVector)); // each column is set to vector+column
        
    }

    System.Console.WriteLine(destination_DoubleMatrix.ToString());

}

//3. Reshape & Flatten
{    

    Matrix<double> reshaped_DoubleMatrix = Matrix<double>.Build.DenseOfMatrix(matrix_DoubleMatrixArray[0]); //copied the first matrix of the array

    System.Console.WriteLine("Reshaped:");
    
    System.Console.WriteLine(reshaped_DoubleMatrix.ToString());

    Matrix<double> flatten_DoubleMatrix = Matrix<double>.Build.DenseOfRowVectors(reshaped_DoubleMatrix.Row(1)); //copied the first row of the reshaped matrix

    System.Console.WriteLine("Flattened:");

    System.Console.WriteLine(flatten_DoubleMatrix.ToString());

}

//END OF TASK 3 ----------------------------

//Task 4
{

    System.Console.WriteLine("--- Task 4:");

    //1. Dot Multiplication    
    Matrix<double> first_DoubleMatrix = Matrix<double>.Build.Dense(3,3,(i,j)=>1+3/5*j-i+RandomNumberGenerator.GetInt32(1,3)); //(psuedo-)random matrix 1

    Matrix<double> second_DoubleMatrix = Matrix<double>.Build.Dense(3,3,(i,j)=>2/5*j-i+RandomNumberGenerator.GetInt32(1,3)); //(psuedo-)random matrix 2

    System.Console.WriteLine("first matrix:");

    System.Console.WriteLine(first_DoubleMatrix.ToString());

    System.Console.WriteLine("second matrix:");

    System.Console.WriteLine(second_DoubleMatrix.ToString());

    Matrix<double> multiplier_DoubleMatrix = Matrix<double>.Build.DenseOfMatrix(first_DoubleMatrix.Multiply(second_DoubleMatrix)); //new matrix set to multiplicaton of the two (psuedo-)random matrices

    System.Console.WriteLine("multiplication:");

    System.Console.WriteLine(multiplier_DoubleMatrix.ToString());

    //2. Determinant & Inverse
    System.Console.WriteLine("determinant:");

    System.Console.WriteLine(multiplier_DoubleMatrix.Determinant()); //determinant of the resulting matrix

    System.Console.WriteLine("inverse:"); 

    System.Console.WriteLine(multiplier_DoubleMatrix.Inverse().ToString()); //inverse of the resulting matrix

    //3. Eigen Values & Vectors

    Evd<double> eigenCalculation_DoubleEvd = first_DoubleMatrix.Evd(); //setting the eigen value

    Matrix<double> eigenVectors_DoubleMatrix = eigenCalculation_DoubleEvd.EigenVectors; //extracting the vectors to a matrix

    System.Console.Write("Eigen Vectors: ");

    System.Console.WriteLine(eigenVectors_DoubleMatrix.ToString());

    Vector<System.Numerics.Complex> eigenValues_DoubleVector  = eigenCalculation_DoubleEvd.EigenValues; // extracting complex values to a vector

    System.Console.Write("Eigen Values: ");

    System.Console.WriteLine(eigenValues_DoubleVector.ToString());

}

//END OF TASK 4 ----------------------------

//Task 5
{

    //1. Descriptive //self explanatory

    System.Console.WriteLine("---Task 5\nDescription:");

    Vector<double> initial_DoubleVector = Vector<double>.Build.Dense(3,(i)=>3*i+RandomNumberGenerator.GetInt32(1,7)+2.5); //(psuedo-)random vector (data) 1

    Vector<double> destination_DoubleVector = Vector<double>.Build.Dense(3,(i)=>2*i+0.5*RandomNumberGenerator.GetInt32(1,7)-2); //(psuedo-)random vector (data) 2

    System.Console.Write("vector: ");

    System.Console.WriteLine(initial_DoubleVector.ToString());

    System.Console.Write("mean: ");

    System.Console.WriteLine(initial_DoubleVector.Mean());

    System.Console.Write("variance: ");

    System.Console.WriteLine(initial_DoubleVector.Variance());

    System.Console.Write("median: ");

    System.Console.WriteLine(initial_DoubleVector.Median());

    System.Console.Write("standard deviation: ");

    System.Console.WriteLine(initial_DoubleVector.StandardDeviation());

    //2. Correlation //self explanatory

    System.Console.WriteLine();

    System.Console.WriteLine("--Correlation:");

    System.Console.Write("vector 1: ");

    System.Console.WriteLine(initial_DoubleVector.ToString());

    System.Console.Write("vector 2: ");

    System.Console.WriteLine(destination_DoubleVector.ToString());

    //this section is related to coding the formula to calculate correlation based on a yt video (seems like it uses Pearson Coefficient)

    int numberOfElements_Double = initial_DoubleVector.Count;

    //multiplying index i of vector 1 to index i of vector 2
    //*sidenote: I made 2 matrix sqaure, one of them has the first vector as first row, the other has the 2nd vector as first column
    //multiplying the 2 matrices, the diagonal elements are the result of multiplying index[i] of vector 1 to index[i] of vector 2
    //so I multiply the matricies and grab the diagonal stack as a vector, and then use the sum of them.
    //I could probably find a better way but, if it works, don't change it!!!
    double multiplicationSum_Double = Matrix<double>.Build.DenseOfColumnVectors(initial_DoubleVector).
        Multiply(Matrix<double>.Build.DenseOfRowVectors(destination_DoubleVector)).Diagonal().Sum();

    double firstSquaredSum_Double = Matrix<double>.Build.DenseOfColumnVectors(initial_DoubleVector).
        Multiply(Matrix<double>.Build.DenseOfRowVectors(initial_DoubleVector)).Diagonal().Sum();

    double destinationSquaredSum_Double = Matrix<double>.Build.DenseOfColumnVectors(destination_DoubleVector).
        Multiply(Matrix<double>.Build.DenseOfRowVectors(destination_DoubleVector)).Diagonal().Sum();

    double correlation_Double = (numberOfElements_Double * multiplicationSum_Double -
        initial_DoubleVector.Sum()*destination_DoubleVector.Sum()) /
            double.Sqrt(
                (numberOfElements_Double * firstSquaredSum_Double -
                    initial_DoubleVector.Sum() * initial_DoubleVector.Sum()) *
                        (numberOfElements_Double * destinationSquaredSum_Double -
                            destination_DoubleVector.Sum() * destination_DoubleVector.Sum()));

    //end of formula

    System.Console.Write("\"Spearman\" Correlation: ");
    
    System.Console.WriteLine(Correlation.Spearman([.. initial_DoubleVector], [.. destination_DoubleVector]));

    System.Console.Write("\"Pearson\" Correlation: ");

    System.Console.Write(Correlation.Pearson([.. initial_DoubleVector], [.. destination_DoubleVector]));

    System.Console.WriteLine(" (same as hand written code, last digit may differ due to hardware limitations and internal methods)");

    System.Console.WriteLine($"hand written code: {correlation_Double} (calculations based on a yt math video: https://youtu.be/11c9cs6WpJU?si=3L3zy_9KBfOVv1aG)");

}

//END OF TASK 5 ----------------------------

//Task 6
// Polynomial Fit
{

    System.Console.WriteLine();

    System.Console.WriteLine("--- Task 6\nPolynomial: ");

    Vector<double> first_DoubleVector = Vector<double>.Build.Dense(3 , i => 
        RandomNumberGenerator.GetInt32(1,9) +
            RandomNumberGenerator.GetInt32(1,9) /
                RandomNumberGenerator.GetInt32(1,9) *
                    i - RandomNumberGenerator.GetInt32(1,9)); //making a really (psuedo-)random vector

    Vector<double> second_DoubleVector = Vector<double>.Build.Dense(3 , i =>
        RandomNumberGenerator.GetInt32(1,9) /
            RandomNumberGenerator.GetInt32(1,9) *
                i + RandomNumberGenerator.GetInt32(1,9)); //making another really (psuedo-)random vector

    System.Console.WriteLine($"first array: {first_DoubleVector.ToString()}");

    System.Console.WriteLine($"second array: {second_DoubleVector.ToString()}");

    Polynomial initial_Polynomial = Polynomial.Fit([..first_DoubleVector],[..second_DoubleVector],2); // honestly i dont have any idea what are polynomial

    System.Console.WriteLine($"PolyNomial Fit: {initial_Polynomial}");

    static double function_Func(double x, double y) => x * y / (x + y); //a function to find a curve based on it? i dont know

    System.Console.WriteLine($"Best Fit For Curve Of (x,y)=>x*y/(x+y): {Fit.Curve([..first_DoubleVector],[..second_DoubleVector],function_Func,RandomNumberGenerator.GetInt32(0,10))}");//have no forking idea what this does

    System.Console.WriteLine($"Roots (vector): {Vector<System.Numerics.Complex>.Build.Dense(initial_Polynomial.Roots()).ToString()}");//complex roots of sth?

    //no idea what or why is evaluating

    double[] firstEvaluation_DoubleArray = initial_Polynomial.Evaluate(first_DoubleVector).ToArray();

    double[] secondEvaluation_DoubleArray = initial_Polynomial.Evaluate(second_DoubleVector).ToArray();

    System.Console.Write($"first evaluation: ");

    foreach (double element in firstEvaluation_DoubleArray)
    {

        System.Console.Write($"{element} ");
        
    }

    System.Console.Write($" |  second evaluation: ");

    foreach (double element in secondEvaluation_DoubleArray)
    {

        System.Console.Write($"{element} ");
        
    }

}

//END OF TASK 6 ----------------------------

//END OF TASKS -----------------------------

//Challenges
System.Console.WriteLine();

System.Console.WriteLine();

System.Console.WriteLine("--- Challenges:");

//Single Value Decomposition (used in image processing and data compression, solving linear equations and recommendation systems)
{

    //same explanations as Eigen values :/

    System.Console.WriteLine();

    System.Console.WriteLine("-Single Value Decomposition-");

    Matrix<double> first_DoubleMatrix = Matrix<double>.Build.Dense(3,3,(i,j)=>1+3/5*j-i+RandomNumberGenerator.GetInt32(1,3));

    Svd<double> eigenCalculation_DoubleEvd = first_DoubleMatrix.Svd();

    System.Console.WriteLine($"matrix: {first_DoubleMatrix.ToString()}");

    System.Console.WriteLine();

    System.Console.Write("SVD \"U\" Matrix: ");

    System.Console.WriteLine(eigenCalculation_DoubleEvd.U.ToString());

    System.Console.Write("SVD \"Sigma\" Matrix: ");

    System.Console.WriteLine(eigenCalculation_DoubleEvd.W.ToString());

    System.Console.Write("SVD \"VT\" Matrix: ");

    System.Console.WriteLine(eigenCalculation_DoubleEvd.VT.ToString());


}

//Probability Distributions
{

    //probability and stuff, some of it is obvious (median, mean, average,standard deviation)
    //others i have no idea (normal dist, mode of normal dist, cumalative dist at [number], generated sample from normal dist with box-muller algorithm)

    System.Console.WriteLine();

    System.Console.WriteLine("-Probability Distributions-");

    Vector<double> first_DoubleMatrix = Vector<double>.Build.Dense(100, i => i*RandomNumberGenerator.GetInt32(70,170) + RandomNumberGenerator.GetInt32(300,10000)-RandomNumberGenerator.GetInt32(0,300));

    System.Console.WriteLine($"Data: {first_DoubleMatrix.ToString()}");

    System.Console.WriteLine($"Average: {first_DoubleMatrix.Average()}");

    System.Console.WriteLine($"Mean: {first_DoubleMatrix.Mean()}");    

    System.Console.WriteLine($"Standard Deviation: {first_DoubleMatrix.StandardDeviation()}");

    System.Console.WriteLine($"Normal Distribution: {new Normal(first_DoubleMatrix.Mean(),first_DoubleMatrix.StandardDeviation())}");

    System.Console.WriteLine($"Mode Of Normal Distribution: {new Normal(first_DoubleMatrix.Mean(),first_DoubleMatrix.StandardDeviation()).Mode}");

    System.Console.WriteLine($"Precision Of Normal Distribution: {new Normal(first_DoubleMatrix.Mean(),first_DoubleMatrix.StandardDeviation()).Precision}");

    System.Console.WriteLine($"Median Of Normal Distribution: {new Normal(first_DoubleMatrix.Mean(),first_DoubleMatrix.StandardDeviation()).Median}");

    System.Console.WriteLine($"Variance Of Normal Distribution: {new Normal(first_DoubleMatrix.Mean(),first_DoubleMatrix.StandardDeviation()).Variance}");

    System.Console.WriteLine($"Entropy Of Normal Distribution: {new Normal(first_DoubleMatrix.Mean(),first_DoubleMatrix.StandardDeviation()).Entropy}");

    int randomNumber_Int = RandomNumberGenerator.GetInt32(0,20000);

    System.Console.WriteLine($"Cumalative Distribution At {randomNumber_Int}: {new Normal(first_DoubleMatrix.Mean(),first_DoubleMatrix.StandardDeviation()).CumulativeDistribution(randomNumber_Int)}");

    System.Console.WriteLine($"Generated Sample From Normal Distribution (Box-Muller): {new Normal(first_DoubleMatrix.Mean(),first_DoubleMatrix.StandardDeviation()).Sample()}");

}

System.Console.WriteLine("Press Anything To Exit");

Console.ReadKey(true);

//END OF Challenges -----------------------------
//thank you for your patience! ;)