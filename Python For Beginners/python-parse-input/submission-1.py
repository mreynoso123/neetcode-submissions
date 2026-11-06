from typing import List

def read_integers() -> List[int]:
    line = input()
    strings = line.split(",")
    list = []
    for string in strings:
        list.append(int(string))
    return list

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
