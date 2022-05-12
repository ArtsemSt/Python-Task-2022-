# Наследование
class AntihypertensiveDrugs():
    name = str
    maximum_dayli_doz = float
    form = str

    # color
    # price - необязательныe параметры  <- Абстракция
    def __init__(self, name, maximum_dayli_doz):
        self.name = name
        self.maximum_dayli_doz = maximum_dayli_doz

    def __str__(self):
        return f'drugs: {self.name}, maximum daily doz - {self.maximum_dayli_doz} mg'


class Inhibitor_APF(AntihypertensiveDrugs):
    @staticmethod
    def form():
        print("Oval")  # изменение метода родительского класса <- Полиморфизм


class Diuretic(AntihypertensiveDrugs):
    @staticmethod
    def form():
        print("Cirle")  # изменение метода родительского класса


inhibitor_APF = Inhibitor_APF("Lisinopril", 80)
diuretic = Diuretic("Indapamid", 2.5)

print(inhibitor_APF)
print(diuretic)


