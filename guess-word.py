word = "hello"
guess_word = ""
limit = 3
count_limit = 0

while guess_word != word and count_limit < limit:
   guess_word = input("Guess the word: ")
   count_limit += 1

if guess_word == word:
   print("You win!")
else:
   print("Out of guesses, you lose")
