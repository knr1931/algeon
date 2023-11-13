from __future__ import annotations

import numpy as np
from ._matypes import _allow__matypes
from ._typing import (
    MatrixElemTypes,
    MatrixInputData
)

class Matrix(np.ndarray):
    
    _rows: int
    _cols: int = 1
    def __new__(cls: type[Matrix],data: MatrixInputData) -> Matrix:
        matrix_obj = np.asarray(data).view(cls)
        if matrix_obj.dtype not in _allow__matypes:
            raise TypeError("Matrix should only contain real or complex numbers as it's elements")
        return matrix_obj

    def determinant(self):
        return _allow__matypes