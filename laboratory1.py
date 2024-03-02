import datetime


with open('data1.txt', 'r', encoding='utf-8') as file:
    arr = [int(i) for i in file.read().split()]
founder = int(input())
binarr = sorted(arr)
t1 = datetime.datetime.now(datetime.timezone.utc)
for i in range(len(arr)):
    if founder == arr[i]:
        print(i)
        t2 = datetime.datetime.now(datetime.timezone.utc)
        break
print(t2 - t1)
t3 = datetime.datetime.now(datetime.timezone.utc)
for j in range(len(binarr)):
    if founder == binarr[j]:
        print(j)
        t4 = datetime.datetime.now(datetime.timezone.utc)
        break
print(t4 - t3)