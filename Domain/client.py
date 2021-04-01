import datetime


class Client:

    def __init__(self, cnp, last_name, first_name, email):
        self.__cnp = cnp
        self.last_name = last_name
        self.first_name = first_name
        self.age_group = Client.get_age_group(cnp)
        self.email = email

    def __str__(self):
        return f'{self.__cnp}, {self.last_name}, {self.first_name}, {self.email}'

    def get_cnp(self):
        return self.__cnp

    @staticmethod
    def get_age_group(cnp):
        today = datetime.datetime.today()

        if int(cnp[0]) <= 2:
            decades = 1900
        else:
            decades = 2000
        born = datetime.datetime(
            year=int(cnp[1:3]) + decades,
            month=int(cnp[3:5]),
            day=int(cnp[5:7]))
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        if age < 18:
            return '<18'
        if 18 <= age <= 24:
            return '18-24'
        if 25 <= age <= 34:
            return '25-34'
        if 35 <= age <= 44:
            return '35-44'
        if 45 <= age <= 54:
            return '45-54'
        if age >= 55:
            return '>=55'