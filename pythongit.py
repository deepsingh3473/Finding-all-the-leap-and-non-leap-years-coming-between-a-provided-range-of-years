year1 = int(input("Enter a starting year: "))
year2 = int(input("Enter a ending year: "))
leap = []
non_leap = []
for i in range(year1, year2 + 1):
    if i % 4 == 0:
        if i % 100 != 0:
            leap.append(i)
        else:
            if i % 400 == 0:
                leap.append(i)
            else:
                non_leap.append(i)
    else:
        non_leap.append(i)

print("Leap years are:", leap)
print("Non-Leap years are:", non_leap)