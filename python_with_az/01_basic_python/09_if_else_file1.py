import re


haider_age = 20
required_age_at_school = 5

# question: can haider go to school

if required_age_at_school == haider_age:
    print("Haider can join the school")
elif haider_age > required_age_at_school:
    print("Join primary school")

elif haider_age <= 2:
    print("take care haider")

else:
    print("Haider can join school")
