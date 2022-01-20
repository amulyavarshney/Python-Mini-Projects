#cartoonify.py
import sys
import os
import cv2 #for image preprocessing
import numpy as np #to store image data
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import easygui #for very simple and easy GUI programming
import imageio #to read/write image stored at a path

""" fileopenbox opens the box to choose file and help us store file path as string"""
def upload():
    ImagePath = easygui.fileopenbox()
    cartoonify(ImagePath)

def cartoonify(ImagePath):
    img = cv2.imread(ImagePath)
    if img is None:
        print("Can't find Image. Choose image file.")
        sys.exit()

    img_copy = img
    # width, height = smooth_gray.shape[:2]
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # resize = cv2.resize(img, (960, 540))
    plt.imshow(img, cmap='gray')

    #converting img to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    smooth_gray = cv2.medianBlur(gray, 5)
    plt.imshow(smooth_gray, cmap='gray')

    #retrieving the edges for cartoon effect
    #using threshold technique
    edged_img = cv2.adaptiveThreshold(smooth_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    plt.imshow(edged_img, cmap='gray')

    #applying bilateral filter to remove noise and smooth the image colors
    #keeping edges sharp as required
    color_img = cv2.bilateralFilter(img, 9, 300, 300)
    plt.imshow(color_img, cmap='gray')

    #masking edged image with color image
    cartoon_img = cv2.bitwise_and(color_img, color_img, mask=edged_img)
    plt.imshow(cartoon_img, cmap='gray')

    #plotting the whole transition
    imgs = [img_copy, img, gray, edged_img, color_img, cartoon_img]
    fig, axes = plt.subplots(3, 2, figsize=(8,8), subplot_kw={'xticks':[], 'yticks':[]}, gridspec_kw = dict(hspace=0.1, wspace=0.1))
    for i, ax in enumerate(axes.flat):
        ax.imshow(imgs[i], cmap='gray')
    plt.show()

def save(cartoon_img, ImagePath):
    name = 'Cartoonified_img'
    path = os.path.dirname(ImagePath)
    ext = os.path.splitext(ImagePath)[1]
    new_path = os.path.join(path1, name+ext)
    cv2.imwrite(new_path, cv2.cvtColor(cartoon_img, cv2.COLOR_RGB2BGR))
    msg = "Image saved as "+name+" at "+new_path
    tk.messagebox.showinfo(title=None, message=msg)

# ImagePath = 'PROJECTS/1.jpg'
# cartoonify(ImagePath)
if __name__ == "__main__":
    screen = tk.Tk()
    screen.geometry('400x400')
    screen.title('Cartoonify Image')
    screen.configure(background='white')
    label = Label(screen, background='#CDCDCD', font=('calibri', 20, 'bold'))

    upload = Button(screen, text="Cartoonify an Image", command=upload, padx=10, pady=5)
    upload.configure(background='#364156', foreground='white', font=('calibri', 10, 'bold'))
    upload.pack(side=TOP, pady=50)

    save = Button(screen, text="Save Cartoonified Image", command=lambda: save(cartoon_img, ImagePath), padx=30, pady=5)
    save.configure(background='#364156', foreground='white', font=('calibri', 10, 'bold'))
    save.pack(side=TOP, pady=50)

    screen.mainloop()