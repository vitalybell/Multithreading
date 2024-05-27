import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, skill):
        threading.Thread.__init__(self)
        self.name = name
        self.skill = skill
        self.enemies_remaining = 100

    def run(self):
        days = 0
        while self.enemies_remaining > 0:
            self.enemies_remaining -= self.skill
            days += 1
            time.sleep(1)  # Один день проходит за 1 секунду
            print(f"  {self.name} сражается  {days} день(дня), осталось воинов: {self.enemies_remaining}  ")
        print(f"{self.name} одержал победу {days} дней.")


# Создание Рыцарей
knight1 = Knight("Sir Lancelot", 10)
knight2 = Knight("Sir Galahad", 20)


print('Sir Lancelot! на нас напали')
print('Sir Galahad! на нас напали')