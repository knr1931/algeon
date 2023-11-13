from nweng.matrix import Matrix

TEST_MATRIX_INPUT_1D = [1,2,3]

def test_matrix_creation1d():
    A = Matrix(TEST_MATRIX_INPUT_1D)
    assert isinstance(A,Matrix)


