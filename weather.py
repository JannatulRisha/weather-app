from tkinter import *


win = Tk()
win.title("Wscube Tech")
win.config(bg = "blue")
win.geometry("500*570")

name_label = label(win,text="Wscube Weather App",
                   font=("Time New Roman",30,"bold"))
name_label.place(x=25,y=50,height=50,width=450)

list_name =["Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu","Lakshadweep","National Capital Territory of Delhi","Puducherry"]

com =ttk.Combobox(win,text="Wscube Weather App",values=list_name,
                  font=("Time New Roman",20,"bold"))

com_label.place(x=25,y=120,height=50,width=450)

done_button = Button(win,text="Done",
                  font=("Time New Roman",20,"bold"))

done_button.place=(y=190,height=50,width=100,x=200)


w_label = label(win,text="Weather Climate",
                   font=("Time New Roman",20))
w_label.place(x=25,y=260,height=50,width=210)

w_label1= label(win,text="t",
                   font=("Time New Roman",20))
w_label1.place(x=250,y=260,height=50,width=210)


wb_label = label(win,text="Weather Description",
                   font=("Time New Roman",17))
wb_label.place(x=250,y=330,height=50,width=210)

wb_label1= label(win,text="",
                   font=("Time New Roman",17))
wb_label1.place(x=25,y=330,height=50,width=210)


temp_label = label(win,text="Temperature",
                   font=("Time New Roman",20))
temp_label.place(x=25,y=400,height=50,width=210)

temp_label1 = label(win,text="",
                   font=("Time New Roman",20))
temp_label1.place(x=250,y=400,height=50,width=210)


per_label = label(win,text="Pressure",
                   font=("Time New Roman",20))
per_label.place(x=25,y=470,height=50,width=210)

per_label1 = label(win,text="",
                   font=("Time New Roman",20))
per_label1.place(x=250,y=470,height=50,width=210)




win.mainloop()



