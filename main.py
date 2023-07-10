import pyttsx3
import PyPDF2
import PySimpleGUI as sg

def convert_to_audio(filename):
    book = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(book)
    pages = len(pdfReader.pages)
    print(pages)
    speaker = pyttsx3.init()
    for num in range(0, pages):
        page = pdfReader.pages[num]
        text = page.extract_text()
        speaker.say(text)
        speaker.runAndWait()

layout = [
    [sg.Text("Input File:"), sg.Input(key='-IN-'), sg.FileBrowse(file_types=(("PDF Files", "*.pdf"),))],
    [sg.Exit(), sg.Button("Play Audiobook")]
]

window = sg.Window("PDF Text to Speech", layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    if event == "Play Audiobook":
        convert_to_audio(filename=values["-IN-"])
window.close()