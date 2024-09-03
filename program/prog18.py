# this program search for the data in the given object of dict..

student = {
    "lalit": {
        "name": "lalit",
        "Age": 25,
        "Grade": "A",
        "blood": "AB",
        "gender":"male",
        "address": "Ahmedabad",
    },
    "vidhi": {
        "name": "vidhi",
        "Age":  22,
        "Grade": "E",
        "blood": "AB",
        "gender":"female",
        "address": "pune"
    },
    "suresh": {
        "name": "suresh",
        "Age": 30,
        "Grade": "B",
        "blood": "O",
        "gender":"male",
        "address": "surat"
    },
    "ramesh": {
        "name":  "ramesh",
        "Age": 35,
        "Grade":  "C",
        "blood": "A",
        "gender":"male",
        "address": "rajkot"
    },
    "roshni":{
        "name": "roshni",
        "Age": 20,
        "Grade": "D",
        "blood":  "B",
        "gender":"female",
        "address": "mumbai"
    },
    "vidhi": {
        "name": "vidhi",
        "Age":  22,
        "Grade": "E",
        "blood": "AB",
        "gender":"female",
        "address": "pune"
    },
}

for name in student:
    print()
    print(name)
    for key, val in student[name].items():
        print(key.capitalize(), "  ==>  " , val)
print()

print("""---------------------------------------
        what will be search ?
            1. Name
            2. Age
            3. Grade
            4. Blood
            5. Gender
            6. Address
            7. Exit      
    """)

start = 1

while start == 1:
    keyValue = input("Enter the key  to search: ").capitalize()

    if keyValue == "Exit":
        start = 0
    else:
        if keyValue == "Age":
            valueSearch = int(input("Enter the value to search: "))
        else:
            valueSearch = input("Enter the  value to search: ").capitalize()

    print()
    for i in student:
        for k, v in student[i].items():
            if  k.capitalize() == keyValue:
                if keyValue == "Age":
                    if v == valueSearch:
                        print(i.upper())
                        print(k.capitalize(), "==>" , v, "\n")
                else:
                    if v.capitalize() == valueSearch:
                        print(i.upper())
                        print(k.capitalize(), "==>" , v.capitalize(),  "\n")

    print()
    
    if keyValue == "Exit":
        start = 0
    else:
        start = int(input("Can  you search again ? 1. yes 2. no: "))
    print(" Thank you for using this program. ")
    