import mysql.connector
import NISINSERT
import NISUPDATE
import NISDELETE
passk=12345678
mydb=mysql.connector.connect(host="localhost",user="root",password="kdss2707",database="school")
mycursor=mydb.cursor()
passkey="kdss2707"
while True:
    print("              To insert record press 1")
    print("              To delete record press 2")
    print("              To update record press 3")
    print("              To view record press 4")
    print("              To search by press 5")
    try:    
        n=int(input())
        if n==1:
            t=input("Insert Record For Teacher or Student")
            if t.upper()=="STUDENT":
                NISINSERT.insertrecordstudent()
            elif t.upper()=="TEACHER":
                NISINSERT.insertrecordteacher()
            else:
                print("Enter Either Teacher or Student only")
        elif n==2:
            t=input("Delete Record For Teacher or Student")
            if t.upper()=="STUDENT":
                try:
                    rolldel=int(input("Enter rollno of student"))
                except:
                    print("Enter actual roll no")
                pw=input("enter password")
                mycursor.execute("select password from student where rollno=({0})".format(rolldel))
                mp=mycursor.fetchall()
                if pw==mp[0][0]:
                    NISDELETE.deletestudent(rolldel)
                else:
                    print("Password does not match")
            elif t.upper()=="TEACHER":
                try:
                    rolldel=int(input("Enter rollno of teacher"))
                except:
                    print("Enter actual roll no")
                pw=input("enter password")
                mycursor.execute("select password from teacher where rollno=({0})".format(rolldel))
                mp=mycursor.fetchall()
                if pw==mp[0][0]:
                    NISDELETE.deleteteacher()
                else:
                    print("Password does not match")
            else:
                print("Enter Either Teacher or Student only")
        elif n==3:
            t=input("Update Record For Teacher or Student")
            if t.upper()=="STUDENT":
                try:
                    rollup=int(input("Enter rollno of student"))
                except:
                    print("Enter actual roll no")
                pw=input("enter password")
                mycursor.execute("select password from student where rollno=({0})".format(rollup))
                mp=mycursor.fetchall()
                if pw==mp[0][0]:
                    print("4 colums to update from,AGE,CITY,MARKS,NAME")
                    str=input("what do you want to update")
                    if str.upper()=="MARKS":
                        NISUPDATE.updatestudentmarks(rollup)
                    elif str.upper()=="NAME":
                        NISUPDATE.updatestudentname(rollup)
                    elif str.upper()=="CITY":
                        NISUPDATE.updatestudentcity(rollup)
                    elif str.upper()=="AGE":
                        NISUPDATE.updatestudentage(rollup)
                else:
                    print("Password does not match")
            elif t.upper()=="TEACHER":
                try:
                    rollup=int(input("Enter rollno of teacher"))
                except:
                    print("Enter actual roll no")
                pw=input("enter password")
                mycursor.execute("select password from teacher where rollno=({0})".format(rollup))
                mp=mycursor.fetchall()
                if pw==mp[0][0]:
                    print("3 colums to update from,AGE,CITY,NAME")
                    str=input("what do you want to update")
                    if str.upper()=="NAME":
                        NISUPDATE.updateteachername(rollup)
                    elif str.upper()=="CITY":
                        NISUPDATE.updateteachercity(rollup)
                    elif str.upper()=="AGE":
                        NISUPDATE.updateteacherage(rollup)
                else:
                    print("Password does not match")
            else:
                print("Enter Either Teacher or Student only")
        elif n==4:
            t=input("View Record For Teacher or Student")
            if t.upper()=="STUDENT":
                try:
                    roll=int(input("enter rollno"))
                except:
                    print("Enter actual roll no")
                pw=input("enter password")
                mycursor.execute("select password from student where rollno=({0})".format(roll))
                mp=mycursor.fetchall()
                if pw==mp[0][0]:
                    mycursor.execute("select * from student where rollno=({0})".format(roll))
                    row=mycursor.fetchone()
                    print("               Rollno",row[0])
                    print("               Name",row[2])
                    print("               Age",row[3])
                    print("               City",row[4])
                    print("               Marks",row[5])
                else:
                    print("Password does not match")
            elif t.upper()=="TEACHER":
                try:
                    roll=int(input("Enter rollno of teacher"))
                except:
                    print("Enter actual roll no")
                pw=input("enter password")
                mycursor.execute("select password from teacher where rollno=({0})".format(roll))
                mp=mycursor.fetchall()
                if pw==mp[0][0]:
                    mycursor.execute("select * from teacher where rollno=({0})".format(roll))
                    row=mycursor.fetchone()
                    print("               Rollno",row[0])
                    print("               Name",row[2])
                    print("               Age",row[3])
                    print("               City",row[4])
                else:
                    print("Password does not match")
            else:
                print("Enter Either Teacher or Student only")
        elif n==5:
            passkey1=int(input("enter passkey"))
            if passkey1==passk:
                t=input("View Record For Teacher or Student")
                if t.upper()=="STUDENT":
                    mycursor.execute("select * from student")
                    row=mycursor.fetchall()
                    for i in row:
                        print(i[0],"",i[2],"",i[3],"",i[4],"",i[5])
                elif t.upper()=="TEACHER":
                    mycursor.execute("select * from student")
                    row=mycursor.fetchall()
                    for i in row:
                        print("           ",i[0],"",i[2],"",i[3],"",i[4])        
        else:
            print("please select the above options")
    except:
        print("Enter Number only")
    breaker=input("Do you want to continue")
    if breaker.upper()=="NO":
        break
    

            
        
    
    
            
        
            
     
