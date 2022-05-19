import tkinter

window = tkinter.Tk()
window.geometry("300x150")

messageUsername = tkinter.Label(text="Please enter you username.")
messageUsername.pack()

userName = tkinter.Entry(window, )
userName.pack()

messagePassword = tkinter.Label(text="Please enter your password.")
messagePassword.pack()

userPassword = tkinter.Entry(window, show="*")
userPassword.pack()


window.mainloop()
