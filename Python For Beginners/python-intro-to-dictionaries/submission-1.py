from typing import List, Dict

def create_dict(name: str, age: int) -> Dict[str, int]:
    return {name:age}


def list_to_dict(words: List[str]) -> Dict[str, int]:
    result = {}
    for i in range(len(words)): # 0 through the length of the list
        current_word = words[i] # each string 
        result[current_word] = i # string:i where i is the index number from the list
    return result



# don't modify code below this line
print(create_dict("Alice", 25))
print(create_dict("Jane", 35))
print(create_dict("Joe", 45))

print(list_to_dict(["Alice", "Jane", "Joe"]))
print(list_to_dict(["Apple", "Banana", "Watermelon", "Pineapple"]))
