import pytest

# @pytest.fixture(autouse=True, scope='function')
# def log_test():
#     print('НАЧАЛО ТЕСТА')
#     yield
#     print('КОНЕЦ ТЕСТА')
#
# def test_add():
#     assert 10 + 15 == 25
#
# def test_multy():
#     assert 5 * 5 == 25

class Counter:
    function_count = 0
    class_count = 0
    module_count = 0

@pytest.fixture(scope='function')
def fixture_function():
    Counter.function_count += 1
    print(f'\n')
@pytest.fixture(scope='class')
def fixture_class():
    pass

@pytest.fixture(scope='module')
def fixture_module():
    pass

class TestA:

    def test_simple_thing1(self):
        assert 1 + 1 == 2


    def test_simple_thing2(self):
        assert 2 * 2 == 4

class TestB:

    def test_simple_thing3(self):
        assert 2 / 2 == 1

    def test_simple_thing4(self):
        assert 2 ** 2 == 4

def test_simple_thing5():
    assert abs(-42) == 42