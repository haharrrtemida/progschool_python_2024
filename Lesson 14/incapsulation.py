class Wallet:
    __current_balance = 0

    def get_current_balance(self):
        return self.__current_balance
    
    def change_balance(self, value):
        if self.__current_balance + value <= 0:
            raise ValueError("Баланс не может быть отрицательным!")
        else:
            self.__current_balance += value


    
class Bankomat:
    def give_money(self, money, wallet : Wallet):
        if money > 0 and wallet.get_current_balance() > money:
            wallet.change_balance(money)
        else:
            raise ValueError("Недостаточно средств")



wallet = Wallet()
bankomat = Bankomat()

print(wallet.get_current_balance())
wallet.change_balance(1000)
print(wallet.get_current_balance())

bankomat.give_money(10000, wallet)
print(wallet.get_current_balance())