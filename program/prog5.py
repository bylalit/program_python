# Rent Calculator Mini Project


rent = int(input("Enter Your hostel/flate rent = "))
foodAmount = int(input("Enter the amount of food orderes = "))
electricity = int(input("Enter the totl of electricity spend = "))
unit = int(input("Enter the charge par unit = "))
person = int(input("Enter the number of persons living in room/flat = "))

def a():
    rentFoodBill = rent + foodAmount
    electricityBill = electricity * unit
    
    fullTotal = rentFoodBill + electricityBill
    
    final = int(fullTotal / person)
    return final
    
    
total = a()
print("Each person will pay = ",total)