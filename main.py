# This fine italian meal was created by Josh Gordon AKA Seraph


import requests
import PySimpleGUIQt as catGui
import webbrowser
import os
import pathlib
import random
import pyautogui as screenMeasure

# Establish Technical Variables

# Get Screen Resolution
width, height = screenMeasure.size()
# print(width, height)
width = width / 1.3
height = height / 1.6


# Brain of the app


def parseServerResponse(x):  # Puts actual line breaks instead of one long one
    currentLetterNumber = 0
    firstRun = True
    newResponse = ""
    while True:
        try:
            newResponse += x[currentLetterNumber]  # Go through character by character until the line runs out
            currentLetterNumber += 1
            if currentLetterNumber % 100 == 0:
                while x[currentLetterNumber] != " ":
                    newResponse += x[currentLetterNumber]
                    currentLetterNumber += 1
                newResponse += "\n"
                currentLetterNumber += 1
        except IndexError:
            if x[currentLetterNumber - 1] != ".":  # Adds period if one is missing, which sometimes they are
                newResponse += "."
                print("Added Period")
            print(newResponse)
            return newResponse


# Gets the fact about the cat
def getCatFact():
    response = requests.get("https://catfact.ninja/fact")
    print(response)

    # Sets the response variable to what I actually wanted to get: Spent 15 minutes looking for why it was printing the wrong crap
    response = (response.json()['fact'])
    response = parseServerResponse(response)
    return response


# Gets random cat png
def getCatImage():
    # Getting url
    initialResponse = requests.get("https://api.thecatapi.com/v1/images/search?mime_types=png",
                                   headers={"x-api-key": "27881ddf-32d9-47e1-b162-d15a3684240d"})

    # print(initialResponse.json())

    pictureUrl = (initialResponse.json()[0]['url'])
    # open picture in default browser from url

    webbrowser.open(pictureUrl)


# Opens a cat gif in the browser
def getCatGIF():
    # Getting url
    initialResponse = requests.get("https://api.thecatapi.com/v1/images/search?mime_types=gif",
                                   headers={"x-api-key": "27881ddf-32d9-47e1-b162-d15a3684240d"})

    # print(initialResponse.json())

    pictureUrl = (initialResponse.json()[0]['url'])
    # open picture in default browser from url

    webbrowser.open(pictureUrl)


# Chooses random photo from generated photoList
# No longer needed it but keeping it cause ya never know
"""
def chooseRandomPhoto():
    choice = random.choice(os.listdir("Photos"))
    print(choice)
    return choice   
"""

# -----------------------------------------------------------------------------------------------------------------


# Gui Garbage

# Theme

# Custom Theme
YaelTheme = {'BACKGROUND': '#F99FC9',
             'TEXT': 'black',
             'INPUT': '#DDE0DE',
             'SCROLL': '#E3E3E3',
             'TEXT_INPUT': 'black',
             'BUTTON': ('black', '#85c7e3'),
             'PROGRESS': 'blue',
             'BORDER': 1,
             'SLIDER_DEPTH': 0,
             'PROGRESS_DEPTH': 0}

catGui.LOOK_AND_FEEL_TABLE['YaelTheme'] = YaelTheme
catGui.theme('YaelTheme')

# Elements

# Text Areas
# print(width)
factTextbox_element = [
    catGui.Text(size_px=(width, height / 6), key="factTextBox", font=("Helvetica, 15"), justification='c')]
# Buttons
catFactButton_element = [catGui.Button("Cat Fact", size=(20, 2))]
cuteCatPicButton_element = [catGui.Button("Cute Cat Pic", size=(20, 2))]
cuteCatGifButton_element = [catGui.Button("Cute Cat GIF", size=(20, 2))]
creepyPastaButton_element = [catGui.Button("Random CreepyPasta", size=(20, 2))]

# Image element
# img_element = [catGui.Button("Best of YJ"), catGui.Image(data=None, key="YJFrame")]

imageButton_element = [catGui.Button("Best of YJ", size=(20, 2))]
imageFrame_element = [catGui.Image(key="YJFrame")]

# Column Setup

buttonCol = [catFactButton_element,
             cuteCatPicButton_element,
             cuteCatGifButton_element,
             imageButton_element,
             creepyPastaButton_element]

imgCol = [imageFrame_element]

# Layout of app - Frames and stuff
layout = [[catGui.Frame(title='Cat Facts', layout=[factTextbox_element], visible=True, element_justification='c',
                        relief='RELIEF_FLAT')],
          [catGui.Column(buttonCol), catGui.Column(imgCol)]]

# Actually making the window now

window = catGui.Window("Yael Central", layout, size=(width, height))

# Initilizations
# Theme
print(catGui.theme_list())
# Makes a Array of all the photo names and randomizes it

# Current Directory
currentDir = str(pathlib.Path(__file__).resolve().parent)
print(currentDir)
photoList = os.listdir(currentDir + "/Photos")
random.shuffle(photoList)
photoCounter = 0  # Keeps track of where the user is in the photo array

# event loop to keep the window open and allow the user to close it

while True:
    # PysimpeGui runs off events
    event, values = window.read()
    if event == ("Cat Fact"):  # If user presses the fact button
        newFact = getCatFact()
        window["factTextBox"].Update(newFact)  # Updates Text

    if event == ("Cute Cat Pic"):  # Opens cat pic in browser
        getCatImage()

    if event == ("Cute Cat GIF"):  # Opens cat gif in browser
        getCatGIF()

    if event == ("Best of YJ"):
        print(photoList, photoCounter)  # Test Prints
        try:
            pic = photoList[photoCounter]
            window["YJFrame"].update("Photos/" + pic)
            photoCounter += 1  # moves the counter to the next picture
        except IndexError:  # Catches the array when it ends and reshuffles and resets the counter
            random.shuffle(photoList)
            photoCounter = 0
            pic = photoList[photoCounter]
            window["YJFrame"].update("Photos/" + pic)
            photoCounter += 1  # moves the counter to the next picture

    if event == ("Random CreepyPasta"):  # Opens cat gif in browser
        webbrowser.open("https://www.creepypasta.com/random")

    if event == catGui.WIN_CLOSED:  # Stops program if user exits out
        break

window.close()
