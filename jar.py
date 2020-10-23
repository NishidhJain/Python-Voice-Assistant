import tkinter as tk
import tkinter.font as tkFont
import pyttsx3
import speech_recognition as sr
import datetime
import pyaudio
import wikipedia
import smtplib
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def sendEmail(to,content):
	server=smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.login('youremail@gmail.com','password')
	server.sendmail('youremail@gmail.com',to,content)
	server.close()

def wishMe():
	hour=int(datetime.datetime.now().hour)
	if hour>=0 and hour<12:
		speak("Good morning!");
	elif hour>=12 and hour<18:
		speak("Good afternoon!")
	else:
		speak("Good Evening!")
	speak("I am your personal voice assistant. How may i help you!")

def googlecmd():
    print("What do you want to search?")
    speak("What do you want to search")
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold=1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        speak("Recognizing...")
        question=r.recognize_google(audio)
        print(f"User said: {question}\n")
        speak("you said ")
        speak(question)

    except Exception as e:
        print("Please try it again..")
        speak("I cannot recognize . Please say it again..")
        return "None"
    return question


def takeCommand():
 	r=sr.Recognizer()
 	with sr.Microphone() as source:
 		speak("Listening...")
 		r.adjust_for_ambient_noise(source)
 		print("Listening...")
 		r.pause_threshold=1
 		audio=r.listen(source)

 	try:
 		print("Recognizing...")
 		query=r.recognize_google(audio)
 		print(f"User said: {query}\n")

 	except Exception as e:
 		print(" Please say it again...")
 		return "None"
 	return query

def inpt():
	wishMe()
	query=takeCommand().lower()

	if "wikipedia" in query:
		print("Searching wikipedia...")
		query=query.replace("wikipedia","")
		results=wikipedia.summary(query, sentences=3)
		print(results)
		speak("According to wikipedia")
		speak(results)

	elif "open youtube" in query:
		query = googlecmd()
        driver = webdriver.Chrome("C://Users/ASUS/Downloads/chromedriver_win32/chromedriver.exe")
        driver.get("https://www.youtube.com")
        driver.maximize_window()
        element = driver.find_element_by_name("q")
        element.clear()
        element.send_keys(query)
        element.send_keys(Keys.RETURN)
        options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        options.add_experimental_option("prefs",prefs)

	elif "open google" in query:
		query=googlecmd()
        driver = webdriver.Chrome("C://Users/ASUS/Downloads/chromedriver_win32/chromedriver.exe")
        driver.get("https://www.google.com")
        driver.maximize_window()
        element = driver.find_element_by_name("q")
        element.clear()
        element.send_keys(query)
        element.send_keys(Keys.RETURN)
        options = webdriver.ChromeOptions()
        prefs = {"profile.default_content_setting_values.notifications" : 2}
        options.add_experimental_option("prefs",prefs)

	elif "play music" in query:
		music_dir="C:\\songs"
		songs=os.listdir(music_dir)
		print(songs)
		os.startfile(os.path.join(music_dir,songs[1]))

	elif "the time" in query:
		strTime=datetime.datetime.now().strftime("%H:%M:%S")
		print("Time is ", strTime)
		speak(f"The time is {strTime}")

	elif "send email" in query:
		try:
			speak("What should i say?")
			content=takeCommand()
			to = receiver_email@gmail.com
			sendEmail(to,content)
			speak("Email has been send.")

		except Exception as e:
			print(e)
			speak("Email not sent")

window = tk.Tk()
window.geometry("700x500")
window.title("Voice Assistant")

fontStyle = tkFont.Font(family="Lucida Grande", size=50)
btnfontStyle = tkFont.Font(family="Lucida Grande", size=25)

label = tk.Label(window, text = "VOICE", font = fontStyle).pack()
label1 = tk.Label(window, text = "ASSISTANT", font = fontStyle).pack()

btn = tk.Button(window, text="Voice Search", command = inpt, bd = 7, padx = 10, pady = 10, font = btnfontStyle).place(x = 230, y = 250)

window.mainloop()