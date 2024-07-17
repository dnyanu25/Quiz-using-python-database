import random
import sqlcon as sc

def fetch_random_questions(c, num_questions, table_name):
    c.execute(f"SELECT QUES, OPT1, OPT2, OPT3, OPT4, ANSWEROPT FROM {table_name} ORDER BY RANDOM() LIMIT ?", (num_questions,))
    questions = c.fetchall()
    return questions

def display_question(question):
    print("\n", question[0], "\n")  # Print the question
    options = question[1:5]  # Extract options from the tuple
    for idx, option in enumerate(options, start=1):
        print(f"{idx}. {option}")  # Display options

def user():
    c, connection = sc.createconn()
    print("\n\tWELCOME TO QUIZ\n\n")
    username = input("Enter Your Name:\n")

    # Check if the user exists
    c.execute("SELECT ID, scores FROM user WHERE NAME=?", (username,))
    existing_user = c.fetchone()

    if existing_user:
        print("Welcome back, {}!".format(username))
        current_score = existing_user[1]  # Get the current score of the user
    else:
        print("New user detected. Creating a new record for {}.".format(username))
        current_score = 0  # New user starts with a score of 0

    print("\nSelect category\n1) Java coding\n2) Python coding\n3) Quit")
    choice = int(input("Enter your choice: "))

    if choice in [1, 2]:
        category = "Java coding" if choice == 1 else "Python coding"
        table_name = "Questionjava" if choice == 1 else "Questionpython"
        num_questions = 10  # Number of questions to display
        questions = fetch_random_questions(c, num_questions, table_name)
        final_score = 0

        for question in questions:
            display_question(question)
            answer = int(input("Enter your answer (1/2/3/4): "))
            if answer == question[5]:  # Check if the answer is correct
                print("Correct!")
                final_score += 1
            else:
                print("Incorrect!")

        print(f"\n\nYour final score: {final_score}/{num_questions}")

        # Calculate the new total score
        total_score = final_score

        if existing_user:
            # Update user's score in the database with the new total score
            c.execute("UPDATE user SET scores=?, QuizScore=? WHERE NAME=? AND category=?", (total_score, num_questions, username, category))
        else:
            # Insert new record for the user
            c.execute("INSERT INTO user (NAME, scores, category, QuizScore) VALUES (?, ?, ?, ?)", (username, total_score, category, num_questions))

        connection.commit()
    elif choice == 3:
        print("\nGoodbye!")
    else:
        print("\nInvalid choice. Please select again.")

    connection.close()

# user()