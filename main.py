from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip


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
    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(title='Oops!!', message="please don't leave any fields empty!")

    else:

        is_ok = messagebox.askokcancel(title=f'{website}', message=f'These are the details entered: \nEmail: {email}'
                                                                   f'\nPassword: {password} \n Is it ok '
                                                                   f'to save?')

        if is_ok:
            with open('data.txt', 'w') as f:
                f.write(f"{website} | {email} | {password} \n")
            website_input.delete(0, END)
            password_input.delete(0, END)


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

website_input = Entry(width=35)
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

window.mainloop()
