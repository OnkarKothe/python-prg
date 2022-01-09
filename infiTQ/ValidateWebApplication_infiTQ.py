# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 18:26:11 2022

@author: Onkar
"""

'''
Write a python program to validate the details provided by a user as part of registering to a web application.

Write a function validate_name(name) to validate the user name
    Name should not be empty, name should not exceed 15 characters
    Name should contain only alphabets

Write a function validate_phone_no(phoneno) to validate the phone number
    Phone number should have 10 digits
    Phone number should not have any characters or special characters
    All the digits of the phone number should not be same.
    Example: 9999999999 is not a valid phone number

Write a function validate_email_id(email_id) to validate email Id
    It should contain one '@' character and '.com'
    '.com' should be present at the end of the email id.
    Domain name should be either 'gmail', 'yahoo' or 'hotmail'
Note: Consider the format of email id to be username@domain_name.com

All the functions should return true if the corresponding value is valid. Otherwise, it should return false.

Write a function validate_all(name,phone_no,email_id) which should invoke appropriate functions to validate the arguments passed to it and display appropriate message. Refer the comments provided in the code.

Note: You may use str.isalpha(), str.isdigit() methods to check whether a string contains alphabets or digits alone.


'''

def validate_name(name):
    cnt=0
    if len(name)<16 and len(name)>1:
        for i in name:
            if i.isalpha():
                cnt+=1
    if cnt==len(name):
        return True
    return False

def validate_phone_no(phno):
      cnt=0
      for i in phno:
         if i.isdigit():
            if phno.count(i) < 9:
                cnt+=1
      if cnt==10 and len(phno)==10 :
          return True
      return False
    
def validate_email_id(email_id):
    if email_id.count("@")==1 and email_id.count(".com")==1 :
        if email_id.endswith(".com"):
           #print(1)
           a=(len(email_id)-4)
           if (email_id[0:a]).endswith("yahoo") or (email_id[0:a]).endswith("gmail" ) or (email_id[0:a]).endswith("hotmail" ):
               return True
    return False

def validate_all(name,phone_no,email_id):
    if validate_name(name) :
    
      if validate_phone_no(phone_no) :
          if validate_email_id(email_id):
               print("All the details are valid")
          else:
              print("Invalid email id") 
      else:
        print("Invalid phone number")
    else:
        print("Invalid Name")

#Provide different values for name, phone_no and email_id and test your program
validate_all("str.isalpha()", "9988776655", "Tom@123")