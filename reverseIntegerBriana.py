def reverse1(integer):
    toString = str(integer)
    end = len(toString) - 1
    res = ''

    for i in range(len(toString)):
        res += toString[end]
        end = end - 1
    return int(res)


def reverse2(integer):
    toString = list(str(integer))
    start = 0
    end = len(toString) - 1

    while end > start:
        toString[start], toString[end] = toString[end], toString[start]
        start = start + 1
        end = end - 1
    return ''.join(str(i) for i in toString)


def reverse3(integer):
    reversedInt = ''
    for i in range(len(str(integer))):
        reversedInt += str(integer % 10)
        integer = integer // 10
    return reversedInt


def reverse4(integer):
    result = 0

    while integer > 0:
        remainder = integer % 10
        integer = integer // 10
        result = result * 10 + remainder

    return result


if __name__ == '__main__':
    print(reverse1(56789))
    print(reverse2(56789))
    print(reverse3(56789))
    print(reverse4(56789))
