import random
word_list=["Naruto","Luffy","Ichigo","Goku"]
chosen_word=random.choice(word_list).lower()
c=0
attempts=0
word_list=["_"]*len(chosen_word)
while c!=len(chosen_word):
    letter=str(input("Please enter a letter you think is present in word\n"))
    attempts+=1
    if letter in chosen_word:
        c+=1
        print("Yes, Entered letter is present in word\n")
        for i in range(0,len(chosen_word)):
            if chosen_word[i]==letter:
                word_list[i]=letter
    else:
        print("No, entered letter is not present in word\n")
    print(f"Present result is {word_list}")
print(f"You took {attempts} attempts to guess the word.")