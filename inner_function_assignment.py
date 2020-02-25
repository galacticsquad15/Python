def main():
    message = measurements([2.1, 3.4])
    print(message)

def measurements(list):
    myArea = area(list)
    myPerimeter = perimeter(list)
    message = 'Perimeter = %.2f Area = %.2f' % (myPerimeter, myArea)

    return message

def area(areaList):
    myList = []

    for i in areaList:
        myList.append(i)

    if len(myList) == 1:
        shapeArea = float(myList[0] * myList[0])
    else:
        shapeArea = float(myList[0] * myList[1])

    return float(shapeArea)


def perimeter(perimeterList):
    myList = []

    for i in perimeterList:
        myList.append(i)

    if len(myList) == 1:
        shapePerimeter = myList[0] + myList[0] + myList[0] + myList[0]
    else:
        shapePerimeter = myList[0] + myList[0] + myList[1] + myList[1]

    return shapePerimeter


if __name__ == '__main__':
    main()