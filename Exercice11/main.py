def design_print(func):
    def wrapper(*args, **kwargs):
        print("=======================")
        res = func(*args, **kwargs)
        print("=======================")
        return res

    return wrapper


class BankAccount:
    def __init__(self, account_holder: str, balance: float):
        self.account_holder = account_holder
        self.balance = balance

    @design_print
    def deposit(self, amount: int):
        self.balance += amount
        print(f"Vous avez déposé: {amount}€")

    @design_print
    def withdraw(self, amount: int):
        if amount > self.balance:
            print(f"Retrait de {amount}€ refusé votre solde est insuffisant")
            print(f"Solde disponible: {self.balance}€")
            return
        self.balance -= amount
        print(f"Vous avez retiré: {amount}€")

    def display_balance(self):
        print(f"Solde: {self.balance}€, titulaire: {self.account_holder}")
        print()


account = BankAccount("Will", 15000)
account.display_balance()

account.deposit(3000)
account.display_balance()

account.withdraw(19000)

account.withdraw(10000)
account.display_balance()
