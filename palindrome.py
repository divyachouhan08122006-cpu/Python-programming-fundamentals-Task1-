#to check palindrome
string=input("enter a string:")
rev_string=string[::-1]
if string==rev_string:
    print("palindrome.")
else:
    print("not palindrome.")
