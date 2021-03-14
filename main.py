class abonent:
    def __init__(self):
        id = 'Идентификационный номер: '+input('Введите id: ')
        surname = 'Фамилия: '+input('Введите фамилию: ')
        name='Имя: '+input('Введите имя: ')
        lastname = 'Отчество: '+input('Введите отчество: ')
        address = 'Адрес: ' + input('Введите адрес: ')
        cardnumber = 'Номер карты: '+input('Введите номер кредитной карточки: ')
        debet='Дебет'+input('Введите дебет: ')
        credit = 'Кредит' + input('Введите кредит: ')
        outspeaktime = 'Время международных переговоров: '+input('Введите время международных переговоров: ')
        inspeaktime='Время городских переговоров: '+input('Введите время городских переговоров: ')
        self.abonent=[id,surname,name,lastname,address,cardnumber,debet,credit,outspeaktime,inspeaktime]

    def setid(self):
        newattr = input('Введите новое id: ')
        self.abonent[0] = 'Идентификационный номер: ' + newattr

    def setsurname(self):
        newattr = input('Введите новое значение фамилии: ')
        self.abonent[1] = 'Фамилия: ' + newattr

    def setname(self):
        newattr = input('Введите новое значение имени: ')
        self.abonent[2] = 'Имя: ' + newattr

    def setlastname(self):
        newattr = input('Введите новое значение отчества: ')
        self.abonent[3] = 'Отчество: ' + newattr

    def setaddress(self):
        newattr = input('Введите новое значение адреса: ')
        self.abonent[4] = 'Адрес: ' + newattr

    def setcardnumber(self):
        newattr = input('Введите новое значение номера карточки ')
        self.abonent[5] = 'Номер карты: ' + newattr

    def setdebet(self):
        newattr = input('Введите новое значение дебета')
        self.abonent[6] = 'Дебет: ' + newattr

    def setcredit(self):
        newattr = input('Введите новое значение кредита')
        self.abonent[7] = 'Кредит: ' + newattr

    def setoutspeaktime(self):
        newattr = input('Введите новое значение времени международных переговоров: ')
        self.abonent[8] = 'Время международных переговоров: ' + newattr

    def setinspeaktime(self):
        newattr = input('Введите новое значение времени городских переговоров: ')
        self.abonent[9] = 'Время городских переговоров: ' + newattr

    def getAttributes(self):
        for i in range(10):
            print(self.abonent[i])

    def getid(self):
        print(self.abonent[0])

    def getsurname(self):
        print(self.abonent[1])

    def getname(self):
        print(self.abonent[2])

    def getlastname(self):
        print(self.abonent[3])

    def getaddress(self):
        print(self.abonent[4])

    def getcardnumber(self):
        print(self.abonent[5])

    def getdebet(self):
        print(self.abonent[6])

    def setcredit(self):
        print(self.abonent[7])

    def setoutspeaktime(self):
        print(self.abonent[8])

    def setinspeaktime(self):
        print(self.abonent[9])
