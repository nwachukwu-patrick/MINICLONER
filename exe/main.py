import tkinter as tk
from functools import partial
from tkinter import  ttk
from pywebcopy import save_website

class OreBank(tk.Tk):

    def __init__(self):
        super(OreBank, self).__init__()
        super(OreBank, self).geometry("400x600")
        super(OreBank, self).config(bg="#6FAFE7")
        super(OreBank, self).title("MINI PYTHON CLONER")
        self.contents = tk.StringVar()

        # username label and text entry box
        self.usernameLabel = tk.Label(self,width=300, pady=10, text="Output folder",bg="#6FAFE7").pack(side="top")
        self.username = tk.StringVar()
        self.usernameEntry = tk.Entry(self,width=50, textvariable=self.username).pack(side="top")

        # project name label and text entry box
        self.projectnameLabel = tk.Label(self, width=300, pady=10, text="Project Name", bg="#6FAFE7").pack(side="top")
        self.projectname = tk.StringVar()
        self.projectnameEntry = tk.Entry(self, width=50, textvariable=self.projectname).pack(side="top")

        # password label and password entry box
        self.passwordLabel = tk.Label(self, text="Website Url To Clone",bg="#6FAFE7").pack(side="top")
        self.password = tk.StringVar()
        self.passwordEntry = tk.Entry(self,width=50, textvariable=self.password).pack(side="top")

        self.validateLogin = partial(self.GetText, self.username, self.password,self.projectname)
        self.loginButton = tk.Button(self, text="Clone",foreground="#fff", background="blue",width=20,command=self.validateLogin).pack(pady=10)



    def quitbtn(self):
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.destroy)
        self.quit.pack(side="bottom")
    def GetText(self,username,password,projectname):
        url = password.get()
        outputfolder =   username.get()
        projectname = projectname.get()
        tk.Label(self, text=f'Cloning Started...\n\n url to clone: {url} \n\n '
                            f'Output Directory:  {outputfolder}\n\nProject Name:  {projectname} \n\n', font=30,
                  pady=10).pack(side="top")
        try:
            save_website(
            url=url,
            project_folder=outputfolder,
            project_name=projectname,
            bypass_robots=True,
            debug=False,
            open_in_browser=True,
            delay=None,
            threaded=False,
            )
        except:
           pass
        tk.Label(self, text="Cloned...",font=30, pady=10,padx=10).pack(side="top")

    # def
    def start(self):
        # self.FolderName()
        # self.Url()
        # self.Clonebtn()
        self.quitbtn()
        super(OreBank, self).mainloop()



bank = OreBank()
bank.start()

# def validateLogin(username, password):
# 	print("username entered :", username.get())
# 	print("password entered :", password.get())
# 	return
#
# #window
# tkWindow = tk.Tk()
# tkWindow.geometry('400x150')
# tkWindow.title('Tkinter Login Form - pythonexamples.org')
#
# #username label and text entry box
# usernameLabel = tk.Label(tkWindow, text="User Name").grid(row=0, column=0)
# username = tk.StringVar()
# usernameEntry = tk.Entry(tkWindow, textvariable=username).grid(row=0, column=1)
#
# #password label and password entry box
# passwordLabel = tk.Label(tkWindow, text="Password").grid(row=1, column=0)
# password = tk.StringVar()
# passwordEntry = tk.Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)
#
# validateLogin = partial(validateLogin, username, password)
#
# #login button
# loginButton = tk.Button(tkWindow, text="Login", command=validateLogin).grid(row=4, column=0)
#
# tkWindow.mainloop()


# from pywebcopy import save_website
# save_website(
# url="http://localhost:800/",
# project_folder="C:\\Users\\Patrick\\Desktop\\CHIBIKE\\test\\",
# project_name="localhost800",
# bypass_robots=True,
# debug=True,
# open_in_browser=True,
# delay=None,
# threaded=False,
# )