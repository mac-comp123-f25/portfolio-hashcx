original_money = 732
money = original_money

dollars = money // 100
money = money % 100

quarters = money // 25
money = money % 25

dimes = money // 10
money = money % 10

nickels = money // 5
money = money % 5

print("Making chane for " + str(original_money) + " cents:")
print(" Dollars: " + str(dollars))
print(" Quarters: " + str(quarters))
print(" Dimes: " + str(dimes))
print(" Nickels: " + str(nickels))
print(" Pennies: " + str(money))
