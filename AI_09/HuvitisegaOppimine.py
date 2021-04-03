import random

AI = 0
PLAYER = 1

ROLL = 0
PASS = 1

def pig_game(first_ai, sec_ai):
    rolled = 0
    turn = PLAYER
    player_points = ai_points = 0

    while player_points < 100 and ai_points < 100:


        if turn == PLAYER:

            decision = first_ai(turn, rolled, player_points, ai_points)
            if decision == PASS:

                rolled = 0
                turn = AI
            else:
                dieroll = random.randint(1, 6)

                if dieroll == 1:
                    player_points -= rolled # lose all points again
                    rolled = 0
                    turn = AI
                else:
                    rolled += dieroll
                    player_points += dieroll

        else:
            decision = sec_ai(turn, rolled, ai_points, player_points)
            if decision == PASS:

                rolled = 0
                turn = PLAYER
            else:
                dieroll = random.randint(1, 6)

                if dieroll == 1:
                    ai_points -= rolled # lose all points again
                    rolled = 0
                    turn = PLAYER
                else:
                    rolled += dieroll
                    ai_points += dieroll



    if player_points >= 100:
        first_ai(turn, rolled, player_points, ai_points)
        sec_ai(turn, rolled, ai_points, player_points)
        return PLAYER
    elif ai_points >= 100:
        first_ai(turn, rolled, player_points, ai_points)
        sec_ai(turn, rolled, ai_points, player_points)
        return AI


class QLearner:
    def __init__(self):
        self.Q = {}
        self.gamma = 0.8    # discount factor
        self.alpha = 0.2   # learning rate
        self.last_action = 0
        self.last_state = 0
        self.init_Q()
    def init_Q(self):

        for ai in range(101):

            for op in range(101):

                for roll in range(51):
                    self.Q[self.state_idx(ai, op, roll)] = [0, 0]



    def ql_ai(self, turn, rolled, my_points, opp_points):

        reward = 0
        if my_points >= 100:
            reward = 100
        elif opp_points >= 100:
            reward = -100

        state = self.state_idx(my_points, opp_points, rolled)
        max_Q = max(self.Q[state][PASS], self.Q[state][ROLL])

        if not (my_points == 0 and rolled == 0):
            self.update(self.last_state, self.last_action, reward, max_Q)

        if self.Q[state][PASS] > self.Q[state][ROLL] and rolled != 0:
            action = PASS
        else:
            action = ROLL

        if my_points + rolled > 100:
            action = PASS



        self.last_action = action
        self.last_state = state


        return action

    def update(self, s, action, reward, s_prim):

        self.Q[s][action] += self.alpha * (reward + self.gamma * s_prim - self.Q[s][action])


    def state_idx(self, ai_points, opp_points, rolled):
        ap = min(ai_points // 10, 10)  # ai points: 0-9, 10-19, ..., 90-99, 100
        op = min(opp_points // 10, 10)
        r = min(rolled // 5, 10)  # rolled: 0-4, 5-9, ..., 45-49, 50+
        return (ap, op, r)

def dummy_ai(turn, rolled, my_points, opp_points):
    if rolled < 21:
        return ROLL
    else:
        return PASS

def run_game():

    first_q = QLearner()
    sec_q = QLearner()

    wins = 0
    total = 0

    for i in range(1000):
        total += 1
        if pig_game(first_q.ql_ai, sec_q.ql_ai) == PLAYER:
            wins += 1
    print(first_q.Q)

    wins = 0
    total = 0
    for i in range(100):
        total += 1
        if pig_game(first_q.ql_ai, dummy_ai) == PLAYER:
            wins += 1
        print(wins / total)

    for i in first_q.Q:
        #print(i)
        if(i[1] == 5):
            if(first_q.Q[i] != [0,0]):
                print(first_q.Q[i])



run_game()
