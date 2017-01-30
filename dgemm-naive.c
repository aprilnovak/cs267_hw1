#include <stdlib.h> // For: malloc
#include <stdio.h> // For: printf

const char* dgemm_desc = "Naive, three-loop dgemm.";

/* This routine performs a dgemm operation
 *  C := C + A * B
 * where A, B, and C are lda-by-lda matrices stored in column-major format.
 * On exit, A and B maintain their input values. */    
void square_dgemm (int n, double* A, double* B, double* C)
{
  // transpose A so that it is row-major
  /*double * aij = 0;
  aij = (double*) malloc(n * n * sizeof(double));
  
  if (aij == NULL)
    printf("Memory allocation error!");

  for (int i = 0; i < n; ++i)
  {
    for (int j = 0; j < n; ++j)
        aij[i + j*n] = A[j + i*n];    
  }*/
    
  for (int i = 0; i < n; ++i)
    for (int j = 0; j < n; ++j) 
    {
      double cij = C[i+j*n];
      for( int k = 0; k < n; k++ )
        //C[i+j*n] += A[i+k*n] * B[k+j*n];
        cij += A[i+k*n] * B[k+j*n];
        //cij += aij[k+i*n] * B[k+j*n];
      C[i+j*n] = cij;
    }
  //free(aij);
}
