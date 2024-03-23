import tkinter

MW = tkinter.Tk()

MW.title('Calculator')

button1 = tkinter.Button(MW, text = '1', width = 10, height = 5)
button2 = tkinter.Button(MW, text = '2', width = 10, height = 5)
button3 = tkinter.Button(MW, text = '3', width = 10, height = 5)
button4 = tkinter.Button(MW, text = '4', width = 10, height = 5)
button5 = tkinter.Button(MW, text = '5', width = 10, height = 5)
button6 = tkinter.Button(MW, text = '6', width = 10, height = 5)
button7 = tkinter.Button(MW, text = '7', width = 10, height = 5)
button8 = tkinter.Button(MW, text = '8', width = 10, height = 5)
button9 = tkinter.Button(MW, text = '9', width = 10, height = 5)
button0 = tkinter.Button(MW, text = '0', width = 10, height = 5)

button1.pack(side = 'left')
button2.pack(side = 'left')
button3.pack(side = 'left')
button4.pack(side = 'left')
button5.pack(side = 'left')
button6.pack(side = 'left')
button7.pack(side = 'left')
button8.pack(side = 'left')
button9.pack(side = 'left')
button0.pack(side = 'left')

buttonPlus = tkinter.Button(MW, text = '+', width = 10, height = 5)
buttonMinus = tkinter.Button(MW, text = '-', width = 10, height = 5)
buttonMulti = tkinter.Button(MW, text = '*', width = 10, height = 5)
buttonDivi = tkinter.Button(MW, text = '/', width = 10, height = 5)

buttonPlus.pack(side = 'right')
buttonMinus.pack(side = 'right')
buttonMulti.pack(side = 'right')
buttonDivi.pack(side = 'right')

textBox = tkinter.Text(state = 'disabled')

textBox.pack(side = 'top')

MW.mainloop()