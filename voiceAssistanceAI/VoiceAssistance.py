import speech_recognition
import pyttsx3 as tts
import openai
import sys

recognizer = speech_recognition.Recognizer()

speaker = tts.init()
speaker.setProperty('rate', 200)
engine = tts.init()

# openai.api_key = "your openai.api_key"
todo_list = ['Go shopping', 'Clean room', 'Get a new job']


def create_note():
    global recognizer

    speaker.say("What would you like to write on your note?")
    speaker.runAndWait()

    done = False

    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                note = recognizer.recognize_google(audio)
                note = note.lower()

                speaker.say("Choose a file name")
                speaker.runAndWait()

                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                filename = recognizer.recognize_google(audio)
                filename = filename.lower()

            with open(filename, 'w') as f:
                f.write(note)
                done = True
                speaker.say(f"Your note has successfully been added and saved to {filename}")
                speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I didn't get that. Please repeat that again")
            speaker.runAndWait()
            continue


def add_todo():
    global recognizer

    speaker.say("What would you like to add?")
    speaker.runAndWait()

    done = False

    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)
                item = recognizer.recognize_google(audio)
                item = item.lower()

            todo_list.append(item)
            done = True
            speaker.say(f"I added {item} to the todo list")
            speaker.runAndWait()

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            speaker.say("I didn't get that. Please repeat that again")
            speaker.runAndWait()
            continue


def show_todo():
    speaker.say("The items in the todo list are:")
    for item in todo_list:
        speaker.say(item)
    speaker.runAndWait()


def say_hello():
    speaker.say("Hello Ulle! How are you doing?")
    speaker.runAndWait()


def quit():
    speaker.say("Goodbye Olle!")
    speaker.runAndWait()
    sys.exit()


mapping = {
    "greeting": say_hello,
    "goodbye": quit,
    "add_todo": add_todo,
    "show_todos": show_todo,
    "create_note": create_note,
}




def generate_response(prompt):
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to answer your friend about questions."},
            
        ]
    )
    print(response.choices[0].message.content)



# Example usage
prompt = "What is the meaning of life?"
print(generate_response(prompt))


def speak_text(text):
    engine.say(text)
    engine.runAndWait()


def main():

    while True:
        print("Say hello to start recording")
        try:
            with speech_recognition.Microphone() as mic:
                recognizer = speech_recognition.Recognizer()
                mic.pause_threshold = 1
                audio = recognizer.listen(mic, phrase_time_limit=20, timeout=None)

                text = recognizer.recognize_google(audio)
                print(f"you said {text}")
                if text.lower() == "hello":
                    gpttext = generate_response(text)
                    print(f"gpttext text is {gpttext}")

                    speak_text(gpttext)

        except Exception as e:
            print("Sorry, ", e.message)
            recognizer = speech_recognition.Recognizer()


if __name__ == "__main__":
    main()
