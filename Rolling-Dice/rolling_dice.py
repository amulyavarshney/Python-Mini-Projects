import tkinter as tk
from PIL import Image, ImageTk
import random

#main window
root = tk.Tk()
root.geometry("400x400")
root.title('Roll the dice')

#adding label into the frame
line = tk.Label(root, text='')
line.pack()

#adding label with different font and formatting
header = tk.Label(root, text="Hello!!", fg='light green', bg='dark green', font='Calibri 16 bold italic')
header.pack()

#images
img1 = 'rolling dice/1.gif'
img2 = 'rolling dice/2.gif'
img3 = 'rolling dice/3.gif'
img4 = 'rolling dice/4.gif'
img5 = 'rolling dice/5.gif'
img6 = 'rolling dice/6.gif'
dice = [img1, img2, img3, img4, img5, img6]
#simulating the dice with random random no. & generating images
img = ImageTk.PhotoImage(Image.open(random.choice(dice)))

#construct a label widget for image
label = tk.Label(root, image=img)
label.image = img
label.pack(expand=True)

#function activated by the button
def rolling():
    img = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    #update image
    label.configure(image=img)
    #keep a reference
    label.image = img

#adding button to activate function
button = tk.Button(root, text='Roll', fg='blue', font='Calibri 16 bold', command=rolling)
button.pack(expand=True)

root.mainloop()