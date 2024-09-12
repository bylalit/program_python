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
        'blood_group': 'B+',
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
        'blood_group': 'B+',
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
        'blood_group': 'A+',
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
        'blood_group': 'AB',
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
        'blood_group': 'AB',
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
        'blood_group': 'B+',
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
        'blood_group': 'B+',
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
        'blood_group': 'B+',
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
        'blood_group': 'AB',
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
        'blood_group': 'AB-',
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
        "blood_group":"A+",
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
        "blood_group":"A+",
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
        "blood_group":"A+",
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
        "blood_group":"AB",
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
        "blood_group":"A+",
    },
}

print("")
for student in students:
    print("")
    print(student.upper())
    for a,b in students[student].items():
        if type(b) == str:
            print(f"            {a.capitalize()}:=> {b.capitalize()}            ")
        else:
            print(f"            {a.capitalize()}:=> {b}            ")
            

print("""----------------Select one of the following options to search----------------
    1. Fname for press 1 
    2. Mname for press 2
    3. Lname for press 3
    4. Gender for press 4
    5. Area for press 5
    6. Address for press 6
    7. Pincode for press 7
    8. Age for press 8
    9. Blood Group for press 9
    """)


start = 1

while start == 1:
    option = input("Enter your choice: ").capitalize()
    
    for i in students:
        for a,b in students[i].items():
            if  a.capitalize() == option:
                print(a,b)


    
    
    start = int(input("Can you repete again the : "))