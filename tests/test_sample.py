import unittest


class RunnerSmokeTest(unittest.TestCase):
    def test_python_runtime(self):
        self.assertEqual(2 + 2, 4)


if __name__ == '__main__':
    unittest.main()
