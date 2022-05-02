

# # Wordle Game
# 
# ## Inputs Required
# 
# - Word Corpus as a text file (See format as in WORDLE_FIVE_LETTER_CORPUS.txt
# - n - number of letters to guess (This should be according to your corpus)
# - p - number of tries available to the user
# - The rules for wordle remain the same
# 
# - Green is when a letter is in the word and in the right place
# - Yellow is when a letter is in the word but not in the right place
# - Gray is when the letter isn't in the word

import random


FIVE_LETTER_CORPUS = []
final_cleaned_corpus = open("WORDLE_FIVE_LETTER_CORPUS.txt", "r")
for line in final_cleaned_corpus.readlines():
    FIVE_LETTER_CORPUS.append(line.strip())
    
final_cleaned_corpus.close()





#len(FIVE_LETTER_CORPUS)


# ### I: Getting the n-word list




# n is chosen by user

vocab = FIVE_LETTER_CORPUS
n = 5 #Fixed for our corpus, can change with another corpus
n_words = [w for w in vocab if len(w)==n]








# ### Making sure all words are unique

#n_words = list(set(n_words))











removal_corpus = n_words.copy()


# ### II: Using the n-word list to get word of the 'day' 
# - Once we get it, we remove from removal_corpus, so as to not repeat the word of the day untill we're fully exhuasted










word_of_day = random.choice(removal_corpus)




removal_corpus.remove(word_of_day)





#len(removal_corpus)


# ### III: Logic for Wordle
# - User can set number of tries




class WordError(Exception):
    pass





class WordSetError(Exception):
    pass





def generate_dic(word):
    word_dic = {}
    word = word.lower()
    for letter in word:
        if(letter in word_dic):
            word_dic[letter]+=1
        else:
            word_dic[letter] = 1
            
    return word_dic





p = 6
char_in_word = set(list(word_of_day))

for tries in range(p):
    word_dic = generate_dic(word_of_day)
    flag = 1
    while flag:
        try:
            guess = input("\nEnter your guess!\n")
            flag = 0

            if(len(guess)!=n):
                raise WordError() 
                
            if(guess not in set(n_words)):
                raise WordSetError()
            
        except WordError:
            print(f"\nPlease enter a {n} letter word\n")
            flag = 1
        except WordSetError:
            print("\nWord not in Vocab\n")
            flag = 1

    word_reference = list(word_of_day)
    result_list = [2 for i in range(n)] #Used at end to tell user his result
    possible_yellow = []
    
    #Look for all Greens and Grays first
    for place in range(n):
        guess_word = guess[place]
        if(guess_word==word_of_day[place]):
            word_dic[guess_word]-=1
            result_list[place] = 1
        elif(guess_word not in char_in_word):
            result_list[place] = 0
        
        else:
            possible_yellow.append(place)
            

    #In the result list: 1s are greens and 0s are grays
    #Left are to be decided as yellow or grey based on word_dic
    
    for place in possible_yellow:
        guess_word = guess[place]
        if(word_dic[guess_word]==0):
            result_list[place] = 0
        else:
            word_dic[guess_word]-=1
            
            
    # Result based on the list
    correct_guess = 0
    
    for res in result_list:
        if(res==1):
            print(" Green ", end=" ")
            correct_guess+=1
        elif(res==2):
            print(" Yellow ", end=" "),
        else:
            print(" Gray ", end=" ")
            
    if(correct_guess==len(result_list)):
        print("Guessed Correctly!")
        break
            
print("\nCorrect Word is: ", word_of_day)
        
    
    





