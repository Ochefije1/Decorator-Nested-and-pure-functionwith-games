import random
import time
import pickle


def pairAlphaIndex(alphas:list):
    alpha_index = zip(alphas, range(len(alphas))) 
    return list(alpha_index)

def pairAlpha(pairs:list):
    choice_1, choice_2 = random.choices(pairs, k=2)
    pair_alphas = choice_1[0] + choice_2[0]
    total_index = choice_1[1] + choice_2[1]
    return pair_alphas, total_index

def cumPair(alphas, players, turn):
    cum = str()
    cum_total = int()
    identitals = []
    print(players)

    currentPlayer = players[turn]

    print(currentPlayer)

    print(
        f"current Player: {currentPlayer['name']}" 
    )
    
    trials = 0

    while len(cum) <= cum_total:
        pairs = pairAlphaIndex(alphas)
        pair_alphas, total_index = pairAlpha(pairs)
        cum += pair_alphas
        cum_total += total_index

        if pair_alphas[0] == pair_alphas[1]:
            identitals.append(pair_alphas)
            trials += 1
        time.sleep(1)
        print(identitals)

    print(identitals, len(identitals), trials)
        
    updateScore(currentPlayer, len(identitals))

    turn = 0 if turn else turn + 1

    print('turn', turn)

    print(currentPlayer, trials)

    if input('Continue ? ').lower() == 'y':
        cumPair(alphas, players, turn)

    saveScore(players)

    showScoreBoard(players)

def start_game(alphas, players, turn):
    option = input("1. Start New Game\n2. Continue Previous Game\n_____")
    
    if option == '1':
        cumPair(alphas, players, 0)
    else:
        loaded_players = loadScore
        cumPair(alphas, loaded_players, 0)

def showScoreBoard(players):
    board= f"""
    FINAL SCORE:
    \n
    ================================
    \n
    \t Player 1: name: {players[0]['name']}, score: {players[0]['score']}
    \n
    \t Player 2: name: {players[1]['name']}, score: {players[1]['score']}
    \n
    ================================
    """
    print(board)

def updateScore(currentPlayer:dict, score:int) -> None:
    currentPlayer['score'] += score


def saveScore(players):
    with open('savedScores', 'wb') as file:
        pickle.dump(players, file)


def loadScore():
    loaded_score = pickle.load('savedScores')
    return loaded_score


players =[
    {'name':'John', 'score':0},
    {'name':'Nelson', 'score':0}
]

alphas = ['A', 'B', 'C']

start_game(alphas, players, 0)
