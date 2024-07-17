import sqlcon as sc
import pandas as pd
import sys
import main 


c, connection = sc.createconn()
#connection
def fetchQjava(c):
    c, connection = sc.createconn()
    c.execute("SELECT ID, QUES, OPT1, OPT2, OPT3, OPT4, ANS, ANSWEROPT FROM Questionjava")
    rows = c.fetchall()
    columns = ['ID', 'QUES', 'OPT1', 'OPT2', 'OPT3', 'OPT4', 'ANS', 'ANSOPT']
    df = pd.DataFrame(rows, columns=columns)
    print(df)

def fetchq(c):
    c, connection = sc.createconn()
    c.execute("select Questionjava.ID,Questionjava.QUES,Questionjava.ANS,Questionpython.QUES,Questionpython.ANS from Questionpython LEFT JOIN Questionjava on Questionpython.ID=Questionjava.ID")
    rows = c.fetchall()
    columns = ['ID', 'QUES Java', 'Ans', 'QUES Python', 'Ans', ]
    df = pd.DataFrame(rows,columns=columns)
    print(df)
def fetchQpy(c):
    c, connection = sc.createconn()
    c.execute("SELECT ID, QUES, OPT1, OPT2, OPT3, OPT4, ANS, ANSWEROPT FROM Questionpython")
    rows = c.fetchall()
    columns = ['ID', 'QUES', 'OPT1', 'OPT2', 'OPT3', 'OPT4', 'ANS', 'ANSOPT']
    df = pd.DataFrame(rows, columns=columns)
    print(df)


def fetch_all_users(c):
    # Execute the SQL query and fetch all rows
    rows = c.execute("SELECT ID, NAME, SCORES, QUIZSCORE FROM user").fetchall()

    # Create a DataFrame from the fetched rows
    df = pd.DataFrame(rows, columns=["ID", "NAME", "SCORES", "QUIZSCORE"])

    # Return the DataFrame
    print(df)
# fetch(c)

def admin():
    attempts = 0
    while attempts < 3:
        pin = int(input("\nEnter the Admin pin:\n"))
        if pin == 8642:
            print("\nCorrect PIN entered!\n")
            admin_menu()
            break
        else:
            attempts += 1
            print("Incorrect PIN. Please try again. Attempts left:", 3 - attempts)
    else:
        print("Maximum attempts reached. Returning to main menu.")
        main.begin()


def admin_menu():
    c,connection=sc.createconn()
    print("\n 1)User Data\n2)Questions \n3)Edit Question\n4)Exit")
    i = int(input("Enter your choice: "))
    
    if i == 1:
        print("\nUser data\n")
        user_data()
    elif i == 2:
        print("Questions with category")
        question()
    elif i==3:
        print("\n editing question\n")
        editQ()
        
    elif i == 4:
        print("Quit")
        sys.exit()
    else:
        print("Invalid choice")

# user_data()   
def user_data():
    try:
        print("User data")
        print("1) Specific user")
        print("2) All users")
        print("3) Menu")
        
        ch = int(input("Enter your choice: "))
        
        if ch == 1:
            userId = int(input("Enter User ID: "))
            c.execute("SELECT ID, NAME, SCORES, QUIZSCORE FROM user WHERE ID=?", (userId,))
            specific_user_data = c.fetchall()
            if specific_user_data:
                # Create a DataFrame from the fetched data
                user_df = pd.DataFrame(specific_user_data, columns=["ID", "NAME", "SCORES", "QUIZSCORE"])
                print(user_df)
            else:
                print("No user found with the specified ID.")
            user_data()
        elif ch == 2:
            print("\nAll Users Data\n")
            fetch_all_users(c)
            
            user_data()
        elif ch == 3:
            print("Go to menu")
            admin_menu()
        else:
            print("Invalid choice. Please select again.")
            user_data()
    
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        user_data()
    except Exception as e:
        print("An error occurred:", e)
    finally:
        connection.close()

# user_data()


# question()              
def question():
    c, connection = sc.createconn()

    try:
        print("1) Specific Category\n2) All Questions\n3) Menu")
        ch = int(input("Enter your choice: "))

        if ch == 1:
            print("\n1) Java coding \n2) Python coding\n")
            category_choice = int(input("Enter Category (1 or 2): "))
            if category_choice == 1:
                category = "Java coding"
                # c.execute("SELECT * FROM Questionjava")
                fetchQjava(c)
            elif category_choice == 2:
                category = "Python coding"
                # c.execute("SELECT * FROM Questionpython")
                fetchQpy(c)
            else:
                print("Invalid choice. Please try again.")
                return  # Exit the function if the choice is invalid
            
            
            question()
        
        elif ch == 2:
            print("\nAll Questions Data\n")
            
            fetchq(c)
            print("Done\n\n")
            question()
        
        elif ch == 3:
            print("Go to Menu")
            admin_menu()
        
        else:
            print("Enter correct option")
            question()
    
    except Exception as e:
        print("An error occurred:", e)

    finally:
        connection.close()



  
