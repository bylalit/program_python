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