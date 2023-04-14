# import pyttsx3
# friend = pyttsx3.init()
# friend.say("hello")
# # """ RATE"""
# rate = friend.getProperty('rate')   # getting details of current speaking rate
# print (rate)                        #printing current voice rate
# friend.setProperty('rate', 80) 
# voices = friend.getProperty('voices')
# friend.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
# friend.runAndWait()

# import pyttsx3
# engine = pyttsx3.init()

# engine.say("I will speak this text")

# engine.runAndWait()


from tkinter import *
import pyttsx3


top = Tk()
top.title('tkinter text-to-speech')
top.geometry('800x500')
top.config(bg='#123456')

def talk():
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)  #setting up new voice rate
    #voices = engine.getProperty('voices')
    #engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female
    engine.say(my_entry.get())
    
    #engine.save_to_file('Hello World', 'test1.mp3')
    engine.runAndWait()
    my_entry.delete(0,END)



my_entry = Entry(top, font=('Lora', 15))
my_entry.pack(pady=20)
my_button = Button(top, text='click me', command=talk)
my_button.pack(pady=20)

top.mainloop()
