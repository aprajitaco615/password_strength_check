# password_strength_check
A Python command-line program that checks the strength of a password against either standard or custom user-defined conditions.
The program can also optionally modify the password to meet the selected requirements.


This project is currently Version 1 (v1) and is being actively improved.


##What the program does:
Features (v1)
###--Standard Mode
Checks the password against default conditions:
Minimum length: 8 characters
At least 1 uppercase letter
At least 1 lowercase letter
At least 1 number
At least 1 special character

###--Custom Mode
Allows the user to define:
Minimum password length
Minimum number of uppercase letters
Minimum number of lowercase letters
Minimum number of numbers
Minimum number of special characters

--If the total of the selected requirements exceeds the minimum length, the program automatically adjusts the minimum length so all conditions can be satisfied.

###--Automatic Fix Option
If the password does not meet the chosen conditions, the user can opt to:
Automatically add missing character types
Randomly insert required characters
Extend the password length if needed
The updated password is then displayed.
