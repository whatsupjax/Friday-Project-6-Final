import tkinter

MW = tkinter.Tk()

MW.title('Calculator')

textBox = tkinter.Text(state = 'disabled', width = 100, height = 5)
textBox.pack(side = 'top')



numericFrame = tkinter.Frame(MW)
numericFrame.pack(side = 'top')

button1 = tkinter.Button(numericFrame, text = '1', width = 10, height = 5)
button2 = tkinter.Button(numericFrame, text = '2', width = 10, height = 5)
button3 = tkinter.Button(numericFrame, text = '3', width = 10, height = 5)
button4 = tkinter.Button(numericFrame, text = '4', width = 10, height = 5)
button5 = tkinter.Button(numericFrame, text = '5', width = 10, height = 5)
button6 = tkinter.Button(numericFrame, text = '6', width = 10, height = 5)
button7 = tkinter.Button(numericFrame, text = '7', width = 10, height = 5)
button8 = tkinter.Button(numericFrame, text = '8', width = 10, height = 5)
button9 = tkinter.Button(numericFrame, text = '9', width = 10, height = 5)
button0 = tkinter.Button(numericFrame, text = '0', width = 10, height = 5)

button1.grid(row = 0, column = 0)
button2.grid(row = 0, column = 1)
button3.grid(row = 0, column = 2)
button4.grid(row = 1, column = 0)
button5.grid(row = 1, column = 1)
button6.grid(row = 1, column = 2)
button7.grid(row = 2, column = 0)
button8.grid(row = 2, column = 1)
button9.grid(row = 2, column = 2)
button0.grid(row = 3, column = 1)

operatorFrame = tkinter.Frame(MW)
operatorFrame.pack(side = 'top')

buttonPlus = tkinter.Button(operatorFrame, text = '+', width = 10, height = 5)
buttonMinus = tkinter.Button(operatorFrame, text = '-', width = 10, height = 5)
buttonMulti = tkinter.Button(operatorFrame, text = '*', width = 10, height = 5)
buttonDivi = tkinter.Button(operatorFrame, text = '/', width = 10, height = 5)

buttonPlus.grid(row = 0, column = 0)
buttonMinus.grid(row = 0, column = 1)
buttonMulti.grid(row = 0, column = 2)
buttonDivi.grid(row = 0, column = 3)

MW.mainloop()