import tkinter as tk

#creating window
window = tk.Tk()
window.title("the tkinter window")

# create the label
label = tk.Label(window, text = "Welcome to the tkinter window")
label.pack()

# create the button
button = tk.Button(window, text = "Click here!", command = lambda: print("Button clicked!"))
button.pack()

#start eventloop
window.mainloop()