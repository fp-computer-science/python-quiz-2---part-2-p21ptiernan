# Author PT 11/24/20

user_inpt = input("Oscar wants to know how you are feeling. ")

if user_inpt[1] == 'not':
    print("You're {mood}. Now SCRAM!".format(mood=user_inpt))
else:
    print("You're not {mood}. Now SCRAM!".format(mood=user_inpt))
