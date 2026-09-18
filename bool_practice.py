
user_number = int(input("Enter a number: "))
is_positive = user_number > 0
is_negative = user_number < 0
is_zero = user_number == 0
is_even = (user_number % 2 == 0)
is_odd = (user_number % 2 != 0)

print("Is positive:", is_positive)
print("Is negative:", is_negative)
print("Is zero:", is_zero)
print("Is even:", is_even)
print("Is odd:", is_odd)
