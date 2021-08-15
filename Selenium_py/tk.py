
import tkinter
r = tkinter.Tk()
r.geometry("0x0+1600+200")
print(r.winfo_screenwidth())
print(r.winfo_screenheight())
r.protocol("WM_DELETE_WINDOW", lambda: sys.exit(0));



