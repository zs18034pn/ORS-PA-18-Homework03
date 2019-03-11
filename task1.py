"""
===================   TASK 1   ====================
* Name: Sum Number Digits
*
* Write a function `sum_digits` that will return
* sum of digits for given integer number.
* If passed value is invalid, function should
* return -1 which indicates something went wrong.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""
def sum_digits(number):
    number = int(number)
    allowed_character = ['0','1','2','3','4','5','6','7','8','9']
    for i in str(number):
        if i not in allowed_character:
            return -1
        else:
            pass
    sumDigit=0
    for digits in str(number):
        sumDigit += int(digits)
    return sumDigit

def main():
    number = 1234
    digit_sum = sum_digits(number)
    print("Sum of digits for given numbers is: ", digit_sum)

main()