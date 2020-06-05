from random import randint

array1 = [randint(0, 10) for i in range(10)]
array2 = []
array3 = []


# Сортровка пузырьком
def bubbleSortUnic(array1, array2):
    pass
    for x in range(0, len(array1)):
        for y in range(0, len(array1)):
            if array1[x] > array1[y]:
                array1[x] = array1[x] + array1[y]
                array1[y] = array1[x] - array1[y]
                array1[x] = array1[x] - array1[y]

    print(array1)

    # Уникальные значения
    for x in array1:
        if x not in array2:
            array2.append(x)

    print(len(array2))


def countingSequence(array1, array2, array3):
    c = 0
    for x in range(0, len(array1)):
        if x + 1 == len(array1):
            array2.append(c)
            array3.append(array1[x])
            break
        if array1[x] != array1[x + 1]:
            array2.append(c)
            array3.append(array1[x])
            c = 0
        c = c + 1

    print("Массив")
    print(array1)
    print("значения")
    print(array3)
    print("Количество")
    print(array2)


def bubbleSortOff(array1):
    for i in range(len(array1) - 1):
        isChange = False
        for j in range(len(array1) - i - 1):
            if array1[j] > array1[j + 1]:
                array1[j], array1[j + 1] = array1[j + 1], array1[j]
                isChange = True
        if not isChange:
            print("final")
            print(array1)
            break

bubbleSortOff(array1)


arrays = [
    {"date": "25.06.04",
     "name": "q"},
    {"date": "25.06.04",
     "name": "w"},
    {"date": "23.06.04",
     "name": "s"},
    {"date": "22.06.04",
     "name": "d"},
    {"date": "22.06.04",
     "name": "a"},
    {"date": "22.06.04",
     "name": "a"}]

arrays2 = []
arrays3 = []
for i in range(0, len(arrays)):
    print(arrays[i])
    if i + 1 == len(arrays):
        if arrays[i]["date"] != arrays[i - 1]["date"]:
            arrays2.append({arrays[i]["date"]: {}})
        if arrays[i]["date"] == arrays[i - 1]["date"]:
            arrays2.append({arrays[i]["date"]: {}})
        break
    if arrays[i]["date"] != arrays[i + 1]["date"]:
        arrays2.append({arrays[i]["date"]: {}})
print(arrays2)
arrays3 = arrays2.keys()
print(arrays3)
for i in range(0, len(arrays2)):
    for j in range(0, len(arrays)):

        if arrays2[i] == arrays[j]["date"]:
            arrays2[i].append(arrays["name"])

print(arrays2)