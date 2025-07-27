import webbrowser
import pyttsx4

engine = pyttsx4.init()
# user input
engine.say("Hello! How is your mood right now? sad or happy")
print("Hello! How is your mood right now? [sad or happy]")
engine.runAndWait()

#loop
while True:
    usermood = input("[sad or happy]: ").lower()

    if usermood == "sad":
        engine.say("alright , im redirecting you to the playlist based on your mood ")
        print("alright , im redirecting you to the playlist based on your mood")
        engine.runAndWait()
        webbrowser.open("https://youtu.be/Jy-dLvnJaw8")
        break

    elif usermood == "happy":
        engine.say("alright , im redirecting you to the playlist based on your mood ")
        print("alright , im redirecting you to the playlist based on your mood")
        engine.runAndWait()
        webbrowser.open("https://youtu.be/2_Q08jJcqe0")
        break

    else:
        engine.say("Invalid choice ! try again")
        print("Invalid choice ! try again")
        engine.runAndWait()