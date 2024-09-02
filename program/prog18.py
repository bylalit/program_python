student = {
    "lalit": {
        "Full_Name": "prajapati lalit",
        "Age": 25,
        "Grade": "A",
        "bood_group": "AB",
        "gender":"male",
        "address": "Ahmedabad",
    },
    "vidhi": {
        "Full_Name": "nager vidhi",
        "Age":  22,
        "Grade": "E",
        "bood_group": "AB",
        "gender":"female",
        "address": "pune"
    },
    "suresh": {
        "Full_Name": "prajapati suresh",
        "Age": 30,
        "Grade": "B",
        "bood_group": "O",
        "gender":"male",
        "address": "surat"
    },
    "ramesh": {
        "Full_name":  "prajapati ramesh",
        "Age": 35,
        "Grade":  "C",
        "bood_group": "A",
        "gender":"male",
        "address": "rajkot"
    },
    "roshni":{
        "Full_Name": "prajapati roshni",
        "Age": 20,
        "Grade": "D",
        "bood_group":  "B",
        "gender":"female",
        "address": "mumbai"
    },
    "vidhi": {
        "Full_Name": "nager vidhi",
        "Age":  22,
        "Grade": "E",
        "bood_group": "AB",
        "gender":"female",
        "address": "pune"
    },
}


for name in student:
    print()
    for key, val in student[name].items():
        print(key,  val)
print()


print("""---------------------------------------
        what will be search ?
            1. Full_name
            2. Age
            3. Grade
            4. bood_group
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