# 3.	Задайте список из k чисел последовательности (1 + 1\k)^k и выведите на экран их сумму.

k = int(input("Введите  размер списка: "))
i=1
list=[]
sum=0
while i<k+1:
  number = round((1+1/i)**i, 2)
  sum=sum+number
  list.append(number)
  i+=1  
print(list)
print(f'Сумма чисел списка равна {sum}')
