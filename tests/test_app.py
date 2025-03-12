import pytest
from myapp.app import multiply_by_two, divide_by_two

@pytest.fixture
def numbers():
    a = 10
    b = 20
    return [a, b]

class TestApp:
    @pytest.mark.easy_operation
    def test_multiplication(self, numbers):
        res = multiply_by_two(numbers[0])
        assert res == numbers[1]

    @pytest.mark.easy_operation
    def test_division(self, numbers):
        res = divide_by_two(numbers[1])
        assert res == numbers[0]

    # New test based on student ID (30)
    @pytest.mark.difficult_operation
    def test_student_id_case(self):
        input_value = 15  # Since 15 * 2 = 30
        expected_output = 30  # Last two digits of roll number
        assert multiply_by_two(input_value) == expected_output

    
