
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime#inBuilt
import wikipedia #pip install wikipedia
import webbrowser#inBuilt
import os#inBuilt
from random import choice
import requests
# import pywhatkit as kit
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("we are F 5 along with group member Nandini , Omkar , Pratiksha , Shreyas , Shraddhey . Please tell me how may I help you")       

opening_text = [
    "Cool, I'm on it sir.",
    "Okay sir, I'm working on it.",
    "Just a second sir.",
]

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query


OPENWEATHER_APP_ID = "343c052bbd40667682f5353e84ece734"


def get_weather_report(city):
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=343c052bbd40667682f5353e84ece734&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"


def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]


def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']


def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mumba45indians2.0@gmail.com', 'yourpassword')
    server.sendmail('mumba45indians2.0@gmail.com', to, content)
    server.close()
    

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('What do you want to search on Wikipedia, sir?')
            search_query = takeCommand().lower()
            results = wikipedia.summary(query, sentences=2)
            speak(f"According to Wikipedia, {results}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(results)
            
        elif 'youtube' in query:
            speak('What do you want to play on Youtube, sir?')
            video = takeCommand().lower()
            kit.playonyt(video)
            


        # elif 'open youtube' in query or "youtube" in query:
        #     webbrowser.open("https://www.youtube.com/")
            
        # elif 'youtube' in query:
        #     speak('What do you want to play on Youtube, sir?')
        #     video = take_user_input().lower()
        #     play_youtube(video)    

        elif 'search on google' in query:
            speak('What do you want to search on Google, sir?')
            query = takeCommand().lower()
            kit.search(query)
            
            
        elif "trending movies" in query:
            speak("Some of the trending movies are: {get_trending_movies()}")
            speak("For your convenience, I am printing it on the screen sir.")
            webbrowser.open("https://m.vegamovies.lol/category/bollywood/")
            query = takeCommand().lower()
            kit.search(query)
            # print(*get_trending_movies(), sep='\n')     
        
        
        elif 'open google' in query or "google" in query:
            webbrowser.open("https://www.google.co.in/")
            
            
            
        elif 'open vit website' in query or "vit website" in query:
            webbrowser.open("https://www.vit.edu/")
            
            
            
        elif 'play kgf' in query or "kgf" in query:
            webbrowser.open("https://www.youtube.com/watch?v=AgjSx_nYKNY") 
            
             

        elif 'open erp' in query or "erp" in query:
             webbrowser.open("https://learner.vierp.in/dashboardLearnerProfile") 
             
             
        elif 'joke' in query:
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen sir.")
            print(joke)

        elif "advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen sir.")
            print(advice)
             
        elif "send whatsapp message" in query:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = takeCommand().lower()
            kit.sendwhatmsg_instantly(f"+91{number}", message)
            speak("I've sent the message sir.")    
        
        elif 'weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")      
        
        elif 'date' in query:
            x = datetime.datetime.now()
            print(x.strftime("%x %A"))
            speak(x.strftime("%x %A"))
            
            
           
        elif 'open classroom' in query or "classroom" in query:
             webbrowser.open("https://classroom.volp.in/learner-profile")
             
             
             
        elif 'open snakify' in query or "snakify" in query:
             webbrowser.open("https://snakify.org/en/")  
             
             
             
        elif 'play songs' in query or "songs" in query:
             webbrowser.open("https://www.youtube.com/watch?v=3GI_uE4SxSU&t=30089s")
             
             
             
        elif 'open whatsapp' in query or "whatsapp" in query:
             webbrowser.open("https://web.whatsapp.com/") 
             
             
            
        elif 'open linkedin' in query or "linkedin" in query:
             webbrowser.open("https://www.linkedin.com/feed/")
             
             
             
        elif 'open instagram' in query or "instagram" in query:
             webbrowser.open("https://www.instagram.com/deokar_om/") 
             
             
             
        elif 'open discord' in query or "discord" in query:
             webbrowser.open("https://discord.com/channels/764733596585689108/764800326300598272/")   
             
                
             
        elif 'make speed test' in query or "speed test" in query:
             webbrowser.open("https://www.speedtest.net/")  
             
             
             
        elif 'send email' in query or "email" in query:
             webbrowser.open("https://mail.google.com/mail/u/0/#sent?compose=GTvVlcSGKZRNTkcHpkKHSxnWGRCDDtbCGWSgMDCcnRFgWMgqZHkXkdrFmKqJpdtltsLqfQjXrzCxL")  
             
             
             
        elif 'open ppt' in query or "ppt" in query:
             webbrowser.open("https://www.canva.com/design/DAFDFxm9lcc/kf4f5EUW4Binel12X1vbPQ/edit?utm_content=DAFDFxm9lcc&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton")      
             
                       
               
        elif 'open notepad' in query or "notepad" in query:
            codePath = "C:\\Windows\\notepad.exe"
            os.startfile(codePath)
            
            
            
        elif 'open word' in query or "word" in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk"
            os.startfile(codePath) 
            
            
            
        elif 'open excel' in query or "excel" in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk"
            os.startfile(codePath)  
            
            
            
        elif 'show group photo' in query or "group photo" in query:
            codePath = "C:\\Users\\user\\AppData\\Roaming\\Telegram Desktop\\d-12.jpg"
            os.startfile(codePath)
            
            
            
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by d 5.")  
            
                  
            
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()             
      # elif 'play music' in query:
        #     music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
        #     songs = os.listdir(music_dir)
        #     print(songs)    
        #     os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        # elif 'open code' in query:
        #      codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        #      os.startfile(codePath)

        elif 'email to pratik' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "de0kar0mb@gmail,com" 
                codePath = "https://mail.google.com/mail/u/0/#sent?compose=new"   
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend deokar . I am not able to send this email")  
               
                
                #
