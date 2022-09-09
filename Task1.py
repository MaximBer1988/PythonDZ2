# 1.Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# 1.	Пример:
# 0,56 -> 11

n = float(input("Введите вещественное число: "))
sum = 0
to_string = str(n)
temp_list = to_string.split('.')
one_digit= temp_list[0]+temp_list[1]
length=len(one_digit)
i=0
while i<length:
  sum=sum+int(one_digit[i])
  i=i+1
print(sum)
