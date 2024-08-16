import mysql.connector  
from tkinter import messagebox

def Save_Data_MySql(B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R):
    try:
        # Connect to the MySQL server <<<<<<<<<<<<<<

        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Vikas@380'
        )
        mycursor = mydb.cursor()
        print("Connection established !!!")

        # Create database and table if they don't exist <<<<<<<<<<<<<<

        mycursor.execute("CREATE DATABASE IF NOT EXISTS heart_list")
        mycursor.execute("USE heart_list")
        mycursor.execute("CREATE TABLE IF NOT EXISTS data(user INT AUTO_INCREMENT PRIMARY KEY NOT NULL, Name VARCHAR(50), Date VARCHAR(100), DOB VARCHAR(100), age VARCHAR(100), sex VARCHAR(100), Cp VARCHAR(100), trestbps VARCHAR(100), chol VARCHAR(100), fbs VARCHAR(100), restecg VARCHAR(100), thalach VARCHAR(100), exang VARCHAR(100), oldpeak VARCHAR(100), slop VARCHAR(100), ca VARCHAR(100), thal VARCHAR(100), Result VARCHAR(100))")

        # Insert data into the table <<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        
        command = "INSERT INTO data(Name, Date, DOB, age, sex, Cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slop, ca, thal, Result) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        mycursor.execute(command, (B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R))
        mydb.commit()
        messagebox.showinfo("Register", "New user added successfully!!!!")

    except mysql.connector.Error as err:
        messagebox.showerror("Database Error", f"An error occurred: {err}")
    finally:
        if mydb.is_connected():
            mydb.close()
            print("MySQL connection is closed !!!")
