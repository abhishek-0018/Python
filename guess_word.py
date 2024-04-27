import random
word_list=["Naruto","Luffy","Ichigo","Goku"]
chosen_word=random.choice(word_list).lower()
letter=str(input("Please enter a letter to be searched\n"))
print(chosen_word)
c=0
for i in chosen_word:
    if i == letter:
        c+=1
        break
if c==1:
    print("Yes, letter is present in the random word")
else:
    print("No, letter is not present in random word")