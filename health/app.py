import joblib
import streamlit as st
import pandas as pd
from tkinter import *
data = pd.read_csv('insurance.csv')

model = joblib.load('model_joblib_gr')
master = Tk()

def show_entry():
    p1 = float(e1.get())
    p2 = float(e2.get())
    p3 = float(e3.get())
    p4 = float(e4.get())
    p5 = float(e5.get())
    p6 = float(e6.get())
    result = model.predict([[p1,p2,p3,p4,p5,p6]])
    Label(master, text = "Insurance Cost").grid(row = 7)
    Label(master, text = result).grid(row=8)
master.title("insurance cost prediction")
label = Label(master,text = "insurance cost prediction",bg = "black",fg = "white").grid(row=0,columnspan=2)
Label(master, text = "Enter your age").grid(row=1)
Label(master, text = "male or female [1/0]").grid(row=2)
Label(master, text = "Enter your Bmi").grid(row=3)
Label(master, text = "enter no of children").grid(row=4)
Label(master, text = "smoker yes or no [1/0]").grid(row=5)
Label(master, text = "Region [1-4]").grid(row=6)


e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e6 = Entry(master)
    
        
e1.grid(row=1,column=1)
e2.grid(row=2,column=1)
e3.grid(row=3,column=1)
e4.grid(row=4,column=1)
e5.grid(row=5,column=1)
e6.grid(row=6,column=1)
        
Button(master,text ="Predict",command = show_entry).grid()
mainloop()