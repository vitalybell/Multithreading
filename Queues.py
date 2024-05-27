import threading
import queue
import time


class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False


class Cafe:
    def __init__(self, tables):
        self.queue = queue.Queue()
        self.tables = tables

    def customer_arrival(self):
        for i in range(20):
            time.sleep(1)
            customer = Customer(i+1, self)
            customer.start()

    def serve_customer(self, customer):
        for table in self.tables:
            if not table.is_busy:
                table.is_busy = True
                print(f"Посетитель номер {customer.id} сел за стол {table.number}.")
                time.sleep(1)
                table.is_busy = False
                print(f"Посетитель номер {customer.id} покушал и ушел.")
                return
        self.queue.put(customer)
        print(f"Посетитель номер {customer.id} ожидает свободный стол.")


class Customer(threading.Thread):
    def __init__(self, id, cafe):
        super().__init__()
        self.id = id
        self.cafe = cafe

    def run(self):
        print(f"Посетитель номер {self.id} прибыл.")
        self.cafe.serve_customer(self)


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]


cafe = Cafe(tables)


customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()


customer_arrival_thread.join()