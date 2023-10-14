                                                    # Задание семь

N = int(input("Введите количество элементов списка "))

spisok = list(map(int, input().split()))[:N]

e = set(spisok)

print(len(e))

                                                   # задание второе

a = set(input().split())

b = set(input().split())

print (len(a.intersection(b)))     

                                                  # Третье Задание

a = set()

for i in input().split():

 if i not in a:

  a.add(i)

 print('NO')

else:

 print('YES')                                                  
