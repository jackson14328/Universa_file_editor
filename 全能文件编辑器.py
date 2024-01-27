import tkinter
from tkinter import messagebox

print('全能文件编辑器1.0   开源项目，禁止作为商用   by 二氧化碳已爆炸')

def NAME_BUTTON():
    try:
        T = open(name2.get(), 'r', encoding='utf-8')
        text.delete('1.0', 'end')
        text.insert('1.0', T.read())
        T.close()
        messagebox.showinfo("提示","文件读取成功")
    except:
        messagebox.showerror('错误','您输入的文件名:' + name2.get() + ' 不存在，可能您或某些进程删除了它，或它的格式不受支持')

def TEXT_BUTTON():
    try:
        T = open(name2.get(), 'w', encoding='utf-8')
        T.write(text.get('1.0', 'end'))
        T.close()
        messagebox.showinfo("提示","保存成功")
    except:
        messagebox.showerror('错误','您输入的文件名:' + name2.get() + ' 不存在，可能您或某些进程删除了它')

def NEW_BUTTON():
    T = open(new_text2.get(), 'w', encoding='utf-8')
    T.write('')
    T.close()
    messagebox.showinfo("提示","文件创建成功")

root = tkinter.Tk()
root.title('全能文件编辑器1.0')
root.iconbitmap('全能文件编辑器.ico')

new_help = tkinter.Label(root, text='这里输入新的文件名称(带有拓展名)，绝对路径与相对路径均支持')
new_text2 = tkinter.StringVar()
new_text = tkinter.Entry(root, textvariable=new_text2)
new = tkinter.Button(root, text='创建新的文件', command=NEW_BUTTON)
name_help = tkinter.Label(root, text='这里输入文件名称(带有拓展名)，绝对路径与相对路径均支持')
name2 = tkinter.StringVar()
name = tkinter.Entry(root, textvariable=name2)
name_button = tkinter.Button(root, text='确定', command=NAME_BUTTON)
text = tkinter.Text(root)
text_button = tkinter.Button(root, text='保存', command=TEXT_BUTTON)

new_help.pack()
new_text.pack()
new.pack()
name_help.pack()
name.pack()
name_button.pack()
text.pack()
text_button.pack()

root.mainloop()

