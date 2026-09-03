from typing import List

def contains_duplicate(words: List[str]) -> bool:
    my_set = set(words) #convert a copy of the list to a set
    if len(words) > len(my_set):
        return True
    return False

# do not modify code below this line
print(contains_duplicate(["hello", "world", "hello"]))
print(contains_duplicate(["hello", "world", "i", "am", "great"]))
print(contains_duplicate(["hello", "hello", "hello"]))
print(contains_duplicate(["Hello", "hellooo", "hello"]))
