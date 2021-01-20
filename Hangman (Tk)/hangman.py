#THIS PROGRAM WILL BE HANGMAN
from tkinter import *
import time
import os
ALPHABET = "abcdefghijklmnopqrstuvwxyz"
guesses = 6
displayWord=""
ogWord=""

#RESTARTS PROGRAM
def playAgain(*startOverB):
    os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)

#EXITS PROGRAM
def exitpls(*exitB):
    root.destroy()

#STARTS GAME AFTER USER ENTERS WORD
def startGame(*args):
    #MAKE VARIABLES GLOBAL
    global root
    global pictureLabel
    global enterWordLabel
    global wordEntry
    global wordEntered
    global guesses
    global displayWord
    global submitWord
    global ogWord
    
    #GET WORD THAT WAS INPUTTED
    wordEntered = wordEntry.get()
    wordEntered = wordEntered.lower()

    #GET A COPY OF THE OG WORD
    ogWord = wordEntered
    
    #CREATE BLANKS FOR LABEL
    for char in wordEntered:
        if char in ALPHABET:
            wordEntered = wordEntered.replace(char, ("*"))
    print(wordEntered)
    
    #DESTROY LABEL, ENTRY, AND BUTTON
    enterWordLabel.destroy()
    wordEntry.destroy()
    submitWord.destroy()

    # !CREATE REST OF GAME!
    
    #DISPLAY FIRST PHOTO
    pictureLabel = Label(frame, image=photo, relief=SUNKEN, bg="white")
    pictureLabel.grid(row=1, sticky=N, columnspan=13, pady=25)

    #LABEL TO DISPLAY WORD
    displayWord = Label(frame, text=wordEntered, width=(len(wordEntered)+2), font="none 30 bold", bg="white", relief=SUNKEN)
    displayWord.grid(row=2, sticky=N, columnspan=13)

    #BUTTONS FOR GUESSING
    global aB
    aB = Button(frame, bg="white", text="A", width=2, command=aaa, font="none 20 bold")
    aB.grid(row=3, column=1, sticky=N, padx=5, pady=10)
    root.bind("<a>", aaa)
    
    global bB
    bB = Button(frame, bg="white", text="B", width=2, command=bbb, font="none 20 bold")
    bB.grid(row=3, column=2, sticky=N, padx=5, pady=10)
    root.bind("<b>", bbb)
    
    global cB
    cB = Button(frame, bg="white", text="C", width=2, command=ccc, font="none 20 bold")
    cB.grid(row=3, column=3, sticky=N, padx=5, pady=10)
    root.bind("<c>", ccc)
    
    global dB
    dB = Button(frame, bg="white", text="D", width=2, command=ddd, font="none 20 bold")
    dB.grid(row=3, column=4, sticky=N, padx=5, pady=10)
    root.bind("<d>", ddd)
    
    global eB
    eB = Button(frame, bg="white", text="E", width=2, command=eee, font="none 20 bold")
    eB.grid(row=3, column=5, sticky=N, padx=5, pady=10)
    root.bind("<e>", eee)
    
    global fB
    fB = Button(frame, bg="white", text="F", width=2, command=fff, font="none 20 bold")
    fB.grid(row=3, column=6, sticky=N, padx=5, pady=10)
    root.bind("<f>", fff)
    
    global gB
    gB = Button(frame, bg="white", text="G", width=2, command=ggg, font="none 20 bold")
    gB.grid(row=3, column=7, sticky=N, padx=5, pady=10)
    root.bind("<g>", ggg)
    
    global hB
    hB = Button(frame, bg="white", text="H", width=2, command=hhh, font="none 20 bold")
    hB.grid(row=3, column=8, sticky=N, padx=5, pady=10)
    root.bind("<h>", hhh)
    
    global iB
    iB = Button(frame, bg="white", text="I", width=2, command=iii, font="none 20 bold")
    iB.grid(row=3, column=9, sticky=N, padx=5, pady=10)
    root.bind("<i>", iii)
    
    global jB
    jB = Button(frame, bg="white", text="J", width=2, command=jjj, font="none 20 bold")
    jB.grid(row=3, column=10, sticky=N, padx=5, pady=10)
    root.bind("<j>", jjj)
    
    global kB
    kB = Button(frame, bg="white", text="K", width=2, command=kkk, font="none 20 bold")
    kB.grid(row=3, column=11, sticky=N, padx=5, pady=10)
    root.bind("<k>", kkk)
    
    global lB
    lB = Button(frame, bg="white", text="L", width=2, command=lll, font="none 20 bold")
    lB.grid(row=3, column=12, sticky=N, padx=5, pady=10)
    root.bind("<l>", lll)
    
    global mB
    mB = Button(frame, bg="white", text="M", width=2, command=mmm, font="none 20 bold")
    mB.grid(row=3, column=13, sticky=N, padx=5, pady=10)
    root.bind("<m>", mmm)
    
    global nB
    nB = Button(frame, bg="white", text="N", width=2, command=nnn, font="none 20 bold")
    nB.grid(row=4, column=1, sticky=N, padx=5, pady=10)
    root.bind("<n>", nnn)
    
    global oB
    oB = Button(frame, bg="white", text="O", width=2, command=ooo, font="none 20 bold")
    oB.grid(row=4, column=2, sticky=N, padx=5, pady=10)
    root.bind("<o>", ooo)
    
    global pB
    pB = Button(frame, bg="white", text="P", width=2, command=ppp, font="none 20 bold")
    pB.grid(row=4, column=3, sticky=N, padx=5, pady=10)
    root.bind("<p>", ppp)
    
    global qB
    qB = Button(frame, bg="white", text="Q", width=2, command=qqq, font="none 20 bold")
    qB.grid(row=4, column=4, sticky=N, padx=5, pady=10)
    root.bind("<q>", qqq)
    
    global rB
    rB = Button(frame, bg="white", text="R", width=2, command=rrr, font="none 20 bold")
    rB.grid(row=4, column=5, sticky=N, padx=5, pady=10)
    root.bind("<r>", rrr)
    
    global sB
    sB = Button(frame, bg="white", text="S", width=2, command=sss, font="none 20 bold")
    sB.grid(row=4, column=6, sticky=N, padx=5, pady=10)
    root.bind("<s>", sss)
    
    global tB
    tB = Button(frame, bg="white", text="T", width=2, command=ttt, font="none 20 bold")
    tB.grid(row=4, column=7, sticky=N, padx=5, pady=10)
    root.bind("<t>", ttt)
    
    global uB
    uB = Button(frame, bg="white", text="U", width=2, command=uuu, font="none 20 bold")
    uB.grid(row=4, column=8, sticky=N, padx=5, pady=10)
    root.bind("<u>", uuu)
    
    global vB
    vB = Button(frame, bg="white", text="V", width=2, command=vvv, font="none 20 bold")
    vB.grid(row=4, column=9, sticky=N, padx=5, pady=10)
    root.bind("<v>", vvv)
    
    global wB
    wB = Button(frame, bg="white", text="W", width=2, command=www, font="none 20 bold")
    wB.grid(row=4, column=10, sticky=N, padx=5, pady=10)
    root.bind("<w>", www)
    
    global xB
    xB = Button(frame, bg="white", text="X", width=2, command=xxx, font="none 20 bold")
    xB.grid(row=4, column=11, sticky=N, padx=5, pady=10)
    root.bind("<x>", xxx)
    
    global yB
    yB = Button(frame, bg="white", text="Y", width=2, command=yyy, font="none 20 bold")
    yB.grid(row=4, column=12, sticky=N, padx=5, pady=10)
    root.bind("<y>", yyy)
    
    global zB
    zB = Button(frame, bg="white", text="Z", width=2, command=zzz, font="none 20 bold")
    zB.grid(row=4, column=13, sticky=N, padx=5, pady=10)
    root.bind("<z>", zzz)

    root.bind("<Escape>", exitpls)

