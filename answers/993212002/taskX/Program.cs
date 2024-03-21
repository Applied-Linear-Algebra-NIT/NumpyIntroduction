using System.Collections;
using System.Security.Cryptography;
using MathNet.Numerics;
using MathNet.Numerics.LinearAlgebra;
using MathNet.Numerics.Statistics;

Console.WriteLine("Hello, World!");

System.Console.WriteLine();

System.Console.WriteLine("--- Task 1:");

//Task 1
//1. Creat Arrays
//aI. ArrayList
ArrayList list_ArrayList = [];

//or
//aII. List
List<double> list_DoubleList = [];

//or
//aIII. Vector (Random Length)
Vector<double> vector_DoubleVector = Vector<double>.Build.Random(RandomNumberGenerator.GetInt32(3,9));

//b. 2D Matrix
Matrix<double> matrix_DoubleMatrix = Matrix<double>.Build.Dense(3,4);

//cI. 3D Matrix
Matrix<double>[] matrix_DoubleMatrixArray = new Matrix<double>[2];

Matrix<double> matrix2DBuilder_DoubleMatrix = Matrix<double>.Build.Dense(3,4,1);

for (int i = 0; i < 2; i++)
{

    matrix_DoubleMatrixArray[i] = matrix2DBuilder_DoubleMatrix;
    
}

//OR
//cII. 3D Array
double[][][] array3D_DoubleArray3D = new double[2][][];

double[][] array2DBuilder_DoubleArray2D = [[1,1,1,1],[1,1,1,1],[1,1,1,1]];

for (int i = 0; i < 2; i++)
{

    array3D_DoubleArray3D[i] = array2DBuilder_DoubleArray2D;

}

array3D_DoubleArray3D.GetLength(0);

//2. Inspection
//2a. Dimensions
System.Console.WriteLine($"2 Lists: {list_ArrayList.Count} & {list_DoubleList.Count} elements (has no elements; will throw exception while indexing)");

System.Console.WriteLine($"Vector:      {vector_DoubleVector.Count} elements (random length ranging 3~9 with randomized elements; will use this as 1D array)");

System.Console.WriteLine($"2D Matrix:   {matrix_DoubleMatrix.RowCount}x{matrix_DoubleMatrix.ColumnCount} | {matrix_DoubleMatrix.RowCount} rows & {matrix_DoubleMatrix.ColumnCount} columns");

System.Console.WriteLine($"3D Matrix: {matrix_DoubleMatrixArray.Length}x{matrix_DoubleMatrixArray[0].RowCount}x{matrix_DoubleMatrix.ColumnCount} | {matrix_DoubleMatrixArray.Length} matrices, {matrix_DoubleMatrixArray[0].RowCount} rows & {matrix_DoubleMatrixArray[0].ColumnCount} columns each");

System.Console.WriteLine($"3D Array:  {array3D_DoubleArray3D.Length}x{array3D_DoubleArray3D[0].Length}x{array3D_DoubleArray3D[0][0].Length} | {array3D_DoubleArray3D.Length} arrays, {array3D_DoubleArray3D[0].Length} rows & {array3D_DoubleArray3D[0][0].Length} columns each");

//END OF TASK 1 ----------------------------

System.Console.WriteLine();

System.Console.WriteLine("Task 2:");
//Task 2
//1. Indexing
//a. vector index

System.Console.WriteLine("--- Task 2:");

System.Console.WriteLine($"{vector_DoubleVector[2]}");

//b. matrix index
System.Console.WriteLine($"value Of index[2,3] in 2D matrix: {matrix_DoubleMatrix[2,3]}");

//2. Slicing
//2d matrix upper left
Matrix<double> slicedMatrix_DoubleMatrix = matrix_DoubleMatrix.SubMatrix(0,2,0,2);

System.Console.WriteLine($"Sub Matrix:   {slicedMatrix_DoubleMatrix.RowCount}x{slicedMatrix_DoubleMatrix.ColumnCount} | {slicedMatrix_DoubleMatrix.RowCount} rows & {slicedMatrix_DoubleMatrix.ColumnCount} columns");

//3. Iterating
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
//1. Arithmetic
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

    Matrix<double> cMatrix_DoubleMatrix = bMatrix_DoubleMatrix.Multiply(5);

    System.Console.WriteLine(cMatrix_DoubleMatrix.ToString());

    //d. division
    System.Console.WriteLine("Division: every element devided by 3");

    Matrix<double> dMatrix_DoubleMatrix = cMatrix_DoubleMatrix.Divide(3);

    System.Console.WriteLine(dMatrix_DoubleMatrix.ToString());

}

System.Console.WriteLine();

//2. Broadcast
{

    System.Console.WriteLine("Broadcast:");

    Vector<double> initialVector_DoubleVector = Vector<double>.Build.Dense(3,i=>3*i-2);

    System.Console.WriteLine("Vector:");

    System.Console.WriteLine(initialVector_DoubleVector.ToString());

    Matrix<double> destination_DoubleMatrix = Matrix<double>.Build.DenseOfMatrix(matrix_DoubleMatrix);

    System.Console.WriteLine("Matrix:");

    System.Console.WriteLine(destination_DoubleMatrix.ToString());

    System.Console.WriteLine("Broadcasting:");

    for (int i = 0; i < destination_DoubleMatrix.ColumnCount; i++)
    {

        destination_DoubleMatrix.SetColumn(i,destination_DoubleMatrix.Column(i).Add(initialVector_DoubleVector));
        
    }

    System.Console.WriteLine(destination_DoubleMatrix.ToString());

}

