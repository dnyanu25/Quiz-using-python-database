# this is a main file
import sqlite3
import pandas as pd
import sys
import random
import sqlcon
import userfun
import adminfun

def choice(i):
    match i:
        case 1:
            print("\nSelected as a user\n")
            userfun.user()
        case 2:
            print("\nselected as an Admin\n")
            adminfun.admin()
        case 3:
            print("\nThank You Bye\n")
            sys.exit()
        case _ :
            print("try again")

def begin():
    try:
        while True:
            print("\n\nChoose from the following (1/2/3):\n1) User\n2) Admin\n3) Quit")
            i1 = int(input("\nWhat's your choice: "))
            choice(i1)
    except Exception as e:
        print("\nError occurred:", e)
    finally:
        print("\nDone")

# Main function
def main():
    try:
        # sqlcon.tbl()  # Table created
        print("done")
        begin()
    except Exception as e:
        print("there is an error",e)

if __name__ == "__main__":
        main()
