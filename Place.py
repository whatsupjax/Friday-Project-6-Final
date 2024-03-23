import tkinter

MW = tkinter.Tk()

labelUsername = tkinter.Label(MW, text = 'Username')
labelPassword = tkinter.Label(MW, text = 'Password')

labelUsername.place(relx = .5, rely = .5, anchor = 'center')
labelPassword.place(relx = .5, rely = .7, anchor = 'center')

entryUsername = tkinter.Entry(MW)
entryPassword = tkinter.Entry(MW)

entryUsername.place(relx = .5, rely = .6, anchor = 'center')
entryPassword.place(relx = .5, rely = .8, anchor = 'center')

MW.mainloop()