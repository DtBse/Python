import random
class Odnocl:
    def Start(self):
        print('Нещодавно я почав частіше спілкуватися і гуляти з однокласником')

    def Contin(self):
        print('...')


class BestFriend(Odnocl):
    def Contin(self):
        print('Тепер ми з ним найкращі друзі')


class Spectator(BestFriend):
    def __init__(self):
        super().Start()
        super().Contin()

nick = Spectator()
drama = random.randint(0, 1)
if(drama>0):
    print("Мій друг зрадник, проміняв мене на дівчину, тепер у мене немає друга")
else:
    print("Ми продовдуємо дружити")
    g = random.randint(0, 1);
    if(g>0):
        print("В нашій компанії з'явились нові люди! Тепер у нас", random.randint(4, 6), "людей в компанії")
    else:
        print("Ми з другом відкрили нашу автомикйку")
        h = random.randint(0, 1);
        if(h>0):
            print("Нашу автомийку прикрили бандити")
        else:
            print("Справи пішли вгору і тепер ми найпопулярніша автомийка на районі")
            m = random.randint(1, 10000)
            if(m<10000):
                print("Тепер ми багаті")
            else:
                print("Метеорит упав на землю")