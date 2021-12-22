#!/usr/bin/env python3
from enum import Enum
import random
import requests

class Entity(Enum):
    SCISSORS = 0
    PAPER = 1
    ROCK = 2
    LIZARD = 3
    SPOCK = 4

    def loses_to(self, enemy):
        if enemy.value is (self.value+4)%5 or enemy.value is (self.value + 2)%5:
            return True
        return False

def evaluate_winner(p1, p2):
    if p1.value is p2.value:
        return 0
    if p1.loses_to(p2):
        return 2
    return 1

def sendRequest(username, voteScissors, voteRock, votePaper, voteSpock, voteLizard, apiIP = "http://127.0.0.1:5000"):
    reqUrl = apiIP + "/v1/updateRecord"
    reqUrl+= "?username=" + str(username) + "&voteScissors=" + str(voteScissors)
    reqUrl+= "&voteRock=" + str(voteRock) + "&votePaper=" + str(votePaper)
    reqUrl+= "&voteSpock=" + str(voteSpock) + "&voteLizard=" + str(voteLizard)
    responseCode = 0
    try:
        response = requests.post(reqUrl, None)
        responseCode = response.status_code
    except:
        return 0
    return responseCode


input_0 = int(input("Hello. Enter 1 to play vs the computer. Enter 2 to send stats to the api."))
if input_0 == 2:
    stats = open("sspes_stats.txt", "r")
    current_stats = list(map(int, stats.read().split(" ")))
    stats.close()
    print("Request-code: " + str(sendRequest("Alexander", current_stats[2], current_stats[4], current_stats[3], current_stats[6], current_stats[5])))
    exit()

print("You are now playing versus the computer. Pick your Entity:")
print(list(map(lambda c: c.name + ": " + str(c.value), Entity)))

while True:
    stats = open("sspes_stats.txt", "r")
    current_stats = list(map(int, stats.read().split(" ")))
    stats.close()
    
    players_guess = Entity(int(input("Please enter the value of your liking: ")))
    current_stats[2 + players_guess.value] = int(current_stats[2 + players_guess.value]) + 1

    computers_guess = Entity(random.randint(0, 4))
    current_stats[7 + computers_guess.value] = int(current_stats[7 + computers_guess.value]) + 1

    print("The computer has chosen: " + computers_guess.name)
    winner = evaluate_winner(players_guess, computers_guess)
    if winner == 0:
        print("It's a tie!\n")
    if winner == 1:
        print("You have won!\n")
        current_stats[0] = int(current_stats[0]) + 1
    if winner == 2:
        print("The computer has won!\n")
        current_stats[1] = int(current_stats[1]) + 1
    
    stats = open("sspes_stats.txt", "w")
    stats.write(" ".join(list(map(str, current_stats))))