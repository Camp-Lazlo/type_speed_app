import requests
from tkinter import *
import time

api_ninja_endpoint = "https://api.api-ninjas.com/v1/quotes"
api_ninja_key = "5lQpcVwKBRpjA4IEOp0IBw==InSjKEee91RfYWWk"

headers = {
    'X-Api-Key': api_ninja_key
}
response = requests.get(url=api_ninja_endpoint, headers=headers)
response.raise_for_status()
quote = response.json()[0]['quote']
author = response.json()[0]['author']

window = Tk()
window.title("Typing Speed App")

sentence = "at cat"
letter_seq = list(quote)


def callback(label):
    label.config(bg="green")


def keypress(event):
    global current_index, wrong_cnt
    if current_index < len(label_list) and event.char == letter_seq[current_index]:
        callback(label_list[current_index])
        current_index += 1

    else:
        if event.keysym != "Caps_Lock":
            wrong_cnt += 1

    if current_index == len(label_list):
        end_time = time.time()
        time_elapse = end_time - start_time
        char_cnt = len(label_list)
        wpm = round(12 * char_cnt / time_elapse, 1)
        accuracy = round(((char_cnt - wrong_cnt) / char_cnt) * 100, 2)
        quote_btn = Label(window, text=f"- {author}", font=("Times", 14, "bold"))
        quote_btn.pack(side=TOP)
        wpm_btn = Button(window, text=f"Wpm: {wpm}", font=("Times", 14, "bold"))
        wpm_btn.pack(side=TOP)
        accuracy_btn = Button(window, text=f"Accuracy: {accuracy}%", font=("Times", 14, "bold"))
        accuracy_btn.pack(side=TOP)


current_index = 0
wrong_cnt = 0
label_list = []

frame = Frame(window)
frame.pack(pady=50, padx=50)

for char in letter_seq:
    label = Label(frame, text=char, font=("Times", 14, "bold"))
    label.pack(side=LEFT)
    label_list.append(label)

total_width = sum(label.winfo_reqwidth() for label in label_list)
window.geometry(f"{total_width + 100}x300")

start_time = time.time()

window.bind('<Key>', keypress)
window.mainloop()
