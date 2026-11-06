from typing import List

def read_integers() -> List[int]:
    number_input = input()
    string_list = number_input.split(",")
    for item in range(len(string_list)):
        string_list[item] = int(string_list[item])
    return string_list


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
