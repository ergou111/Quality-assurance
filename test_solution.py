import unittest
import HtmlTestRunner
from solution import Solution



class TestSolution(unittest.TestCase):
        
    def test_product_single_element1(self):
        s = Solution()
        self.assertEqual(s.productExceptSelf([1]), [1])
    
    def test_product_single_element2(self):
        s = Solution()
        self.assertEqual(s.productExceptSelf([2]), [1])
    
    def test_product_except_double_element_zero(self):
        s = Solution()
        self.assertEqual(s.productExceptSelf([1, 0]), [0, 1])
        
    def test_product_except_double_element(self):
        s = Solution()
        self.assertEqual(s.productExceptSelf([1, 2]), [2, 1])
        
    def test_product_all_same_element(self):
        s = Solution()
        self.assertEqual(s.productExceptSelf([1, 1, 1, 1]), [1, 1, 1, 1])
        
    def test_product_two_same_element(self):
        s = Solution()
        self.assertEqual(s.productExceptSelf([1, 2, 2, 4]), [16, 8, 8, 4])
        
    def test_product_all_zero(self):
        s = Solution()
        self.assertEqual(s.productExceptSelf([0, 0, 0, 0]), [0, 0, 0, 0])
        
    def test_product_ordinal_number(self):
        s = Solution()
        self.assertEqual(s.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6])
        
    def test_product_reverse_number(self):
        s = Solution()
        self.assertEqual(s.productExceptSelf([0, 1, 2, 3]), [6, 0, 0, 0])
        
    def test_product_contains_zero(self):
        s = Solution()
        self.assertEqual(s.productExceptSelf([1, 2, 0, 4]), [0, 0, 8, 0])
        
    def test_product_two_zero(self):
        s = Solution()
        self.assertEqual(s.productExceptSelf([1, 0, 0, 4]), [0, 0, 0, 0])
    
    def test_product_all_negative(self):
        s = Solution()
        self.assertEqual(s.productExceptSelf([-1, -2, -3, -4]), [-24, -12, -8, -6])
        
    def test_product_single_negative(self):
        s = Solution()
        self.assertEqual(s.productExceptSelf([1, 2, -3, 4]), [-24, -12, 8, -6])
        
    def test_product_interval_negative(self):
        s = Solution()
        self.assertEqual(s.productExceptSelf([1, -1, 2, -2, 3, -3]), [-36, 36, -18, 18, -12, 12])

    def test_invalid_not_list(self):
        s = Solution()
        with self.assertRaises(TypeError):
            s.productExceptSelf('not a list')

if __name__ == '__main__':
     unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test-reports'))