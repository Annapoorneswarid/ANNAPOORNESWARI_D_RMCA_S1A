Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> stringA="I like to play every day"
>>> print("Given string:\n",stringA)
Given string:
 I like to play every day
>>> vowels="AaEeIiOoUu"
>>> res=set([each for each in stringA if each in vowels])
>>> print("The vowels present in the string:\n",res)
The vowels present in the string:
 {'o', 'a', 'e', 'i', 'I'}
>>> 