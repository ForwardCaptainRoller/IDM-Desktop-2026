class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity


class Store:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        self.products.append(Product(name, price, quantity))

    def print_report(self):
        print("Store Inventory")
        print("===============")

        total = 0

        for product in self.products:
            value = product.total_value()
            total += value
            print(f"{product.name} | ${product.price:.2f} | {product.quantity} units | ${value:.2f}")

        print("===============")
        print(f"Total Inventory Value: ${total:.2f}")


store = Store()

store.add_product("Laptop", 899.99, 5)
store.add_product("Keyboard", 79.50, 12)
store.add_product("Mouse", 39.99, 20)
store.add_product("Monitor", 249.99, 8)

store.print_report()
