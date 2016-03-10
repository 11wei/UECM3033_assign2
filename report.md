UECM3033 Assignment #2 Report
========================================================

- Prepared by: Soong Ting Wei
- Tutorial Group: T3

--------------------------------------------------------

## Task 1 --  $LU$ Factorization or SOR method

The reports, codes and supporting documents are to be uploaded to Github at: 

https://github.com/11wei/UECM3033_assign2

The condition i choose is compare the eigenvalues of each matrix A. SOR method will only converge if matrix A is positive
definite matrix, which is a matrix leading principal submatrices have positive determinants. Using np.linalg.eigvals 
function, we can obtain both matric A eigenvalues. Then, determine every eigenavlue in the array which is positve and return
a True of False (boolean type). After that, using if-else statement, python will operate the iteration by using LU method 
or SOR method to find the solution.

In task 1,self define function of lu, sor and solve are created. For LU method, two matrix will be created with is the 
lower matrix and upper matrix whereby A=LU, thus Ax=LUx=b, so will be define into Ly=b and Ux= y. So, we can get the x 
matrix after getting the y matrix.As for the SOR method, omega is assume to be 1.03 which is within the range of 1<omega<2
 that will converge for any initial vector if A matrix is symmetric and positive definite. If omega is greater than 2 , 
SOR method will diverge. If 0 < omega<1, SOR method converges but the convergence rate is slower than the Gauss-Seidal 
method. Then, the iteration limit also needed to be set so that it will not loop until infinity time. In this task, the 
iteration limit is assumed to be 10. We start the iteration by assuming the first x is a zero vector. Then we will 
substitute each x we found to count the new x and iterate until the iteration limit.In order to find the exact answer, 
let sol equal to np.linalg.solve(A,b) else the answer will not be true.

---------------------------------------------------------

## Task 2 -- SVD method and image compression

SVD.jpg

How many non zero element in $\Sigma$?
- All the red,green and,blue $\Sigma$ are non zero elements

HighResolution.jpg

When the resolution is better, $\Sigma_{200}$


LowResolution.jpg

When the resolution is lower , $\Sigma_{30}$

What is a sparse matrix?
- A sparse matrix is a matrix in which most of the elements are zero. By contrast, if most of the elements are nonzero, then the matrix is considered dense. The fraction of non-zero elements over the total number of elements (i.e., that can fit into the matrix, say a matrix of dimension of m x n can accommodate m x n total number of elements) in a matrix is called the sparsity (density).
-----------------------------------

<sup>last modified: 11 March 2016 </sup>
