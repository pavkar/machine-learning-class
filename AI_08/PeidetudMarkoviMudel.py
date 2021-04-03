import BayesiKlassifikaatorUus
import csv
import numpy


def read_csv():
    cont_negative = []
    cont_positive = []
    with open('users_5000.csv', encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        oldrow = ""
        pp = 0
        pn = 0
        np = 0
        nn = 0
        for row in csv_reader:
            if (line_count > 1):
                if (row[0] == "0" and oldrow == "0"):
                    nn += 1
                if (row[0] == "4" and oldrow == "0"):
                    pn += 1
                if (row[0] == "0" and oldrow == "4"):
                    np += 1
                if (row[0] == "4" and oldrow == "4"):
                    pp += 1
            line_count += 1
            oldrow = row[0]
        pp, pn = normalize(pp, pn)
        np, nn = normalize(np, nn)
    return pp, pn, np, nn

cont_negative, cont_positive = BayesiKlassifikaatorUus.read_csv()

def solve_list_of_tweets(list, p, n):
    pp, pn, np, nn = read_csv()
    for i in list:
        p, n = solve_single_tweet(i, p, n)
        p = pp * p + n * np
        n = pn * p + n * nn
    return p,n

def normalize(p, n):
    total = p + n
    p = p / total
    n = n / total
    return p, n

def solve_single_tweet(tweet, p, n):
    listOfMsg = BayesiKlassifikaatorUus.stringMsgToListMsg(tweet)
    negativeChance = BayesiKlassifikaatorUus.calculateProbablityOfHam(listOfMsg)
    positiveChance = BayesiKlassifikaatorUus.calculateProbablityOfSpam(listOfMsg)
    return normalize(positiveChance * p, negativeChance * n)

listOfTweets = ["@anon @anon thx 4 the laughs. I'm going to sleep. My head hurts & my scan is butt crack early. Have fun @anon ",
"@anon doing good. Going to take pics of my sidekick in a little bit. She is going to prom today ",
"@anon how are you feeling that both of your teams lost hahahahahaha...sorry ",
"@anon lol looks like I'm just going to catch a regular season game NEXT YEAR ",
"@anon I like that. I'm going to put that one in my notebook ",
"@anon ok kidding about Dwight. He's cute but I really admire him as a bball player.  I love the game again ",
"Wow once again home alone for the night...hmm now this is sad. I have no life. Nah I take that back, have time to spend w/ God ",
"@anon just wanted to say hi ",
"I'm sorry if I'm a downer but it's hard to not be emotional right now. I didn't want to see Monica pass so I stayed home... ",
"@anon yeah yeah I know.....not really thrilled about that place sorry....that was my bad "]

listOfTweets2 = ["Going to search out areas we would like for our dream home to also home my home based business one day soon. ",
"Have beautiful dreams all, I'm off to snuggle down with my beautiful babies as they are done with the outdoors. ",
"@anon Cheeers to a dull day girl.. hoping for one here also. ",
"@anon That sounds like an awesome day.  Have a terrific time. ",
"Mmmm.. fresh nettle tea so yummy. ",
"I'm wondering what to have for Breaky along with my iced nettle tea??!   Don't really feel hungry for anything else.",
"@anon Oh I love this and have joined myself.. or maybe it was Kind Blog I joined.. I best make sure.   Peace to you lovely lady!",
"@anon Cool!  Thank you.. it's a beautiful flower now is it medicinal? ",
"@anon Good morning hairy vegan rock loving guy!  No dreams that I remember but a lovely sleep non the less!  What did you dream?",
"@anon Sweet book!  I think.. lol  Sounds good anyway. ",
"@anon I'm excited but offering someone a sound healing also sounds great.  I'm starting Reiki at the farmers market also! Here we go! ",
"http://url - Full Moon Wild Rose Petal Rose Quartz honey, vinegar and infusion picked and co-created today.  Love!"]
print(solve_list_of_tweets(listOfTweets, 0.5, 0.5))
print(solve_list_of_tweets(listOfTweets2, 0.5, 0.5))

