import customtkinter
from customtkinter import *
from paths import *

#Set Up Mod Menu
app = customtkinter.CTk()
app.title("Mod Menu By The_Sushi")
app.geometry("400x600")
app.grid_columnconfigure((0), weight=1)

#Controls Blood Gems Values
def button_blood_gems():
    blood_gems = getPointerAddress(game_offset, blood_gems_offsets)
    blood_gems_amount = 1000 + pm.read_double(blood_gems)
    pm.write_double(blood_gems, blood_gems_amount)
    label_blood_gems.configure(text=("Blood Gems Amount: " + str(pm.read_double(blood_gems))))

#Controls Coins Values
def button_coins():
    coins = getPointerAddress(game_offset, coins_offsets)
    try:
     coins_amounts = 999.0
     pm.write_int(coins, coins_amounts)
     label_coins.configure(text=("Coins Amount: " + str(pm.read_double(coins))))
    except:
     coins_amounts = 999.0
     pm.write_double(coins, coins_amounts)
     label_coins.configure(text=("Coins Amount: " + str(pm.read_double(coins))))


#Sets Blood Gems And Coins Value's To Zero
def button_reset_currency():
    blood_gems = getPointerAddress(game_offset, blood_gems_offsets)
    blood_gems_amount = 0.0
    pm.write_double(blood_gems, blood_gems_amount)
    label_blood_gems.configure(text=("Blood Gems Amount: " + str(pm.read_double(blood_gems))))

    coins = getPointerAddress(game_offset, coins_offsets)
    try:
     coins_amounts = 0.0
     pm.write_int(coins, coins_amounts)
     label_coins.configure(text=("Coins Amount: " + str(pm.read_double(coins))))
    except:
     coins_amounts = 0.0
     pm.write_double(coins, coins_amounts)
     label_coins.configure(text=("Coins Amount: " + str(pm.read_double(coins))))


#Sets Health To 999
def button_heal_me():
    health = getPointerAddress(game_offset, health_offsets)
    health_amount = 999.0
    pm.write_double(health, health_amount)


#Controls Player Speed
def slider_player(value):
    player_speed = getPointerAddress(game_offset, player_speed_offsets)
    player_speed_amount = slider_player_speed.get()
    pm.write_double(player_speed, player_speed_amount)
    label_player_speed.configure(text=("Player Speed: " + str(pm.read_double(player_speed))))

#Controls Arrow Speed
def slider_arrow(value):
    arrow_speed = getPointerAddress(game_offset, arrow_speed_offsets)
    arrow_speed_amount = slider_arrow_speed.get()
    pm.write_double(arrow_speed, arrow_speed_amount)
    label_arrow_speed.configure(text=("Arrow Speed: " + str(pm.read_double(arrow_speed))))

#Controls Instant Kill
def damage_event():
    if damage_var.get() == str(1):
     damage = getPointerAddress(game_offset, damage_offsets)
     damage_amount = 99999.0
     pm.write_double(damage, damage_amount)
    else:
     damage = getPointerAddress(game_offset, damage_offsets)
     damage_amount = 3.5
     pm.write_double(damage, damage_amount)


#Controls Infinite Ammo
def ammo_event():
    if ammo_var.get() == str(1):
     ammo = getPointerAddress(game_offset, ammo_offsets)
     ammo_amount = 99999.0
     pm.write_double(ammo, ammo_amount)
     app.after(100, ammo_event)


#Controls Machine Gun
def machine_gun_event():
    if machine_gun_var.get() == str(1):
     machine_gun = getPointerAddress(game_offset, machine_gun_offsets)
     machine_gun_amount = 10.0
     pm.write_double(machine_gun, machine_gun_amount)
    else:
     machine_gun = getPointerAddress(game_offset, machine_gun_offsets)
     machine_gun_amount = 1.0
     pm.write_double(machine_gun, machine_gun_amount)


#Controls God Mode
def god_mode_event():
    if god_mode_var.get() == str(1):
     health = getPointerAddress(game_offset, health_offsets)
     health_amount = 999.0
     pm.write_double(health, health_amount)
     app.after(500, god_mode_event)

