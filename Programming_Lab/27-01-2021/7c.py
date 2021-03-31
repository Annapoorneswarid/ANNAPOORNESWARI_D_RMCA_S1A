Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> list1=[10,12,14,16,18,11,13,15,17,19,12,15]
>>> list2=[10,12,14,16,18,11,13,15,17,19,12,15]
>>> for value in list1:
	if value in list2:
		common=1

		
>>> if common==1:
	print("There are common element")
else:
	print("No common element")

	
There are common element
>>> 