dict = {}
import time
import timeit
import random
turkish_word_list = []
english_word_list = []
def add_to_dictionary(word):
    word = word[:-1]
    liste = word.split("=")
    turkish_word = liste[0]
    english_word = liste[1]
    dict[turkish_word] = english_word
    return "Scaning the words"

number_of_words = 0
with open("top_words.TXT","r",encoding= "utf-8") as word_file:
    for i in word_file:
        add_to_dictionary(i)
        number_of_words += 1

for key in dict.keys():
    turkish_word_list.append(key)
for value in dict.values():
    english_word_list.append(value)
print(turkish_word_list)
print(english_word_list)

print("Number of words:",number_of_words)
while True:
    print("""
    ****************************
                MENU
    ****************************
    1- Daily Word Study
    2- Word List
    3- Only Turkish Words
    4- Only English Words
    5- Ask Randomly
    M- Back to Menu
    """)
    transaction = input("Your Transaction : ")
    if transaction == "1":
        daily_words = random.sample(turkish_word_list,30)
        for word in daily_words:
            question = str(input(word))
            answer = dict[word]
            answer = str(answer)
            if question == answer:
                pass
            else:
                question = str(input(word))
                answer = dict[word]
                answer = str(answer)
                if question == answer:
                    pass
                else:
                    question = str(input(word))
                    answer = dict[word]
                    answer = str(answer)
                    if question == answer:
                        pass
                    else:
                        print("False,","Correct Answer:",answer)
        time.sleep(2)
        continue
    elif transaction == "2":
        for a,b in dict.items():
            print(a,":",b)
        a = input("""Press "M" for back to Menu """)
        if a == "m" or a == "M":
            continue
        else:
            print("You entered an invalid transaction.")
            time.sleep(2)
            continue

    elif transaction == "3":
        for a in turkish_word_list:
            print(a)
        a = input("""Press "M" for back to Menu """)
        if a == "m" or a == "M":
            continue
        else:
            print("You entered an invalid transaction.")
            time.sleep(2)
            continue
    elif transaction == "4":
        for a in english_word_list:
            print(a)
        a = input("""Press "M" for back to Menu """)
        if a == "m" or a == "M":
            continue
        else:
            print("You entered an invalid transaction.")
            time.sleep(2)
            continue
    elif transaction == "5":
        start = time.time()
        just_word = random.choice(turkish_word_list)
        just_question = input(just_word)
        just_answer = dict[just_word]
        just_question = str(just_question)
        just_answer = str(just_answer)
        if just_question == just_answer:
            print("True")
            end = time.time()
            print("Geçen Süre : ", end-start)
            time.sleep(2)
            continue

        else:
            print("False,","Correct Answer :",just_answer)
            end = time.time()
            print("Geçen Süre :", end - start)
            time.sleep(3)

            continue








    
