print("Welcome to our competition!\nPlease enter your answers in lower case.")

point = 100

question1 = input("Which is the largest group on the food pyramid?\n").capitalize()

if question1 != "Plants":
  point -= 10

question2 = input("Where is the tallest building in the world?\n").capitalize()

if question2 != "Dubai":
  point -= 10

question3 = input("Which country produces the most coffee in the world?\n").capitalize()

if question3 != "Brazil":
  point -= 10

question4 = input("What is the capital city of Spain?\n").capitalize()

if question4 != "Madrid":
  point -= 10

question5 = input("What language has the most words?\n").capitalize()

if question5 != "English":
  point -= 10

question6 = input("Name the world's largest ocean.\n").capitalize()

if question6 != "Pacific":
  point -= 10 

question7 = input("Which country is Prague in?\n").capitalize()

if question7 != "Czech republic":
  point -= 10

question8 = input("How many weeks are in a year?\n")

if question8 != "52":
  point -= 10

question9 = input("What is the world's longest river?\n").capitalize() 

if question9 != "Amazon":
  point -= 10

question10 = input("Who played Neo in The Matrix?\n").capitalize()

if question10 != "Keanu reeves":
  point -= 10

if point > 50:
  print(f"Your score is: {point}. Congrats, You win!")
else:
  print(f"Your score is: {point}. You lose.")
