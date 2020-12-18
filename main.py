# This fine italian meal was created by Josh Gordon AKA Seraph


import requests
import PySimpleGUI as catGui
import webbrowser
import os
import random


# Brain of the app


def parseServerResponse(x):  # Puts actual lines instead of one straight one
    currentLetterNumber = 0
    firstRun = True
    newResponse = ""
    while x[currentLetterNumber] is not None:
        if firstRun == False:
            newResponse += "\n"
        else:
            firstRun = True

        while currentLetterNumber < 100 and x[currentLetterNumber] is not None:
            newResponse += x[currentLetterNumber]  # Go through character by character until the line runs out
            ++currentLetterNumber


# Gets the fact about the cat
def getCatFact():
    response = requests.get("https://catfact.ninja/fact")
    print(response)

    # Sets the response variable to what I actually wanted to get: Spent 15 minutes looking for why it was printing the wrong crap
    response = (response.json()['fact'])

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


def chooseRandomPhoto():
    choice = random.choice(os.listdir("Photos"))
    print(choice)
    return choice


# -----------------------------------------------------------------------------------------------------------------

# Gui Garbage
# Elements

# Text Areas
factTextbox_element = [catGui.Text("Cat", size=(100, 5), key="factTextBox")]
factTestTextbox_element = [catGui.Text("Test Fact")]
# Buttons
catFactButton_element = [catGui.Button("Cat Fact")]
cuteCatPicButton_element = [catGui.Button("Cute Cat Pic")]
cuteCatGifButton_element = [catGui.Button("Cute Cat GIF")]
bestOfYJButton_element = [catGui.Button("Best of YJ")]
creepyPastaButton_element = [catGui.Button("Random CreepyPasta")]
# Best Of YJ element
img_element = [catGui.Image(key="YJFrame", size=(200, 200))]

# Layout of app - will rearange dynamically thanks to magic
layout = [factTextbox_element,
          factTestTextbox_element,
          catFactButton_element,
          cuteCatPicButton_element,
          cuteCatGifButton_element,
          bestOfYJButton_element,
          creepyPastaButton_element]

catGui.Column(img_element)

# Actually making the window now

window = catGui.Window("Cat in the App", layout)

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
        pic = chooseRandomPhoto()
        window["YJFrame"].update("/home/josh/Documents/personal/Cats/Photos/" + pic)

    if event == ("Random CreepyPasta"):  # Opens cat gif in browser
        webbrowser.open("https://www.creepypasta.com/random")

    if event == catGui.WIN_CLOSED:  # Stops program if user exits out
        break

window.close()
