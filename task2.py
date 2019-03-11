"""
===================   TASK 2   ====================
* Name: Valid Mobile Number In Montenegro
*
* Write a function `valid_mobile_number` that will
* return True if given string is valid mobile phone
* number in Montenegro. Consider that +382 code will
* not be passed.
*
* Phone number is valid if:
*
*  - Has 9 or 10 digits
*  - Begins with '06'
*  - Third digit has to be one of [3, 6, 7, 8, 9]
*  - Contains digits only
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""


def valid_mobile_number(phone_number):
    allowed_characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in phone_number:
        if i not in allowed_characters:
            return False
        else:
            num = str(phone_number)
            if len(num) == 9 or len(num) != 10:
                return True
            if num[0] == "0":
                return True
            if num[1]!= "6":
                return True
            if num[2] != "3":
                return True
            if num[2] != "6":
                return False
            if num[2] != "7":
                return False
            if num[2] != "8":
                return False
            if num[2] != "9":
                return False
    else:
        return phone_number





def main():

    number_to_test = "0699919991"
    if valid_mobile_number(number_to_test):
        print("Phone number is valid in Montenegro!")
    else:
        print("Phone number is invalid in Montenegro!")

main()