import os
def clear_console():
    os.system('cls')
def menu():
    while 1 == 1:
        def triangle_area():
            print("\n\n")
            print("Calculate the triangle's Area\n")
            print("what would you like to do?\n")
            print("1 - Calculate\n")
            print("2 - Back to menu\n")
            answer = int(input())
            if answer == 1:
                height = float(input("Enter height...\n"))
                base = float(input("Enter base...\n"))
                area = float(height * base)
                print("The triangle's area is " + str("{:.2f}".format(area)))
                triangle_area()
            elif answer == 2:
                a = False
                clear_console()
            else:
                clear_console()
                triangle_area()
        def sum_numbers():
            print("\n\n")
            print("Sum two numbers\n")
            print("what would you like to do?\n")
            print("1 - Calculate\n")
            print("2 - Back to menu\n")
            answer = int(input())
            if answer == 1:
                a = float(input("Enter the first number\n"))
                b = float(input("Enter the second number\n"))
                c = float(a + b)
                print("The result is " + str(c))
                sum_numbers()
            elif answer == 2:
                a = False
                clear_console()
            else:
                clear_console()
                sum_numbers()
        def area_square():
            print("Calculate the area and perimeter of a square\n")
            print("what would you like to do?\n")
            print("1 - Calculate\n")
            print("2 - Back to menu\n")
            answer = int(input())
            if answer == 1:
                a = float(
                    input("Enter the value of the side of the square \n"))
                area = float(a * a)
                perimeter = float(4 * a)
                print("The area value is" + " " + str(area))
                print("The perimeter value is" + " " + str(perimeter))
                area_square()
            elif answer == 2:
                a = False
                clear_console()
            else:
                clear_console()
                area_square()
        def euro_dolar():
            print("Euro to Dollar")
            print("what would you like to do?\n")
            print("1 - Calculate\n")
            print("2 - Back to menu\n")
            answer = int(input())
            if answer == 1:
                print("Enter the amount in euros\n")
                euro = float(input("€:"))
                rateEurToUsd = 1.05
                EurToUsd = float(euro * rateEurToUsd)
                print("€" + str(euro) + " equals $" +
                      str("{:.2f}".format(EurToUsd)))
                euro_dolar()
            elif answer == 2:
                a = False
                clear_console()
            else:
                clear_console()
                euro_dolar()
        def volume():
            print("Area and volume of a cylinder")
            print("what would you like to do?\n")
            print("1 - Calculate\n")
            print("2 - Back to menu\n")
            answer = int(input())
            if answer == 1:
                radius = float(input("Enter radius\n"))
                height = float(input("Enter the height\n"))
                pi = float(3.14159265359)
                volume = float((pi * (radius * radius) * height))
                area = float(2 * pi * radius * height + 2 * pi)
                print("The value of the surface area is" + " " +
                      str("{:.2f}".format(area)))
                print("The volume value is" + " " +
                      str("{:.2f}".format(volume)))
                volume()
            elif answer == 2:
                a = False
                clear_console()
            else:
                clear_console()
                volume()
        def radius():
            print("Radius and Area of a Circle")
            print("what would you like to do?\n")
            print("1 - Calculate\n")
            print("2 - Back to menu\n")
            answer = int(input())
            if answer == 1:
                radius = float(input("Enter radius\n"))
                pi = float(3.14159265359)
                area = float(pi * radius)**2
                circumferenceLength = float(2 * pi * radius)
                print("The area value is" + " " + str("{:.2f}".format(area)))
                print("The circumference length value is " +
                      str("{:.2f}".format(circumferenceLength)))
                radius()
            elif answer == 2:
                a = False
                clear_console()
            else:
                clear_console()
                print("Enter a valid option")
                radius()
        def average():
            print("Average of three numbers")
            print("what would you like to do?\n")
            print("1 - Calculate\n")
            print("2 - Back to menu\n")
            answer = int(input())
            if answer == 1:
                a = float(input("Enter the first number \n"))
                b = float(input("Enter the second number \n"))
                c = float(input("Enter the third number\n"))
                average = (a + b + c) / 3
                print("The average value is" + " " + str(average))
                average()
            elif answer == 2:
                a = False
                clear_console()
            else:
                clear_console()
                print("Enter a valid option")
                average()
        print("What would you like to do?\n")
        print("1 - Calculate the area of a triangle\n")
        print("2 - Sum two numbers\n")
        print("3 - Calculate the area and perimeter of a Squeare\n")
        print("4 - Convert Euros to Dollars\n")
        print("5 - Calculate the Area and Volume of a Cylinder\n")
        print("6 - Calculare the Area and Radius of a Circle\n")
        print("7 - Get the average between 3 numbers\n")
        print("8 - Close\n")
        answer = int(input("i want to: "))
        if answer == 1:
            a = True
            clear_console()
            triangle_area()
        elif answer == 2:
            clear_console()
            sum_numbers()
        elif answer == 3:
            clear_console()
            area_square()
        elif answer == 4:
            clear_console()
            euro_dolar()
        elif answer == 5:
            clear_console()
            volume()
        elif answer == 6:
            clear_console()
            radius()
        elif answer == 7:
            clear_console()
            average()
        elif answer == 8:
            exit()
        else:
            clear_console()
            print("Please enter a valid option")
menu()
