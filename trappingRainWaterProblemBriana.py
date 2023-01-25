def trapped_water(elevation_map):
    if len(elevation_map) < 3:
        totalTrappedWater = 0

    maxLeftValues = []
    maxRightValues = []

    # get maxLeftValues values
    for i in range(len(elevation_map)):
        if i == 0:
            maxLeftValues.append(0)
            continue
        previousLeftValues = elevation_map[0:i]
        maxLeftValues.append(max(previousLeftValues))

    # get maxRightValues values
    reversedList = list(reversed(elevation_map))
    print(reversedList)
    for i in range(len(reversedList)):
        if i == 0:
            maxRightValues.append(0)
            continue
        previousRightValues = reversedList[0:i]
        maxRightValues.append(max(previousRightValues))

    # Continue with the formula of the algorithm
    print(maxLeftValues)
    print(maxRightValues)


if __name__ == '__main__':
    trapped_water([4, 1, 3, 1, 5])

