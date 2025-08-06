while True:
    side_a = float(input("Enter side A:"))
    side_b = float(input("Enter side B:"))
    side_c = float(input("Enter side C:"))
    try:
        if ((side_a+side_b) < side_c) or ((side_a+side_c) < side_b) or ((side_b+side_c) < side_a):
            print("Such triangle is not defined")
        else:
            print("Such triangle is defined")
    finally:
        print()

