while True:
    n1 = int(input("Enter first number:"))
    n2 = int(input("Enter second number:"))
    n3 = int(input("Enter third number:"))
    n4 = int(input("Enter fourth nunber:"))
    try:
        max_price = n1
        if n2 > n1:
            max_price = n2
        if n3 > n2:
            max_price = n3
        if n4 > n3:
            max_price = n4
        print("Max price is", max_price)
    finally:
        print("Another example?")
    print()