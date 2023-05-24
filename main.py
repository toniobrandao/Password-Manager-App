from tkinter import *
from tkinter import messagebox
import pyperclip
import json

# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)


    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [ random.choice(symbols) for symbol in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for number in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)




# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    if len(website)==0 or len(password)==0  or len(username)==0 :
        messagebox.showinfo(title = "Error",message="There are blank areas")
        return
    new_data = {website:
                    {"email":username,"password":password}}
    #messagebox.askokcancel(title=website, message="You sure you want to continue?")
    is_ok = True
    if is_ok:
        try:
            with open("password.json", "r") as passwords_file:
                data = json.load(passwords_file)
                data.update(new_data)
        except FileNotFoundError:
            with open("password.json", "w") as passwords_file:
                json.dump(new_data, passwords_file, indent=4)
        else:
            with open("password.json", "w") as passwords_file:
                json.dump(data, passwords_file, indent=4)
        finally:
            website_entry.delete(0,"end")
            password_entry.delete(0, "end")
            website_entry.focus()
            pyperclip.copy(password)



# ---------------------------- Search Password ------------------------------- #

def search_password():
    with open("password.json", "r") as passwords_file:
        data = json.load(passwords_file)
        website = website_entry.get()
        try:
            data = data[website]
        except:
            messagebox.showinfo(title = "Password not fount",message="You don't have a password saved for this website")
        else:
            messagebox.showinfo(title = f"Your data for {website}",message=f"E-mail: {data['email']}\nPassword: {data['password']}")



# ---------------------------- UI SETUP ------------------------------- #

#Creating a new window and configurations
window = Tk()

window.title("Password Manager")

window.config(padx=20,pady=20)

canvas = Canvas(width=200,height=200,highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(105,112,image = logo_img)
canvas.grid(row=0,column=1)


# Labels:


website_label = Label(text="Website:")
website_label.grid(row=1,column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0)

password_label = Label(text="Password:")
password_label.grid(row=3,column=0)


# Entries:

website_entry =  Entry(width=21)
website_entry.grid(row=1,column=1)
website_entry.focus()

username_entry = Entry(width=36)
username_entry.grid(row=2,column=1,columnspan =2)
username_entry.insert(0,"antoniobrandaolima97@gmail.com")
password_entry =  Entry(width=21) #width=21
password_entry.grid(row=3,column=1)

#Buttons:



#calls action() when pressed
generate_password_btn = Button(text="Generate", command=generate_password,width=12)

generate_password_btn.grid(row=3,column=2)

search_btn = Button(text="Search", command=search_password, width=12)

search_btn.grid(row=1,column=2)

add_btn = Button(text="add", command=add_password, width=36)

add_btn.grid(row=4,column=1,columnspan =2)




window.mainloop()