import time
from threading import Thread

class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power



    def run(self):
        bots= 100
        days = 0
        print(f"{self.name}, на нас напали!")
        while bots > 0:
            days += 1
            bots -= self.power
            time.sleep(1)
            print(f"{self.name}, сражается  {days} дней(дня), осталось {bots} войнов")

        print(f"{self.name}, одержал победу спустя {days} дней(дня)!")


def main():

    first_knight = Knight("Sir Lancelot", 10)

    second_knight = Knight("Sir Galahad", 20)

    first_knight.start()
    second_knight.start()
    first_knight.join()
    second_knight.join()
    print("Все войны окончены, мы одержали победу!")


if __name__ == "__main__":
    main()
