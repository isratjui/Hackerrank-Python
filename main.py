'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

def is_leap(year):
    leap = False
    if (year%4==0)and ((year%100!=0) or (year%400==0)):
        leap = True
        return leap
    
    else:
        return leap
        
n = int(input())
print(is_leap(n))
