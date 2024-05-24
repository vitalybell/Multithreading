from threading import Thread
from time import sleep


def func():
    print(f'Началось   ')
    sleep(0.1)
    for a in "abcdefghij":
        print(f'letter: {a} ')
        sleep(1)


th = Thread(target=func)
th.start()
for i in range(10):
    print(f'Number: {i} ')
    sleep(1)

print(' Финиш! ')


th.join()
