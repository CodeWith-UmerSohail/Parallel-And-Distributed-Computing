import Pyro4

@Pyro4.expose
class BankService:
    def __init__(self):
        self.balance = 5000

    def get_balance(self, name):
        return f"Hello {name}, your current balance is Rs. {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return f"Deposit successful! New balance: Rs. {self.balance}"


daemon = Pyro4.Daemon()
ns = Pyro4.locateNS()

uri = daemon.register(BankService)
ns.register("bank.server", uri)

print("🏦 Bank Server is running...")
daemon.requestLoop()
