print("================== BANK MANAGEMENT SYSTEM ================== ")

while(True):
    print(" ")
    print("Enter 1 to 'CREATE NEW ACCOUNT'")
    print("Enter 2 to 'LOGIN' in existing account")
    print("Enter 3 to 'EXIT'")


    import mysql.connector
    try:
        mydb= mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="",
                    database="dbbank"
                )
    
        mycursor=mydb.cursor()
        print("Database connected successsfully!")

    except Error as e:
        print("Database connection failed:",e)
        exit()
  
     
    number=int(input("Enter operation number you want to perform:"))
    match number:
        case 1:
            print("========== CREATE ACCOUNT ==========")
            sql="insert into create_account(name,phn_no,account_type,pwd,opening_balance,available_balance) values (%s,%s,%s,%s,%s,%s)"
            val1=str(input("Enter name:"))
            val2=str(input("Enter phone number:"))
            val3=str(input("Enter account type:"))
            val4=str(input("Enter password:"))
            try:
                val5=float(input("Enter opening balance:"))
                if val5<0:
                    print("Opening balance cannot be negative.")
                  
            except ValueError:
                print("Please enter a valid amount")
                
            val6=val5
            values=(val1,val2,val3,val4,val5,val6)
            mycursor.execute(sql,values)
            mydb.commit()
            print(mycursor.rowcount,"Record Inserted")

        case 2:
            print("=========== LOGIN ===========")
            sql="select * from create_account where account_no=%s AND pwd=%s"
            acc_no=str(input("Enter account number:"))
            pwd=str(input("Enter password:"))
            values=(acc_no,pwd)
            mycursor.execute(sql,values)
            result=mycursor.fetchone()
            if result:
                print(" ")   
                print("==========WELCOME!==========")
                print(" ")
                while(True):
                    print(" ")
                    print("========== HOME PAGE ==========")
                    print(" ")
                    print("Enter 1 for 'DEPOSIT'")
                    print("Enter 2 for 'WITHDRAW'")
                    print("Enter 3 for 'CHECK BALANCE'")
                    print("Enter 4 for 'TRANSACTION HISTORY'")
                    print("Enter 5 for 'CHANGE PASSWORD'")
                    print("Enter 6 for 'UPDATE ACCOUNT'")
                    print("Enter 7 for 'DELETE ACCOUNT'")
                    print("Enter 8 for 'LOGOUT'")
                    print(" ")

                    num=int(input("Enter operation number you want to perform on this account:"))
                    match num:
                        case 1:
                            print("\n=========== DEPOSIT =========")
                            try:
                                deposit=float(input("Enter amount you want to deposit in your Account:"))
                                if deposit<0:
                                    print("Deposit amount must be greater than 0")

                            except ValueError:
                                print("Please enter valid amount")
                            
                            sql1="update create_account SET available_balance=available_balance+%s where account_no=%s"
                            try:
                                values1=(deposit,acc_no)
                                mycursor.execute(sql1,values1)

                                sql2="insert into transaction_history (account_no,transaction_type,amount,transaction_date) values (%s,%s,%s,NOW())"
                                values=(acc_no,"Deposit",deposit)
                                mycursor.execute(sql2,values)
                                
                                mydb.commit()
                                print("Amount deposited successfully!")
                                print("Deposited Amount:₹",deposit)

                            except Error as e:
                                mydb.rollback()
                                print("Deposit failed:",e)

                        
                        case 2:
                            print("\n=========== WITHDRAW ==========")
                            try:
                                withdraw=float(input("Enter amount you want to withdraw in your Account:"))
                                if withdraw<=0:
                                    print("Withdraw amount must be grater than 0")

                            except ValueError:
                                print("Please enter a valid amount")

                            sql="SELECT available_balance FROM create_account WHERE account_no=%s"
                            try:
                                mycursor.execute(sql,acc_no)
                                balance=mycursor.fetchone()[0]

                                if withdraw>balance:
                                    print("Insufficient Balance")
                                    print("Available balance is:₹ ",balance)

                                else:
                                    sql="update create_account SET available_balance=available_balance-%s where account_no=%s"
                                    values=(withdraw,acc_no)
                                    mycursor.execute(sql,values)

                                sql2="insert into transaction_history (account_no,transaction_type,amount,transaction_date) values (%s,%s,%s,NOW())"
                                values=(acc_no,"withdraw",withdraw)
                                mycursor.execute(sql2,values)
                                                        
                                mydb.commit()
                                print("Amount withdrawn successfully!")

                            except Error as e:
                                mydb.rollback()
                                print("Withdrawn failed:",e)

                        

                        case 3:
                            print("\n============ CHECK BALANCE ===========")
                            sql="select available_balance from create_account where account_no=%s"
                            try:
                                values=(acc_no,)   # because execute accept tuple
                                mycursor.execute(sql,values) 
                                result=mycursor.fetchone()
                                if result:
                                    print("Available Balance:₹ ",result)
                                else:
                                    print("Account not found.")

                            except Error as e:
                                print("Error",e)


                        case 4:
                            print("\n=========== TRANSACTION HISTORY ===========")
                            sql="select * from transaction_history where account_no=%s"
                            try:
                                values=(acc_no,)
                                mycursor.execute(sql,values)
                                result=mycursor.fetchall() 
                                for x in result:
                                    print(x)
                            except Error as e:
                                print("Error",e)

                        case 5:
                            print("\n========== CHANGE PASSWORD ==========")
                            old_password=input("Enter old password:")
                            sql="select pwd from create_account where account_no=%s"
                            mycursor.execute(sql,(acc_no,))
                            result=mycursor.fetchone()
                            if result is None:
                                print("Account not found.")

                            if result[0]!=old_password:
                                print("Incorrect old password.")

                            new_password=input("Enter new password:")
                            if new_password=="":
                                print("Password cannot be empty.")

                            sql="update create_account set pwd=%s where account_no=%s"
                            try:
                                mycursor.execute(sql,(new_password,acc_no))
                                mydb.commit()
                                print("Password changed successfully!")

                            except Error as e:
                                mydb.rollback()
                                print("Error",e)

                        case 6:
                            print("\n============= UPDATE ACCOUNT ===========")
                            print("Enter 1 to update 'NAME'")
                            print("Enter 2 to update 'Phone Number'")
                            print("Enter 3 to update 'Back'")

                            choice=int(input("Enter choice:"))
                            match choice:
                                case 1:
                                    new_name=input("Enter new name:")
                                    sql="update create_account set name=%s where account_no=%s"
                                    try:
                                        values=(new_name,acc_no)
                                        mycursor.execute(sql,values)
                                        mydb.commit()
                                        print("Name updated successfully!")

                                    except Error as e:
                                        print("Error",e)

                                case 2:
                                        new_phn=input("Enter new phone number:")
                                        sql="update create_account set phn_no=%s where account_no=%s"
                                        try:
                                            values=(new_phn,acc_no)
                                            mycursor.execute(sql,values)
                                            mydb.commit()
                                            print("Phone Number updated successfully!")
                                
                                        except Error as e:
                                            mydb.rollback()
                                            print("Error",e)

                                case 3:
                                    break

                                case _:
                                    print("Invalid choice")

                        case 7:
                            print("\n============ DELETE ACCOUNT ===========")
                            confirmation=input("Are you sure you want to delete your account? (yes/no):")
                            if confirmation.lower()!="yes":
                                print("Account deletion cancelled.")

                            try:
                                sql="delete from transaction_history where account_no=%s"
                                mycursor.execute(sql,(acc_no,))

                                sql2="delete from create_account where account_no=%s"
                                mycursor.execute(sql2,(acc_no,))
                                mydb.commit()
                                print("Account deleted successfully!")

                            except Error as e:
                                mydb.rollback()
                                print("Error",e)



                        


                        case 8:
                            print("LOGGED OUT SUCCESSFULLY")
                            break

                        case _:
                            print("Invalid choice")
                            

            else:
                print("INVALID ACCOUNT NUMBER OR PASSWORD")

        case 3:
                print("========== THANK YOY! ==========")
                break

    mycursor.close()
    mydb.close()


        