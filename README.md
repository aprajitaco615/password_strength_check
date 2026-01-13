#password_strength_check
A Python command-line program that checks the strength of a password against either standard or custom user-defined conditions.
The program can also optionally modify the password to meet the selected requirements.
This project is currently Version 2 (v2) and is being actively improved.

##Working of the program :

Features
###v1 – Core Functionality


--Standard Mode
Checks the password against default conditions:
Minimum length: 8 characters
At least 1 uppercase letter
At least 1 lowercase letter
At least 1 number
At least 1 special character


--Custom Mode
Allows the user to define:
Minimum password length
Minimum number of uppercase letters
Minimum number of lowercase letters
Minimum number of numbers
Minimum number of special characters

If the total of the selected requirements exceeds the minimum length, the program automatically adjusts the minimum length so all conditions can be satisfied.


--Automatic Fix Option
If the password does not meet the chosen conditions, the user can opt to:
Automatically add missing character types
Randomly insert required characters
Extend the password length if needed
Display the updated password


###v2 – Improvements & Enhancements

--Improved Length Handling
Password length is recalculated after missing character types are added.
Ensures the final password always meets the minimum length requirement without over- or under-extension.


--Secure Randomization
Newly added characters are shuffled randomly to avoid predictable placement.
Prevents patterns such as added characters always appearing at the end.


--Cleaner Validation Flow
Improved validation logic for custom requirements.
Ensures no requirement is negative or exceeds the minimum length.


--More Robust Password Modification
Character additions are handled in a controlled order:
Required character types
Remaining length adjustment
Prevents logical conflicts between conditions.


© 2026 aprajitaco615 All Rights Reserved.
