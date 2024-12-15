from functions import salary, hello_who

def test_hello_who():
    assert hello_who('Max') =='Hello,Max'


def test_a():
    assert hello_who('Lexa') =='Hello,Lexa'
    assert hello_who('Gleb') =='Hello,Gleb'
    assert hello_who('Pasha') =='Hello,Pasha'
    assert hello_who('Mix') =='Hello,Mix'

def test_salary():
    assert salary(2, 2) != 8
    assert salary(3, 1) != 6
