# ----------------------------------------------------------------------
# Name:      store
# Purpose:   implement an online store
# Author(s):Timothy Phan & Ibrahim Dobashi
# Date:
# ----------------------------------------------------------------------
"""
This is the docstring

This is the detailed description
"""


class Product:
    """
    Represents products sold in a store

    Arguments:
    description (string): the product's description
    list_price (integer): the suggested retail price of the product

    Attributes:
    description (string): the product's description
    list_price (integer): the suggested retail price of the product
    sales (list): the actual prices each product was sold for
    reviews (list): the user reviews for each product
    stock (integer): the initial stock for each product
    id (string): the unique id for each product
    """
    # class variables
    category = 'GN'

    next_serial_number = 1

    def __init__(self, description, list_price):
        self.description = description
        self.list_price = list_price
        self.sales = []
        self.reviews = []
        self.stock = 0
        self.id = self.generate_product_id()

    def __str__(self):
        return f"{self.description}\nProduct ID:" \
               f"{self.id}\nList Price:$" \
               f"{self.list_price:.2f}\nAvailable in Stock:{self.stock}"

    def __add__(self, other):
        return Bundle(self, other)

    def restock(self, quantity):
        """
        Restocks the amount of products
        :param quantity: integer
        :return: None
        """
        self.stock += quantity

    def review(self, stars, text):
        """
        Stores the user reviews inside a list as a tuple
        :param stars: integer
        :param text: string
        :return: None
        """
        self.reviews.append((text, stars))

    def sell(self, quantity, sale_price):
        """
        Stores prices of products sold in a list based on their stock
        :param quantity: integer
        :param sale_price: integer
        :return: None
        """
        for i in range(quantity):
            if self.stock:
                self.sales.append(sale_price)
                self.stock -= 1

    @property
    def lowest_price(self):
        """
        Finds the lowest price a product was sold for
        :return: integer
        """
        if not self.sales:
            return None
        return min(self.sales)

    @property
    def average_rating(self):
        """
        Finds the average rating from the total ratings for a product
        :return: float
        """
        if not self.reviews:
            return None
        stars = [s[1] for s in self.reviews]
        return sum(stars) / len(self.reviews)

    @classmethod
    def generate_product_id(cls):
        """
        Generates a unique id for each product
        :return: string
        """
        product_id = f"{cls.category}{cls.next_serial_number:06}"
        cls.next_serial_number += 1
        return product_id


class VideoGame(Product):
    """
    Represents a video-game product
    Inherits from Product

    Arguments:
    description (string): the product's description
    list_price (integer): the suggested retail price of the product

    Attributes:
    description (string): the product's description
    list_price (integer): the suggested retail price of the product
    """
    category = 'VG'

    next_serial_number = 1

    def __init__(self, description, list_price):
        super().__init__(description, list_price)


class Book(Product):
    """
    Represents a book product
    Inherits from Product

    Arguments:
    description (string): the product's description
    list_price (integer): the suggested retail price of the product
    author (string): the name of the book's author
    pages (integer): the total pages of the book

    Attributes:
    description (string): the product's description
    list_price (integer): the suggested retail price of the product
    author (string): the name of the book's author
    pages (integer): the total pages of the book
    """
    category = 'BK'

    next_serial_number = 1

    def __init__(self, description, author, pages, list_price):
        self.author = author
        self.pages = pages
        super().__init__(description, list_price)

    def __lt__(self, other):
        return self.pages < other.pages


class Bundle(Product):
    """
    Represents a bundle of  products
    Inherits from Product

    Arguments:
    description (string): the product's description
    list_price (integer): the suggested retail price of the product
    first_product(Product): first required product object
    second_product(Product): second required product object
    *products(Product): 0 or more additional product object

    Attributes:
    description (string): the product's description
    list_price (integer): the suggested retail price of the product
    """
    category = 'BL'
    next_serial_number = 1

    bundle_discount = 20

    def __init__(self, first_product, second_product, *products):
        product_bundle = (first_product, second_product) + products

        description = " & ".join(product.description for product in
                                 product_bundle)
        list_price = sum([product.list_price for product in
                          product_bundle]) * (
                             1 - (self.bundle_discount / 100))
        super().__init__(description=description, list_price=list_price)


def main():
    sunglasses = Product('Vans Hip Cat Sunglasses', 14)
    print(Product.category)
    print(Product.next_serial_number)
    print(sunglasses.id)
    print(sunglasses.description)
    print(sunglasses.list_price)
    print(sunglasses.stock)
    print(sunglasses.reviews)
    print(sunglasses.sales)

    headphones = Product('Apple Airpods Pro', 199)
    sunglasses.restock(20)
    headphones.restock(5)
    print(sunglasses)
    print(headphones)
    sunglasses.sell(3, 14)
    sunglasses.sell(1, 10)
    print(sunglasses.sales)
    headphones.sell(8, 170)  # There are only 5 available
    print(headphones.sales)
    print(sunglasses)
    print(headphones)
    sunglasses.restock(10)
    print(sunglasses)
    headphones.restock(20)
    print(headphones)
    sunglasses.review(5, 'Great sunglasses! Love them.')
    sunglasses.review(3, 'Glasses look good but they scratch easily')
    headphones.review(4, 'Good but expensive')
    print(sunglasses.reviews)
    print(headphones.reviews)
    print(Product.category)
    print(Product.next_serial_number)
    print(sunglasses.lowest_price)
    print(sunglasses.average_rating)
    backpack = Product('Nike Explore', 60)
    print(backpack.average_rating)
    print(backpack.lowest_price)

    mario = VideoGame('Mario Tennis Aces', 50)
    mario.restock(10)
    mario.sell(3, 40)
    mario.sell(4, 35)
    print(mario)
    print(mario.lowest_price)
    mario.review(5, 'Fun Game!')
    mario.review(3, 'Too easy')
    mario.review(1, 'Boring')
    print(mario.average_rating)
    lego = VideoGame('LEGO The Incredibles', 30)
    print(lego)
    lego.restock(5)
    lego.sell(10, 20)
    print(lego)
    print(lego.lowest_price)
    print(VideoGame.category)
    print(VideoGame.next_serial_number)

    book1 = Book('The Quick Python Book', 'Naomi Ceder', 472, 39.99)
    print(book1.author)
    print(book1.pages)
    book1.restock(10)
    book1.sell(3, 30)
    book1.sell(1, 32)
    book1.review(5, 'Excellent how to guide')
    print(book1)
    print(book1.average_rating)
    print(book1.lowest_price)
    book2 = Book('Learning Python', 'Mark Lutz', 1648, 74.99)
    book1.restock(20)
    book1.sell(2, 50)
    print(book2)
    print(book1 > book2)
    print(book1 < book2)
    print(Book.category)
    print(Book.next_serial_number)
    bundle1 = Bundle(sunglasses, backpack, mario)
    print(bundle1)
    bundle1.restock(3)
    bundle1.sell(1, 90)
    print(bundle1)
    bundle1.sell(2, 95)
    print(bundle1)
    bundle1.restock(3)
    bundle1.sell(1, 90)
    print(bundle1)
    bundle1.sell(3, 95)
    print(bundle1)
    print(bundle1.lowest_price)
    bundle2 = Bundle(book1, book2)
    bundle2.restock(2)
    print(bundle2)
    print(Bundle.category)
    print(Bundle.next_serial_number)
    print(Bundle.bundle_discount)
    back_to_school_bundle = backpack + book1
    print(back_to_school_bundle)
    best_bundle = sunglasses + headphones + book1 + mario
    print(best_bundle)


if __name__ == '__main__':
    main()
