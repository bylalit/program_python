student = {
    "lalit": {
        "name": "prajapati lalit",
        "Age": 25,
        "Grade": "A",
        "blood": "AB",
        "gender":"male",
        "address": "Ahmedabad",
    },
    "vidhi": {
        "name": "nager vidhi",
        "Age":  22,
        "Grade": "E",
        "blood": "AB",
        "gender":"female",
        "address": "pune"
    },
    "suresh": {
        "name": "prajapati suresh",
        "Age": 30,
        "Grade": "B",
        "blood": "O",
        "gender":"male",
        "address": "surat"
    },
    "ramesh": {
        "name":  "prajapati ramesh",
        "Age": 35,
        "Grade":  "C",
        "blood": "A",
        "gender":"male",
        "address": "rajkot"
    },
    "roshni":{
        "name": "prajapati roshni",
        "Age": 20,
        "Grade": "D",
        "blood":  "B",
        "gender":"female",
        "address": "mumbai"
    },
    "vidhi": {
        "name": "nager vidhi",
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

keyValue = input("Enter the key  to search: ").capitalize()

if keyValue == "Age":
    valueSearch = int(input("Enter the value to search: "))
else:
    valueSearch = input("Enter the  value to search: ")




for i in student:
    print()
    for k, v in student[i].items():
        if  k.capitalize() == keyValue:
            if keyValue == "Age":
                if v == valueSearch:
                    print(i.upper())
                    print(k.capitalize(), "==>" , v)
            else:
                if v == valueSearch:
                    print(i.upper())
                    print(k.capitalize(), "==>" , v.capitalize())

print()