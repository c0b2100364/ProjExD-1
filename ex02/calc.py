import tkinter as tk
import tkinter.messagebox as tkm

def btn_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"[{txt}]ボタンが押されました")

root = tk.Tk()
root.title("電卓")
root.geometry("300x500")

r, c = 0, 0
for i, num in enumerate(range(9,-1, -1), 1):
    btn = tk.Button(root, text=f"{num}", font=("", 30), width=4, height=2)
    btn.bind("<1>", btn_click)
    btn.grid(row=r, column=c)
    c += 1
    if i%3 == 0:
        r += 1
        c = 0
        
root.mainloop()