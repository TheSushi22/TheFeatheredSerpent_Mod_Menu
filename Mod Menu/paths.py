import pymem
from pymem import *
from pymem.ptypes import RemotePointer

#Searches For Game By Name
pm = Pymem("TheFeatheredSerpent_V4.5.exe")

#Game Offset
game_offset = pm.base_address + 0x023D2BC0

#Offsets
blood_gems_offsets = offsets=[0x1E0, 0x58, 0x20, 0x70, 0x58, 0x20, 0xB90]

coins_offsets = offsets=[0x1E0, 0x58, 0x20, 0x70, 0x58, 0x20, 0xBF0]

health_offsets = offsets=[0x1E0, 0x58, 0x20, 0x70, 0x58, 0x20, 0x230]

damage_offsets = offsets=[0x1E0, 0x58, 0x20, 0x70, 0x58, 0x20, 0xC68]

ammo_offsets = offsets=[0x1E0, 0x58, 0x20, 0x70, 0x58, 0x20, 0xC20]

machine_gun_offsets = offsets=[0x1E0, 0x58, 0x20, 0x70, 0x58, 0x20, 0xD40]

player_speed_offsets = offsets=[0x1E0, 0x58, 0x20, 0x70, 0x58, 0x20, 0xD10] #Working

#Uses Game Offset And Offsets To Direct Script Where To Read And Write From
def getPointerAddress(base, offsets):
    remote_pointer = RemotePointer(pm.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(pm.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset

#Tells getPointerAddress What Offset To Mix With Game Offset And Saves It To Appropriate Name
blood_gems = getPointerAddress(game_offset, blood_gems_offsets)

coins = getPointerAddress(game_offset, coins_offsets)

health = getPointerAddress(game_offset, health_offsets)

damage = getPointerAddress(game_offset, damage_offsets)

ammo = getPointerAddress(game_offset, ammo_offsets)

machine_gun = getPointerAddress(game_offset, machine_gun_offsets)

player_speed = getPointerAddress(game_offset, player_speed_offsets)
