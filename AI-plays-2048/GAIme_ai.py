import numpy as np
import random
import GAIme

runs = 100
actions = ["left", "right", "down", "up"]
defActions = [GAIme.Game.left, GAIme.Game.right, GAIme.Game.down, GAIme.Game.up]

actionsScores = [0, 0, 0, 0]


def bestMove(current):
    for i, action in enumerate(actions):
        for i in range(runs // 4):
            AI = GAIme.Game()
            AI.matrix = current.getMatrix()
            if action == "left":
                GAIme.Game.left(AI, "<Left>")
            elif action == "right":
                GAIme.Game.right(AI, "<Right")
            elif action == "down":
                GAIme.Game.down(AI, "<Down>")
            elif action == "up":
                GAIme.Game.up(AI, "<Up>")
            while not (GAIme.Game.game_over(AI)):
                random.choice(defActions)()
            actionsScores[i] += AI.getScore()

    highestScore = max(actionsScores)
    highestScoreIndex = actionsScores.index(highestScore)
    topMove = actions[highestScoreIndex]

    if topMove == "left":
        GAIme.Game.left(AI, "<Left>")
    elif topMove == "right":
        GAIme.Game.right(AI, "<Right")
    elif topMove == "down":
        GAIme.Game.down(AI, "<Down>")
    elif topMove == "up":
        GAIme.Game.up(AI, "<Up>")
