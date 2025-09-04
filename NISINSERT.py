import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="kdss2707",database="school")
mycursor=mydb.cursor()
def insertrecordstudent():
    try:
        rollno=int(input("enter roll number"))
    except:
        print("please enter integer for the given attribute")
    password=input("enter password")
    name=input("enter name")
    try:
        age=int(input("enter age"))
    except:
        print("please enter integer for the given attribute")
    city=input("enter city")
    try:
        marks=int(input("enter marks"))
    except:
        print("please enter integer for the given attribute")
    mycursor.execute("INSERT INTO student VALUES({0},'{1}','{2}',{3},'{4}',{5})".format(rollno,password,name,age,city,marks))
    mydb.commit()
    print("Record Added")
def insertrecordteacher():
    try:
        rollno=int(input("enter Roll number"))
    except:
        print("please enter integer for the given attribute")
    password=input("enter password")
    name=input("enter name")
    try:
        age=int(input("enter age"))
    except:
        print("please enter integer for the given attribute")
    city=input("enter city")
    mycursor.execute("INSERT INTO teacher VALUES({0},'{1}','{2}',{3},'{4}')".format(rollno,password,name,age,city))
    mydb.commit()
    print("Record Added")
