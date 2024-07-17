import sqlite3

def createconn():
    con = sqlite3.connect("Quiz.db")
    c = con.cursor()
    return c, con

def tbl():
    c, connection = createconn()
    c.execute("CREATE TABLE IF NOT EXISTS admin (ID INTEGER, NAME TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS user (ID INTEGER PRIMARY KEY, NAME TEXT, scores INTEGER, category TEXT, QuizScore INTEGER)")
    c.execute("CREATE TABLE IF NOT EXISTS Questionpython(ID INTEGER PRIMARY KEY, QUES TEXT UNIQUE, OPT1 TEXT, OPT2 TEXT, OPT3 TEXT, OPT4 TEXT, ANS TEXT, ANSWEROPT INTEGER, CATEGORY TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS Questionjava(ID INTEGER PRIMARY KEY, QUES TEXT UNIQUE, OPT1 TEXT, OPT2 TEXT, OPT3 TEXT, OPT4 TEXT, ANS TEXT, ANSWEROPT INTEGER, CATEGORY TEXT)")
    c.execute("CREATE TABLE IF NOT EXISTS CATAGORY(ID INTEGER ,CATG TEXT UNIQUE)")
    connection.commit()  # Make sure to commit the changes after creating the tables
    connection.close()  # Close the connection after committing changes
    print("Tables created successfully")
    # addData()

# def addData():
#         c, connection = createconn()

#         questions_java = [
#            ("Who invented Java?", "James Gosling", "Bill Gates", "Steve Jobs", "Linus Torvalds", "James Gosling"),
#            ("What is the default value of byte datatype in Java?", "0", "0.0", "null", "undefined", "0"),
#            ("What is the size of int datatype in Java?", "8 bits", "16 bits", "32 bits", "64 bits", "32 bits"),
#            ("Which keyword is used to prevent method overriding in Java?", "static", "final", "abstract", "private", "final"),
#            ("What does JVM stand for?", "Java Virtual Machine", "Java Very Machine", "Java Virtual Mechanism", "Java Visual Machine", "Java Virtual Machine"),
#            ("What is the output of 5 + 7 * 2?", "19", "24", "23", "21", "19"),
#            ("Which collection class allows you to associate a key with a value pair?", "HashMap", "ArrayList", "HashSet", "Hashtable", "HashMap"),
#            ("What is the correct way to declare a constant in Java?", "const int MY_CONSTANT = 10;", "static final int MY_CONSTANT = 10;", "final int MY_CONSTANT = 10;", "final MY_CONSTANT = 10;", "static final int MY_CONSTANT = 10;"),
#            ("What does OOP stand for?", "Object Oriented Programming", "Object Oriented Protocol", "Object Oriented Process", "Object Oriented Procedure", "Object Oriented Programming"),
#            ("Which method is used to compare two strings for equality in Java?", "equals()", "equal()", "compareTo()", "compare()", "equals()"),
#            ("What is the output of the following code?\nString s1 = new String(\"hello\");\nString s2 = new String(\"hello\");\nSystem.out.println(s1 == s2);", "true", "false", "compile error", "runtime error", "false"),
#            ("What is the parent class of all classes in Java?", "Object", "Main", "Super", "Parent", "Object"),
#            ("What is the use of 'super' keyword in Java?", "To call superclass method", "To call subclass method", "To access subclass variable", "To access superclass variable", "To call superclass method"),
#            ("Which exception is thrown when an array is accessed with an illegal index?", "ArrayOutOfBoundsException", "ArrayIndexOutOfBoundsException", "IllegalArrayIndexException", "IndexOutOfBoundsException", "ArrayIndexOutOfBoundsException")
#         ]

#         for question in questions_java:
#                c.execute("INSERT INTO Questionjava (QUES, OPT1, OPT2, OPT3, OPT4, ANS, ANSWEROPT, CATEGORY) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
#                    (question[0], question[1], question[2], question[3], question[4], question[1], 1, "java coding"))
#         python_questions = [
#                 ("What is Python?", "A programming language", "A reptile", "A bird", "A mammal", "A programming language"),
#                 ("Which keyword is used to define a function in Python?", "def", "function", "define", "fn", "def"),
#                 ("What is the output of print(2 == 2)?", "True", "False", "Error", "None", "True"),
#                 ("Which data type is mutable in Python?", "List", "Tuple", "String", "Integer", "List"),
#                 ("What is the result of 'python'[1:4]?", "yth", "pyt", "tho", "ython", "yth"),
#                 ("How do you start a comment in Python?", "//", "/*", "#", "--", "#"),
#                 ("What does the function len() do in Python?", "Returns the length of an object", "Converts to lowercase", "Joins elements of a list", "Returns a random number", "Returns the length of an object"),
#                 ("What is the output of the expression 3 * 'ab'?", "ababab", "abab", "abababab", "ab", "ababab"),
#                 ("Which one is NOT a valid variable name in Python?", "my-var", "_var", "var1", "1var", "1var"),
#                 ("What does the 'break' keyword do in a loop?", "Exits the loop", "Continues to the next iteration", "Creates an infinite loop", "None of the above", "Exits the loop"),
#                 ("What is the result of 2 ** 3?", "6", "8", "16", "4", "8"),
#                 ("What is the output of 'Python'[::-1]?", "nohtyP", "Python", "nythoP", "h", "nohtyP"),
#                 ("How do you round the number 4.5 to the nearest integer in Python?", "round(4.5)", "ceil(4.5)", "floor(4.5)", "truncate(4.5)", "round(4.5)"),
#                 ("What is the syntax for creating a tuple in Python?", "(1, 2, 3)", "[1, 2, 3]", "{1, 2, 3}", "<1, 2, 3>", "(1, 2, 3)"),
#                 ("Which of the following is NOT a valid data type in Python?", "int", "char", "str", "float", "char"),
#                 ("What does the 'and' operator do in Python?", "Logical AND", "Bitwise AND", "Logical OR", "Bitwise OR", "Logical AND"),
#                 ("How do you open a file named 'file.txt' in Python?", "open('file.txt')", "file.open('file.txt')", "file.txt.open('r')", "fopen('file.txt')", "open('file.txt')"),
#                 ("What is the result of 10 / 3 in Python?", "3.3333", "3.0", "3", "3.33", "3.3333"),
#                 ("What is the output of the expression 'Python'[1:-1]?", "ytho", "Pyth", "Python", "yth", "ytho"),
#                 ("Which module in Python supports regular expressions?", "re", "regex", "reg", "regular", "re"),
#                 ("How do you convert a string to uppercase in Python?", "upper()", "to_upper()", "uppercase()", "upper_case()", "upper()"),
#                 ("What is the result of 10 % 3?", "1", "3", "0.1", "2", "1"),
#                 ("What is the output of 'Python' + 'Programming'?", "PythonProgramming", "Python Programming", "PythonProgram", "ProgrammingPython", "PythonProgramming"),
#                 ("How do you check the number of elements in a list in Python?", "len()", "count()", "size()", "length()", "len()"),
#                 ("Which of the following is NOT a valid loop in Python?", "for", "while", "do-while", "foreach", "do-while"),
       
#                     ]

#                 # Insert Python questions into the database
#         for question in python_questions:
#                           c.execute("INSERT  INTO  Questionpython (QUES, OPT1, OPT2, OPT3, OPT4, ANS, ANSWEROPT, CATEGORY) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", 
#                                   (question[0], question[1], question[2], question[3], question[4], question[5], 1, "python coding"))
#         connection.commit()
#         connection.close()
tbl()
# # addData()
    


       

        
