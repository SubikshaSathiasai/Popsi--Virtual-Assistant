import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()

machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

talk("Hello there! I'm Popsi, what can I do for you?")

def input_instruction():
    global instruction
    instruction = ''
    try:
        with sr.Microphone() as source:
            print("I'm Listening..")
            speech = listener.listen(source)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if 'popsi' in instruction:
                instruction = instruction.replace('popsi', ' ')
                print(instruction)               
    except:
        pass
    return instruction
  
def play_Popsi():
    while True:
        instruction = input_instruction()
        print(instruction)
        if "play" in instruction:
            song = instruction.replace('play', " ")
            talk("playing" + song)
            pywhatkit.playonyt(song)
          
        elif 'time' in instruction:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time' + time)
          
        elif 'date' in instruction:
            date = datetime.datetime.now().strftime('%d %M %Y')
            talk("Today's date" + date)
          
        elif 'how are you' in instruction:
            talk("Spotlight! Moonlight! I will be better tonight! Haha... just kidding... much better now that you are with me.")
          
        elif 'What is your name' in instruction:
            talk("I'm POPSI. What can I do for you?")
           
        elif 'Who is' in instruction:
            human = instruction.replace('who is', " ")
            info = wikipedia.summary(human, 1)
            print(info)
            talk(info)
          
        else:
            talk("Could you say that again, please?")
          
play_Popsi()
