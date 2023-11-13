from nweng.matrix import Matrix
import pytest

class TestClassMatrixCreation:
    
    test_int_input = [5,4,6]
    test_float_input = [4.55454654, 5.8454, 58.5]
    test_int_float_input = [[1,2,3],[4.5,7.5,3]]
    test_input_three_dims = [[[1,4],[2,5],[3,6]]]
    test_str_input1 = [1,'2','fgjd']
    test_str_input2 = [[1,2,4],['ifd','jgk','5']]
    test_str_input3 = [[1,'f'],['gh']]
    

    def test_matrix_creation1(self):
        A = Matrix(self.test_int_input)
        assert isinstance(A,Matrix)
        assert A.get_rows() == 1
        assert A.get_cols() == 3
    
    def test_matrix_creation2(self):
        A = Matrix(self.test_float_input)
        assert isinstance(A,Matrix)
        assert A.get_rows() == 1
        assert A.get_cols() == 3

        
    def test_matrix_creation3(self):
        A = Matrix(self.test_int_float_input)
        assert isinstance(A,Matrix)
        assert A.get_rows() == 2
        assert A.get_cols() == 3

    def test_matrix_do_not_accept_3dims(self):
        with pytest.raises(ValueError):
            Matrix(self.test_input_three_dims)

    def test_does_not_accept_str1(self):   
        with pytest.raises(TypeError):
            Matrix(self.test_str_input1)
    
    def test_does_not_accept_str2(self):   
        with pytest.raises(TypeError):
            Matrix(self.test_str_input2)
    
    def test_does_not_accept_str3(self):   
        with pytest.raises(ValueError):
            Matrix(self.test_str_input3)


