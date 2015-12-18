#  File: Day.py

#  Description: Returns the day of the week when given year, month, and date.

#  Student Name: Evan Yacek

#  Student UT EID: ety78

#  Course Name: CS 303E

#  Unique Number: 50475

#  Date: 9/12/2015

#  Date Last Modified: 9/13/2015

def main():
    
# This is where I prompted the user, and included loops to error check the given data
# I realize some of these variables arent necessary I kept them to help clarify, and simplify my train of thought
    year = h
    month = m
    day = f
    century = d
    
h= int(input("Enter year:"))
while((h < 1900) or (h > 2100)):
    h= int(input("Enter year:"))

# Here I defined my leap year function, so that it is either True or False

isLeapYear = (h % 4 == 0 and h % 100 != 0) or (h % 400 == 0)

# Most the code below is error checking
# By using while loops and my leap year function I was able to reprompt users for non-existent dates

m= int(input("Enter month:"))
while((m < 1) or ( m > 12)):
    m= int(input("Enter month:"))
f= int(input("Enter day:"))

# Error Checking for February during leap year

while((isLeapYear == True) and (m == 2) and (f > 29) or (f < 1)):
    f= int(input("Enter day:"))

# Error Checking for 31 dayed months

while((f < 1) or (f > 31)):
    f= int(input("Enter day:"))

#Error checking for February during non leap years

while((isLeapYear == False) and (m == 2) and (f > 28) or (f < 1)):   
    f= int(input("Enter day:"))

# Error Checking for 30 dayed months

while(((m == 4) or (m == 6) or (m == 9) or (m == 11)) and (f > 30) or (f < 1)):
    f= int(input("Enter day:"))


# This is where I changed the months from our typical calander to the one used in the algorithm

if (m == 2):
   a = 12
elif (m == 1):
   a = 11
elif (m >= 3):
   a = m - 2

# Below I redefined some variables so that they fit into the day of the week algorithm
# Also I determined the d value(century), and c value(years of century)
# I subtracted by one more when calculating the years of the century to account for the proper year

b = f
if (h - 1 >= 1900) and (h - 1 < 2000):
  d = 19
elif(h - 1 >= 2000):
  d = 20
elif( h == 1900):
 d = 18
if (d == 19):
 c = h - 1901
elif( d == 20):
 c = h - 2001
elif(d == 18):
 c = h - 1801

# Below is the given algorithm
 
w = (13 * a - 1 ) // 5 
x = c // 4 
y = d // 4 
z = w + x + y + b + c - 2 * d
r = z % 7 
r = (r + 7) % 7

# Here is where I had to configure my ouput so that the algorithm would be correct for Leap and NonLeap years
# Also the months of February and January gave me trouble, so I created theses statements to ensure the p value was correct

if (isLeapYear == True) and (m == 2) or (m == 1):
    p = r - 1
elif(isLeapYear == False) and (m ==2) or (m == 1):
    p = r - 1
elif (isLeapYear == True):
    p = r + 1
elif(isLeapYear == False):
    p = r

# Finally I included one more negative value, and one more positive -1, 7, since we are potentially adding or subtracting 1

if(p == -1):
  print("The day is Sunday.")
elif(p == 0):
  print("The day is Monday.")
elif(p == 1):
  print("The day is Tuesday.")  
elif(p == 2):
  print("The day is Wednesday.")  
elif(p == 3):
  print("The day is Thursday.")
elif(p == 4):
  print("The day is Friday.")
elif(p == 5):
  print("The day is Saturday.")
elif(p == 6):
  print("The day is Sunday.")
elif(p == 7):
  print("The day is Monday.")

main()