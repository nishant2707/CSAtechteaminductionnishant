import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="kdss2707",database="school")
mycursor=mydb.cursor()
def deletestudent(rolldel):
    mycursor.execute("delete from student where rollno=({0})".format(rolldel))
    mydb.commit()
    print("recorded deleted")
def deleteteacher(rolldel):
    mycursor.execute("delete from student where rollno=([0])".format(rolldel))
    mydb.commit()
    print("recorded deleted")
