def leapyear(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                print("leap year")
            else:
                print("Not a leap year")
        else:
            print("Leap year")
year=int(input("Enter a year:"))
leapyear(year)
