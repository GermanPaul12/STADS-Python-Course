# Project 2 Love Generator

Everyone knows the love generators from the internet. You input two names and get a love score.
Today you will programm your own love generator. You can be creative and create it all alone with your own creativity or you can use the this template:

name1 = your name
name2 = their name
comndined_string = name1 + name2  # it's a good idea to convert it to all lowercase

t = number of t's in combined_string
r = number of r's in combined_string
u = number of u's in combined_string
e = number of e's in combined_string

first_digit = t + r + u + e

l = number of l's in combined_string
o = number of o's in combined_string
v = number of v's in combined_string
e = number of e's in combined_string

second_digit = l + o + v + e

love_score = first_digit + second_digit

if the love score is under 10 or greater than 90 then print the score and the phrase "you go together like coke and mentos"
if the love is between inclusive 40 and inclusive 50 then print the score and the phrase "you are mid together"
if the love score is 69 then print the score and the phrase "you are like ying and yang"
else print the score and the phrase "you are like bonnie and clyde"
