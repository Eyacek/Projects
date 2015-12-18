#  File: EasterSunday.py

#  Description: Calculates date of Easter Sunday

#  Evan Yacek

#  Date Created: 9/4/2015

#  Date Last Modified: 9/4/2015


def main():

# Here I defined my variable y so that I would not recieve a Name error

    year = y

# By using the int function here I was able to turn the user entered string into a integer

y = int(input("Enter year: "))

# After collecting the users data I defined these specific variables in accordance to Gauss' algorithm

a = y % 19
b = y // 100
c = y % 100
d = b // 4
e = b % 4
g = (8 * b + 13) // 25
h = (19  *a + b - d - g + 15) % 30
j = c // 4
k = c % 4
m = (a + 11 * h) // 319
r = (2 * e + 2 * j - k - h + m + 32) % 7
n = (h - m + r + 90) // 25
p = (h - m + r + n + 19) % 32

# Finally since Easter only falls in one of two months I created two if statements with two different outputs
# Since I previously defined y and p I can call on them in my output.

if n == 3 :
    print("In", y , "Easter Sunday is on", p, "March.")
if n == 4 :
    print("In", y , "Easter Sunday is on", p, "April.")
	
main()


	
