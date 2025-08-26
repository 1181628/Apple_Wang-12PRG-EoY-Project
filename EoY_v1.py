import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import datetime
from datetime import timedelta

root = tk.Tk()
root.title("")
root.geometry("520x750+300+90")

data = {}
user_catalogue = {}
existed_catalogue = {}
frame = {}

def upload_catalogue():
    with open('user_catalogue_file.txt','r')as usercatalogue_file:
        for each in usercatalogue_file.readlines():
            if each:
                name, charatistic = each.strip().split(':', 1)
                user_catalogue[name.strip()] = [item.strip() for item in charatistic.split(',')]
    with open('existed_catalogue.txt','r')as existedcatalogue_file:
        for each in existedcatalogue_file.readlines():
            if each:
                name, charatistic = each.strip().split(':', 1)
                existed_catalogue[name.strip()] = [item.strip() for item in charatistic.split(',')]

def view_user_catalogue():
    with open('grocery_list.txt','r')as grocery_listFile:

def laybel_user_catalogue():
    frames["catalogue"] = tk.Frame(root, bg="grey")
    frames["catalogue"].pack()
    frames["catalogue"].grid_propagate(False)

upload_catalogue()
user_catalogue_button = tk.Button(root, text="View your card catalogue", command=view_user_catalogue)
exist_catalogue_button = tk.Button(root, text="View existing card's catalogue", command=view_existed_catalogue)
manage_catalogue_button = tk.Button(root, text="Manage your card catalogue", command=manage_user_catalogue)
user_catalogue_button.pack()
exist_catalogue_button.pack()
manage_catalogue_button.pack()

#New changes
