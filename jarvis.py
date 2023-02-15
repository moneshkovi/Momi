import pyttsx3
import speech_recognition as sr
from datetime import datetime
import wikipedia
import webbrowser 
import os 
import smtplib 
from random import randint
import pyowm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import psutil
import platform
import datefinder
import winsound
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json
from googletrans import Translator,LANGUAGES 
import pyautogui
import cv2
import numpy as np
from moviepy.editor import VideoFileClip
import pytube
import time
import random   



def find_files(filename, search_path):
    result = []

    # Wlaking top-down from the root
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(os.path.join(root, filename))
    return result
print(find_files("Eternal5", "F:"))


def search_web(query):
    driver = webdriver.Chrome(r"C:\Users\monesh\PycharmProjects\Jarvis\chromedriver.exe")
    driver.implicitly_wait(1)
    driver.maximize_window()
    if 'youtube' in query.lower():
        speak("Opening in youtube")
        indx = query.lower().split().index('youtube')
        querys = query.split()[indx + 1:]
        driver.get("http://www.youtube.com/results?search_query=" + '+'.join(querys))
        return


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voices', voices[1].id)
print(len(voices))

# system configuration
uname = platform.uname()
# CPU configuration
cpufreq = psutil.cpu_freq()
# battery configuration
battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = str(battery.percent)
secsleft = str(battery.secsleft)
plugged = "Charging" if plugged else "Discharging"


def afternoonquotes():
    f = open("afternoon.txt", "r")
    lines = f.readlines()
    # print(lines)
    length = len(lines)
    r1 = random.randint(0, length - 1)
    print(lines[r1])
    speak(lines[r1])
    f.close()





def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():

    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Your mind belives in your heart, so tell it positive things")
        speak("Good Morning Boss")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Boss")
        afternoonquotes()
    else:
        speak("Good Evening Boss")

    speak("I am momi. At your service!")



def weather():
    owm = pyowm.OWM("0adcfab7a6c3dc1cb0145b807aed5b8b")
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place('bangalore,in')  # the observation object is a box containing a weather object
    weather = observation.weather
    ws = weather.status  # short version of status (eg. 'Rain')
    wds = weather.detailed_status
    print(weather)
    print(ws)
    print(wds)
    speak(weather)
    speak(f"today's weather gonna be {ws}")
    speak(f"to be more specific {wds}")
    sunrise_unix = weather.sunrise_time()  # default unit: 'unix'
    sunrise_iso = weather.sunrise_time(timeformat='iso')
    sunrise_date = weather.sunrise_time(timeformat='date')
    sunrset_unix = weather.sunset_time()  # default unit: 'unix'
    sunrset_iso = weather.sunset_time(timeformat='iso')
    sunrset_date = weather.sunset_time(timeformat='date')
    print(sunrise_iso)
    print(sunrset_iso)
    temp_dict_celsius = weather.temperature('celsius')
    print(temp_dict_celsius)


