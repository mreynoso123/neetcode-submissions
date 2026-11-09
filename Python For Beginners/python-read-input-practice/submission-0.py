def add_two_numbers() -> int:
    user_input = input()
    numbers = user_input.split(",")
    index0 = int(numbers[0])
    index1 = int(numbers[1])
    
    return index0 + index1



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
