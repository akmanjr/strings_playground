"""
strings_playground.py
This program shows various methods to work with strings.
@author: Can Akman @ the Laboratory
@version: 10.01.2018_v1.0
"""

firstName = "hank"
lastName = "hill"

#Convert into all uppercase letters
print(firstName.upper())
print(lastName.upper())

#Convert into all lowercase letters
print(firstName.lower())
print(lastName.lower())

#Concentenate
fullName = firstName + " " + lastName

#Capitalize the first letter of each word
print(fullName.title())

#Get the count of letters
print(len(firstName))

#Combine strings with coma
print(fullName.title(), "lives on 123 Rainy Street.")
 
#Check if a letter is included in a string. Returns a boolean
print("h" in firstName)
print("i" not in lastName)

#Strip out white blank spaces from a string
print("  Peggy Hill  ".strip())

#Get the letter at a certain index in a string
print(firstName[1])

#Search for and return the index of a given character in a string
print(firstName.find("k"))

#Return the count of a given character in a string
print(lastName.count("l"))

#Replace a character in a string
print(firstName.replace("h", "t"))