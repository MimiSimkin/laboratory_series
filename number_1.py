import random


with open('data1.txt', 'w', encoding='utf-8') as file:
    for i in range(100000):
        num = random.randint(-10**5, 10**5)
        file.write(str(num) + ' ')