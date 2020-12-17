import speech_recognition as sr


def legend():
    r = sr.Recognizer()
    mic = sr.Microphone()
    main_text = []
    wright_count = 0

    with mic as source:

        def recorder():
            global wright_count
            print("Listening...")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print(text)
                main_text.append(text)
                print(main_text)
                if "right" in text or "write" in text:
                    wright_count += 1
                print(wright_count)
                recorder()
            except:
                print(wright_count)
                recorder()
        recorder()
