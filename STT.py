from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *
import speech_recognition as sr

root = Tk()
root.title('Speech to Text')
root.geometry('400x600')
root.config(bg= 'mistyrose')

text= ''

Label(root, text= 'Voice Note', font= '30').pack(pady= 15)

Outputext= Text(root, width=40, height=20)
Outputext.pack(pady= 20)

def Trans_message():
    global text
    #Initiate Recogniser
    r= sr.Recognizer()

    #Mention the source( Microphone or File)
    with sr.Microphone() as source:
        print('Speak Now')
        voice= r.listen(source)
        try:
            text= r.recognize_google(voice)
        except:
            print(text)
            text= 'Sorry, please try again.'
        Outputext.delete(1.0, END)
        Outputext.insert(END, text)

def savefile():
    files= [
        ('all files','*.*' ), ('python files', '*.py'), ('html files', '*.html')
    ]
    file= asksaveasfile(filetypes= files, defaultextension= files,)
    file.write(text)

save= Button(root, text= 'Save the data', command= savefile)
save.pack(pady= 20)

Translate= Button(root, text= 'Translate', command= Trans_message)
Translate.pack(pady= 20)



root.mainloop()