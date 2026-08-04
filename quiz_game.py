questions=("how many continents are there?",
           "which is the largest ocean?",
           "what is the capital of France?",
           "how many planets are in the solar system?",
           "which is the smallest prime number?")
options=((" A. 7"," B. 6"," C. 8"," D. 5"," E. 9"),
         (" A. Pacific"," B. Atlantic", "C. Indian"," D. Southern"," E. Arctic"),
         (" A. Paris"," B. Rome"," C. Berlin"," D. Madrid"," E. Amsterdam"),
         (" A. 8"," B. 9"," C. 10"," D. 7"," E. 6"),
         (" A. 2"," B. 3"," C. 5"," D. 7"," E. 11"))
answers=("A", "A", "A", "A", "A")
guesses=[]
score=0
question_num=0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]: 
        print(option)
    guess=input("Enter (A, B, C, D, or E): ").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1
print("-------------------------")
print("         RESULTS         ")
print("-------------------------")
print("Answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()
print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()
score=int(score/len(questions)*100)
print(f"Your score is: {score}%")
