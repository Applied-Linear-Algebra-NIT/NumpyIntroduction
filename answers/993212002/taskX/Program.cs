using System.Collections;
using System.Security.Cryptography;
using MathNet.Numerics.LinearAlgebra;
Console.WriteLine("Hello, World!");

//Task 1
//1a. ArrayList
ArrayList list_ArrayList = [];

//or
//1a. Vector (Random Length)
Vector<double> vector_Vector = MathNet.Numerics.LinearAlgebra.Vector<double>.Build.Random(RandomNumberGenerator.GetInt32(1,25));

//1b. 2D Matrix
Matrix<double> matrix2D_Matrix = Matrix<double>.Build.Dense(3,4);

//1cI. 3D Matrix
Matrix<double>[] matrix3D_Matrix = new Matrix<double>[2];

Matrix<double> matrix2DBuilder_Matrix = Matrix<double>.Build.Dense(3,4,1);

for (int i = 0; i < 2; i++)
{

    matrix3D_Matrix[i] = matrix2DBuilder_Matrix;
    
}

//OR
//1cII. 3D Array
double[][][] array3D_Double = new double[2][][];

double[][] array2DBuilder_Double = [[1,1,1,1],[1,1,1,1],[1,1,1,1]];

for (int i = 0; i < 2; i++)
{

    array3D_Double[i] = array2DBuilder_Double;

}

array3D_Double.GetLength(0);

//2. Inspection
//2a. Dimensions
System.Console.WriteLine($"List:         {list_ArrayList.Count}x elements (has no elements)");

System.Console.WriteLine($"Vector:      {vector_Vector.Count}x elements (random number and randomized elements)");

System.Console.WriteLine($"2D Matrix:   {matrix2D_Matrix.RowCount}x{matrix2D_Matrix.ColumnCount} | {matrix2D_Matrix.RowCount} rows & {matrix2D_Matrix.ColumnCount} columns");

System.Console.WriteLine($"3D Matrix: {matrix3D_Matrix.Length}x{matrix3D_Matrix[0].RowCount}x{matrix2D_Matrix.ColumnCount} | {matrix3D_Matrix.Length} matrices, {matrix3D_Matrix[0].RowCount} rows & {matrix3D_Matrix[0].ColumnCount} columns each");

System.Console.WriteLine($"3D Array:  {array3D_Double.Length}x{array3D_Double[0].Length}x{array3D_Double[0][0].Length} | {array3D_Double.Length} arrays, {array3D_Double[0].Length} rows & {array3D_Double[0][0].Length} columns each");