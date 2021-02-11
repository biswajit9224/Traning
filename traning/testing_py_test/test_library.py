from .library import is_even,is_palendrom
# import library.is_even
class Testlibrary_:

    def test_demo():
        print('hai')

    def test_odd():
        print('excicuting test_odd')
        assert is_even(3)==False


    def test_string():
        print('excicuting test_string')
        assert is_even('10')==True

    def test_palindrom():
        print('excicuting test_palindrom')
        assert is_palendrom('hello')==False

    def test_not_palendrom():
        print('excicuting test_not_palindrom')
        assert is_palendrom('racecar')==True

    def test_number_palendrom():
        print('Excuting test_number_palendrom')
        assert is_palendrom(12321)==False

class Hai:

    def test_hai():
        print("test_________hi")