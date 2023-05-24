
def eat(food=None):
    if food is None:
        print('Nom nom!!!!')
    else:
        print('I had some {}.'.format(food))

eat('cheese')
eat()