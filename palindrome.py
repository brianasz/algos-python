def palindrome(s):
    originalString = s
    reverseString = reverse(s)

    if originalString == reverseString:
        return True
    return False


# 0(N) linear running time where N is the number of letters in string s N=len(s)
def reverse(data):
    data = list(data)
    # pointing to the first item
    start_index = 0
    # pointing to the end item
    end_index = len(data) - 1

    while end_index > start_index:
        # keep swapping the items
        data = list(data)
        data[start_index], data[end_index] = data[end_index], data[start_index]
        start_index = start_index + 1
        end_index = end_index - 1

    return ''.join(data)


def palindrome_python(s):
    if s == s[::-1]:
        return True
    return False


if __name__ == '__main__':
    print(palindrome('kevin'))
