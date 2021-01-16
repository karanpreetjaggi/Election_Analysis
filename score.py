#what is the score?
score = int(input("what is the score? "))

#Determine the grade
if score >= 90:
   print('Your grade is A.')
elif score >= 80:
    print('Your grade is B.')
elif score >= 70:
    print('Your grade is C.')
elif score >= 60:
    print('Your score is D.')
else:
    print('Your score is F.')