#FUNCTION FOR WHEN USER WINS OR LOSES
def endGame(winOrLose):
    global displayWord
    aB.grid_forget()
    bB.grid_forget()
    cB.grid_forget()
    dB.grid_forget()
    eB.grid_forget()
    fB.grid_forget()
    gB.grid_forget()
    hB.grid_forget()
    iB.grid_forget()
    jB.grid_forget()
    kB.grid_forget()
    lB.grid_forget()
    mB.grid_forget()
    nB.grid_forget()
    oB.grid_forget()
    pB.grid_forget()
    qB.grid_forget()
    rB.grid_forget()
    sB.grid_forget()
    tB.grid_forget()
    uB.grid_forget()
    vB.grid_forget()
    wB.grid_forget()
    xB.grid_forget()
    yB.grid_forget()
    zB.grid_forget()
	#START OVER BUTTON
    startOverB = Button(frame, text="PLAY AGAIN", width=28, command=playAgain, font="none 20 bold", bg="black", fg="white")
    startOverB.grid(row=3, column=0, sticky=N, columnspan=13, pady=10)
    root.bind("<space>", playAgain)
	#EXIT BUTTON
    exitB = Button(frame, text="EXIT", width=28, command=exitpls, font="none 20 bold", bg="red", fg="white")
    exitB.grid(row=4, column=0, sticky=N, columnspan=13, pady=10)
    if winOrLose == "Loss":
        displayWord.config(fg="red", text=ogWord, bg="white", relief=SUNKEN)
    elif winOrLose == "Win":
        displayWord.config(fg="lime", text=ogWord, bg="white", relief=SUNKEN)

