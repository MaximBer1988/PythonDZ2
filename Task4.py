# 4.	Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.
import random
n = int(input("Введите  размер списка: "))
i=0
list=[]
result=1
while i<n:
  number = random.randint(-n,n)
  result=result*number
  list.append(number)
  i+=1  
print(list)
print(result)  
