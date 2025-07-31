import random
words=["Python","apple","banana","car","nice","computer","book","desk"]
selected_word=random.choice(words)
rights=6
letters_called=[]
predicted=["_"]*len(selected_word)
while rights>0 and "_" in predicted:
    print("\n" + "".join(predicted))
    print(f"Remaining right:{rights}")
    print(f"Tried letters: {', '.join(letters_called)}")
    letter = input("Guess a letter: ").lower()
    if not letter.isalpha() or len(letter) != 1:
        print("Please enter only one letter.")
        continue
    if letter in letters_called:
        print("You already tried this letter.")
        continue
    letters_called.append(letter)
    if letter in selected_word:
        for i in range(len(selected_word)):
            if selected_word[i] == letter:
                predicted[i] = letter
    else:
        rights -= 1
        print("Wrong guess!")
if "_" not in letters_called:
    print("\nCongratulations! You won! Word:", selected_word)
else:
    print("\nYou lost! Kelime:", selected_word)