while True:
    year = int(input("Enter year:"))
    try:
        if year % 400 == 0:
            print("This is leap year")
        elif year % 4 == 0:
            if year % 4 ==0 and year % 100 == 0:
                print("This is not a leap year")
            print("This is leap year")
        else:
            print("This is not leap year")
    finally:
        print()