# -*- coding: utf-8 -*-
"""
Created on Mon May 31 15:20:58 2021

@author: Gouri
"""

#Exceptional handling in Python:
try:
    #code block where exception can occur
    a=b
except:
    print('Some problem might have occured')
    
try:
    #code block where exception can occur
    a=b
except Exception as ex: 
    print(ex)    #it prints message as of error throws
    
a=b  #there is NameError..but the frontend user may not understand what exactly he must do in order to fix it

try:
    #code block where exception can occur
    a=b
except NameError as ex1:
    print('The User has not defined the Varialbe')
except Exception as ex: 
    print(ex)    #it prints message as of error throws

try:
    #code block where exception can occur
    a=1
    b='s'
    c=a+b
except NameError as ex1:
    print('The User has not defined the Varialbe')
except Exception as ex: 
    print(ex)    #it prints message as of error throws

a=1
b='s'
c=a+b
try:
    #code block where exception can occur
    a=1
    b='s'
    c=a+b

except TypeError: #we are throwing our own error
    print('Make the variables of similar datatypes')

except NameError:
    print('The User has not defined the Varialbe')
except Exception as ex: 
    print(ex)    #it prints message as of error throws

try:
    #code block where exception can occur
    a=int(input('Enter the number 1'))
    b=int(input('enter the number 2'))
    c=a/b
    d=a*b
    e=a+b
    print(c)
    print(d)
    print(e)
except TypeError: #we are throwing our own error
    print('Make the variables of similar datatypes')

except NameError:
    print('The User has not defined the Varialbe')
except Exception as ex: 
    print(ex)    #it prints message as of error throws
    
try:
    #code block where exception can occur
    a=int(input('Enter the number 1'))
    b=int(input('enter the number 2'))
    c=a/b
    d=a*b
    e=a+b
    print(c)
    print(d)
    print(e)
except TypeError: #we are throwing our own error
    print('Make the variables of similar datatypes')
except ZeroDivisionError: 
    print("Don't provide 0 as Value of b..rather greater than 0")
except NameError:
    print('The User has not defined the Varialbe')
except Exception as ex: 
    print(ex)    #it prints message as of error throws

try:
    #code block where exception can occur
    a=int(input('Enter the number 1'))
    b=int(input('enter the number 2'))
    c=a/b
    d=a*b
    e=a+b
 
except TypeError: #we are throwing our own error
    print('Make the variables of similar datatypes')
except ZeroDivisionError: 
    print("Don't provide 0 as Value of b..rather greater than 0")
except NameError:
    print('The User has not defined the Varialbe')
except Exception as ex: 
    print(ex)    #it prints message as of error throws
else: # when none of the exceptiona are not caught, then this else part is executed
     print(c)
     print(d)
     print(e)
#else block is executed only when code in try block gets executed without getting caught by exceptions
#try else finally: finally block gets executed irrerespective of success of exection of try block code
try:
    #code block where exception can occur
    a=int(input('Enter the number 1'))
    b=int(input('enter the number 2'))
    c=a/b
    d=a*b
    e=a+b
 
except TypeError: #we are throwing our own error
    print('Make the variables of similar datatypes')
except ZeroDivisionError: 
    print("Don't provide 0 as Value of b..rather greater than 0")
except NameError:
    print('The User has not defined the Varialbe')
except Exception as ex: 
    print(ex)    #it prints message as of error throws
else: # when none of the exceptiona are not caught, then this else part is executed
     print(c)
finally:
    print('The execution is done')
#finally has application in database connection. When we exceptions occur after connecting to a database, such exceptions are handled by exception handling mechanism, but we can still close the database as finally block can access local variables of try block which are necessary to close the database which will be still opened in such scenarios. 
    
#custom exception:
class Error(Exception):
    pass
class dobException(Error):
    pass
class customgeneric(Error):
    pass
year=int(input("Enter your Year of birth"))
age=2021-year
try:  
   if(age<=30 & age>20):
       print("Age is valid. You can apply for the exams")
   else:
       raise dobException
except dobException:
    print(" The age is not within the range to apply for exam...You cannot apply for exam")
    