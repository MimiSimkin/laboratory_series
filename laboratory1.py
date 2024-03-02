with open('data1.txt', 'r', encoding='utf-8') as file:
    arr = [int(i) for i in file.read().split()]
founder = int(input())
binarr = sorted(arr)
for i in range(len(arr)):
    if founder == arr[i]:
        print(i)
        break
for j in range(len(binarr)):
    if founder == binarr[j]:
        print(j)
        break


with open('tutorial.txt', 'w', encoding='utf-8') as gifa:
    gifa.write(str(i) + ' ' + str(j) + '\n')