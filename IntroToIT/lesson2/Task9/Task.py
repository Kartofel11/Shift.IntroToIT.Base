#INTRO TO IT 2nd COURSE
# Задача 9: Палиндром ли это?
# Определи, является ли введенная строка палиндромом.
def this is a palindrome(string):
return string == string[::-1]
string = "radar"
print(f"Is '{string}' a palindrome? {this is a palindrome(string)}")