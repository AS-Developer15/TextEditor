from ttkbootstrap import *
from tkinter import *
import webbrowser
from random import choice
def newWindow():
# Sub Function Decleration

    def webAbtUs():
        webbrowser.open_new_tab("https://google.com")
        
    def helpProv():
        webbrowser.open_new_tab("https://google.com")
        
    def themeChanger():
        themeWindow= Tk()
        Label(themeWindow,text="Choose Theme".title()).pack()
        themeVal = Entry(themeWindow)
        themeVal.pack()
        strThemeVal= themeVal.get()
        def changeTheme():
            window.style.theme= strThemeVal
            window.bell()  
            themeWindow.destroy()
            
        Button(themeWindow,command=changeTheme,text="Change Theme").pack()
        themeWindow.mainloop()
    
    
    def formattingWin():

        formattingWindow= Tk()
        formattingWindow.geometry('450x300')
        Label(formattingWindow,text="Change Configuration").pack(pady=10)
        mainFrame = Frame(formattingWindow)         
        fontValFrame =  Frame(mainFrame)
        fontSizeFrame=  Frame(mainFrame)
        fontStylFrame=  Frame(mainFrame)
        
        Label(fontValFrame,text="Choose Font Face ").pack(side="left",pady=5,padx=3)
        fontVal =  Entry(fontValFrame)
        fontVal.pack(side= "left",padx=3)
        fontValFrame.pack()
               
        Label(fontSizeFrame,text="Choose Font Size  ").pack(side="left",pady=5,padx=3)
        fontSizeVal =  Entry(fontSizeFrame)
        fontSizeVal.pack(side= "left",padx=3)
        fontSizeFrame.pack()
        
        Label(fontStylFrame,text="Choose Font Style").pack(side="left",pady=5,padx=3)
        fontStyleVal=  Entry(fontStylFrame)
        fontStyleVal.pack(side= "left",padx=3)        
        fontStylFrame.pack()
       
        def changeConfig():
       
            fontFaceValue = str(fontVal.get()).lower()
            fontSizeValue = int(fontSizeVal.get())
            fontWeightValue= str(fontStyleVal.get()).lower()
        
            if fontFaceValue == "":
                fontFaceValue="calibri"
           
            if str(fontSizeValue)=="":
                fontSizeValue=12

            if fontWeightValue == "":
                fontWeightValue="normal"
                
            fontConfig= font.Font(family=fontFaceValue,size=fontSizeValue,weight=fontWeightValue)
            textEntryWindow.config(font=fontConfig)    
            formattingWindow.destroy()
        mainFrame.pack()         
        Button(formattingWindow,text="Change Configuration",command=changeConfig).pack(pady=10)
        formattingWindow.mainloop()
    
    def fileSave():
        nameWindow= Tk()
        nameWindow.title("Save File")
        
        Label(nameWindow,text="Choose File Name").pack()
        fileSavingFrame = Frame(nameWindow)
        fileName = Entry(fileSavingFrame)
        fileName.pack(side="left")
        fileSavingFrame.pack() 
        def saveFile():
            savingName = fileName.get()   
            data = textEntryWindow.get(index1=1.0,index2="end")
            with open(f"./{savingName}.txt","w") as file:
                file.write(data)    
        Button(fileSavingFrame,text="Save",command=saveFile).pack(side="left")
        nameWindow.mainloop()

    def exitEditor():
        window.destroy()

# Program Window Configuration

    themes=['cosmo', 'flatly', 'litera', 'minty', 'lumen', 'sandstone', 'yeti', 'pulse', 'united', 'morph', 'journal', 'darkly', 'superhero', 'solar', 'cyborg', 'vapor', 'simplex', 'cerculean']
    window = Window("Text Editor",themename=choice(themes))
    window.maxsize(window.winfo_screenwidth(),window.winfo_screenheight())
    print(themes)


# File Menu
    menuBar = Menu(window)
    fileMenu =Menu(menuBar,tearoff=0)
    fileMenu.add_command(label="New",command=newWindow)
    fileMenu.add_command(label="Save",command=fileSave)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit",command=exitEditor)
    menuBar.add_cascade(label="File",menu=fileMenu)


# Editing Menu
    editingMenu= Menu(menuBar,tearoff=0)
    editingMenu.add_command(label="Edit",command=formattingWin)
    editingMenu.add_command(label="BackGround",command=themeChanger)
    menuBar.add_cascade(label="Edit",menu=editingMenu)


# Help Menu
    helpMenu = Menu(menuBar,tearoff=0 )
    helpMenu.add_command(label="About Us",command=webAbtUs)
    helpMenu.add_command(label="Developer",command=helpProv) 
    menuBar.add_cascade(menu=helpMenu,label="Help")
    window.config(menu=menuBar)


# Actual Window
    textEntryWindow = ScrolledText(window,background="white",width=200,height=25,font=('Algerian',12))
    textEntryWindow.pack(fill= tk.BOTH , expand=True)
    window.mainloop()
       
newWindow()