with open('data1.txt', 'r', encoding='utf-8') as file:
    g = open('tutorial.txt', 'a', encoding='utf-8')
    arr = [int(i) for i in file.read().split()]
    founder = int(input())
    binarr = sorted(arr)
    for i in range(len(arr)):
        if founder == arr[i]:
            print(i)
            break
    print(i)
    for j in range(len(binarr)):
        if founder == binarr[j]:
            print(j)
            break
    print(j)
    g.write(str(i) + ' ' + str(j) + '\n')
    g.close()