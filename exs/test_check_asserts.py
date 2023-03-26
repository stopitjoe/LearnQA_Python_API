class TestExample:
    def test_check_math(self):
        a = 5
        b = 9
        assert a + b == 14

    def test_check_math2(self):
        a = 5
        b = 11
        expected_sum = 14
        assert a + b == expected_sum, f'{expected_sum} is not correct sum'
