from math import sqrt, ceil


order_max = 10000  # Only for first X Prime numbers
div_possible = 0
primenum_list = [2, 3, 5, 7, 11, 13, 17, 19]  # First 8 prime numbers

while True:
    for num in range(21, 999999999999, 2):  # Even numbers are not Prime numbers
        if num % 3 != 0 and num % 5 != 0 and num % 7 != 0 and num % 11 != 0 and num % 13 != 0 and num % 17 != 0 and num % 19 != 0:
            for divisor in range(1, ceil(sqrt(num+1))):
                if num % divisor == 0:
                    div_possible += 1
            if div_possible == 1:
                primenum_list.append(num)
            div_possible = 0
        if len(primenum_list) == order_max:
            break
    break


input_num = input('''Zadej pořadí hledaného prvočísla (max {}).
Můžeš zadat i více hodnot oddělených čárkou: '''.format(order_max))

input_num = list(input_num.split(','))
for i, num in enumerate(input_num):
    num = int(num.strip())
    input_num[i] = num

rank_num = []
for num in input_num:
    if 0 < num < (order_max + 1):
        rank_num.append(num)

for num in rank_num:
    print('Prvočíslo s pořadím {} je {}.'.format(num, primenum_list[num-1]))