//3. Reshape & Flatten
{    

    Matrix<double> reshaped_DoubleMatrix = Matrix<double>.Build.DenseOfMatrix(matrix_DoubleMatrixArray[0]);

    System.Console.WriteLine("Reshaped:");
    
    System.Console.WriteLine(reshaped_DoubleMatrix.ToString());

    Matrix<double> flatten_DoubleMatrix = Matrix<double>.Build.DenseOfRowVectors(reshaped_DoubleMatrix.Row(1));

    System.Console.WriteLine("Flattened:");

    System.Console.WriteLine(flatten_DoubleMatrix.ToString());

}

//END OF TASK 3 ----------------------------

//Task 4
{

    System.Console.WriteLine("--- Task 4:");

    //1. Dot Multiplication    
    Matrix<double> first_DoubleMatrix = Matrix<double>.Build.Dense(3,3,(i,j)=>1+3/5*j-i+RandomNumberGenerator.GetInt32(1,3));

    Matrix<double> second_DoubleMatrix = Matrix<double>.Build.Dense(3,3,(i,j)=>2/5*j-i+RandomNumberGenerator.GetInt32(1,3));

    System.Console.WriteLine("first matrix:");

    System.Console.WriteLine(first_DoubleMatrix.ToString());

    System.Console.WriteLine("second matrix:");

    System.Console.WriteLine(second_DoubleMatrix.ToString());

    Matrix<double> multiplier_DoubleMatrix = Matrix<double>.Build.DenseOfMatrix(first_DoubleMatrix.Multiply(second_DoubleMatrix));

    System.Console.WriteLine("multiplication:");

    System.Console.WriteLine(multiplier_DoubleMatrix.ToString());

    //2. Determinant & Inverse
    System.Console.WriteLine("determinant:");

    System.Console.WriteLine(multiplier_DoubleMatrix.Determinant());

    System.Console.WriteLine("inverse:");

    System.Console.WriteLine(multiplier_DoubleMatrix.Inverse().ToString());

    //3. Eigen Values & Vectors

}

//END OF TASK 4 ----------------------------

//Task 5
{

    //1. Descriptive

    System.Console.WriteLine("---Task 5\nDescription:");

    Vector<double> initial_DoubleVector = Vector<double>.Build.Dense(3,(i)=>3*i+RandomNumberGenerator.GetInt32(1,7)+2.5);

    Vector<double> destination_DoubleVector = Vector<double>.Build.Dense(3,(i)=>2*i+0.5*RandomNumberGenerator.GetInt32(1,7)-2);

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

    //2. Correlation

    System.Console.WriteLine();

    System.Console.WriteLine("--Correlation:");

    System.Console.Write("vector 1: ");

    System.Console.WriteLine(initial_DoubleVector.ToString());

    System.Console.Write("vector 2: ");

    System.Console.WriteLine(destination_DoubleVector.ToString());

    int numberOfElements_Double = initial_DoubleVector.Count;

    double multiplicationSum_Double = Matrix<double>.Build.DenseOfColumnVectors(initial_DoubleVector).
        Multiply(Matrix<double>.Build.DenseOfRowVectors(destination_DoubleVector)).Diagonal().Sum();

    double firstSquaredSum_Double = Matrix<double>.Build.DenseOfColumnVectors(initial_DoubleVector).
        Multiply(Matrix<double>.Build.DenseOfRowVectors(initial_DoubleVector)).Diagonal().Sum();

    double destinationSquaredSum_Double = Matrix<double>.Build.DenseOfColumnVectors(destination_DoubleVector).
        Multiply(Matrix<double>.Build.DenseOfRowVectors(destination_DoubleVector)).Diagonal().Sum();

    double correlation_Double = (numberOfElements_Double * multiplicationSum_Double -
        initial_DoubleVector.Sum()*destination_DoubleVector.Sum()) /
            double.Sqrt(
                (numberOfElements_Double * firstSquaredSum_Double - initial_DoubleVector.Sum() * initial_DoubleVector.Sum()) *
                    (numberOfElements_Double * destinationSquaredSum_Double - destination_DoubleVector.Sum() * destination_DoubleVector.Sum()));

    System.Console.Write("\"Spearman\" Correlation: ");
    
    System.Console.WriteLine(Correlation.Spearman([.. initial_DoubleVector], [.. destination_DoubleVector]));

    System.Console.Write("\"Perason\" Correlation: ");

    System.Console.Write(Correlation.Pearson([.. initial_DoubleVector], [.. destination_DoubleVector]));

    System.Console.WriteLine(" (same as hand written code)");

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
                    i - RandomNumberGenerator.GetInt32(1,9));

    Vector<double> second_DoubleVector = Vector<double>.Build.Dense(3 , i =>
        RandomNumberGenerator.GetInt32(1,9) /
            RandomNumberGenerator.GetInt32(1,9) *
                i + RandomNumberGenerator.GetInt32(1,9));

    System.Console.WriteLine($"first array: {first_DoubleVector.ToString()}");

    System.Console.WriteLine($"second array: {second_DoubleVector.ToString()}");

    Polynomial initial_Polynomial = Polynomial.Fit([..first_DoubleVector],[..second_DoubleVector],2);

    System.Console.WriteLine($"PolyNomial Fit: {initial_Polynomial}");

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