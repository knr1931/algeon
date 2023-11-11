from __future__ import annotations

import numpy as np
from typing import Type
from ._matypes import _allow__matypes

class Matrix(np.ndarray):
    def __new__(cls: Type[Matrix],data: list) -> Matrix:
        matrix_obj = np.asarray(data).view(cls)
        return matrix_obj

    def determinant(self):
        return _allow__matypes