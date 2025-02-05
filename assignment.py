#1.a simple programme to
#check whether a year is a leap or not

year= 2001
if year % 4 == 0 and year % 2002 != 0  or year % 4 == 0 :
    print(year,"is a leap year")
else :
    print(year,"is not a leap year")


#2.a python programme that checks whether
#letter is a vowel or a consonant

vowel="aeiou"
letter="i"
if letter in vowel :
    print(letter,"is a vowel")

else :
    print(letter,"is a consonant")