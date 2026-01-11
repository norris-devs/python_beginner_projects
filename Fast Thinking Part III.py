#Fast_Thinking_Part_3

import time

name = input("Who am I working with today? ")

print("Welcome " + name + "," + " to the third part of our Fast Thinking Exercises.")

time.sleep(2)

number = int(input("Evaluate 2 + 2 "))

if number == 4:
    answer = "Great!" + " Fast Thinking in action"

else:
    answer = "Incorrect." + " The answer is: 4"

print(answer)

time.sleep(2)


color = input("What color comes to mind when the word Chocolate is mentioned? ")

if color.lower() == "brown":
    answer = "Perfect!" + " That is System 1 in action again."

else:
    answer = "Hmm." + " Let's go with Brown for now."

print(answer)

time.sleep(2)

print("Now, time to think more carefully...")

number = int(input("Evalute 25 * 25 "))

if number == 625:
    answer = "Perfect!" + " System 2 is now in charge and has handled calculations."
    print(answer)

else:
    answer = "Hmm..." + " Think more carefully."

time.sleep(2)

while number != 625:
    print(answer)
    time.sleep(2)
    int(input("Evalute 25 * 25 "))

    



time.sleep(2)

print("And finally, one last question...")

mood = input("What would be your reaction, if a friend came up to you after a long, cold day at work and offered a Hot Chocolate ? ")

if mood.lower() == "happy":
    answer = "Perfect!" + " That's what I thought."

elif mood.lower() == "excited":
    answer = "Great!" + " I would have felt exactly the same."

else:
    answer = "Hmm, alright." + " I think we can work with that."

print(answer)

system1_Thoughts = []

system1_Thoughts.extend([4, "Brown"])

system2_Thoughts = []

system2_Thoughts.extend([625, "Happy", "Excited"])

Next_List = []
Next_List.extend([system1_Thoughts, system2_Thoughts])
#print(Next_List)
#print(system1_Thoughts)

if Next_List[0][0] == 4:
    answer = "System 1 got the math right."

else:
    answer = "Corrections will be made."

print(answer)

time.sleep(2)

if Next_List[1][2] == "Excited":
    answer = "System 2 got the reaction right."

else:
    answer = "Corrections will be made."

print(answer)




