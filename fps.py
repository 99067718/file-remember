####
import random
import threading
import time
import tkinter
import pygame
import os.path
import json
from tkinter import messagebox

if os.path.exists("data/highscore.json"):
    with open("data/highscore.json","r") as file:
        highscoreDict = json.load(file)
else:
    with open("data/highscore.json","w") as file:
        file.write('{"highscore1" : 0,"highscore2" : 0,"highscore3" : 0,"highscore4": 0,"highscore5" : 0,"highscore6" : 0,"highscore7" : 0,"highscore8" : 0,"highscore9" : 0,"highscore10" : 0}')
        highscoreDict = {"highscore1" : 0,"highscore2" : 0,"highscore3" : 0,"highscore4": 0,"highscore5" : 0,"highscore6" : 0,"highscore7" : 0,"highscore8" : 0,"highscore9" : 0,"highscore10" : 0}

highscore = highscoreDict["highscore1"]

currentScore = 0
listOfMoves = ["Press A", "Press S", "Press D", "Press W", "Triple Click", "Double Click","Click Once", "Press SpaceBar"]
#######################

#########3

def restartGame():
    global currentScore
    print("restarting game...")
    threading.Timer(1.0, timerOfGame).start()
    finalScoreLabel.destroy()
    currentScore = 0
    RestartButton.destroy()
    exitButton.destroy()
    movePicker()


def addScore(event):
    global currentScore
    global highscore
    match chosenMove:
        case "Press A":
            window.unbind("<a>")
        case "Press S":
            window.unbind("<s>")
        case "Press D":
            window.unbind("<d>")
        case "Press W":
            window.unbind("<w>")
        case "Press SpaceBar":
            window.unbind("<space>")
    if chosenMove == "Triple Click" or chosenMove == "Double Click" or chosenMove == "Click Once":
        currentScore += 2
    else:
        currentScore += 1
    if currentScore > highscore:
        highscore = currentScore
        HSValue.set(f"Highscore: {highscore}")
    currentScoreVar.set(f"Current Score: {currentScore}")
    TaskLabel.destroy()
    movePicker()

def exitGame():
    window.destroy()
    
    for i in range(9):
        var1 = 11 - i
        var2 = 10 - i
        print(var1)
        try:
            if highscoreDict[var1] < highscoreDict[var2]:
                highscoreDict[var1] = highscoreDict[var2]
        except:
            print("poop")
    print(highscoreDict)
    highscoreDict["highscore1"] = highscore
    with open("data/highscore.json","w") as file:
        file.write(str(highscoreDict))
    messagebox.showinfo(message=str(highscoreDict))
    exit()

def timerOfGame():
    global finalScoreLabel
    global timeLeft
    global RestartButton
    global exitButton
    timeLeftText = " seconds left"
    timeLeft = 60
    timeVar = tkinter.StringVar(value= str(timeLeft) + timeLeftText)
    timerLabel = tkinter.Label(textvariable=timeVar, bg="black",fg="white",font=("Comic Sans MS", 14))
    timerLabel.place(y=10,x=330)
    for i in range(60):
        time.sleep(1)
        timeLeft -= 1
        timeVar.set(str(timeLeft) + timeLeftText)
    i = 0
    timerLabel.config(bg="black",fg="red")
    for i in range(10):
        time.sleep(0.05)
        TaskLabel.destroy()
    finalScore = currentScore
    finalTextvar = tkinter.StringVar(value=f"Your final score is: {currentScore}") 
    finalScoreLabel = tkinter.Label(textvariable=finalTextvar, padx=70,pady=50,font=("Comic Sans MS", 14))
    finalScoreLabel.place(x= 100, y= 110)
    RestartButton = tkinter.Button(text="Click here to restart",command= restartGame,padx=10,pady=30)
    RestartButton.place(x= 50, y= 300)
    exitButton = tkinter.Button(text="Close game", command= exitGame,padx=10,pady=30)
    exitButton.place(x= 400, y= 300)


def movePicker():
    global TaskLabel
    global chosenMove
    chosenMove = random.choice(listOfMoves)
    TaskLabel = tkinter.Label(window,text=chosenMove,font=("Comic Sans MS", 12),pady=10,padx=16)
    Xpos = random.randint(0,400)
    Ypos = random.randint(50,350)
    TaskLabel.place(x=Xpos,y=Ypos)
    match chosenMove:
        case "Press A":
            window.bind("<a>", addScore)
        case "Press S":
            window.bind("<s>", addScore)
        case "Press D":
            window.bind("<d>", addScore)
        case "Press W":
            window.bind("<w>", addScore)
        case "Triple Click":
            TaskLabel.bind("<Triple-Button-1>", addScore)
        case "Double Click":
            TaskLabel.bind("<Double-Button-1>", addScore)
        case "Click Once":
            TaskLabel.bind("<Button-1>", addScore)
        case "Press SpaceBar":
            window.bind("<space>", addScore)

window = tkinter.Tk()
window.attributes('-topmost',True)
HSValue = tkinter.StringVar(value=f"Highscore: {highscore}")
window.geometry("500x400")
MainFrame = tkinter.Label(bg="#21354a",padx=1000,pady=1000)
MainFrame.pack()
blackbar = tkinter.Label(padx=1000,pady=12,bg="black")
blackbar.place(x=0,y=0)
highscoreFrame = tkinter.Label(textvariable=HSValue, bg="black",fg="white",font=("Comic Sans MS", 14))
highscoreFrame.place(x= 10, y=10)
currentScoreVar = tkinter.StringVar(value=f"Current Score: {currentScore}")
currentScoreFrame = tkinter.Label(textvariable=currentScoreVar,bg="black",fg="white",font=("Comic Sans MS", 14))
currentScoreFrame.place(y=10,x=150)
threading.Timer(1.0, movePicker).start()
threading.Timer(1.0, timerOfGame).start()
window.mainloop()


