import random
dice = [1,2,3,4,5,6]
result = random.choice(dice)
print("The number on the dice is: ", result)

probability = round(dice.count(6)/len(dice), 5)
print("Probability of getting 6 is: ", probability)