def addQ():
    c, connection = sc.createconn()

    try:
        print("Select category:\n1) Java coding\n2) Python coding")
        category_choice = int(input("Enter your choice (1 or 2): "))

        if category_choice == 1:
            category = "Java coding"
        elif category_choice == 2:
            category = "Python coding"
        else:
            print("Invalid choice. Please select again.")
            return

        # Take inputs from the user
        question = input("Enter the question: ")
        opt1 = input("Enter option 1: ")
        opt2 = input("Enter option 2: ")
        opt3 = input("Enter option 3: ")
        opt4 = input("Enter option 4: ")
        correct_answer = input("Enter the correct answer: ")

        # Determine the correct answer option index
        options = [opt1, opt2, opt3, opt4]
        answer_index = options.index(correct_answer) + 1
        
        # Insert the data into the appropriate question table based on the category
        if category_choice == 1:
            c.execute("INSERT INTO Questionjava (QUES, OPT1, OPT2, OPT3, OPT4, ANS, ANSWEROPT, CATEGORY) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
               (question, opt1, opt2, opt3, opt4, correct_answer, answer_index, category))

        elif category_choice == 2:
            c.execute("INSERT INTO Questionpython (QUES, OPT1, OPT2, OPT3, OPT4, ANS, ANSWEROPT, CATEGORY) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
               (question, opt1, opt2, opt3, opt4, correct_answer, answer_index, category))

        connection.commit()
        print("Question added successfully")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        connection.close()
  

def updateQ():
    c, connection = sc.createconn()

    try:
        # Prompt user to select category
        print("Select category:\n1) Java coding\n2) Python coding")
        category_choice = int(input("Enter your choice (1 or 2): "))

        if category_choice == 1:
            category = "Java coding"
            table_name = "Questionjava"
        elif category_choice == 2:
            category = "Python coding"
            table_name = "Questionpython"
        else:
            print("Invalid choice. Please select again.")
            return

        # Prompt user to enter question ID
        question_id = int(input("Enter the ID of the question you want to update: "))

        # Retrieve question details
        c.execute(f"SELECT * FROM {table_name} WHERE ID=?", (question_id,))
        question_data = c.fetchone()

        if question_data:
            print("Current question details:")
            print("Question:", question_data[1])
            print("Option 1:", question_data[2])
            print("Option 2:", question_data[3])
            print("Option 3:", question_data[4])
            print("Option 4:", question_data[5])
            print("Correct Answer:", question_data[6])

            # Prompt user to enter updated question details
            updated_question = input("Enter the updated question: ")
            updated_opt1 = input("Enter updated option 1: ")
            updated_opt2 = input("Enter updated option 2: ")
            updated_opt3 = input("Enter updated option 3: ")
            updated_opt4 = input("Enter updated option 4: ")
            updated_correct_answer = input("Enter the updated correct answer: ")

            # Update the question in the database
            c.execute(f"UPDATE {table_name} SET QUES=?, OPT1=?, OPT2=?, OPT3=?, OPT4=?, ANS=? WHERE ID=?",
                       (updated_question, updated_opt1, updated_opt2, updated_opt3, updated_opt4, updated_correct_answer, question_id))
            connection.commit()
            print("Question updated successfully.")
        else:
            print("Question not found. Please enter a valid question ID.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        connection.close()


def deleteQ():
    c, connection = sc.createconn()

    try:
        # Prompt user to select category
        print("Select category:\n1) Java coding\n2) Python coding")
        category_choice = int(input("Enter your choice (1 or 2): "))

        if category_choice == 1:
            category = "Java coding"
            table_name = "Questionjava"
        elif category_choice == 2:
            category = "Python coding"
            table_name = "Questionpython"
        else:
            print("Invalid choice. Please select again.")
            return

        # Prompt user to enter question ID
        question_id = int(input("Enter the ID of the question you want to delete: "))

        # Check if the question exists in the database
        c.execute(f"SELECT * FROM {table_name} WHERE ID=?", (question_id,))
        question_data = c.fetchone()

        if question_data:
            print("\nCurrent question details:\n")
            print("Question:", question_data[1],"\n")
            print("Option 1:", question_data[2])
            print("Option 2:", question_data[3])
            print("Option 3:", question_data[4])
            print("Option 4:", question_data[5])
            print("Correct Answer:", question_data[6],"\n")


            confirm_delete = input("Are you sure you want to delete this question? (yes/no): ")
            if confirm_delete.lower() == "yes":
                # Delete the question from the database
                c.execute(f"DELETE FROM {table_name} WHERE ID=?", (question_id,))
                connection.commit()
                print("Question deleted successfully.")
            else:
                print("Deletion cancelled.")
        else:
            print("Question not found. Please enter a valid question ID.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        connection.close()





def editQ():
    print("\n1)add Question \n2)Update Question \n3)Delete question \n4)menu")
    i=int(input("Enter ur choice"))
    if i==1:
        addQ()
        editQ()
    elif i==2:
        updateQ()
        editQ()
    elif i==3:
        deleteQ()
        editQ()
    else:
        print("enter correct choice")

# fetchQpy(c)
