# -*- coding: utf-8 -*-
"""
Created on Sat May 16 11:35:00 2020

@author: Ritul Singh
"""
# import wolframalpha library for Create the client.
import wolframalpha
client = wolframalpha.Client("lilpumpsaysnopeeking")

# import wikipedia library
import wikipedia

# import PySimpleGUI library
import PySimpleGUI as sg
sg.theme('Reddit')

# All the stuff inside the window.
layout =[[sg.Text('Enter the word you want to know about :'), sg.InputText()],[sg.Button('Ok'), sg.Button('Cancel')]]

# Create the Window
window = sg.Window('Information About The Word', layout)

# pyttsx3 is a text-to-speech conversion library in Python
import pyttsx3
engine = pyttsx3.init()

# all working part

while True:
    event, values = window.read()
    if event in (None, 'Cancel'):
        break
    try:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking("Wolfram Result: "+wolfram_res,"Wikipedia Result: "+wiki_res)
    except wikipedia.exceptions.DisambiguationError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except wikipedia.exceptions.PageError:
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wolfram_res)
        sg.PopupNonBlocking(wolfram_res)
    except:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        engine.say(wiki_res)
        sg.PopupNonBlocking(wiki_res)

    engine.runAndWait()

    print (values[0])

window.close()