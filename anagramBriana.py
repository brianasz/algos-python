def anagram1(word1, word2):
    sizeWord1 = len(word1)
    sizeWord2 = len(word2)

    if sizeWord1 != sizeWord2:
        return False
    else:
        for i in word1:
            if i not in word2:
                return False
        return True


def anagram2(s1, s2):
    sizeString1 = len(s1)
    sizeString2 = len(s2)

    if sizeString1 != sizeString2:
        return False

    s1 = sorted(s1)
    s2 = sorted(s2)

    print(s1)
    print(s2)

    for i in range(sizeString1):
        if s1[i] != s2[i]:
            return False
    return True


if __name__ == '__main__':
    print(anagram2('restful anabri','fluster briana'))