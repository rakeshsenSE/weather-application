import tkinter as tk
from tkinter import messagebox
from langchain_community.utilities import OpenWeatherMapAPIWrapper
from dotenv import load_dotenv


load_dotenv()

def get_weather():
    city = city_entry.get()

    if not city or city == "Enter City name":
        messagebox.showerror("Error", "please enter a valid city name!!")
        return
  
    try:
        weather_model = OpenWeatherMapAPIWrapper()
        result = weather_model.run(city)

        if "No weather information found" in result or "City not found" in result:
            messagebox.showerror("Error", "City not found! please cheak the spelling.")
            return

        result_label.config(text=result, fg='#2c3e50', justify="left")

        temp_label.config(text="")
        desc_label.config(text="")
        humidity_label.config(text="")

    except Exception as e:
      messagebox.showerror("Error", f"Failed to connect to the internet or API error.\nDetails: {e}")
root = tk.Tk()
root.title("Weather App (LangChain)")
root.geometry("450x500")
root.configure(bg="#f0f3f4")

title_label= tk.Label(root,text="Weather App", font=("Helvetica",18,"bold"),bg="#f0f3f4",fg="#34495e")
title_label.pack(pady=20)


city_entry=tk.Entry(root,font=("Helvetica",14),width=20,justify="center",bd=2,relief="groove")
city_entry.pack(pady=10)
city_entry.insert(0,"Enter City name")

search_btn=tk.Button(root,text="Search Weather",font=("Helvetica", 11, "bold"),bg="#3498db",fg="white",activebackground="#2980b9",activeforeground="white",width=15, command=get_weather)
search_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Courier", 10), bg="#ffffff", bd=1, relief="solid", padx=10, pady=10, width=50, height=30)
result_label.pack(pady=15)

temp_label=tk.Label(root,text="",bg="#f0f3f4")
temp_label.pack()
desc_label=tk.Label(root,text="",bg="#f0f3f4")
desc_label.pack()
humidity_label=tk.Label(root,text="",bg="#f0f3f4")
humidity_label.pack()


def clear_placeholder(event):
    if city_entry.get() == "Enter City name":
        city_entry.delete(0, tk.END)


city_entry.bind("<FocusIn>", clear_placeholder)


root.mainloop()




