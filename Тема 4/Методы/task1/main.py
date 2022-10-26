def get_list_number_divisors(number):
    ...  # TODO найти список делителей числа number
    list_[]
     for division in range(1, number+1):
        if number % division == 0:
            list_append(division)
            return list_


print(get_list_number_divisors(23))
print(get_list_number_divisors(2 ** 16))
