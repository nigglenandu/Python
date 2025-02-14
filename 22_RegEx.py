#Regular expressions are used to search for patterns in text, such as matching words, digits, or specific characters.

#Importing the re Module:
import re  # Import the regex module

#Matching a Pattern:
pattern = "hello"
text = "hello world"
result = re.search(pattern, text)
print(result)  # Output: <re.Match object; span=(0, 5), match='hello'>


#Search a String for a Pattern:
result = re.findall("a", "banana")
print(result)  # Output: ['a', 'a', 'a']


#Matching a Pattern at the Beginning:
result = re.match("hello", "hello world")
print(result)  # Output: <re.Match object; span=(0, 5), match='hello'>


#Search and Replace:
text = "I love cats"
result = re.sub("cats", "dogs", text)
print(result)  # Output: I love dogs


#Using Metacharacters:
# \d matches any digit
result = re.findall("\d", "123abc456")
print(result)  # Output: ['1', '2', '3', '4', '5', '6']


#Character Classes:
# [a-z] matches any lowercase letter
result = re.findall("[a-z]", "Hello World")
print(result)  # Output: ['e', 'l', 'l', 'o', 'o', 'r', 'l', 'd']


#Quantifiers:
# + means one or more occurrences of the previous character
result = re.findall("a+", "aaabaaaabaaa")
print(result)  # Output: ['aaa', 'aaaa', 'aaa']