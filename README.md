# Password Strength Calculator

The script calculates and prints the score of the password strength (from 1 to 10)

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

# Calculation logic

Password scores:
* only 1 point if lenght = 1
* 2 points if lenght > 6
* 2 points if it has lower chars
* 2 points if it has upper chars
* 2 points if it has digits
* 2 points if it has spacial chars (%@! etc)

# Quickstart

Example of script launch on Linux, Python 3.5:
```
$ python password_strenght.py
Please enter password:
Your password strength is: 10
```

