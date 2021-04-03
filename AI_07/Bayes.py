import os

NUMBER_OF_LETTERS = 6000

def stopword(wstr):
    w = wstr.strip()
    return True if len(w) < 4 else False

def read_directory(dirn):
    cont_l = []
    for fn in os.listdir(dirn):
        with open(os.path.join(dirn, fn), encoding="latin-1") as f:
            words = [w.strip()
                for w in f.read().replace("\n", " ").split(" ")
                    if not stopword(w)
            ]
            cont_l.append(words)
    return cont_l

def count_list(listOfWords, dict):
    for i in listOfWords:
        if(i in dict):
            dict[i] = dict[i] + 1
        else:
            dict[i] = 1
    return  dict

def read_list(spam_ham_list):
    spam_dictionary = {}
    for list_content in spam_ham_list:
        count_list(list_content, spam_dictionary)
    return spam_dictionary


def count_total_words(wordDictionary):
    total = 0
    for key, value in wordDictionary.items():
        total += value
    return total

def calculate_probablity_of_word(wordsDictionary, nrOfUniqueWords, word):
    return (wordsDictionary[word] + 1) / (nrOfUniqueWords +  nrOfUniqueWords) if word in wordsDictionary else 1 / (nrOfUniqueWords +  nrOfUniqueWords)

def calculate_ham_chance(msg):
    words_ham = read_list(ham)
    unique_words_ham = len(words_ham.keys())

    spam_probability = len(ham) / NUMBER_OF_LETTERS
    probability = 0
    for i in msg:
        probability += calculate_probablity_of_word(words_ham, unique_words_ham, i)
    return probability + spam_probability

def calculate_spam_chance(msg):
    words_spam = read_list(spam)
    unique_words_spam = len(words_spam.keys())

    spam_probability = len(spam) / NUMBER_OF_LETTERS
    probability = 0
    for i in msg:
        probability += calculate_probablity_of_word(words_spam, unique_words_spam, i)
    return probability + spam_probability

def solve(listOfMsg):
    ham_chance = calculate_ham_chance(listOfMsg)
    spam_chance = calculate_spam_chance(listOfMsg)
    return False if spam_chance < ham_chance else True


def make_string_to_list(msgString):
    words = [w.strip()
             for w in msgString.replace("\n", " ").split(" ")
             if not stopword(w)
             ]
    return words

if __name__ == '__main__':
    ham = read_directory("enron3\ham")
    spam = read_directory("enron3\spam")
    
    read_ham_words = {}
    
    text = """Subject: cleburne issues
    daren , with megan gone i just wanted to touch base with you on the status of the enron payments owed to the cleburne plant . the current issues are as follows :
    november gas sales $ 600 , 377 . 50
    october payment to ena for txu pipeline charges $ 108 , 405 . 00
    cleburne receivable from enron $ 708 , 782 . 50
    less : november gas agency fees ( $ 54 , 000 . 00 )
    net cleburne receivable from enron $ 654 , 782 . 50
    per my discussions with megan , she stated that about $ 500 k of the $ 600 k nov gas sales was intercompany ( desk to desk ) sales , with the remainder from txu . are we able to settle any intercompany deals now ? are we able to settle with txu ?
    additionally , you ' ll see that i included the oct txu payment in the receivable owed to cleburne also . this is because i always pay megan based upon the pipeline estimates in michael ' s file , even though they are not finalized until the next month . therefore in my november payment to enron , i paid ena for october ' s estimate , of which megan would have paid the final bill on 12 / 26 / 01 when it was finalized . however , i had to pay the october bill directly last month , even though i had already sent the funds to ena in november . therefore , i essentially paid this bill twice ( once to ena in nov & once to txu in dec ) . i deducted the november agency fees from these receivable totals to show the net amount owed to cleburne .
    please advise as to the status of these bills . you can reach me at 713 - 853 - 7280 . thanks ."""
    
    text_spam = """Subject: immediate contract payment .
    immediate contract payment . our ref : cbn / ird / cbx / 021 / 05
    attn :
    during the auditing and closing of all financial records of the central bank of nigeria ( cbn ) it was discovered from the records of outstanding foreign contractors due for payment with the federal government of nigeria in the year 2005 that your name and company is next on the list of those who will received their fund .
    i wish to officially notify you that your payment is being processed and will be released to you as soon as you respond to this letter . also note that from the record in our file , your outstanding contract payment is usd $ 85 , 000 , 000 . 00 ( eighty - five million united states dollars ) .
    kindly re - confirm to me if this is inline with what you have in your record and also re - confirm the information below to enable this office proceed and finalize your fund remittance without further delays .
    1 ) your full name .
    2 ) phone , fax and mobile # .
    3 ) company name , position and address .
    4 ) profession , age and marital status .
    5 ) copy of drivers license i . d .
    as soon as the above information are received , your payment will be made available to you via an international certified bank draft , which will be delivered to your doorstep for your confirmation . you should call my direct number as soon as you receive this letter for further discussion and more clarification . also get back to me on this e - mail address ( payment _ info _ 10 @ yahoo . com ) and ensure that you fax me all the details requested to my direct fax number as instructed .
    best regards ,
    prof . charles c . soludo .
    executive governor
    central bank of nigeria ( cbn )
    tel : 234 - 1 - 476 - 5017
    fax : 234 - 1 - 759 - 0130
    website : www . cenbank . org
    mail sent from webmail service at php - nuke powered site
    - http : / / yoursite . com"""
    
    print(solve(make_string_to_list(text)))
    print(solve(make_string_to_list(text_spam)))








