def palindrome(word):
    # pointing to the first item
    start_index = 0
    # pointing to the end item
    end_index = len(word) - 1

    for i in range(len(word)-1):
        if word[start_index + i] == word[end_index - i]:
            if start_index + i == end_index - i:
                return True
        else:
            return False


if __name__ == '__main__':
    print(palindrome('briana'))