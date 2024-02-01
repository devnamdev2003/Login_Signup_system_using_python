from verification_otp_using_text_message import verification
import re

import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
def login():
    entry = False
    print()
    f = open(
        r"C:\Users\dell\Documents\codeing\programing\python\login_signup\data.txt", "r")
    text = f.read()
    list = text.split("\n")
    key = input("Enter Email: ")
    for i in range(1, len(list)):
        list1 = list[i].split("|")
        if(key == list1[3]):
            entry = True
            break
        elif i == len(list)-1:
            print("Your Email is Wrong / You don't have an account")
            input("Press Enter")
            print()
            return -1
    if entry == True:
        while True:
            password = input("Enter Password: ")
            if password != list1[5]:
                print("")
                print("--"+"⚠️"+"  Wrong Password"+"⚠️"+" --")
                print("for forget password: 1")
                print("for re-enter password: 2")
                print("for back to login signup page: 3")
                event = input("Enter Your Command: ")
                print()
                if event == "1":
                    while True:
                        num = "+91"+input("Enter Your Number: ")
                        if num == list1[4]:
                            verification(num)
                            print()
                            input("For See Your Password Press Enter:")
                            print("Your Password is:", list1[5])
                            print()
                            break
                        else:
                            print("--"+"⚠️"+"  Wrong Number"+"⚠️"+" --")
                            print()
                if event == "3":
                    print()
                    break
            else:
                print("")
                for i in range(int((int(len(list1[3]))+28)/2)):
                    print("-*", end="")
                print()
                print("| Your ID:            ", list1[0])
                print("* Your Name:          ", list1[1])
                print("| Your Branch:        ", list1[2])
                print("* Your Email:         ", list1[3])
                print("| Your Mobile Number: ", list1[4])
                for i in range(int((int(len(list1[3]))+28)/2)):
                    print("*-", end="")
                print()
                input("Press Enter")
                print()
                break
    else:
        print("Your Email is Wrong / You don't have an account")
        input("Press Enter")
        print()
        return -1
    f.close()


def signup():
    f = open(
        r"C:\Users\dell\Documents\codeing\programing\python\login_signup\data.txt", "r")
    text = f.read()
    list = text.split("\n")
    print("")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    while True:
        first = input("| Enter Your Name: ")
        if first == "":
            continue
        else:
            break
    while True:
        stream = input("* Enter Your Branch: ")
        if stream == "":
            continue
        else:
            break
    while True:
        present = False
        email = input("| Enter Your Email: ")
        if re.search("@.*.com$", email):
            pass
        else:
            print("* Wrong format"+"⚠️")
            continue
        for i in range(1, len(list)):
            list2 = list[i].split("|")
            if(email == list2[3]):
                print()
                print("| This Account Is Already Preasent")
                print("* For back Login Signup Page: 1")
                print("| For re-enter Email:         2")
                get = input("* Enter Your Command: ")
                if get == "2":
                    present = True
                    break
                else:
                    print()
                    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
                    print()
                    return -1
            else:
                present = False
        if present == False:
            break
        else:
            print()
            continue
    while True:
        try:
            number = int(input("* Enter Your Mobile Number: "))
            number = str(number)
            if len(number) != 10:
                print("| Wrong Number ⚠️")
                continue
            else:
                break
        except ValueError:
            print("| Enter only numbers ⚠️")

    password = input("| Enter Your password: ")
    id = 2000+len(list)
    print("* ----Thanks 🙏 For Creating an account-----")
    information = ["\n", str(id), "|", first,
                   "|", stream, "|", email, "|+91", number, "|", password]
    f = open(
        r"C:\Users\dell\Documents\codeing\programing\python\login_signup\data.txt", "a")
    f.writelines(information)
    f.close()
    print("| -------- Your Key is:", id, "---------")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    input("Press Enter")
    print()
    id = id+1


id = 2000


def main():
    print("")
    print("-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*")
    print("-*-*-*--LOGIN/SIGNUP SYSTEM--*-*-*-*-")
    print("-*-*-*-*-*-*-*-*-*--*-*-*-*-*-*-*-*-*")

    while True:
        print("For login: 1")
        print("For Signup: 2")
        print("For exit: 3")
        command = input("Enter your command: ")
        if command == '1':
            login()
        elif command == '2':
            signup()
        elif command == '3':
            print("Thank you!😊")
            break
        else:
            print()
            print("Wrong command ⚠️")
            print()
main()
