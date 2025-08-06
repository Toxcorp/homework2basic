while True:
    flat_number = int(input("Enter the flat number:"))
    floor_total = 9
    flatpfloor = 4
    try:
        x = (flat_number/flatpfloor)
        if (x > floor_total):
            y = (x / 2)
            if (y > 9):
                z = x / 3
                if (z > 9):
                    j = floor_total - ((144 - flat_number) // 4)
                    print("Part 4, floor:", int(j))
                else:
                    h = floor_total - ((108 - flat_number) //4)
                    print("Part 3, floor:", int(h))
            else:
                f = floor_total - ((72 - flat_number) // 4)
                print("Part 2, floor:", int(f))
        else:
            if flat_number % 4 != 0:
                t = ((x+1) // 1)
                print("Part 1, floor:", int(t))
            else:
                print("Part 1, floor:",int(x))
    
    finally:
        print()