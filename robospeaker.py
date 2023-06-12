import pyttsx3

if __name__ == '__main__':
    print("Welcome to Robospeaker 1.1")
    engine = pyttsx3.init()
    while True:
        x = input("Enter what you want to speak (q to quit): ")
        if x == "q":
            break
        engine.say(x)
        engine.runAndWait()