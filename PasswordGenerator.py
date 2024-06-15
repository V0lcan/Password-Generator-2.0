import tkinter as tk
import random

global specials_var, numbers_var, uppercase_var

#Config
with open("config.txt", "r") as file: #Get the filepath from the config file.
            for line in file: 
                if "filepath=" in line: #If the line contains the filepath.
                    filepath = line.split("=")[1] #Get the filepath.
                    filepath = filepath[:-1] #Remove the newline character.

                if "characters_min=" in line: #Set min characters
                    characters_min = int(line.split("=")[1])

                if "characters_max=" in line: #Set max characters
                    characters_max = int(line.split("=")[1])

                if "window_size=" in line:
                    window_size = line.split("=")[1]

def password_generator(CharacterAmount, Special_Characters, Numbers, UpperCase):

    if CharacterAmount < characters_min or CharacterAmount > characters_max:
        error_message.configure(text="Please enter a valid number.")
        return

    #Lists of characters
    Special_Characters_List = "!@#$%^&*()_-+=<>?"
    Numbers_List = "0123456789"
    UpperCase_List = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    LowerCase_List = "abcdefghijklmnopqrstuvwxyz"

    #The generated password
    Password = ""

    for i in range(CharacterAmount):
        X = random.randint(0, 3)

        if Special_Characters == True and X == 0:
            Password += Special_Characters_List[random.randint(0, 13)]
        elif UpperCase == True and X == 1:
            Password += UpperCase_List[random.randint(0, 25)]
        elif Numbers == True and X == 2:
            Password += Numbers_List[random.randint(0, 9)]
        elif X == 3:
            Password += LowerCase_List[random.randint(0, 25)]
        else:
            Password += LowerCase_List[random.randint(0, 25)]

    generated_password.delete(1.0, "end")
    generated_password.insert("1.0", Password)
    generated_password.tag_configure("center", justify="center")
    generated_password.tag_add("center", "1.0", "end")

def save_password_to_file(Source, Username, Password):
    if len(Source) < 1 or Source == " ":
        error_message.configure(text="Filename cannot be empty.")
        return
    elif len(Username) < 1 or Username == " ":
        error_message.configure(text="Username cannot be empty.")
        return
    else:
        open(f"{filepath}\\{Source}.txt", "w").write(f"Username: {Username}\nPassword: {Password}")
        error_message.configure(text="Saved to: " + filepath + f"\\{Source}.txt")

def copy_to_clipboard(text_to_copy):
    app.clipboard_clear()
    app.clipboard_append(text_to_copy[:-1])

#Colors
c1 = "#2e3440"
c2 = "#3b4252"
c3 = "#434c5e"
c4 = "#4c566a"

#App
app = tk.Tk()
app.title("Password Generator")
app.geometry(window_size)
app.resizable(False, False)
app.configure(bg=c1, padx=10, pady=20)

#Amount of characters
text1 = tk.Label(app, text="How many characters do you want in your password?", fg="white", bg=c1)
text1.pack()
character_amount = tk.Entry(app, width=20, fg="white", bg=c2)
character_amount.pack()

specials_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
uppercase_var = tk.BooleanVar()

#Check frame
check_frame = tk.Frame(app, bg=c1, pady=10)

#Special Characters
special_characters = tk.Checkbutton(check_frame, text="Special Characters", fg=c4, bg=c1, activebackground=c1, activeforeground=c2, onvalue=1, offvalue=0, variable=specials_var)
special_characters.grid(row=0, column=0)

#Numbers
numbers = tk.Checkbutton(check_frame, text="Numbers", fg=c4, bg=c1, activebackground=c1, activeforeground=c2, onvalue=1, offvalue=0, variable=numbers_var)
numbers.grid(row=0, column=1)

#Uppercase
uppercase = tk.Checkbutton(check_frame, text="Uppercase", fg=c4, bg=c1, activebackground=c1, activeforeground=c2, onvalue=1, offvalue=0, variable=uppercase_var)
uppercase.grid(row=0, column=2)

check_frame.pack()

#Generate frame
generate_frame = tk.Frame(app, bg=c4)
generate_frame.pack()

#Generate Button
generate = tk.Button(generate_frame, cursor="hand2", text="Generate Password", fg="white", bg=c2, activebackground=c3, activeforeground="white", command=lambda: password_generator(int(character_amount.get()), specials_var.get(), numbers_var.get(), uppercase_var.get()))
generate.grid(row=0, column=0)

#Copy to clipboard
copy = tk.Button(generate_frame, cursor="hand2", text="Copy to Clipboard", fg="white", bg=c2, activebackground=c3, activeforeground="white", command=lambda: copy_to_clipboard(generated_password.get("1.0", "end")))
copy.grid(row=0, column=1)

#Generated password
generated_password = tk.Text(app, cursor="arrow", height=1, fg="white", bg=c1, border=0, pady=5)
generated_password.pack()

#Divider
divider = tk.Label(app, text="", fg="white", bg=c1, height=0, pady=1)
divider.pack()

#Save frame
save_frame = tk.Frame(app, bg=c1)

#Save password to file
save_source = tk.Label(save_frame, text="Filename:", fg="white", bg=c1, justify="right")
save_source.grid(row=0, column=0, sticky="e")
save_source_entry = tk.Entry(save_frame, width=20, fg="white", bg=c2)
save_source_entry.grid(row=0, column=1, pady=5)

save_username = tk.Label(save_frame, text="Username:", fg="white", bg=c1, justify="right")
save_username.grid(row=1, column=0, sticky="e")
save_username_entry = tk.Entry(save_frame, width=20, fg="white", bg=c2)
save_username_entry.grid(row=1, column=1, pady=5)

save_frame.pack()

save = tk.Button(save_frame, cursor="hand2",text="Save Password to File", fg="white", bg=c2, activebackground=c3, activeforeground="white", command=lambda: save_password_to_file(save_source_entry.get(), save_username_entry.get(), generated_password.get("1.0", "end")))
save.grid(row=2, column=0, columnspan=2)

#Error message
error_message = tk.Label(app, text="", fg="red", bg=c1, pady=5)
error_message.pack()

app.mainloop()