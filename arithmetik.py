def add(*args):
    sum = 0
    try:
        for i in args:
            sum += int(i)
        return sum
    except ValueError:
        print('lütfen sadece Integer deger giriniz')
    finally:
        print('......')

def divide(x = 'dividend', y = 'divisor'):
    try:
        return x / y
    except ZeroDivisionError:
        print('Sayilar sifira böünemez')
    finally:
        print('.......')