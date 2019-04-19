max_range = 20

print('=' * 80)
print('Least Common Multiple - The smallest number divisible by numbers from 1 to {}'.format(max_range))
print()


my_list = []
for num in range(2, max_range+1):
    help_num = num
    decom = []  # Decomposition of number to prime numbers
    while True:
        for divisor in range(2, max_range+1):
            if help_num % divisor == 0:
                decom.append(divisor)
                help_num = int(help_num/divisor)
                break
        if help_num == 1:
            break
    if help_num != 1:
        decom.append(help_num)

    help = []
    help.extend(my_list)
    count = len(decom)
    for x in range(count):
        if decom[x] in help:
            del help[help.index(decom[x])]
        else:
            my_list.append(decom[x])

result = 1
for i in my_list:
    result *= i

print('Result: The smallest number divisible by numbers from 1 to {} is {}'. format(max_range, result))
