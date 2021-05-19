import pymysql

db = pymysql.connect(host="localhost", user="root", passwd="", database="b_d_m_s")
command_handler = db.cursor()


def Updata_Info():

    user_input = str(input("Enter donor first name or last name: "))
    query_vals = (user_input, user_input)
    command_handler.execute("select * from d_info where fname = %s or lname = %s", query_vals)
    results = command_handler.fetchall()
    for d_info in results:
        print(d_info)

    print('''
          Which you want to update?
          1. Fname
          2. Lname
          3. Age
          4. Gender
          5. Blood Group
          6. Address
          7. Mobile
          8. Job
          9. Month''')
    choose = int(input("Enter the option: "))
    if choose == 1:
        user = str(input("enter donor new first name : "))
        user_id = int(input("Enter donor id  for confirm : "))
        query_vals2 = (user, user_id)
        command_handler.execute("UPDATE d_info set fname= %s where id= %s", query_vals2)
        db.commit()
        print(command_handler.rowcount, "record(s) update")
    elif choose == 2:
        user = str(input("enter donor new last name : "))
        user_id = int(input("Enter donor id  for confirm : "))
        query_vals2 = (user, user_id)
        command_handler.execute("UPDATE d_info set lname= %s where id= %s", query_vals2)
        db.commit()
        print(command_handler.rowcount, "record(s) update")
    elif choose == 3:
        user = int(input("enter donor updated Age : "))
        user_id = int(input("Enter donor id  for confirm : "))
        query_vals2 = (user, user_id)
        command_handler.execute("UPDATE d_info set age = %s where id= %s", query_vals2)
        db.commit()
        print(command_handler.rowcount, "record(s) update")
    elif choose == 4:
        user = str(input("enter donor updated Gender : "))
        user_id = int(input("Enter donor id  for confirm : "))
        query_vals2 = (user, user_id)
        command_handler.execute("UPDATE d_info set gender = %s where id= %s", query_vals2)
        db.commit()
        print(command_handler.rowcount, "record(s) update")
    elif choose == 5:
        user = str(input("enter donor updated blood group : "))
        user_id = int(input("Enter donor id  for confirm : "))
        query_vals2 = (user, user_id)
        command_handler.execute("UPDATE d_info set b_grp = %s where id= %s", query_vals2)
        db.commit()
        print(command_handler.rowcount, "record(s) update")
    elif choose == 6:
        user = str(input("enter donor updated Area : "))
        user_id = int(input("Enter donor id  for confirm : "))
        query_vals2 = (user, user_id)
        command_handler.execute("UPDATE d_info set address = %s where id= %s", query_vals2)
        db.commit()
        print(command_handler.rowcount, "record(s) update")
    elif choose == 7:
        user = str(input("enter donor updated phone number : "))
        user_id = int(input("Enter donor id  for confirm : "))
        query_vals2 = (user, user_id)
        command_handler.execute("UPDATE d_info set mobile = %s where id= %s", query_vals2)
        db.commit()
        print(command_handler.rowcount, "record(s) update")
    elif choose == 8:
        user = str(input("enter donor updated occupation : "))
        user_id = int(input("Enter donor id  for confirm : "))
        query_vals2 = (user, user_id)
        command_handler.execute("UPDATE d_info set job = %s where id= %s", query_vals2)
        db.commit()
        print(command_handler.rowcount, "record(s) update")
    elif choose == 9:
        user = str(input("enter donor last donation Month : "))
        user_id = int(input("Enter donor id  for confirm : "))
        query_vals2 = (user, user_id)
        command_handler.execute("UPDATE d_info set month = %s where id= %s", query_vals2)
        db.commit()
        print(command_handler.rowcount, "record(s) update")



def DeleteDonor():

    print(" ")
    user_input = str(input("Enter donor first name or last name: "))
    query_vals = (user_input, user_input)
    command_handler.execute("delete from d_info where fname = %s or lname = %s",query_vals)
    db.commit()
    print(command_handler.rowcount, "record(s) deleted")



def Search():
    print('''
      1. Blood group
      2. blood group and area
      3. blood group and month
      ''')
    choose = int(input("Enter the option: "))
    if choose== 1 :
        user_input = str(input("Enter the blood group: "))
        query_vals = (user_input)
        command_handler.execute("select * from d_info where b_grp= %s", query_vals)
        results = command_handler.fetchall()
        for d_info in results:
            print(d_info)
    elif choose == 2:
        user_input = str(input("Enter the blood group: "))
        user_input2 = str(input("Enter the area: "))
        query_vals = (user_input, user_input2)
        command_handler.execute("select * from d_info where b_grp = %s and address = %s", query_vals)
        results = command_handler.fetchall()
        for d_info in results:
            print(d_info)
    elif choose == 3:
        user_input = str(input("Enter the blood group: "))
        user_input2 = str(input("Enter the month: "))
        query_vals = (user_input, user_input2)
        command_handler.execute("select * from d_info where b_grp = %s and month = %s", query_vals)
        results = command_handler.fetchall()
        for d_info in results:
            print(d_info)
    else:
        print("Not found!!")


def AddNewDonor():
    fname = str(input("Enter Donor First name: "))
    lname = str(input("Enter Donor Last name: "))
    age = str(input("Enter Donor age : "))
    gender = str(input("Enter Donor Gender : "))
    b_grp = str(input("Enter Donor Blood Group : "))
    address = str(input("Enter Donor Address area :"))
    mobile = str(input("Enter Donor Phone Number : "))
    job = str(input("Enter Donor Occupation : "))
    month = str(input("Last Blood Donation month : "))
    query_vals = (fname, lname, age, gender, b_grp, address, mobile, job, month)
    command_handler.execute(
        "insert into d_info(fname,lname,age,gender,b_grp,address,mobile,job,month)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        query_vals)
    db.commit()
    print(fname + " " + lname + " has been insert successfully.")


def displayAllDonor():
    print("")
    retrive = "Select * from d_info;"

    command_handler.execute(retrive)
    rows = command_handler.fetchall()
    for row in rows:
        print(row)
    db.commit()
    #db.close()


def main():
    print('''
  1. Add new Donor
  2. Search Donor
  3. Delete Donor from list
  4. Update donor Information
  5. Display all donor''')
    choose = int(input("Enter the option: "))
    if choose == 1:
        AddNewDonor()
        main()
    elif choose == 2:
        Search()
        main()
    elif choose == 3:
        DeleteDonor()
        main()
    elif choose == 4:
        Updata_Info()
        main()
    elif choose == 5:
        displayAllDonor()
        main()
    else:
        print("No valid option was selected.")


print("\n\tWelcome to Blood Donation Management System")
print("***************************************************")
main()
