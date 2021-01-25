import pytest, pickle
from arithmetik import add, divide

# data_add = [(3,5,8),(2,3,5),(12,45,57),('bedret','tin','bedrettin')]
# data_divide = [(12,3,4),(3,5,0.6),(-10,2,-5),(-25,-5,5),(13,0,0)]
#
# pickle.dump(data_add, open('add.bin', 'wb'))
# pickle.dump(data_divide, open('divide.bin', 'wb'))

data_add = pickle.load(open('add.bin', 'rb'))
data_divide = pickle.load(open('divide.bin', 'rb'))

@pytest.mark.parametrize('x,y,expected',data_add )
def test_add(x, y, expected):
    assert add(x, y) == expected

@pytest.mark.parametrize('x,y,expected', data_divide)
def test_divide(x, y, expected):
    assert divide(x, y) == expected


