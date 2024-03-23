import tkinter

MW = tkinter.Tk()

labelName = tkinter.Label(MW, text = 'Name')
labelEmail = tkinter.Label(MW, text = 'Email')
labelPassword = tkinter.Label(MW, text = 'Password')

labelName.grid(row = 0, column = 0)
labelEmail.grid(row = 0, column = 1)
labelPassword.grid(row = 0, column = 2)

textboxName = tkinter.Text()
textboxEmail = tkinter.Text()
textboxPassword = tkinter.Text()

textboxName.grid(row = 1, column = 0)
textboxEmail.grid(row = 1, column = 1)
textboxPassword.grid(row = 1, column = 2)

buttonSignUp = tkinter.Button(MW, text = 'Sign-Up')
buttonSignUp.grid(row = 3, column = 1)

MW.mainloop()