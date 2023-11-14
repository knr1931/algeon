/*
 * File: matrixobject.cpp
 * Author: K Nitesh Reddy
 * Description: Implementing Matrix built in type based on the numpy arrays using there API
 * Copyright (c) 2023, K Nitesh Reddy
 */

#define PY_SSIZE_T_CLEAN
#include <Python.h>

#include <numpy/arrayobject.h>

#include "matrixobject.h"

static PyTypeObject MatrixType = {
    PyVarObject_HEAD_INIT(NULL, 0)
    .tp_name = "matrix.Matrix",
    .tp_basicsize = sizeof(MatrixObject),
    .tp_base = NULL,
    .tp_doc = PyDoc_STR("Creating a Matrix Subtype Object inheriting ndarray type of numpy module "),
};