                                                    # Задание семь
print("Колличество элементов массива: ")

print(*[int(input()) for _ in range(int(input()))][::-1])

                                                   # задание второе

def rcr(a):
    res = [a[-1]]
    res += a[:n-1]
    return res
 
n = int(input('n = '))
lst = [x for x in input().split()]
print(*rcr(lst))

                                                  # Третье Задание

print("Масса которую выдерживает лодка: ")
m = int(input())
n = int(input())
a = []
b = []
for i in range(n):
    a.append(int(input()))
 
for x in range(len(a)):
    if a[x] + min(a) <= m:
        b += [[a[x], min(a)]]
        a[x] += m
        a[a.index(min(a))] += m
    else:
        if a[x] > m:
            continue
        else:
            b += [[a[x]]]
print(len(b))