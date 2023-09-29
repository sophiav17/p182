from tkinter import*
from tkinter import ttk
from googletrans import Translator
from googletrans import LANGUAGES

root = Tk()

root.title("Language Translator")
root.geometry("800x600")
root.configure(background = "pink")

label_title = Label(root, text = "LANGUAGE TRANSLATOR", bg = "pink", font = ("Comic Sans MS", 18))
label_title.place(relx = 0.5, rely = 0.1, anchor = CENTER)

label_text = Label(root, text = "Enter Text", bg = "pink", font = ("Comic Sans MS", 14))
label_text.place(relx = 0.1, rely = 0.2, anchor = W)

text_area = Text(root, bg = "white", font = ("Comic Sans MS", 12), height = 10, wrap = WORD, width = 40, padx = 10, pady = 1, bd = 0)
text_area.place(relx = 0.02, rely = 0.5, anchor = W)

language_list = list(LANGUAGES.values())

languages_dropdown = ttk.Combobox(root, state = "readonly", values = language_list, width = 10, font = ("Comic Sans MS", 12))
languages_dropdown.place(relx = 0.3, rely = 0.2, anchor = W)

languages_dropdown.set("English")

output_displayed = Label(root, text = "Output", bg = "pink", font = ("Comic Sans MS", 12))
output_displayed.place(relx = 0.7, rely = 0.2, anchor = E)

output_dropdown = ttk.Combobox(root, state = "readonly", values = language_list, width = 20, font = ("Comic Sans MS", 12))
output_dropdown.place(relx = 0.9, rely = 0.2, anchor = E)

output_dropdown.set("Choose Output Language")

output_text = Text(root, bg = "white", font = ("Comic Sans MS", 12), height = 10, wrap = WORD, width = 40, padx = 10, pady = 1, bd = 0)
output_text.place(relx = 0.98, rely = 0.5, anchor = E)

label_footer = Label(root, text = "Created by Sophia", font = ("Comic Sans MS", 12))
label_footer.place(relx = 0.5, rely = 0.9, anchor = CENTER)

def Translate() :
    translator = Translator()
    try: 
        translated = translator.translate((text, 1.0,END), src = src_lang.get(), dest = dest_lang.get())
        output_text.delete(1.0, END)
        output_text.insert(END, translated.text)
    except:
        print("Try again")
        
btn = Button(root, text = "Translate", command = Translate, font = ("Comic Sans MS", 14), bg = "IndianRed1", activebackground = "GoldenRod1", relief = FLAT, pady = 10)
btn.place(relx = 0.5, rely = 0.7, anchor = CENTER)        
        
root.mainloop()