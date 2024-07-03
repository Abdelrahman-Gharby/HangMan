import random


def importaword():
    with open('words.txt', 'r') as file:
        content = file.read()
    words = content.split('\n')
    word = random.choice(words)
    word = word.lower()
    characters = list(word)
    return word, characters


def checker(new_letter, new_word, correct, my_word, history, tries, result):

    if new_letter in history:
        print('you used this character')
        return result , tries
    history.append(new_letter)
    if new_letter in new_word:

        correct.append(new_letter)
        my_word.append(new_letter)
        count = new_word.count(new_letter)
        if count > 1:
            for i in range(1, count):
                my_word.append(new_letter)
        my_word = sorted(my_word)
        result = hd(new_word, correct )


    else:
        tries -= 1
        result = hd(new_word, correct)
        print(f" you have a {tries} tries")

    return result ,tries


def hd(new_word, correct):
    strr = ''
    for i in new_word:
        if i in correct:
            strr += i
        else:
            strr += '_'
    return strr


def printer(actuall, my_word, tries):
    if actuall == my_word:
        return 2
    elif tries == 0:
        return 0



word, characters = importaword()
#print(word)
tries = 10

history = []
correct = []
my_word = []
result = hd(characters,correct)
print(result)
while tries != 0:
    letter = input('please enter a guess ').lower()
    if len(letter) != 1 or not letter.isalpha():
        print("Please enter a single letter.")
        continue
    result, tries = checker(letter,characters, correct, my_word, history, tries ,result)
    print("your word is " + result)
    state = printer(word, result, tries)
    if state == 2:
        print('you won')
        break
    elif state == 0:
        print('you lose')
        break

