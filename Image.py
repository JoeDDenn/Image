# import tkinter and open cv
from tkinter import *
from tkinter import filedialog
import numpy as np
import cv2
from PIL import Image, ImageTk

# create a window
window = Tk()

# create a canvas
canvas = Canvas(window, width=500, height=400)
canvas.pack(side=TOP, fill=Y, expand=YES)

# add button to the center of the window to browse file system and select image


def browseImage():
    global img
    filename = filedialog.askopenfilename(
        initialdir="/", title="Select A File", filetype=(("png files", "*.png"), ("jpeg files", "*.jpg"), ("all files", "*.*")))
    img = cv2.imread(filename)
    img = Image.fromarray(img)
    img = ImageTk.PhotoImage(img)
    canvas.create_image(20, 20, anchor=NW, image=img)


button = Button(window, text="Browse Image",
                command=lambda: browseImage())
button.pack(side=TOP, fill=Y, expand=YES)

# add button to add smoothing filter and dispaly image in the same window


def addSmoothingFilter():
    global img
    filename = filedialog.askopenfilename(
        initialdir="/", title="Select A File", filetype=(("png files", "*.png"), ("jpeg files", "*.jpg"), ("all files", "*.*")))
    img = cv2.imread(filename)
    img = cv2.GaussianBlur(img, (5, 5), 500)
    cv2.imshow("Image", img)


button = Button(window, text="Add Smoothing Filter",
                command=lambda: addSmoothingFilter())
button.pack(side=TOP, fill=Y, expand=YES)


# add button to add sobel filter and dispaly image in the same window
def addSobelFilter():
    global img
    filename = filedialog.askopenfilename(
        initialdir="/", title="Select A File", filetype=(("png files", "*.png"), ("jpeg files", "*.jpg"), ("all files", "*.*")))
    img = cv2.imread(filename)
    img = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=7)
    cv2.imshow("Sobel Filter", img)


button = Button(window, text="Add Sobel Filter",
                command=lambda: addSobelFilter())
button.pack(side=TOP, fill=Y, expand=YES)

# add button to add laplacian filter and dispaly image in the same window


def addLaplacianFilter():
    global img
    filename = filedialog.askopenfilename(
        initialdir="/", title="Select A File", filetype=(("png files", "*.png"), ("jpeg files", "*.jpg"), ("all files", "*.*")))
    img = cv2.imread(filename)
    img = cv2.Laplacian(img, cv2.CV_64F)
    cv2.imshow("Laplacian Filter", img)


button = Button(window, text="Add Laplacian Filter",
                command=lambda: addLaplacianFilter())
button.pack(side=BOTTOM, fill=Y, expand=YES)


# run the window loop
window.mainloop()
