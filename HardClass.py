class Pracivnik_Poshti:
    def vidpravka(self):
        print('Надсилання посилки...')


class Vodiy:
    def perevez(self):
        print('Перевезення...')


class SmartPhone(Vodiy, Pracivnik_Poshti):
    pass


vidpravka = SmartPhone()
vidpravka.vidpravka()
vidpravka.perevez()
