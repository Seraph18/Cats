# This fine italian meal was created by Josh Gordon AKA Seraph


import requests
import PySimpleGUI as catGui
import json


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


# -----------------------------------------------------------------------------------------------------------------

# Gui Garbage

# Layout of app - will rearange dynamically thanks to magic
layout = [[catGui.Text("Cat", size=(100, 5), key="factTextBox")], [catGui.Text("Test Fact")],
          [catGui.Button("Get Fact")]]

# Actually making the window now

window = catGui.Window("Cat in the App", layout, size=(1000, 1000))

# event loop to keep the window open and allow the user to close it

while True:
    # PysimpeGui runs off events
    event, values = window.read()
    if event == ("Get Fact"):
        newFact = getCatFact()
        window["factTextBox"].Update(newFact)  # Updates Text

    if event == catGui.WIN_CLOSED:
        break

window.close()
