import customtkinter
from customtkinter import *
from paths import *

app = customtkinter.CTk()
app.title("Mod Menu By The_Sushi")
app.geometry("400x400")
app.grid_columnconfigure((0), weight=1)


def button_blood_gems():
    blood_gems = getPointerAddress(blood_gems_address, blood_gems_offsets)
    blood_gems_amount = 1000 + pm.read_double(blood_gems)
    pm.write_double(blood_gems, blood_gems_amount)
    label_blood_gems.configure(text=("Blood Gems Amount: " + str(pm.read_double(blood_gems))))

def button_coins():
    coins = getPointerAddress(coins_address, coins_offsets)
    try:
     coins_amounts = 999.0
     pm.write_int(coins, coins_amounts)
     label_coins.configure(text=("Coins Amount: " + str(pm.read_double(coins))))
    except:
     coins_amounts = 999.0
     pm.write_double(coins, coins_amounts)
     label_coins.configure(text=("Coins Amount: " + str(pm.read_double(coins))))

def button_reset_currency():
    blood_gems = getPointerAddress(blood_gems_address, blood_gems_offsets)
    blood_gems_amount = 0.0
    pm.write_double(blood_gems, blood_gems_amount)
    label_blood_gems.configure(text=("Blood Gems Amount: " + str(pm.read_double(blood_gems))))

    coins = getPointerAddress(coins_address, coins_offsets)
    try:
     coins_amounts = 0.0
     pm.write_int(coins, coins_amounts)
     label_coins.configure(text=("Coins Amount: " + str(pm.read_double(coins))))
    except:
     coins_amounts = 0.0
     pm.write_double(coins, coins_amounts)
     label_coins.configure(text=("Coins Amount: " + str(pm.read_double(coins))))

def button_heal_me():
    health = getPointerAddress(health_address, health_offsets)
    health_amount = 999.0
    pm.write_double(health, health_amount)

def slider_event(value):
    arrow_speed = getPointerAddress(arrow_speed_address, arrow_speed_offsets)
    arrow_speed_amount = slider_arrow_speed.get()
    pm.write_double(arrow_speed, arrow_speed_amount)
    label_arrow_speed.configure(text=("Arrow Speed: " + str(pm.read_double(arrow_speed))))



label_blood_gems = customtkinter.CTkLabel(app, text=("Blood Gems Amount: " + str(pm.read_double(blood_gems))), fg_color="transparent")
label_blood_gems.grid(row=0, column=1, padx=20, pady=20, sticky="e", columnspan=1)
button_blood_gems = customtkinter.CTkButton(app, text="Add Blood Gems +1,000", command=button_blood_gems)
button_blood_gems.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

label_coins = customtkinter.CTkLabel(app, text=("Coins Amount: " + str(pm.read_double(coins))), fg_color="transparent")
label_coins.grid(row=1, column=1, padx=20, pady=20, sticky="e", columnspan=1)
button_coins = customtkinter.CTkButton(app, text="Max Coins To 999", command=button_coins)
button_coins.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

button_reset_currency = customtkinter.CTkButton(app, text="Reset Currency To Zero", command=button_reset_currency)
button_reset_currency.grid(row=2, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

button_heal_me = customtkinter.CTkButton(app, text="Heal Me", command = button_heal_me)
button_heal_me.grid(row=3, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

slider_arrow_speed = customtkinter.CTkSlider(app, from_=0, to=1000, number_of_steps = 1000, command=slider_event)
slider_arrow_speed.grid(row=4, column=0, padx=20, pady=20, sticky="ew", columnspan=1)
label_arrow_speed = customtkinter.CTkLabel(app, text=("Arrow Speed: " + str(pm.read_double(arrow_speed))), fg_color="transparent")
label_arrow_speed.grid(row=4, column=1, padx=20, pady=20, sticky="e", columnspan=1)


app.mainloop()
