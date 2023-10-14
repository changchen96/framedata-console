import os
import sys
import json
import requests

def queryFrames(char, movestring):
    movelist_path = os.getcwd() + "/tekken7/" + str(char) + ".json"
    with open(movelist_path) as movelist_file:
        movelist = json.load(movelist_file)
    for move in movelist:
        if movestring.lower() == "ra":
            print(moveDictionary(movelist[0]))
            exit()
        if movestring == move[0]:
            print(moveDictionary(move))
            exit()

def moveDictionary(move):
    return {
        "Command": move[0],
        "Hit level": move[1],
        "Damage": move[2],
        "Start-up frame": move[3],
        "Block frame": move[4],
        "Hit frame": move[5],
        "Counter-hit frame": move[6],
        "Notes": move[7]
    }

char = sys.argv[1]
movestring = sys.argv[2]

queryFrames(char, movestring)