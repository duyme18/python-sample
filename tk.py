# Khai báo module tkinter
from tkinter import *
from tkinter.ttk import *

# Tạo cửa sổ chính cho giao diện
root = Tk()

# Đặt tiêu đề cho cửa sổ chính
root.title("First_Program")

# Tạo text “Hello World !” , đây là kết quả sẽ in ra
label = Label(root, text="Hello World !").pack()

# Sử dụng phương thức để cửa sổ chính giao diện hiển thị ra màn hình
root.mainloop()