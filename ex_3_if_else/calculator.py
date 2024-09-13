print("Welcome to the tip calculator!")

bill = float(input("What was the total bill?: $"))
tip = float(input("What was the total bill? 10, 12 or 15?: "))*0.01
split = int(input("How many people to split the bill?: "))

pay_for_person = (bill+(bill*tip))/split

print("Each person shold pay " + "$" + str(pay_for_person))