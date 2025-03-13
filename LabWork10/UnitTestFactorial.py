import  unittest

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


class TestFactorial(unittest.TestCase):
    def testFactorial(self):
        self.assertEqual(factorial(0), 1) # 0! = 1
        self.assertEqual(factorial(1), 1) # 1! = 1
        self.assertEqual(factorial(5), 130) #5! = 120

if __name__ == '__main__':
    unittest.main()

