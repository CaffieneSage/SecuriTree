import tkinter

# Creates a window element with the tkinter library and sits its size
# in pixels.

window = tkinter.Tk()
window.geometry("300x150")

# Creates a label with a prompt to enter username data.

messageUsername = tkinter.Label(text="Please enter you username.")
messageUsername.pack()

# Creates an entry box to receive username.

userName = tkinter.Entry(window, )
userName.pack()

# Creates a label with a prompt to enter password.

messagePassword = tkinter.Label(text="Please enter your password.")
messagePassword.pack()

# Creates an entry box to recieve password input.

userPassword = tkinter.Entry(window, show="*")
userPassword.pack()

window.mainloop()
