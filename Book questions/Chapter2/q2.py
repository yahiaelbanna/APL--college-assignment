class Positive:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name, 0)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"{self.name} must be non-negative")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class BankAccount:
    balance = Positive("balance")

    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


account = BankAccount(100)
print(f"Initial balance: ${account.balance}")

account.deposit(50)
print(f"After deposit: ${account.balance}")

account.withdraw(30)
print(f"After withdrawal: ${account.balance}")
