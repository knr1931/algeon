from __future__ import annotations

import numpy as np
from ._matypes import _allow__matypes
from ._typing import (
    MatrixElemTypes,
    MatrixInputData
)

class Matrix(np.ndarray):
    
    def __new__(cls: type[Matrix],data: MatrixInputData) -> Matrix:
        try:
            matrix_obj = np.asarray(data).view(cls)
            if matrix_obj.dtype not in _allow__matypes:
                raise TypeError("Matrix should only contain real or complex numbers as it's elements")
            if matrix_obj.ndim > 2:
                raise ValueError("Matrix has only 1 or 2 dimensions") 
            return matrix_obj
        except ValueError:
            raise ValueError("Matrix has insufficient number of elements")
    
    """
        Checks wheter the input is a vector or not
    """
    def isVector(self) -> bool:
        return self.ndim == 1    
    
    def get_rows(self) -> int:
        if self.isVector(): 
            return 1
        return self.shape[0]
        
    def get_cols(self) -> int:
        if self.isVector():
            return self.shape[0]
        return self.shape[1]
        