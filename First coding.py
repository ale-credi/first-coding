# Current Year
year = 2023
# Ask for the name of the person
user_name = input('What is your first name ')
print('Hello ', user_name)
# Ask for first and last name to put them together with function
last_name = input('What is your last name ')
full_name = user_name + ' ' + last_name
print('Your full name is', full_name)
print('Your full name length is', len(full_name),
      'characters long'
      )
# Ask for the birth year and calculate the age
birth_year = int(input('What is your year of birth (YYYY) '))
# Ask for the age
age = year - birth_year
print('You are ',
      age,
      ' years old.')
# If-else statements
if age >= 18:
    print('You are an adult')
elif age >= 13:
    print('You are a teen')
else:
    print('You are too young')
if age < 13:
    print('You are not eligible to have a bank account')
else:
    print('Welcome to Credi Banking')

# Check eligibility
if age > 13:
    # Generate Password and Store as a value
    password_bank = user_name[0].upper() + last_name[0].upper() + str(birth_year % 100)
    print(
        'Your automatically generated password is: ',
        password_bank,
    )
    print('Your password will be shown as',
          '*' * 4)
# Verify user password
login_password = input('Please re-enter your password: ')
if login_password == password_bank:
    print("Password correct! You have successfully signed up.")
else:
    while login_password != password_bank:
       print("Password incorrect. Please re-enter your password: ")
       login_password = input()
# Fill in more data after successfull login
print("Welcome to your Credi Banking Account")
address = input("Please enter your address: ")
print("Your address is ", address)
phone_number = input("Please enter your phone number: ")
print("Your phone number is: ", phone_number)
Home_Currency = input("We currently offer accounts in USD, EUR and GBP. Enter your currency of choice: ")
print("Your account will now be opened in ", Home_Currency)
# Account value
account_money = str(input("Enter the amount of money you want transfer to this account: "))
print("You have a total balance of ", account_money, Home_Currency)
# Convert account balance in different currency

