#ifndef MATRIX_OBJECT_H
#define MATIX_OBJECT_H

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <numpy/arrayobject.h>


#ifdef __cplusplus
extern "C" {
#endif

/*
*
*   Creating a Matrix Subtype inheriting ndarray type of numpy module 
*
**/
typedef struct MatrixObjectStructure {
    PyArrayObject base;
    /* number of rows in a matrix*/
    size_t rows;
    /* number of colums in a matrix */
    size_t columns;
} MatrixObject;

#ifdef __cplusplus
}
#endif

#endif