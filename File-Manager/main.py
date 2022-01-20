import os
import tkinter as tk
import easygui
import shutil

# open a file box window when we want to select a file
def open_window():
    path = easygui.fileopenbox()
    return path

# open file function
def open_file():
    file_path = easygui.fileopenbox()
    try:
        os.startfile(file_path)
    except:
        tk.messagebox.showinfo("Confirmation", "File not found!")

# open folder function
def open_folder():
    folder_path = easygui.fileopenbox()
    try:
        os.startfile(folder_path)
    except:
        # tk.messagebox.showinfo("Confirmation", "Folder not found!")
        easygui.exceptionbox()

# copy file function
def copy_file():
    source_file = easygui.fileopenbox()
    destination_path = tk.filedialog.askdirectory()
    shutil.copy(source_file, destination_path)
    tk.messagebox.showinfo('Confirmation', "File Copied Sucessfully!")

# delete file function
def delete_file():
    del_file = open_window()
    if os.path.exists(del_file):
        os.remove(del_file)             
    else:
        tk.messagebox.showinfo('confirmation', "File not found !")

# rename file function
def rename_file():
    chosenFile = open_window()
    path1 = os.path.dirname(chosenFile)
    extension=os.path.splitext(chosenFile)[1]
    print("Enter new name for the chosen file")
    newName=input()
    path = os.path.join(path1, newName+extension)
    print(path)
    os.rename(chosenFile,path) 
    tk.messagebox.showinfo('confirmation', "File Renamed !")

# move file function
def move_file():
    source = open_window()
    destination = tk.filedialog.askdirectory()
    if(source==destination):
        tk.messagebox.showinfo('confirmation', "Source and destination are same")
    else:
        shutil.move(source, destination)  
        tk.messagebox.showinfo('confirmation', "File Moved !")

# function to make a new folder
def make_folder():
    newFolderPath =  tk.filedialog.askdirectory()
    print("Enter name of new folder")

    newFolder=input()
    path = os.path.join(newFolderPath, newFolder)  

    os.mkdir(path)
    tk.messagebox.showinfo('confirmation', "Folder created !")

# function to remove a folder
def remove_folder():
    delFolder =  tk.filedialog.askdirectory()
    os.rmdir(delFolder)
    tk.messagebox.showinfo('confirmation', "Folder Deleted !")

# function to list all the files in folder
def list_files():
    folderList =  tk.filedialog.askdirectory()
    sortlist=sorted(os.listdir(folderList))       
    i=0
    print("Files in ", folderList, "folder are:")
    while(i<len(sortlist)):
        print(sortlist[i]+'\n')
        i+=1

root = tk.Tk()
# creating a canvas to insert image
canv = tk.Canvas(root, width=500, height=420, bg='white')
canv.grid(row=0, column=2)

# img = ImageTk.PhotoImage(Image.open("D:\\learn\\TechVidvan\\TechVidvan.png"))  
# canv.create_image(20, 20, anchor=NW, image=img)

# creating label and buttons to perform operations
tk.Label(root, text="My File Manager", font=("Helvetica", 16), fg="green").grid(row = 5, column = 2)

tk.Button(root, text = "Open a File", command = open_file).grid(row=15, column =2)

tk.Button(root, text = "Copy a File", command = copy_file).grid(row = 25, column = 2)

tk.Button(root, text = "Delete a File", command = delete_file).grid(row = 35, column = 2)

tk.Button(root, text = "Rename a File", command = rename_file).grid(row = 45, column = 2)

tk.Button(root, text = "Move a File", command = move_file).grid(row = 55, column =2)

tk.Button(root, text = "Make a Folder", command = make_folder).grid(row = 75, column = 2)

tk.Button(root, text = "Remove a Folder", command = remove_folder).grid(row = 65, column =2)

tk.Button(root, text = "List all Files in Directory", command = list_files).grid(row = 85,column = 2)

root.mainloop()