class Product:
    name = str()
    weight = float()
    category = str()

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return str(f'{self.name}, {self.weight}, {self.category}')

class Shop (Product):

    def __init__(self, name, weight, category, __file_name = 'products.txt'):
        super().__init__(name, weight, category)
        self.__file_name = __file_name

    def get_products(self):
        from pprint import pprint
        products = open(self.__file_name, 'r')
        pprint(products.read())
        products_list = products.read()
        products.close()
        print(f'{products_list}')

    def add(self, *products):
        self.get_products()
        for product in products:
            product_item = str(product)
            products = open(self.__file_name, 'r')
            products_list = products.read()
            products.close()
            if product_item in products_list:
                print(f'\n{product_item} уже есть в магазине\n')
            else:
                products = open(self.__file_name, 'a')
                products.write(f'\n{product_item}\n')
                products.close()

# product = Product('Potato', 28.5, 'Vegetables')
# print(product)

s1 = Shop('', 0, '')
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

















