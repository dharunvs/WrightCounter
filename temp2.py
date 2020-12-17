import speech_recognition as sr

r = sr.Recognizer()
main_text = []
wright_count = 0

with sr.Microphone() as source:

    def recorder():
        global wright_count
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
            for i in main_text:
                if "right" in i:
                    wright_count += 1
            print(wright_count)
            recorder()
        except:
            print("Listening...")
            print(wright_count)
            recorder()
    recorder()
