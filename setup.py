import cx_Freeze 
from cx_Freeze import *

setup(
    name = "jarvis",
    options = ("build_exe":f('packages':['pyttsx3','speech_recognition','selenium','pyautogui','winsound','pyowm']))
    executables={
          Executables( 
              "jarvis.py",
 

              )

        }

    )
