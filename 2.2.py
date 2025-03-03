class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Jumlah deposit harus lebih dari nol!")
            self.balance += amount
            print(f"Deposit sebesar {amount} berhasil dilakukan. saldo sekarang: {self.balance}")
        except ValueError as e:
            print(e)

    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise ValueError("Saldo tidak cukup untuk melakukan penarikan!")
            self.balance -= amount
            print(f"Penarikan sebesar {amount} berhasil dilakukan. saldo sekarang: {self.balance}")
        except Exception as e:
            print(e)

# membuat objek dari class BankAccount
my_account = BankAccount(1000)

# melakukan deposit sebesar -500 (akan menghasilkan ValueError)
my_account.deposit(-500)

# melakukan deposit sebesar 500 (berhasil)
my_account.deposit(500)
