class Ocinkizatest:
    def __init__(self, mark, time):
        self.mark = mark
        self.time = time
    def nacinka(self, amount):
        self.mark += amount
    def univer(self):
        if self.mark > 9:
            print('Ви поступили в Універ')
        else:
            print("Занизька оцінка")
Bogdan = Ocinkizatest(11, 39)
print(Bogdan.mark)
print(Bogdan.time)
Max = Ocinkizatest(9, 25)
print(Max.mark)
print(Max.time)
print('-------------------')
print(Bogdan.mark)
Bogdan.nacinka(1)
print(Bogdan.mark)
print('-------------------')
print(Max.mark)
Max.univer()
