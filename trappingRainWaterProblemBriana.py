def max_left_values(elevation_map):
    maxLeftValues = []

    # get maxLeftValues values
    for i in range(len(elevation_map)):
        if i == 0:
            maxLeftValues.append(0)
            continue
        previousLeftValues = elevation_map[0:i]
        maxLeftValues.append(max(previousLeftValues))
    return maxLeftValues


def max_right_values(elevation_map):
    maxRightValues = []

    # get maxRightValues values
    reversedList = list(reversed(elevation_map))
    for i in range(len(reversedList)):
        if i == 0:
            maxRightValues.append(0)
            continue
        previousRightValues = reversedList[0:i]
        maxRightValues.append(max(previousRightValues))
    return maxRightValues


def apply_formula(elevation_map):
    trappedWaterList = []
    maxRightValues = max_right_values(elevation_map)
    maxLeftValues = max_left_values(elevation_map)

    for i in range(len(elevation_map)):
        height = elevation_map[i]
        maxLeft = maxLeftValues[i]
        maxRight = maxRightValues[i]

        formula = min(maxLeft, maxRight) - height

        trappedWaterList.append(formula)
    return trappedWaterList


def trapped_water(elevation_map):
    totalTrappedWater = 0
    if len(elevation_map) < 3:
        return totalTrappedWater

    trappedWaterListResults = apply_formula(elevation_map)

    for i in range(len(trappedWaterListResults)):
        if trappedWaterListResults[i] < 0:
            trappedWaterListResults[i] = 0
        totalTrappedWater += trappedWaterListResults[i]

    return totalTrappedWater


if __name__ == '__main__':
    print(trapped_water([4, 1, 3, 1, 5]))
