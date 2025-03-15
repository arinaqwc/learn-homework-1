
def place_go(age):
    try: 
        age=int(age)
        if age<3:
         return 'Вы слишком малы для детского сада'
        if 3<=age<7:
         return 'Вы должны ходить в детский сад'
        if 7<=age<=18:
         return 'Вы должны ходить в школу'
        if 18<age<=24:
         return 'Вы должны ходить в ВУЗ'
        else:
         return 'Вы должны работать'

    except ValueError:
       return 'Введите число'
       



age=input('Сколько вам лет? ')
result=place_go(age)
print(result)
