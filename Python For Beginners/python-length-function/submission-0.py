def get_longer_word(word1: str, word2: str) -> str:
    count_word1 = len(word1)
    count_word2 = len(word2)

    if count_word1 > count_word2:
        return word1
    elif count_word2 > count_word1:
        return word2
    else:
        return word1    


# do not modify below this line
print(get_longer_word("yellow", "orange"))
print(get_longer_word("red", "blue"))
print(get_longer_word("green", "blue"))
