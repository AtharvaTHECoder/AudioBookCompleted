import pyttsx3
import PyPDF2
from PyPDF2 import PdfFileReader

speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[9].id) 
newVoiceRate = 115
speaker.setProperty('rate',newVoiceRate)
book = open('gullivers-travels.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
page = pdfReader.getPage(10)
text = page.extractText()
speaker.say(text)
speaker.runAndWait()
