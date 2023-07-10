import pyttsx3
import PyPDF2
import PySimpleGUI as sg
from gtts import gTTS
import pathlib

def shorten_path(filepath):
    path = pathlib.Path(filepath)
    return path.stem

def convert_to_audio(filename, location):
    book = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(book)
    pages = len(pdfReader.pages)

    txtlist = []
    for i in range(pages):
        try:
            page = pdfReader.pages[i]
            txtlist.append(page.extract_text())
        except:
            pass
    textstring = ' '.join(txtlist)
    language = 'en'
    myAudio = gTTS(text=textstring, lang=language, slow=False)
    myAudio.save(location + "/" + shorten_path(filename) + ".mp3")

layout = [
    [sg.Text("Input File:"), sg.Input(key='-IN-'), sg.FileBrowse(file_types=(("PDF Files", "*.pdf"),))],
    [sg.Text("Download Location:"), sg.Input(key='-IN2-'), sg.FolderBrowse()],
    [sg.Exit(), sg.Button("Create MP3")]
]

window = sg.Window("PDF Text to Speech", layout)

while True:
    event, values = window.read()
    if event in (sg.WINDOW_CLOSED, "Exit"):
        break
    if event == "Create MP3":
        convert_to_audio(filename=values["-IN-"], location=values["-IN2-"])
window.close()
