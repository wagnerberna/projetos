def is_palindrome_recursive(word, low_index, high_index):
    print(word, low_index, high_index)
    if word == "":
        return False
    if word[low_index] != word[high_index]:
        return False
    if low_index == high_index:
        return True
    low_index += 1
    high_index -= 1

    return is_palindrome_recursive(word, low_index, high_index)


word_test = "REVIVER"
print(is_palindrome_recursive(word_test, 0, len(word_test) - 1))
