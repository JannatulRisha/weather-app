from tkinter import*
from tkinter import ttk

import requests

def data_get():
 
   city = city_name.get()
   data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=f49434163c2a98a429a252bd2eb4e0ff").json()


   w_label1.config(text=data["weather"][0]["main"])

   wb_label1.config(text=data["weather"][0]["description"])

   temp_label1.config(text=str(int(data["main"]["temp"]-273.15)))

   per_label1.config(text=data["main"]["pressure"])


win = Tk()
win.title("Weather APP")
win.config(bg = "#404040")
win.geometry("500x600")
name_label = Label(win,text="Weather App",justify="center",bg="#404040", border=0, fg="white",
                   font=("Time New Roman", 30 , "bold"))
name_label.place(x=25,y=50,height=50,width=450)

city_name = StringVar()
list_name = ["Barisal","Chittagong","Dhaka","Khulna","Rajshahi","Rajshahi","Sylhet"]
com = ttk.Combobox(win,text="Weather App",values=list_name,
                   font=("Time New Roman", 30 , "bold"),textvar=city_name)
com.place(x=25,y=120,height=50,width=450)



w_label = Label(win,text="Weather Climate",
                   font=("Time New Roman", 15))
w_label.place(x=25,y=260,height=50,width=210)

w_label1 = Label(win,text="",
                   font=("Time New Roman", 15))
w_label1.place(x=250,y=260,height=50,width=210)



wb_label = Label(win,text="Weather Description",
                   font=("Time New Roman", 15))
wb_label.place(x=25,y=330,height=50,width=210)

wb_label1 = Label(win,text=" ",
                   font=("Time New Roman", 15))
wb_label1.place(x=250,y=330,height=50,width=210)



temp_label = Label(win,text="Temperature",
                   font=("Time New Roman", 15))
temp_label.place(x=25,y=400,height=50,width=210)
temp_label1 = Label(win,text="",
                   font=("Time New Roman", 15))
temp_label1.place(x=250,y=400,height=50,width=210)


per_label = Label(win,text="Pressure",
                   font=("Time New Roman", 15))
per_label.place(x=25,y=470,height=50,width=210)
per_label1 = Label(win,text="",
                   font=("Time New Roman", 15))
per_label1.place(x=250,y=470,height=50,width=210)

done_button = Button(win,text="Done",
                   font=("Time New Roman", 20 , "bold"),command=data_get)
done_button.place(x=200,y=190,height=50,width=100)



win.mainloop()
