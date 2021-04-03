import os
import csv

NR_OF_LETTERS = 5000

def stopword(wstr):
    w = wstr.strip()
    if len(w) < 4:
        return True
    return False

def get_words(sentence):
    l = sentence.split()
    return l

def read_csv():
    cont_negative = []
    cont_positive = []
    with open('users_5000.csv', encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if(row[0] == "4"):
                for i in get_words(row[3]):
                    if(not stopword(i)):
                        cont_positive.append(i)
            else:
                for i in get_words(row[3]):
                    if(not stopword(i)):
                        cont_negative.append(i)
            line_count += 1

    return cont_negative, cont_positive

ham_l, spam_l = read_csv()

read_ham_words = {}

def countInList(listOfWords, dict):
    l = []
    for i in listOfWords:
        if(i in dict):
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
    return  dict

def listReader(hamSpamList):
    d = {}
    for i in hamSpamList:
        countInList(i, d)
    return d

def totalWords(dict):
    total = 0
    for key, value in dict.items():
        total += value
    return total

def calculate_probablity_of_word(wordsDictionary, nrOfUniqueWords, word, nrOfTotalWords):
    if(word in wordsDictionary):
        return (wordsDictionary[word] + 1) / (nrOfUniqueWords +  nrOfTotalWords)
    else:
        return 1 / (nrOfUniqueWords +  nrOfTotalWords)

def calculateProbablityOfSpam(msg):
    spamWords = listReader(spam_l)
    uniqueWordsSpam = len(spamWords.keys())
    totalWordsSpam = totalWords(spamWords)

    p_spam = len(spam_l) / NR_OF_LETTERS
    probability = 0
    for i in msg:
        #print(probability)
        probability += calculate_probablity_of_word(spamWords, uniqueWordsSpam, i, totalWordsSpam)
    return probability + p_spam

def calculateProbablityOfHam(msg):
    hamWords = listReader(ham_l)
    uniqueWordsHam = len(hamWords.keys())
    totalWordsHam = totalWords(hamWords)

    p_spam = len(ham_l) / NR_OF_LETTERS
    probability = 0
    for i in msg:
        probability += calculate_probablity_of_word(hamWords, uniqueWordsHam, i, totalWordsHam)
    return probability + p_spam

def solve(listOfMsg):
    hamChance = calculateProbablityOfHam(listOfMsg)
    spamChance = calculateProbablityOfSpam(listOfMsg)
    if(hamChance > spamChance):
        return "Negative"
    else:
        return "Positive"

def stringMsgToListMsg(msgString):
    words = [w.strip()
             for w in msgString.replace("\n", " ").split(" ")
             if not stopword(w)
             ]
    return words

msg = "thx 4 the laughs. I'm going to sleep. My head hurts & my scan is butt crack early. Have fun @anon "
msg2 = "no more puppy  i'm really sad"
