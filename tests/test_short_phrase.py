class TestLenPhrase:
    def test_len_phrase(self):
        phrase = input("Please, set a phrase:")

        assert len(phrase) < 15, f"Your phrase have length more than 15, length = {len(phrase)} "
