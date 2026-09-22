#password security checker
password = input("enter your password: ")
print("\nPassword security results:")
password_lower = password.lower()
#password checks

if len(password) >= 8:
    print ("password is long enough")
else:
    print ("password is too short")

if any(char.isdigit() for char in password):
    print ("password contains a number")
else:
    print("password needs a number")

if any(char.isupper() for char in password):
    print ("password contains an uppercase letter")
else:
    print("password needs an uppercase letter")

if any(char.islower() for char in password):
    print ("password contains a lowercase letter")
else:
    print ("password needs a lowercase letter")

if any( not char.isalnum() for char in password):
    print("password has a special character")
else:
    print("password needs a special character")

#password points
score = 0
if len(password) >= 8:
    score += 1

if any(char.isdigit() for char in password):
    score += 1

if any(char.isupper() for char in password):
    score += 1

if any(char.islower() for char in password):
    score += 1

if any(not char.isalnum() for char in password):
    score += 1

#comparing entered passwords to common weak passwords
common_passwords = [
"password123",
"12345",
"123456",
"123456789",
"test1",
"password",
"12345678",
"zinch",
"qwerty",
"1234567890",
"1234567",
"Aa123456.",
"iloveyou",
"1234",
"abc123",
"111111",
"123123",
"dubsmash",
"test",
"princess"
]

common_found = False
for common_password in common_passwords:
    if common_password in password_lower:
        common_found = True

is_common = common_found

if common_found:
    print("this is a common weak password")

else:
    print("this password is not a common password")

#number patterns
patterns = [
"1234",
"1111",
"2222",
"3333",
"0000"
]
pattern_found = False
for pattern in patterns:
    if pattern in password:
        print("this password contains an obvious pattern")
        pattern_found = True
if pattern_found:
    score -=1

#repeated character checker
repeated = False
for char in password:
    if password.count(char) >=4:
        repeated = True

if repeated:
    print("character is repeated too many times")
    score -=1

#password rating
if is_common:
    print("\npassword is common")

elif score >= 5:
    print("\npassword is strong")

elif score >= 3:
    print("\npassword is medium")

else:
    print("\npassword is weak")

#user feedback
print("\npassword feedback:")

if len(password) < 8:
    print(" minimum of 8 characters needed for a strong password")

if not any(char.islower() for char in password):
    print(" password needs a lowercase character")

if not any(char.isupper() for char in password):
    print("password needs an uppercase character")

if not any(char.isdigit() for char in password):
    print("password needs one or more numbers")

if not any(not char.isalnum() for char in password):
    print("password needs a special character")

if score < 0:
    score = 0
print("\nSecurity score:", score, "/5")

#password summary
if score == 5 and not is_common:
    print("password passes all requirements")

if score <5:
    print("password could be stronger")

