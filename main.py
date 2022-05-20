import words
import random
from art import logo, stages
from replit import clear 

print(logo)

lives = 6

#Palabra aleatoria
chosen_word = random.choice(words.word_list)

#Blanks
display = []

#Cantidad de Blanks por palabra
for _ in range(len(chosen_word)):
  display += "_"

print(display)

end_of_game = False


while end_of_game == False:
  guess = input("Guess a letter: ").lower()
  clear()
  if guess in chosen_word:
    print(f"You've already guessed {guess}.")
  for position in range(len(chosen_word)):
      letter = chosen_word[position]
      if letter == guess:
        display[position] = letter
  if guess not in chosen_word:
      print(f"You guessed {guess}, that's not in the word. You lose a life.")
      lives = lives - 1
      if lives == 0:
        end_of_game=True
        print("You lose!")
  print(f"{' '.join(display)}")

  
  if "_" not in display:
    end_of_game = True
    print("You win!")
  print(stages[lives])