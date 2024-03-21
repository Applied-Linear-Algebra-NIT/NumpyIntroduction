using System.Collections;
using System.Security.Cryptography;
using MathNet.Numerics.LinearAlgebra;

Console.WriteLine("Hello, World!");

System.Console.WriteLine();

System.Console.WriteLine("Task 1:");

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

    ShowMatrix_Function(matrix);
    
}

//END OF TASK 2 ----------------------------

System.Console.WriteLine();

System.Console.WriteLine("Task 3:");
//Task 3
//1. Arithmetic
{

    //a. addition
    System.Console.WriteLine("Addition: every element +5");

    Matrix<double> aMatrix_DoubleMatrix = matrix_DoubleMatrix.Add(5);

    ShowMatrix_Function(aMatrix_DoubleMatrix);

    //b. subtraction
    System.Console.WriteLine("Subtraction: every element -2");

    Matrix<double> bMatrix_DoubleMatrix = aMatrix_DoubleMatrix.Subtract(2);

    ShowMatrix_Function(bMatrix_DoubleMatrix);

    //c. nultiplication
    System.Console.WriteLine("Miltiplication: every element x5");

    Matrix<double> cMatrix_DoubleMatrix = bMatrix_DoubleMatrix.Multiply(5);

    ShowMatrix_Function(cMatrix_DoubleMatrix);

    //d. division
    System.Console.WriteLine("Division: every element devided by 3");

    Matrix<double> dMatrix_DoubleMatrix = cMatrix_DoubleMatrix.Divide(3);

    ShowMatrix_Function(dMatrix_DoubleMatrix);

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

    ShowMatrix_Function(destination_DoubleMatrix);

    System.Console.WriteLine("Broadcasting:");

    for (int i = 0; i < destination_DoubleMatrix.ColumnCount; i++)
    {

        destination_DoubleMatrix.SetColumn(i,destination_DoubleMatrix.Column(i).Add(initialVector_DoubleVector));
        
    }

    ShowMatrix_Function(destination_DoubleMatrix);

}

//3. Reshape & Flatten
{    

    Matrix<double> reshaped_DoubleMatrix = Matrix<double>.Build.DenseOfMatrix(matrix_DoubleMatrixArray[0]);

    System.Console.WriteLine("Reshaped:");
    
    ShowMatrix_Function(reshaped_DoubleMatrix);

    Matrix<double> flatten_DoubleMatrix = Matrix<double>.Build.DenseOfRowVectors(reshaped_DoubleMatrix.Row(1));

    System.Console.WriteLine("Flattened:");

    ShowMatrix_Function(flatten_DoubleMatrix);

}

//END OF TASK 3 ----------------------------


//END OF TASKS ----------------------------
//Functions

static void ShowMatrix_Function(Matrix<double> matrix)
{

    int row_Int = 1;

    System.Console.Write($"  ");

    for (int i = 0; i < matrix.ColumnCount; i++)
    {

        System.Console.Write($"c{i} ");
        
    }

    System.Console.WriteLine();

    foreach (double[] row in matrix.ToRowArrays())
    {

        System.Console.Write($"r{row_Int}");

        row_Int++;

        foreach (double element in row)
        {

            if(element<0)
                System.Console.Write($"{element} ");
            else
                System.Console.Write($" {element} ");
            
        }

        System.Console.WriteLine();
        
    }

    System.Console.WriteLine();

}