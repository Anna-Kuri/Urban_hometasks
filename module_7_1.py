class Product:
    def __init__(self, name: str, weight: float, category: str) -> None:
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self) -> str:
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self) -> None:
        self.__file_name = "products.txt"

    def get_products(self) -> str:
        file = open(self.__file_name, "r")
        self.list_of_products = file.read()
        file.close()
        return self.list_of_products

    def add(self, *products: Product) -> None:
        if len(products):
            list_of_products = self.get_products()

            file = open(self.__file_name, "a")

            for product in products:
                if product.name not in list_of_products:
                    file.write(f"{product.__str__()}\n")
                else:
                    print(f"Product {product} is already in the store")

            file.close()


s1 = Shop()
p1 = Product("Potato", 50.5, "Vegetables")
p2 = Product("Spaghetti", 3.4, "Groceries")
p3 = Product("Potato", 5.5, "Vegetables")

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

