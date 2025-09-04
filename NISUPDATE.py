import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="kdss2707",database="school")
mycursor=mydb.cursor()
def updatestudentmarks(rollup):
    up=int(input("Enter updated marks")) 
    mycursor.execute("Update student set marks=%s where rollno=%s",(up,rollup))
    mydb.commit()
    print("Record Updated")
def updatestudentname(rollup):
    up=input("Enter Updated name")
    mycursor.execute("Update student set name=%s where rollno=%s",(up,rollup))
    mydb.commit()
    print("Record Updated")
def updatestudentcity(rollup):
    up=input("Enter Updated city")
    mycursor.execute("Update student set city=%s where rollno=%s",(up,rollup))
    mydb.commit()
    print("Record Updated")
def updatestudentage(rollup):
    up=input("Enter Updated age")
    mycursor.execute("Update student set age=%s where rollno=%s",(up,rollup))
    mydb.commit()
    print("Record Updated")
    
def updateteachername(rollup):
    up=input("Enter Updated name")
    mycursor.execute("Update teacher set name=%s where rollno=%s",(up,rollup))
    mydb.commit()
    print("Record Updated")
def updateteachercity(rollup):
    up=input("Enter Updated city")
    mycursor.execute("Update teacher set city=%s where rollno=%s",(up,rollup))
    mydb.commit()
    print("Record Updated")
def updateteacherage(rollup):
    up=input("Enter Updated age")
    mycursor.execute("Update teacher set age=%s where rollno=%s",(up,rollup))
    mydb.commit()
    print("Record Updated")