#FUNCTIONS TO GO WITH KEYBOARD BUTTONS
def aaa(*a):
    global guesses
    global photo
    global photoNum
    global ogWord
    global wordEntered
    global displayWord
    global aB
    acc = 0
    if "a" not in ogWord: #IF THE USER GUESSES AN INCORRECT LETTER
        photoNum = photoNum + 1
        photo = PhotoImage(file=('hang' + str(photoNum) + '.png'))
        guesses = guesses - 1
        pictureLabel = Label(frame, image=photo, relief=SUNKEN, bg="white")
        pictureLabel.grid(row=1, sticky=N, columnspan=13, pady=25)
        aB.config(bg="red", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if guesses == 0: #IF THE USER GUESSES AN INCORRECT LETTER, AND LOSES
        endGame("Loss")
    elif "a" in ogWord: #IF THE USER GUESSES CORRECTLY
        convertList = list(wordEntered)
        while acc != len(ogWord):
            if ogWord[acc] == "a":
                convertList[acc] = "a"
                acc += 1
            else:
                acc += 1
        wordEntered = "".join(convertList)
        displayWord = Label(frame, text=wordEntered, width=(len(wordEntered)+2), font="none 30 bold", bg="white", relief=SUNKEN)
        displayWord.grid(row=2, sticky=N, columnspan=13)
        aB.config(bg="lime", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if "*" not in wordEntered: #IF THE USER GUESSES CORRECTLY AND WINS
        endGame("Win")
    root.unbind("<a>", aaa)


def bbb(*b):
    global guesses
    global photo
    global photoNum
    global ogWord
    global wordEntered
    global displayWord
    global bB
    convertList = list()
    acc = 0
    if "b" not in ogWord and guesses != 0:
        photoNum = photoNum + 1
        photo = PhotoImage(file=('hang' + str(photoNum) + '.png'))
        guesses = guesses - 1
        pictureLabel = Label(frame, image=photo, relief=SUNKEN, bg="white")
        pictureLabel.grid(row=1, sticky=N, columnspan=13, pady=25)
        bB.config(bg="red", state=DISABLED, disabledforeground="white")
    if guesses == 0:
        endGame("Loss")
    elif "b" in ogWord and guesses != 0:
        convertList = list(wordEntered)
        while acc != len(ogWord):
            if ogWord[acc] == "b":
                convertList[acc] = "b"
                acc += 1
            else:
                acc += 1
        wordEntered = "".join(convertList)
        displayWord = Label(frame, text=wordEntered, width=(len(wordEntered)+2), font="none 30 bold", bg="white", relief=SUNKEN)
        displayWord.grid(row=2, sticky=N, columnspan=13)
        bB.config(bg="lime", state=DISABLED, disabledforeground="white")
    if "*" not in wordEntered:
        endGame("Win")
    root.unbind("<b>", bbb)


def ccc(*c):
    global guesses
    global photo
    global photoNum
    global ogWord
    global wordEntered
    global displayWord
    global cB
    convertList = list()
    acc = 0
    if "c" not in ogWord and guesses != 0:
        photoNum = photoNum + 1
        photo = PhotoImage(file=('hang' + str(photoNum) + '.png'))
        guesses = guesses - 1
        pictureLabel = Label(frame, image=photo, relief=SUNKEN, bg="white")
        pictureLabel.grid(row=1, sticky=N, columnspan=13, pady=25)
        cB.config(bg="red", state=DISABLED, disabledforeground="white")
    if guesses == 0:
        endGame("Loss")
    elif "c" in ogWord and guesses != 0:
        convertList = list(wordEntered)
        while acc != len(ogWord):
            if ogWord[acc] == "c":
                convertList[acc] = "c"
                acc += 1
            else:
                acc += 1
        wordEntered = "".join(convertList)
        displayWord = Label(frame, text=wordEntered, width=(len(wordEntered)+2), font="none 30 bold", bg="white", relief=SUNKEN)
        displayWord.grid(row=2, sticky=N, columnspan=13)
        cB.config(bg="lime", state=DISABLED, disabledforeground="white")
    if "*" not in wordEntered:
        endGame("Win")
    root.unbind("<c>", ccc)

def ddd(*d):
    global guesses
    global photo
    global photoNum
    global ogWord
    global wordEntered
    global displayWord
    global dB
    convertList = list()
    acc = 0
    if "d" not in ogWord and guesses != 0:
        photoNum = photoNum + 1
        photo = PhotoImage(file=('hang' + str(photoNum) + '.png'))
        guesses = guesses - 1
        pictureLabel = Label(frame, image=photo, relief=SUNKEN, bg="white")
        pictureLabel.grid(row=1, sticky=N, columnspan=13, pady=25)
        dB.config(bg="red", state=DISABLED, disabledforeground="white")
    if guesses == 0:
        endGame("Loss")
    elif "d" in ogWord and guesses != 0:
        convertList = list(wordEntered)
        while acc != len(ogWord):
            if ogWord[acc] == "d":
                convertList[acc] = "d"
                acc += 1
            else:
                acc += 1
        wordEntered = "".join(convertList)
        displayWord = Label(frame, text=wordEntered, width=(len(wordEntered)+2), font="none 30 bold", bg="white", relief=SUNKEN)
        displayWord.grid(row=2, sticky=N, columnspan=13)
        dB.config(bg="lime", state=DISABLED, disabledforeground="white")
    if "*" not in wordEntered:
        endGame("Win")
    root.unbind("<d>", ddd)

def eee(*e):
    global guesses
    global photo
    global photoNum
    global ogWord
    global wordEntered
    global displayWord
    global eB
    convertList = list()
    acc = 0
    if "e" not in ogWord and guesses != 0:
        photoNum = photoNum + 1
        photo = PhotoImage(file=('hang' + str(photoNum) + '.png'))
        guesses = guesses - 1
        pictureLabel = Label(frame, image=photo, relief=SUNKEN, bg="white")
        pictureLabel.grid(row=1, sticky=N, columnspan=13, pady=25)
        eB.config(bg="red", state=DISABLED, disabledforeground="white")
    if guesses == 0:
        endGame("Loss")
    elif "e" in ogWord and guesses != 0:
        convertList = list(wordEntered)
        while acc != len(ogWord):
            if ogWord[acc] == "e":
                convertList[acc] = "e"
                acc += 1
            else:
                acc += 1
        wordEntered = "".join(convertList)
        displayWord = Label(frame, text=wordEntered, width=(len(wordEntered)+2), font="none 30 bold", bg="white", relief=SUNKEN)
        displayWord.grid(row=2, sticky=N, columnspan=13)
        eB.config(bg="lime", state=DISABLED, disabledforeground="white")
    if "*" not in wordEntered:
        endGame("Win")
    root.unbind("<e>", eee)


def fff(*f):
    global guesses
    global photo
    global photoNum
    global ogWord
    global wordEntered
    global displayWord
    global fB
    convertList = list()
    acc = 0
    if "f" not in ogWord and guesses != 0:
        photoNum = photoNum + 1
        photo = PhotoImage(file=('hang' + str(photoNum) + '.png'))
        guesses = guesses - 1
        pictureLabel = Label(frame, image=photo, relief=SUNKEN, bg="white")
        pictureLabel.grid(row=1, sticky=N, columnspan=13, pady=25)
        fB.config(bg="red", state=DISABLED, disabledforeground="white")
    if guesses == 0:
        endGame("Loss")
    elif "f" in ogWord and guesses != 0:
        convertList = list(wordEntered)
        while acc != len(ogWord):
            if ogWord[acc] == "f":
                convertList[acc] = "f"
                acc += 1
            else:
                acc += 1
        wordEntered = "".join(convertList)
        displayWord = Label(frame, text=wordEntered, width=(len(wordEntered)+2), font="none 30 bold", bg="white", relief=SUNKEN)
        displayWord.grid(row=2, sticky=N, columnspan=13)
        fB.config(bg="lime", state=DISABLED, disabledforeground="white")
    if "*" not in wordEntered:
        endGame("Win")
    root.unbind("<f>", fff)


def ggg(*g):
    global guesses
    global photo
    global photoNum
    global ogWord
    global wordEntered
    global displayWord
    global gB
    convertList = list()
    acc = 0
    if "g" not in ogWord and guesses != 0:
        photoNum = photoNum + 1
        photo = PhotoImage(file=('hang' + str(photoNum) + '.png'))
        guesses = guesses - 1
        pictureLabel = Label(frame, image=photo, relief=SUNKEN, bg="white")
        pictureLabel.grid(row=1, sticky=N, columnspan=13, pady=25)
        gB.config(bg="red", state=DISABLED, disabledforeground="white")
    if guesses == 0:
        endGame("Loss")
    elif "g" in ogWord and guesses != 0:
        convertList = list(wordEntered)
        while acc != len(ogWord):
            if ogWord[acc] == "g":
                convertList[acc] = "g"
                acc += 1
            else:
                acc += 1
        wordEntered = "".join(convertList)
        displayWord = Label(frame, text=wordEntered, width=(len(wordEntered)+2), font="none 30 bold", bg="white", relief=SUNKEN)
        displayWord.grid(row=2, sticky=N, columnspan=13)
        gB.config(bg="lime", state=DISABLED, disabledforeground="white")
    if "*" not in wordEntered:
        endGame("Win")
    root.unbind("<g>", ggg)


def hhh(*h):
    global guesses
    global photo
    global photoNum
    global ogWord
    global wordEntered
    global displayWord
    global hB
    convertList = list()
    acc = 0
    if "h" not in ogWord and guesses != 0:
        photoNum = photoNum + 1
        photo = PhotoImage(file=('hang' + str(photoNum) + '.png'))
        guesses = guesses - 1
        pictureLabel = Label(frame, image=photo, relief=SUNKEN, bg="white")
        pictureLabel.grid(row=1, sticky=N, columnspan=13, pady=25)
        hB.config(bg="red", state=DISABLED, disabledforeground="white")
    if guesses == 0:
        endGame("Loss")
    elif "h" in ogWord and guesses != 0:
        convertList = list(wordEntered)
        while acc != len(ogWord):
            if ogWord[acc] == "h":
                convertList[acc] = "h"
                acc += 1
            else:
                acc += 1
        wordEntered = "".join(convertList)
        displayWord = Label(frame, text=wordEntered, width=(len(wordEntered)+2), font="none 30 bold", bg="white", relief=SUNKEN)
        displayWord.grid(row=2, sticky=N, columnspan=13)
        hB.config(bg="lime", state=DISABLED, disabledforeground="white")
    if "*" not in wordEntered:
        endGame("Win")
    root.unbind("<h>", hhh)


def iii(*i):
    global guesses
    global photo
    global photoNum
    global ogWord
    global wordEntered
    global displayWord
    global iB
    convertList = list()
    acc = 0
    if "i" not in ogWord and guesses != 0:
        photoNum = photoNum + 1
        photo = PhotoImage(file=('hang' + str(photoNum) + '.png'))
        guesses = guesses - 1
        pictureLabel = Label(frame, image=photo, relief=SUNKEN, bg="white")
        pictureLabel.grid(row=1, sticky=N, columnspan=13, pady=25)
        iB.config(bg="red", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if guesses == 0:
            endGame("Loss")
    elif "i" in ogWord and guesses != 0:
        convertList = list(wordEntered)
        while acc != len(ogWord):
            if ogWord[acc] == "i":
                convertList[acc] = "i"
                acc += 1
            else:
                acc += 1
        wordEntered = "".join(convertList)
        displayWord = Label(frame, text=wordEntered, width=(len(wordEntered)+2), font="none 30 bold", bg="white", relief=SUNKEN)
        displayWord.grid(row=2, sticky=N, columnspan=13)
        iB.config(bg="lime", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if "*" not in wordEntered:
            endGame("Win")
    root.unbind("<i>", iii)


def jjj(*j):
    global guesses
    global photo
    global photoNum
    global ogWord
    global wordEntered
    global displayWord
    global jB
    convertList = list()
    acc = 0
    if "j" not in ogWord and guesses != 0:
        photoNum = photoNum + 1
        photo = PhotoImage(file=('hang' + str(photoNum) + '.png'))
        guesses = guesses - 1
        pictureLabel = Label(frame, image=photo, relief=SUNKEN, bg="white")
        pictureLabel.grid(row=1, sticky=N, columnspan=13, pady=25)
        jB.config(bg="red", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if guesses == 0:
            endGame("Loss")
    elif "j" in ogWord and guesses != 0:
        convertList = list(wordEntered)
        while acc != len(ogWord):
            if ogWord[acc] == "j":
                convertList[acc] = "j"
                acc += 1
            else:
                acc += 1
        wordEntered = "".join(convertList)
        displayWord = Label(frame, text=wordEntered, width=(len(wordEntered)+2), font="none 30 bold", bg="white", relief=SUNKEN)
        displayWord.grid(row=2, sticky=N, columnspan=13)
        jB.config(bg="lime", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if "*" not in wordEntered:
            endGame("Win")
    root.unbind("<j>", jjj)


def kkk(*k):
    global guesses
    global photo
    global photoNum
    global ogWord
    global wordEntered
    global displayWord
    global kB
    convertList = list()
    acc = 0
    if "k" not in ogWord and guesses != 0:
        photoNum = photoNum + 1
        photo = PhotoImage(file=('hang' + str(photoNum) + '.png'))
        guesses = guesses - 1
        pictureLabel = Label(frame, image=photo, relief=SUNKEN, bg="white")
        pictureLabel.grid(row=1, sticky=N, columnspan=13, pady=25)
        kB.config(bg="red", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if guesses == 0:
            endGame("Loss")
    elif "k" in ogWord and guesses != 0:
        convertList = list(wordEntered)
        while acc != len(ogWord):
            if ogWord[acc] == "k":
                convertList[acc] = "k"
                acc += 1
            else:
                acc += 1
        wordEntered = "".join(convertList)
        displayWord = Label(frame, text=wordEntered, width=(len(wordEntered)+2), font="none 30 bold", bg="white", relief=SUNKEN)
        displayWord.grid(row=2, sticky=N, columnspan=13)
        kB.config(bg="lime", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if "*" not in wordEntered:
            endGame("Win")
    root.unbind("<k>", kkk)


def lll(*l):
    global guesses
    global photo
    global photoNum
    global ogWord
    global wordEntered
    global displayWord
    global lB
    convertList = list()
    acc = 0
    if "l" not in ogWord and guesses != 0:
        photoNum = photoNum + 1
        photo = PhotoImage(file=('hang' + str(photoNum) + '.png'))
        guesses = guesses - 1
        pictureLabel = Label(frame, image=photo, relief=SUNKEN, bg="white")
        pictureLabel.grid(row=1, sticky=N, columnspan=13, pady=25)
        lB.config(bg="red", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if guesses == 0:
            endGame("Loss")
    elif "l" in ogWord and guesses != 0:
        convertList = list(wordEntered)
        while acc != len(ogWord):
            if ogWord[acc] == "l":
                convertList[acc] = "l"
                acc += 1
            else:
                acc += 1
        wordEntered = "".join(convertList)
        displayWord = Label(frame, text=wordEntered, width=(len(wordEntered)+2), font="none 30 bold", bg="white", relief=SUNKEN)
        displayWord.grid(row=2, sticky=N, columnspan=13)
        lB.config(bg="lime", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if "*" not in wordEntered:
            endGame("Win")
    root.unbind("<l>", lll)


def mmm(*m):
    global guesses
    global photo
    global photoNum
    global ogWord
    global wordEntered
    global displayWord
    global mB
    convertList = list()
    acc = 0
    if "m" not in ogWord and guesses != 0:
        photoNum = photoNum + 1
        photo = PhotoImage(file=('hang' + str(photoNum) + '.png'))
        guesses = guesses - 1
        pictureLabel = Label(frame, image=photo, relief=SUNKEN, bg="white")
        pictureLabel.grid(row=1, sticky=N, columnspan=13, pady=25)
        mB.config(bg="red", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if guesses == 0:
            endGame("Loss")
    elif "m" in ogWord and guesses != 0:
        convertList = list(wordEntered)
        while acc != len(ogWord):
            if ogWord[acc] == "m":
                convertList[acc] = "m"
                acc += 1
            else:
                acc += 1
        wordEntered = "".join(convertList)
        displayWord = Label(frame, text=wordEntered, width=(len(wordEntered)+2), font="none 30 bold", bg="white", relief=SUNKEN)
        displayWord.grid(row=2, sticky=N, columnspan=13)
        mB.config(bg="lime", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if "*" not in wordEntered:
            endGame("Win")
    root.unbind("<m>", mmm)


def nnn(*n):
    global guesses
    global photo
    global photoNum
    global ogWord
    global wordEntered
    global displayWord
    global nB
    convertList = list()
    acc = 0
    if "n" not in ogWord and guesses != 0:
        photoNum = photoNum + 1
        photo = PhotoImage(file=('hang' + str(photoNum) + '.png'))
        guesses = guesses - 1
        pictureLabel = Label(frame, image=photo, relief=SUNKEN, bg="white")
        pictureLabel.grid(row=1, sticky=N, columnspan=13, pady=25)
        nB.config(bg="red", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if guesses == 0:
            endGame("Loss")
    elif "n" in ogWord and guesses != 0:
        convertList = list(wordEntered)
        while acc != len(ogWord):
            if ogWord[acc] == "n":
                convertList[acc] = "n"
                acc += 1
            else:
                acc += 1
        wordEntered = "".join(convertList)
        displayWord = Label(frame, text=wordEntered, width=(len(wordEntered)+2), font="none 30 bold", bg="white", relief=SUNKEN)
        displayWord.grid(row=2, sticky=N, columnspan=13)
        nB.config(bg="lime", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if "*" not in wordEntered:
            endGame("Win")
    root.unbind("<n>", nnn)


def ooo(*o):
    global guesses
    global photo
    global photoNum
    global ogWord
    global wordEntered
    global displayWord
    global oB
    convertList = list()
    acc = 0
    if "o" not in ogWord and guesses != 0:
        photoNum = photoNum + 1
        photo = PhotoImage(file=('hang' + str(photoNum) + '.png'))
        guesses = guesses - 1
        pictureLabel = Label(frame, image=photo, relief=SUNKEN, bg="white")
        pictureLabel.grid(row=1, sticky=N, columnspan=13, pady=25)
        oB.config(bg="red", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if guesses == 0:
            endGame("Loss")
    elif "o" in ogWord and guesses != 0:
        convertList = list(wordEntered)
        while acc != len(ogWord):
            if ogWord[acc] == "o":
                convertList[acc] = "o"
                acc += 1
            else:
                acc += 1
        wordEntered = "".join(convertList)
        displayWord = Label(frame, text=wordEntered, width=(len(wordEntered)+2), font="none 30 bold", bg="white", relief=SUNKEN)
        displayWord.grid(row=2, sticky=N, columnspan=13)
        oB.config(bg="lime", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if "*" not in wordEntered:
            endGame("Win")
    root.unbind("<o>", ooo)


def ppp(*p):
    global guesses
    global photo
    global photoNum
    global ogWord
    global wordEntered
    global displayWord
    global pB
    convertList = list()
    acc = 0
    if "p" not in ogWord and guesses != 0:
        photoNum = photoNum + 1
        photo = PhotoImage(file=('hang' + str(photoNum) + '.png'))
        guesses = guesses - 1
        pictureLabel = Label(frame, image=photo, relief=SUNKEN, bg="white")
        pictureLabel.grid(row=1, sticky=N, columnspan=13, pady=25)
        pB.config(bg="red", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if guesses == 0:
            endGame("Loss")
    elif "p" in ogWord and guesses != 0:
        convertList = list(wordEntered)
        while acc != len(ogWord):
            if ogWord[acc] == "p":
                convertList[acc] = "p"
                acc += 1
            else:
                acc += 1
        wordEntered = "".join(convertList)
        displayWord = Label(frame, text=wordEntered, width=(len(wordEntered)+2), font="none 30 bold", bg="white", relief=SUNKEN)
        displayWord.grid(row=2, sticky=N, columnspan=13)
        pB.config(bg="lime", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if "*" not in wordEntered:
            endGame("Win")
    root.unbind("<p>", ppp)


def qqq(*q):
    global guesses
    global photo
    global photoNum
    global ogWord
    global wordEntered
    global displayWord
    global qB
    convertList = list()
    acc = 0
    if "q" not in ogWord and guesses != 0:
        photoNum = photoNum + 1
        photo = PhotoImage(file=('hang' + str(photoNum) + '.png'))
        guesses = guesses - 1
        pictureLabel = Label(frame, image=photo, relief=SUNKEN, bg="white")
        pictureLabel.grid(row=1, sticky=N, columnspan=13, pady=25)
        qB.config(bg="red", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if guesses == 0:
            endGame("Loss")
    elif "q" in ogWord and guesses != 0:
        convertList = list(wordEntered)
        while acc != len(ogWord):
            if ogWord[acc] == "q":
                convertList[acc] = "q"
                acc += 1
            else:
                acc += 1
        wordEntered = "".join(convertList)
        displayWord = Label(frame, text=wordEntered, width=(len(wordEntered)+2), font="none 30 bold", bg="white", relief=SUNKEN)
        displayWord.grid(row=2, sticky=N, columnspan=13)
        qB.config(bg="lime", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if "*" not in wordEntered:
            endGame("Win")
    root.unbind("<q>", qqq)


def rrr(*r):
    global guesses
    global photo
    global photoNum
    global ogWord
    global wordEntered
    global displayWord
    global rB
    convertList = list()
    acc = 0
    if "r" not in ogWord and guesses != 0:
        photoNum = photoNum + 1
        photo = PhotoImage(file=('hang' + str(photoNum) + '.png'))
        guesses = guesses - 1
        pictureLabel = Label(frame, image=photo, relief=SUNKEN, bg="white")
        pictureLabel.grid(row=1, sticky=N, columnspan=13, pady=25)
        rB.config(bg="red", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if guesses == 0:
            endGame("Loss")
    elif "r" in ogWord and guesses != 0:
        convertList = list(wordEntered)
        while acc != len(ogWord):
            if ogWord[acc] == "r":
                convertList[acc] = "r"
                acc += 1
            else:
                acc += 1
        wordEntered = "".join(convertList)
        displayWord = Label(frame, text=wordEntered, width=(len(wordEntered)+2), font="none 30 bold", bg="white", relief=SUNKEN)
        displayWord.grid(row=2, sticky=N, columnspan=13)
        rB.config(bg="lime", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if "*" not in wordEntered:
            endGame("Win")
    root.unbind("<r>", rrr)


def sss(*s):
    global guesses
    global photo
    global photoNum
    global ogWord
    global wordEntered
    global displayWord
    global sB
    convertList = list()
    acc = 0
    if "s" not in ogWord and guesses != 0:
        photoNum = photoNum + 1
        photo = PhotoImage(file=('hang' + str(photoNum) + '.png'))
        guesses = guesses - 1
        pictureLabel = Label(frame, image=photo, relief=SUNKEN, bg="white")
        pictureLabel.grid(row=1, sticky=N, columnspan=13, pady=25)
        sB.config(bg="red", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if guesses == 0:
            endGame("Loss")
    elif "s" in ogWord and guesses != 0:
        convertList = list(wordEntered)
        while acc != len(ogWord):
            if ogWord[acc] == "s":
                convertList[acc] = "s"
                acc += 1
            else:
                acc += 1
        wordEntered = "".join(convertList)
        displayWord = Label(frame, text=wordEntered, width=(len(wordEntered)+2), font="none 30 bold", bg="white", relief=SUNKEN)
        displayWord.grid(row=2, sticky=N, columnspan=13)
        sB.config(bg="lime", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if "*" not in wordEntered:
            endGame("Win")
    root.unbind("<s>", sss)


def ttt(*t):
    global guesses
    global photo
    global photoNum
    global ogWord
    global wordEntered
    global displayWord
    global tB
    convertList = list()
    acc = 0
    if "t" not in ogWord and guesses != 0:
        photoNum = photoNum + 1
        photo = PhotoImage(file=('hang' + str(photoNum) + '.png'))
        guesses = guesses - 1
        pictureLabel = Label(frame, image=photo, relief=SUNKEN, bg="white")
        pictureLabel.grid(row=1, sticky=N, columnspan=13, pady=25)
        tB.config(bg="red", state=DISABLED, disabledforeground="white", font="none 20 bold")
        if guesses == 0:
            endGame("Loss")
    elif "t" in ogWord and guesses != 0:
        convertList = list(wordEntered)
        while acc != len(ogWord):
            if ogWord[acc] == "t":
                convertList[acc] = "t"
                acc += 1
            else:
                acc += 1
        wordEntered = "".join(convertList)
        displayWord = Label(frame, text=wordEntered, width=(len(wordEntered)+2), font="none 30 bold", bg="white", relief=SUNKEN)
        displayWord.grid(row=2, sticky=N, columnspan=13)
        tB.config(bg="lime", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if "*" not in wordEntered:
            endGame("Win")
    root.unbind("<t>", ttt)


def uuu(*u):
    global guesses
    global photo
    global photoNum
    global ogWord
    global wordEntered
    global displayWord
    global uB
    convertList = list()
    acc = 0
    if "u" not in ogWord and guesses != 0:
        photoNum = photoNum + 1
        photo = PhotoImage(file=('hang' + str(photoNum) + '.png'))
        guesses = guesses - 1
        pictureLabel = Label(frame, image=photo, relief=SUNKEN, bg="white")
        pictureLabel.grid(row=1, sticky=N, columnspan=13, pady=25)
        uB.config(bg="red", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if guesses == 0:
            endGame("Loss")
    elif "u" in ogWord and guesses != 0:
        convertList = list(wordEntered)
        while acc != len(ogWord):
            if ogWord[acc] == "u":
                convertList[acc] = "u"
                acc += 1
            else:
                acc += 1
        wordEntered = "".join(convertList)
        displayWord = Label(frame, text=wordEntered, width=(len(wordEntered)+2), font="none 30 bold", bg="white", relief=SUNKEN)
        displayWord.grid(row=2, sticky=N, columnspan=13)
        uB.config(bg="lime", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if "*" not in wordEntered:
            endGame("Win")
    root.unbind("<u>", uuu)


def vvv(*v):
    global guesses
    global photo
    global photoNum
    global ogWord
    global wordEntered
    global displayWord
    global vB
    convertList = list()
    acc = 0
    if "v" not in ogWord and guesses != 0:
        photoNum = photoNum + 1
        photo = PhotoImage(file=('hang' + str(photoNum) + '.png'))
        guesses = guesses - 1
        pictureLabel = Label(frame, image=photo, relief=SUNKEN, bg="white")
        pictureLabel.grid(row=1, sticky=N, columnspan=13, pady=25)
        vB.config(bg="red", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if guesses == 0:
            endGame("Loss")
    elif "v" in ogWord and guesses != 0:
        convertList = list(wordEntered)
        while acc != len(ogWord):
            if ogWord[acc] == "v":
                convertList[acc] = "v"
                acc += 1
            else:
                acc += 1
        wordEntered = "".join(convertList)
        displayWord = Label(frame, text=wordEntered, width=(len(wordEntered)+2), font="none 30 bold", bg="white", relief=SUNKEN)
        displayWord.grid(row=2, sticky=N, columnspan=13)
        vB.config(bg="lime", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if "*" not in wordEntered:
            endGame("Win")
    root.unbind("<v>", vvv)


def www(*w):
    global guesses
    global photo
    global photoNum
    global ogWord
    global wordEntered
    global displayWord
    global wB
    convertList = list()
    acc = 0
    if "w" not in ogWord and guesses != 0:
        photoNum = photoNum + 1
        photo = PhotoImage(file=('hang' + str(photoNum) + '.png'))
        guesses = guesses - 1
        pictureLabel = Label(frame, image=photo, relief=SUNKEN, bg="white")
        pictureLabel.grid(row=1, sticky=N, columnspan=13, pady=25)
        wB.config(bg="red", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if guesses == 0:
            endGame("Loss")
    elif "w" in ogWord and guesses != 0:
        convertList = list(wordEntered)
        while acc != len(ogWord):
            if ogWord[acc] == "w":
                convertList[acc] = "w"
                acc += 1
            else:
                acc += 1
        wordEntered = "".join(convertList)
        displayWord = Label(frame, text=wordEntered, width=(len(wordEntered)+2), font="none 30 bold", bg="white", relief=SUNKEN)
        displayWord.grid(row=2, sticky=N, columnspan=13)
        wB.config(bg="lime", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if "*" not in wordEntered:
            endGame("Win")
    root.unbind("<w>", www)


def xxx(*x):
    global guesses
    global photo
    global photoNum
    global ogWord
    global wordEntered
    global displayWord
    global xB
    convertList = list()
    acc = 0
    if "x" not in ogWord and guesses != 0:
        photoNum = photoNum + 1
        photo = PhotoImage(file=('hang' + str(photoNum) + '.png'))
        guesses = guesses - 1
        pictureLabel = Label(frame, image=photo, relief=SUNKEN, bg="white")
        pictureLabel.grid(row=1, sticky=N, columnspan=13, pady=25)
        xB.config(bg="red", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if guesses == 0:
            endGame("Loss")
    elif "x" in ogWord and guesses != 0:
        convertList = list(wordEntered)
        while acc != len(ogWord):
            if ogWord[acc] == "x":
                convertList[acc] = "x"
                acc += 1
            else:
                acc += 1
        wordEntered = "".join(convertList)
        displayWord = Label(frame, text=wordEntered, width=(len(wordEntered)+2), font="none 30 bold", bg="white", relief=SUNKEN)
        displayWord.grid(row=2, sticky=N, columnspan=13)
        xB.config(bg="lime", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if "*" not in wordEntered:
            endGame("Win")
    root.unbind("<x>", xxx)

def yyy(*y):
    global guesses
    global photo
    global photoNum
    global ogWord
    global wordEntered
    global displayWord
    global yB
    convertList = list()
    acc = 0
    if "y" not in ogWord and guesses != 0:
        photoNum = photoNum + 1
        photo = PhotoImage(file=('hang' + str(photoNum) + '.png'))
        guesses = guesses - 1
        pictureLabel = Label(frame, image=photo, relief=SUNKEN, bg="white")
        pictureLabel.grid(row=1, sticky=N, columnspan=13, pady=25)
        yB.config(bg="red", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if guesses == 0:
            endGame("Loss")
    elif "y" in ogWord and guesses != 0:
        convertList = list(wordEntered)
        while acc != len(ogWord):
            if ogWord[acc] == "y":
                convertList[acc] = "y"
                acc += 1
            else:
                acc += 1
        wordEntered = "".join(convertList)
        displayWord = Label(frame, text=wordEntered, width=(len(wordEntered)+2), font="none 30 bold", bg="white", relief=SUNKEN)
        displayWord.grid(row=2, sticky=N, columnspan=13)
        yB.config(bg="lime", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if "*" not in wordEntered:
            endGame("Win")
    root.unbind("<y>", yyy)

def zzz(*z):
    global guesses
    global photo
    global photoNum
    global ogWord
    global wordEntered
    global displayWord
    global zB
    convertList = list()
    acc = 0
    if "z" not in ogWord and guesses != 0:
        photoNum = photoNum + 1
        photo = PhotoImage(file=('hang' + str(photoNum) + '.png'))
        guesses = guesses - 1
        pictureLabel = Label(frame, image=photo, relief=SUNKEN, bg="white")
        pictureLabel.grid(row=1, sticky=N, columnspan=13, pady=25)
        zB.config(bg="red", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if guesses == 0:
            endGame("loss")
    elif "z" in ogWord and guesses != 0:
        convertList = list(wordEntered)
        while acc != len(ogWord):
            if ogWord[acc] == "z":
                convertList[acc] = "z"
                acc += 1
            else:
                acc += 1
        wordEntered = "".join(convertList)
        displayWord = Label(frame, text=wordEntered, width=(len(wordEntered)+2), font="none 30 bold", bg="white", relief=SUNKEN)
        displayWord.grid(row=2, sticky=N, columnspan=13)
        zB.config(bg="lime", state=DISABLED, disabledforeground="white", font="none 20 bold")
    if "*" not in wordEntered:
            endGame("Win")
    root.unbind("<z>", zzz)

#CREATE WINDOW
root = Tk()
root.title("THE HANGMAN GAME THAT WAS PROGRAMMED BY A HEAVENLY BEING, KNOWN AS JOSEPH HASKINS")
root.config(bg="lavender")

#CREATE FRAME
frame = Frame(root, bg="lavender")
frame.pack(anchor=CENTER, side=BOTTOM, pady=15, expand=1)

#SIZE WINDOW
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
#window.overrideredirect(1) #ENABLE TO GO FULLSCREEN
root.geometry("%dx%d+0+0" % (w, h))
root.bind("<Escape>", exitpls)

#HANGMAN LABEL
hangmanImage = PhotoImage(file="hangman.png")
hangmanPicLabel = Label(root, image=hangmanImage, relief=SUNKEN, bg="white")
hangmanPicLabel.pack(side=TOP, fill=X, pady=20)

#DEFINE PHOTOS
photo = PhotoImage(file='hang0.png')
photoNum = 0

### !FIRST SCREEN!

#ENTER WORD LABEL
enterWordLabel = Label(frame, text='ENTER A WORD:', width=25, font="none 40 bold", fg="white", bg="maroon")
enterWordLabel.grid(row=2, sticky=N, pady=5)

#ENTER WORD TEXT BOX
wordEntry = Entry(frame, width=25, justify='center', font="none 40 bold")
wordEntry.grid(row=2, column=1, sticky=N, pady=5)
wordEntry.focus_set()

#SUBMIT WORD BUTTON
submitWord = Button(frame, width=50, text='S U B M I T', command=startGame, font="none 40 bold", bg="black", fg="white")
submitWord.grid(row=3, sticky=N, columnspan=2, pady=5)
root.bind("<Return>", startGame)

root.mainloop()