#Aborts Everything And Sets All To Default
def button_abort():

   #Heal The Player
   health = getPointerAddress(game_offset, health_offsets)
   health_amount = 999.0
   pm.write_double(health, health_amount)  

   #Set Player Speed To 1.0
   player_speed = getPointerAddress(game_offset, player_speed_offsets)
   player_speed_amount = 1.0
   pm.write_double(player_speed, player_speed_amount)
   label_player_speed.configure(text=("Player Speed: " + str(pm.read_double(player_speed))))

   #Sets Arrow Speed To 350
   arrow_speed = getPointerAddress(game_offset, arrow_speed_offsets)
   arrow_speed_amount = 350.0
   pm.write_double(arrow_speed, arrow_speed_amount)
   label_arrow_speed.configure(text=("Arrow Speed: " + str(pm.read_double(arrow_speed))))

   #Turns Off All Toggles
   damage_checkbox.deselect()
   damage_event()
   ammo_checkbox.deselect()
   ammo_event()
   machine_gun_checkbox.deselect()
   machine_gun_event()
   god_mode_checkbox.deselect()
   god_mode_event()

   #Set Blood Gems And Coins To Zero
   blood_gems = getPointerAddress(game_offset, blood_gems_offsets)
   blood_gems_amount = 0.0
   pm.write_double(blood_gems, blood_gems_amount)
   label_blood_gems.configure(text=("Blood Gems Amount: " + str(pm.read_double(blood_gems))))

   coins = getPointerAddress(game_offset, coins_offsets)
   try:
     coins_amounts = 0.0
     pm.write_int(coins, coins_amounts)
     label_coins.configure(text=("Coins Amount: " + str(pm.read_double(coins))))
   except:
     coins_amounts = 0.0
     pm.write_double(coins, coins_amounts)
     label_coins.configure(text=("Coins Amount: " + str(pm.read_double(coins))))



#Makes Blood Gems Counter And Button
label_blood_gems = customtkinter.CTkLabel(app, text=("Blood Gems Amount: " + str(pm.read_double(blood_gems))), fg_color="transparent")
label_blood_gems.grid(row=0, column=1, padx=20, pady=20, sticky="e", columnspan=1)
button_blood_gems = customtkinter.CTkButton(app, text="Add Blood Gems +1,000", command=button_blood_gems)
button_blood_gems.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

#Makes Coins Counter And Button
label_coins = customtkinter.CTkLabel(app, text=("Coins Amount: " + str(pm.read_double(coins))), fg_color="transparent")
label_coins.grid(row=1, column=1, padx=20, pady=20, sticky="e", columnspan=1)
button_coins = customtkinter.CTkButton(app, text="Max Coins To 999", command=button_coins)
button_coins.grid(row=1, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

#Makes Rest Currency Button
button_reset_currency = customtkinter.CTkButton(app, text="Reset Currency To Zero", command=button_reset_currency)
button_reset_currency.grid(row=2, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

#Makes Heal Me Button
button_heal_me = customtkinter.CTkButton(app, text="Heal Me", command = button_heal_me)
button_heal_me.grid(row=3, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

#Makes Slider For Player Speed
slider_player_speed = customtkinter.CTkSlider(app, from_=1, to=50, number_of_steps = 49, command=slider_player)
slider_player_speed.grid(row=4, column=0, padx=20, pady=20, sticky="ew", columnspan=1)
label_player_speed = customtkinter.CTkLabel(app, text=("Player Speed: " + str(pm.read_double(player_speed))), fg_color="transparent")
label_player_speed.grid(row=4, column=1, padx=20, pady=20, sticky="e", columnspan=1)

#Makes Slider For Arrow Speed
slider_arrow_speed = customtkinter.CTkSlider(app, from_=0, to=1000, number_of_steps = 1000, command=slider_arrow)
slider_arrow_speed.grid(row=5, column=0, padx=20, pady=20, sticky="ew", columnspan=1)
label_arrow_speed = customtkinter.CTkLabel(app, text=("Arrow Speed: " + str(pm.read_double(arrow_speed))), fg_color="transparent")
label_arrow_speed.grid(row=5, column=1, padx=20, pady=20, sticky="e", columnspan=1)

#Makes Toggle For Instant Kill
damage_var = customtkinter.StringVar(value="off")
damage_checkbox = customtkinter.CTkCheckBox(app, text="Instant Kill", command=damage_event, variable=damage_var)
damage_checkbox.grid(row=6, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

#Makes Toggle For Infinite Ammo
ammo_var = customtkinter.StringVar(value="off")
ammo_checkbox = customtkinter.CTkCheckBox(app, text="Infinite Ammo", command=ammo_event, variable=ammo_var)
ammo_checkbox.grid(row=6, column=1, padx=20, pady=20, sticky="ew", columnspan=1)

#Makes Toggle For Machine Gun
machine_gun_var = customtkinter.StringVar(value="off")
machine_gun_checkbox = customtkinter.CTkCheckBox(app, text="Machine Gun", command=machine_gun_event, variable=machine_gun_var)
machine_gun_checkbox.grid(row=7, column=0, padx=20, pady=20, sticky="ew", columnspan=1)

#Makes Toggle For God Mode
god_mode_var = customtkinter.StringVar(value="off")
god_mode_checkbox = customtkinter.CTkCheckBox(app, text="Gode Mode", command=god_mode_event, variable=god_mode_var)
god_mode_checkbox.grid(row=7, column=1, padx=20, pady=20, sticky="ew", columnspan=1)

#Makes An Abort Button
button_abort = customtkinter.CTkButton(app, text="Abort!", command = button_abort)
button_abort.grid(row=8, column=0, padx=20, pady=20, sticky="ew", columnspan=2)

#Keeps Mod Menu Open
app.mainloop()