def takeCommand():
    '''
    #It takes microphone input from user & return string output

    :return:
    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        # print(e)

        print("Say that again please...")
        #query=input("say that again plz")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smntp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('monesh23456@gmail.com', 'vijay@mone')
    server.sendmail('monesh23456@gmail.com', to, content)

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        print('Sending mail...')
        smtp.login('monesh23456@gmail.com', 'vijay@mone')
        print('logged in')
        subject =  ' This is an automated message '
        print('subject added')
        #body = ''
        msg = f'Subject:{subject}\n\n{body}'
        print('body added')
        smtp.sendmail('monesh2346@gmail.com', 'monesh23456@gmail.com', msg)
        print('Mail sent.!')




def system_status():
    speak("All systems are working fine.")
    speak('Battery Percentage: ' + percent + '%')
    speak('Battery state: ' + plugged)
    speak(f"Current Frequency: {cpufreq.current:}Mhz")
    speak(f"Total CPU Usage: {psutil.cpu_percent()}%")


def screenshot():
    img1 = pyautogui.screenshot()
    img1.save('C:\\Users\\monesh\\Desktop\\screenshot.png')
    speak("Scrrenshot Taken")
    print("Screenshot Taken")


def detail_system_status():
    # let's print System information
    print("=" * 40, "System Information", "=" * 40)
    print(f"System: {uname.system}")
    print(f"Node Name: {uname.node}")
    print(f"Release: {uname.release}")
    print(f"Version: {uname.version}")
    print(f"Machine: {uname.machine}")
    print(f"Processor: {uname.processor}")
    # let's print CPU information
    print("=" * 40, "CPU Info", "=" * 40)
    # number of cores
    print("Physical cores:", psutil.cpu_count(logical=False))
    print("Total cores:", psutil.cpu_count(logical=True))
    # CPU frequencies
    print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
    print(f"Min Frequency: {cpufreq.min:.2f}Mhz")

    print(f"Max Frequency: {cpufreq.max:.2f}MHZ")
    print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
    # CPU usage
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")
    # let's print Battery information
    print(f"Battery percentage: {percent}%")
    print(f"Battery status : {plugged}")
    print(f"seconds left: {secsleft} sec")

#alarm
def alarm(text):
    date_Time_alarm = datefinder.find_dates(text)
    while True:
        for mat in date_Time_alarm:
            print(mat)
        if (mat.hour == datetime.now().hour and mat.minute == datetime.now().minute):
                speak("WAKEUP"*5)
        if(mat.minute<datetime.now().minute):
            speak("YOU LAZY BAGG.!"*5)
            break



#main function
if __name__ == '__main__':
   # py_path = "C:\\Users\\tarun\\PycharmProjects\\momi\\GUI.py"
   # os.startfile(py_path)
    wishme()
    weather()
    system_status()

    while True:
        query = takeCommand().lower()

        if 'hello' in query:
            speak("well, hello")

        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com/")
        elif 'open instagram' in query:
            webbrowser.open("https://www.instagram.com/hitlerism_2001/")
        elif 'play music' in query:
            speak("what should i play?")
            content = takeCommand()
            browser = webdriver.Chrome()
            browser.implicitly_wait(5)
            browser.open_new_tab('https://open.spotify.com')
            browser.find_element_by_xpath("//button[@data-testid='login-button']").click()
            sleep(5)
            with open('test.json') as f:
                data = json.load(f)
            if "spotify" in data:
                email = str(data["discord"]["email"])
                passw = str(data["discord"]["pass"])
            browser.find_element_by_xpath("//input[@ng-model='form.username']").send_keys("dhana2,naidu@gmail.com")
            browser.find_element_by_xpath("//input[@ng-model='form.password']").send_keys("tarunnaidu")
            browser.find_element_by_xpath("//button[@id='login-button']").click()
            sleep(5)
            if "spotify" not in data:
                email = str(input("EMAIL: "))
                passw = str(input("PASSW: "))
                a_dict = {"spotify": {"email": email, "pass": passw}}
                data.append(a_dict)
                with open('test.json', 'w') as f:
                    json.dump(data, f)
            browser.get('https://open.spotify.com/search')
            search = browser.find_element_by_xpath(
                "//input[@class='_748c0c69da51ad6d4fc04c047806cd4d-scss']").send_keys(content)
            browser.find_element_by_xpath("//div[@class='_85fec37a645444db871abd5d31db7315-scss']").click()
        elif 'open my stuff' or 'open my staff' in query:
            webbrowser.open('https://github.com/')
            webbrowser.open('https://dashboard.heroku.com/apps')
            webbrowser.open("https://www.youtube.com/")
            webbrowser.open('https://stackoverflow.com/')
        elif 'the time' in query:
            strTime = datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f'Sir, the time is {strTime}')
        elif 'open code' in query:
            vs_path = "C:\\Users\\monesh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vs_path)
        elif 'open chrome' in query:
            c_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            py_path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.2.1\\bin\\pycharm64.exe"
            os.startfile(c_path)
        elif 'open spotify' in query:
            webbrowser.open("https://open.spotify.com/#_=_")
        elif 'email me' in query:
            try:
                speak("what should i say?")
                body = input()
                to = "monesh23456@gmail.com"
                sendEmail(to, body)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry sir,i am not able to send this email")
        elif 'search' in query:
            search_web(query)
        elif 'bye' in query or 'buy' in query or 'shutdown' in query or 'exit' in query or 'quit' in query or 'go to sleep' in query or 'goodbye' in query:
            speak("Alright sir, Have a good day ")
            exit()
        elif 'system status' in query or 'system report' or 'system info' in query:
            system_status()
            detail_system_status()
        elif 'remind' in query or 'alarm' in query:
            speak('setting alarm')
            alarm(query)
        elif 'weather' in query:
            weather()
        elif 'screenshot' in query:
            screenshot()
        elif 'discord' in query:
            try:
                speak("what should i say?")
                content = takeCommand()
                with open('C:\\Users\\monesh\\PycharmProjects\\Jarvis\\test.json') as f:
                    data = json.load(f)
                if "discord" in data:
                    email = str(data["discord"]["email"])
                    passw = str(data["discord"]["pass"])
                browser = webdriver.Chrome()
                browser.implicitly_wait(5)
                # opening instagram.com
                browser.get('https://discord.com/')
                # -------login process starts

                # finding input boxes for username and password and pasing the appropriate values
                browser.find_element_by_xpath(
                    "//a[@class='button-195cDm buttonWhite-18r1SC buttonSmall-2bnF7I gtm-click-class-login-button button-1x6X9g']").click()
                browser.find_element_by_xpath("//input[@name='email']").send_keys("monesh23456@gmail.com")
                browser.find_element_by_xpath("//input[@name='password']").send_keys("vijay@mone")
                browser.find_element_by_xpath("//button[@type='submit']").click()
                # -------login process ends
                if "discord" not in data:
                    email = str(input("EMAIL: "))
                    passw = str(input("PASSW: "))
                    a_dict = {"discord": {"email": email, "pass": passw}}
                    data.append(a_dict)
                    with open('test.json', 'w') as f:
                        json.dump(data, f)
                _login = WebDriverWait(browser, 20).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "searchBarComponent-32dTOx")))
                not_now_button = browser.find_element_by_xpath("//button[@class='searchBarComponent-32dTOx']")
                sleep(1)
                not_now_button.click()

                browser.find_element_by_xpath("//input[@class='input-2VB9rf']").send_keys("Tróñ")
                sleep(2)
                browser.find_element_by_xpath("//input[@class='input-2VB9rf']").send_keys(Keys.ENTER)
                sleep(2)
                label = 'Message @Tróñ'
                textbox = browser.find_element_by_xpath(f"//div[@aria-label='{label}']")
                textbox.click()
                textbox.send_keys(content, Keys.ENTER)
                browser.close()
            except Exception as e:
                print(e)
                speak("Sorry sir,i am not able to send this email")
                browser.close()


