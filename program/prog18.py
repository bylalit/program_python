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
            1. name
            2. Age
            3. Grade
            4. blood
            5. gender
            6. address
            7. exit      
    """)

keyValue = input("Enter the key  to search: ").capitalize()
valueSearch = input("Enter the  value to search: ")




for i in student:
    print()
    for k, v in student[i].items():
        if  k.capitalize() == keyValue:
            if  v == valueSearch:
                print(i)
                print(k.capitalize(), v)

print()