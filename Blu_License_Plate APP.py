import numpy as np
import matplotlib.pyplot as plt
import cv2
from tkinter import *
from tkinter import filedialog, messagebox
import os

root=Tk()
root.title("Blur_License_Plate APP")
root.geometry("500x250") 
root.resizable(0,0)
root.configure(bg='black')


def open_img():
    global my_image
    root.filename=filedialog.askopenfilename(initialdir='/media/abrar/DATA/projects',title = "Select a File", filetypes = (("all files", "*.*"),("Text files", "*.txt*")))
    my_label=Label(root,text=root.filename).pack()
    my_image=cv2.imread(root.filename)
    
    plate_cascade=cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
    plate_img=my_image.copy()
    roi=my_image.copy()
    plate_rects=plate_cascade.detectMultiScale(plate_img,scaleFactor=1.3,minNeighbors=3)
    
    for (x,y,w,h) in plate_rects:
        roi=roi[y:y+h,x:x+w]
        blurred_roi=cv2.medianBlur(roi,7)
        
        plate_img[y:y+h,x:x+w]=blurred_roi
    
    result=plate_img
    path = '/media/abrar/DATA/projects/License plate blur/output'
    cv2.imwrite(os.path.join(path , 'blurred.jpg'),result)
    messagebox.showinfo(title='Car ', message='Check Output folder')
    
my_btn=Button(root,text='Browse:',command=open_img,height=5,width=15,font=('Comic Sans MS',25,'bold'),bg='DarkOrchid3',fg='Yellow').pack()

root.mainloop()