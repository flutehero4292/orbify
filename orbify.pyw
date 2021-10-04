#Orbify
import tkinter as tk

def orbify(name):
    vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    orbname = ""
    for character in name:
        if character in vowels:
            orbname += "ORB"
        else:
            orbname += character
    return f"{name.upper()} -> {orbname.upper()}"
            
window = tk.Tk()
window.title("Orbify")

frm_entry = tk.Frame(master=window)
frm_entry.pack()

lbl = tk.Label(master=frm_entry, text="Enter the name to be orbified:")
lbl.pack(side=tk.LEFT)
ent = tk.Entry(master=frm_entry)
ent.pack(side=tk.RIGHT)

frm_button = tk.Frame(master=window)
frm_button.pack()

frm_output = tk.Frame(master=window)
frm_output.pack()

txt_output = tk.Text(master=frm_output)
txt_output.pack()

def orbify_button():
    txt_output.delete("0.0", tk.END)
    result = orbify(ent.get())
    txt_output.insert("0.0", result)

btn_orbify = tk.Button(master=frm_button, text="Orbify!", command=orbify_button)
btn_orbify.pack()

window.mainloop()
