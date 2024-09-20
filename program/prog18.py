# this program search for the data in the given object of dict..

students = {
    "rakesh" : {
        "fname": 'prajapati',
        'mname': 'rakesh',
        'lname': 'rameshbhai',
        'age': 18,
        'gender': 'male',
        'area': 'ranip',
        'add': 'c,13 rajendra park, ranip',
        'pincode': 380787,
        'bloodgroup': 'B+',
    },
    "vidhi" : {
        "fname": 'nagar',
        'mname': 'vidhi',
        'lname': 'bharatbhai',
        'age': 20,
        'gender': 'female',
        'area': 'odhav',
        'add': 'c,13 arbudhanager, odhav, ahemdhabad',
        'pincode': 382024,
        'bloodgroup': 'B+',
    },
    "manshi" : {
        "fname": 'thakor',
        'mname': 'manshi',
        'lname': 'saileshbhai',
        'age': 17,
        'gender': 'female',
        'area': 'rajendra',
        'add': '65 mukeshnagar odhav',
        'pincode': 382024,
        'bloodgroup': 'A+',
    },
    "mittal" : {
        "fname": 'prajapati',
        'mname': 'mittal',
        'lname': 'sureshbhai',
        'age': 22,
        'gender': 'female',
        'area': 'cmc',
        'add': '25 ctm char rasta odhav',
        'pincode': 382415,
        'bloodgroup': 'AB',
    },
    "lalit" : {
        "fname": 'prajapati',
        'mname': 'lalit',
        'lname': 'dilipbhai',
        'age': 18,
        'gender': 'male',
        'area': 'odhav',
        'add': 'c, 25 rajendra park, ranip',
        'pincode': 382415,
        'bloodgroup': 'AB',
    },
    "sid" : {
        "fname": 'deshai',
        'mname': 'sid',
        'lname': 'rakeshbhai',
        'age': 25,
        'gender': 'male',
        'area': 'odhav',
        'add': '78 rajendra park, ranip, ahemdhabad',
        'pincode': 382024,
        'bloodgroup': 'B+',
    },
    "aadity" : {
        "fname": 'puvar',
        'mname': 'aadity',
        'lname': 'rakeshbhai',
        'age': 28,
        'gender': 'male',
        'area': 'ranip',
        'add': '56 rajendra park, ranip, ahemdhabad',
        'pincode': 382024,
        'bloodgroup': 'B+',
    },
    "rishi" : {
        "fname": 'prajapati',
        'mname': 'rishi',
        'lname': 'rajubhai',
        'age': 23,
        'gender': 'male',
        'area': 'odhav',
        'add': '56 tulshi park',
        'pincode': 382024,
        'bloodgroup': 'B+',
    },
    "sneh" : {
        "fname": 'bharvad',
        'mname': 'sneh',
        'lname': 'sureshbhai',
        'age': 30,
        'gender': 'male',
        'area': 'shitalchaya',
        'add': '16 vrundhavan vatica',
        'pincode': 382415,
        'bloodgroup': 'AB',
    },
    "jay" : {
        "fname": 'deshai',
        'mname': 'jay',
        'lname': 'deneshbhai',
        'age': 16,
        'gender': 'male',
        'area': 'bhavani nagar',
        'add': '34 hastinapur socity',
        'pincode': 382415,
        'bloodgroup': 'AB-',
    },
        "riddhi":{
        "fname":"nagar",
        "mname":"ridhi",
        "lname":"bharatbhai",
        "gender":"female",
        "area":"vastral",
        "address":"404 vrundavan vatika",
        "pincode":382415,
        "age":20,
        "bloodgroup":"A+",
    },
    "bhavya":{
        "fname":"nagar",
        "mname":"bhavya",
        "lname":"nileshbhai",
        "gender":"male",
        "area":"rajasthan",
        "address":"34 jogeshwari",
        "pincode":382415,
        "age":20,
        "bloodgroup":"A+",
    },
    "ronak":{
        "fname":"parmar",
        "mname":"ronak",
        "lname":"rajubhai",
        "gender":"male",
        "area":"ranip",
        "address":"20  jogeshwari",
        "pincode":382415,
        "age":20,
        "bloodgroup":"A+",
    },
    "suresh":{
        "fname":"prajapati",
        "mname":"suresh",
        "lname":"maheshbhai",
        "gender":"male",
        "area":"odhav",
        "address":"20 maheshvari",
        "pincode":382024,
        "age":23,
        "bloodgroup":"AB",
    },
    "ronak":{
        "fname":"parmar",
        "mname":"ronak",
        "lname":"rajubhai",
        "gender":"male",
        "area":"ranip",
        "address":"20  jogeshwari",
        "pincode":382415,
        "age":20,
        "bloodgroup":"A+",
    },
}

print()
for student in students:
    print()
    print(student.upper())
    for a,b in students[student].items():
        if type(b) == str:
            print(f"            {a.capitalize()}:=> {b.capitalize()}            ")
        else:
            print(f"            {a.capitalize()}:=> {b}            ")
            

print()
print("""----------------Select one of the following options to search----------------
                1. Fname 
                2. Mname
                3. Lname
                4. Gender
                5. Area
                6. Address
                7. Pincode
                8. Age
                9. Bloodgroup
    """)


start = 1

while start == 1:
    option = input("Enter your choice: ").capitalize()
    
    # if  option == "Age" or option == "Pincode":
    #     z = int(input("Enter the you want to search: "))
    # else:
    #     z = input("Enter the you want to search: ").capitalize()


    for i in students:
        # print()
        for a,b in students[i].items():
            if  a.capitalize() == option:
                if  option == "Age" or option == "Pincode":
                    if b == z:
                        print(i.upper())
                        print(f"       {a.capitalize()}:=> {b}       ")
                else:
                    if b.capitalize() == z:
                        print(i.upper())
                        print(f"       {a.capitalize()}:=> {b.capitalize()}       ")


    
    print()
    start = int(input("what can you again search? 1 for yes 0 for no: "))
    print()
    
print("Thank you for using the student Database")
print()