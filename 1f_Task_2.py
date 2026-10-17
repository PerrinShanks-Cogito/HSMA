import random

#list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random_number = [int(random.randint(1, 100)) for i in range(100)]
print(random_number)

def odd_even_checker(num):
    even_list = []
    odd_list = []

    for num in random_number:
        if num % 2 == 0:
            even_list.append(int(num))
        else:
            odd_list.append(int(num))
    return even_list, odd_list

even_numbers, odd_numbers = odd_even_checker(random_number)
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)