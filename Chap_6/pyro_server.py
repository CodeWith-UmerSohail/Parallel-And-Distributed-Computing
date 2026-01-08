import Pyro4


@Pyro4.expose
class StoreServer(object):

    def get_price(self, product):
        prices = {
            "laptop": 120000,
            "mobile": 60000,
            "headphones": 8000
        }
        return prices.get(product.lower(), "Product not available")

    def calculate_bill(self, price, quantity):
        return f"Total Bill = Rs. {price * quantity}"


def startServer():
    server = StoreServer()
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()

    uri = daemon.register(server)
    ns.register("store.server", uri)

    print("🛒 Store Server is running...")
    print("URI:", uri)

    daemon.requestLoop()


if __name__ == "__main__":
    startServer()
