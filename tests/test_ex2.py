from iterative_test_engine import IterativeTestor
from src.ex1 import example_function
from src.ex2 import complex_function


def test_complex_function():
    class MyIterativeTestor(IterativeTestor):
        def __init__(self):
            super().__init__(
                {
                    'a': range(-10, 10),
                    'b': range(-10, 10),
                    'c': range(-10, 10)
                },
                ['a', 'b', 'c']
            )

        def test_template(self, *args):
            a = args[0]
            b = args[1]
            c = args[2]
            assert a * example_function(b, c) == complex_function(a, b, c)
    assert MyIterativeTestor().loop_test_template()
