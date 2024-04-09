'''Все совпадения объектов с реальными людми случайны...'''
class OfficeWorker:
    def __init__(
            self,
            name : str,
            post : str,
            salary : int
            ) -> None:
        self.name = name
        self.post = post
        self.salary = salary

    def work(self, which_work : str):
        print(f'{self.post} {self.name} выполняет работу {which_work}')

    def drink_coffee(self, coffee : str):
        print(f'{self.post} {self.name} решил выпить кофе {coffee}')

    def sleep(self, minutes : int):
        print(f'{self.post} {self.name} заснул на {minutes} минут')

class Boss(OfficeWorker):
    def organize_meetitng(self):
        print(f'{self.post} {self.name} организует совещание')

    def drink_coffee(self, coffee : str):
        super().drink_coffee(coffee)
        print(f"{self.post} {self.name} закрылся в своём личном кабинете")

class Secretary(OfficeWorker):
    def working_with_doсuments(self):
        print(f'{self.post} {self.name} работает с документами')

class Accountant(OfficeWorker):
    def calculate_salary(self):
        print(f'{self.post} {self.name} рассчитывает зарпату.')

class Programmer(OfficeWorker):
    def writes_program(self):
        print(f'{self.post} {self.name} дорабатывает программный код.')
        
class Plankton(OfficeWorker):
    def work(self):
        print(f'{self.post} {self.name} выполняет ИБД')

boss = Boss('Иван Иванович', 'Директор', '120000')
secretary = Secretary('Жанна Васильевна','Личный секретарь руководителя', '90000')
accountant = Accountant('Вера Ивановна','Бухгалтер организации', '95000')
programer = Programmer('Илья', 'Программист', '60000')
plankton = Plankton('Вадим', 'Менеджер','80000')

boss.organize_meetitng()
boss.drink_coffee(coffee='с коньяком')
secretary.working_with_doсuments()
secretary.sleep(15)
accountant.calculate_salary()
programer.writes_program()
programer.drink_coffee(coffee='капучино')
plankton.work()