# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


array = [1, 2, 3, 4, 5]

for index in range(len(array) - 1):
    counter = 0
    while counter < len(array)-1:
        if array[counter] < array[counter+1]:
            # temp = array[counter]
            array[counter], array[counter+1] = array[counter + 1], array[counter]
            # array[counter + 1] = temp
        counter += 1

print(array)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
