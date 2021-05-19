import pymysql

db = pymysql.connect(host="localhost", user="root", passwd="", database="b_d_m_s")
command_handler = db.cursor() # Iterating over data


def Updata_Info():

    user_inpu = str(input("Enter donor first name or last name: "))
    user_input = user_inpu.upper()
    query_vals = (user_input, user_input)
    command_handler.execute("select * from d_info where fname = %s or lname = %s", query_vals)
    results = command_handler.fetchall()
    for d_info in results:
        print(d_info)
    db.commit()
    #command_handler.close()
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
        use = str(input("enter donor new first name : "))
        user = use.upper()
        user_id = int(input("Enter donor id  for confirm : "))
        query_vals2 = (user, user_id)
        command_handler.execute("UPDATE d_info set fname= %s where id= %s", query_vals2)
        db.commit() # commit is the updating of a record in a database.
        print(command_handler.rowcount, "record(s) update")
        command_handler.close()
    elif choose == 2:
        use = str(input("enter donor new last name : "))
        user = use.upper()
        user_id = int(input("Enter donor id  for confirm : "))
        query_vals2 = (user, user_id)
        command_handler.execute("UPDATE d_info set lname= %s where id= %s", query_vals2)
        db.commit()
        print(command_handler.rowcount, "record(s) update")
        command_handler.close()
    elif choose == 3:
        user = int(input("enter donor updated Age : "))
        user_id = int(input("Enter donor id  for confirm : "))
        query_vals2 = (user, user_id)
        command_handler.execute("UPDATE d_info set age = %s where id= %s", query_vals2)
        db.commit()
        print(command_handler.rowcount, "record(s) update")
        command_handler.close()
    elif choose == 4:
        use = str(input("enter donor updated Gender : "))
        user = use.upper()
        user_id = int(input("Enter donor id  for confirm : "))
        query_vals2 = (user, user_id)
        command_handler.execute("UPDATE d_info set gender = %s where id= %s", query_vals2)
        db.commit()
        print(command_handler.rowcount, "record(s) update")
        command_handler.close()
    elif choose == 5:
        use = str(input("enter donor updated blood group : "))
        user = use.upper()
        user_id = int(input("Enter donor id  for confirm : "))
        query_vals2 = (user, user_id)
        command_handler.execute("UPDATE d_info set b_grp = %s where id= %s", query_vals2)
        db.commit()
        print(command_handler.rowcount, "record(s) update")
        command_handler.close()
    elif choose == 6:
        use = str(input("enter donor updated Area : "))
        user = use.upper()
        user_id = int(input("Enter donor id  for confirm : "))
        query_vals2 = (user, user_id)
        command_handler.execute("UPDATE d_info set address = %s where id= %s", query_vals2)
        db.commit()
        print(command_handler.rowcount, "record(s) update")
        command_handler.close()
    elif choose == 7:
        use = str(input("enter donor updated phone number : "))
        user = use.upper()
        user_id = int(input("Enter donor id  for confirm : "))
        query_vals2 = (user, user_id)
        command_handler.execute("UPDATE d_info set mobile = %s where id= %s", query_vals2)
        db.commit()
        print(command_handler.rowcount, "record(s) update")
        command_handler.close()
    elif choose == 8:
        use = str(input("enter donor updated occupation : "))
        user = use.upper()
        user_id = int(input("Enter donor id  for confirm : "))
        query_vals2 = (user, user_id)
        command_handler.execute("UPDATE d_info set job = %s where id= %s", query_vals2)
        db.commit()
        print(command_handler.rowcount, "record(s) update")
        command_handler.close()
    elif choose == 9:
        use = str(input("enter donor last donation Month : "))
        user = use.upper()
        user_id = int(input("Enter donor id  for confirm : "))
        query_vals2 = (user, user_id)
        command_handler.execute("UPDATE d_info set month = %s where id= %s", query_vals2)
        db.commit()
        print(command_handler.rowcount, "record(s) update")
        command_handler.close()



def DeleteDonor():
    print(" ")
    user_inpu = str(input("Enter donor first name or last name: "))
    user_input = user_inpu.upper()
    query_vals = (user_input, user_input)
    command_handler.execute("delete from d_info where fname = %s or lname = %s",query_vals)
    db.commit()
    print(command_handler.rowcount, "record(s) deleted")
    command_handler.close()



def Search():
    print('''
      1. Blood group
      2. blood group and area
      3. blood group and month
      ''')
    choose = int(input("Enter the option: "))
    if choose == 1:
        user_inpu = str(input("Enter the blood group: "))
        user_input = user_inpu.upper()
        query_vals = (user_input)
        command_handler.execute("select * from d_info where b_grp= %s", query_vals)
        results = command_handler.fetchall()
        for d_info in results:
            print(d_info)
        db.commit()
        command_handler.close()
    elif choose == 2:
        user_inpu = str(input("Enter the blood group: "))
        user_input = user_inpu.upper()
        user_inpu2 = str(input("Enter the area: "))
        user_input2 = user_inpu2.upper()
        query_vals = (user_input, user_input2)
        command_handler.execute("select * from d_info where b_grp = %s and address = %s", query_vals)
        results = command_handler.fetchall()
        for d_info in results:
            print(d_info)
        db.commit()
        command_handler.close()
    elif choose == 3:
        user_inpu = str(input("Enter the blood group: "))
        user_input = user_inpu.upper()
        user_inpu2 = str(input("Enter the month: "))
        user_input2 = user_inpu2.upper()
        query_vals = (user_input, user_input2)
        command_handler.execute("select * from d_info where b_grp = %s and month = %s", query_vals)
        results = command_handler.fetchall()
        for d_info in results:
            print(d_info)
        db.commit()
        command_handler.close()
    else:
        print("Not found!!")


def AddNewDonor():
    fnam = str(input("Enter Donor First name: "))
    fname = fnam.upper()
    lnam = str(input("Enter Donor Last name: "))
    lname = lnam.upper()
    age = str(input("Enter Donor age : "))
    gende = str(input("Enter Donor Gender : "))
    gender = gende.upper()
    b_gr = str(input("Enter Donor Blood Group : "))
    b_grp = b_gr.upper()
    addres = str(input("Enter Donor Address area :"))
    address = addres.upper()
    mobile = str(input("Enter Donor Phone Number : "))
    jo = str(input("Enter Donor Occupation : "))
    job = jo.upper()
    mont = str(input("Last Blood Donation month : "))
    month = mont.upper()
    query_vals = (fname, lname, age, gender, b_grp, address, mobile, job, month)
    command_handler.execute(
        "insert into d_info(fname,lname,age,gender,b_grp,address,mobile,job,month)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        query_vals)
    db.commit()
    print(fname + " " + lname + " has been insert successfully ")
    #command_handler.close()


def displayAllDonor():
    print("")
    retrive = "Select * from d_info;"

    command_handler.execute(retrive)
    rows = command_handler.fetchall()
    for row in rows:
        print(row)
    db.commit()
    db.close()


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
