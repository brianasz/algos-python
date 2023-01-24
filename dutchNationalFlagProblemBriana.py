def dutch_national_flag_problem1(array):
    indexPosition = 0
    if indexPosition == 0 and array[indexPosition] > array[indexPosition+1]:
        array[indexPosition], array[indexPosition + 1] = array[indexPosition + 1], array[indexPosition]

    for indexPosition in range(1, len(array)-1):
        goDown = indexPosition
        while goDown > 0:
            if array[goDown] < array[goDown - 1]:
                array[goDown], array[goDown - 1] = array[goDown - 1], array[goDown]
            goDown = goDown - 1

        goUp = indexPosition
        while goUp < len(array)-1:
            if array[goUp] > array[goUp + 1]:
                array[goUp], array[goUp + 1] = array[goUp + 1], array[goUp]
            goUp = goUp + 1
    return array


def dutch_national_flag_problem2(array):
    pivot = 1
    
    # check if number is less than pivot

    # check if number if equal to pivot

    # check if if number is greater than pivot
    indexPosition = 0
    if indexPosition == 0 and array[indexPosition] > array[indexPosition+1]:
        array[indexPosition], array[indexPosition + 1] = array[indexPosition + 1], array[indexPosition]

    for indexPosition in range(1, len(array)-1):
        goDown = indexPosition
        while goDown > 0:
            if array[goDown] < array[goDown - 1]:
                array[goDown], array[goDown - 1] = array[goDown - 1], array[goDown]
            goDown = goDown - 1

        goUp = indexPosition
        while goUp < len(array)-1:
            if array[goUp] > array[goUp + 1]:
                array[goUp], array[goUp + 1] = array[goUp + 1], array[goUp]
            goUp = goUp + 1
    return array


if __name__ == '__main__':
    array1 = [2, 1, 0, 0, 1, 2]
    array2 = [0, 1, 2, 1, 2, 0, 0]

    print(dutch_national_flag_problem1(array1))
    print(dutch_national_flag_problem1(array2))
