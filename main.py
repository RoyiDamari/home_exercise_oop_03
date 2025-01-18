import sqlite_lib as sl
from FoodProduct import FoodProduct
from datetime import datetime

def main():

    sl.connection("food_products.db")

    sl.run_query_update('''
    CREATE TABLE IF NOT EXISTS FoodProduct (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        category TEXT NOT NULL,
        production_date TEXT NOT NULL,
        expiration_date TEXT NOT NULL);
    ''')

    def insert_product(product):
        sl.run_query_update('''
           INSERT INTO FoodProduct (name, price, category, production_date, expiration_date)
           VALUES (?, ?, ?, ?, ?);
           ''', (product.name, product.price, product.category,
                 product.production_date.strftime('%Y-%m-%d %H:%M:%S'),
                 product.expiration_date.strftime('%Y-%m-%d %H:%M:%S')))

    def print_all_products() -> list[FoodProduct]:
        result = sl.run_query_select('''
            SELECT * FROM FoodProduct;
        ''');

        list_result = []
        for product in result:
            new_product = FoodProduct(product['id'], product['name'], product['price'],
                                      product['category'],
                                      datetime.strptime(product['production_date'], '%Y-%m-%d %H:%M:%S'),
                                      datetime.strptime(product['expiration_date'], '%Y-%m-%d %H:%M:%S'))
            list_result.append(new_product)
        return list_result

    product1 = FoodProduct(None,'chocolate_milk', 12.7, 'milk',
                           datetime(2025, 1, 10, 14, 30),
                           datetime(2025, 1, 20, 14, 30))
    product2 = FoodProduct(None, 'buns', 13.9, 'bread',
                           datetime(2025, 1, 10, 14, 30),
                           datetime(2025, 1, 28, 14, 30))

    # insert_product(product1)
    # insert_product(product2)

    product_list = print_all_products()
    print(product_list)
    print(product_list[0] + 5)
    print(product_list[0] - 5)
    print(product_list[0] * 2)
    print(product_list[0] == product_list[1])
    print(product_list[0] == 12)
    print(product_list[0] != product_list[1])
    print(product_list[0] != 12)
    print(product_list[0] > product_list[1])
    print(product_list[0] > 12)
    print(product_list[0] < product_list[1])
    print(product_list[0] < 12)
    print(len(product_list[0]))
    print(hash(product_list[0]))
    print(hash(product_list[1]))

    product3 = FoodProduct(3, 'entrecote', 12.7, 'meat',
                           datetime(2025, 1, 10, 14, 30),
                           datetime(2025, 1, 20, 14, 30))

    # product3.name = 'ab'
    # product3.name = 'porterhouse'
    product3.name = 'filet'
    print(product3.name)

    # product3.price = 102
    product3.price = 90
    print(product3.price)

    # product3.category = 'bread'
    product3.category = 'fur'
    print(product3.category)

    # product3.production_date = datetime(2025, 2, 20, 14, 30)
    product3.production_date = datetime(2025, 1, 15, 14, 30)
    print(product3.production_date)

    # product3.expiration_date = datetime(2025, 1, 22, 14, 30)
    product3.expiration_date = datetime(2025, 2, 20, 14, 30)
    print(product3.expiration_date)

    print(product3.remaining)


    sl.close()


if __name__ == "__main__":
    main()