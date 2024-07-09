from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = ''.join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {website: {
        "email": email,
        "password": password,
    }}
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title='Oops!!', message="please don't leave any fields empty!")

    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as f:
                json.dump(new_data, f, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


def search():
    website = website_input.get()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showerror(title='Error', message='No Data file found')
    else:
        if website in data:
            website_name = data[website]
            email = website_name['email']
            password = website_name['password']
            messagebox.showinfo(title=f"{website}", message=f"Email: {email}\nPassword: {password} \n")
            email_input.delete(0, END)
            email_input.insert(0, email)
            password_input.delete(0, END)
            password_input.insert(0, password)
        else:
            messagebox.showerror(title='Error', message=f'No Details for {website} exists.')


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels

website_text = Label(text='Website: ')
website_text.grid(column=0, row=1)

email_text = Label(text='Email/Username: ')
email_text.grid(column=0, row=2)

password_text = Label(text='Password: ')
password_text.grid(column=0, row=3)

# Entries(Inputs)

website_input = Entry(width=21)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, string='arafathreja0@gmail.com')

password_input = Entry(width=21)
password_input.grid(column=1, row=3, columnspan=2)

# buttons

generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3)

add_btn = Button(text='Add', width=36, command=add)
add_btn.grid(column=1, row=4, columnspan=2)

search_btn = Button(text='Search', command=search, width=13)
search_btn.grid(column=2, row=1)

window.mainloop()
