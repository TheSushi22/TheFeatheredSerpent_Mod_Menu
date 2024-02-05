import pymem
from pymem import Pymem
from pymem.ptypes import RemotePointer

#Game Name
pm = Pymem("TheFeatheredSerpent_KS_V1.7.exe")

#Game Offset

game_offset = pm.base_address + 0x023D2BC0

#Offsets
blood_gems_offsets = offsets=[0x1E0, 0x58, 0x20, 0x70, 0x58, 0x20, 0xA28]

coins_offsets = offsets=[0x1E0, 0x58, 0x20, 0x70, 0x58, 0x20, 0xA58]

health_offsets = offsets=[0x1E0, 0x58, 0x20, 0x70, 0x58, 0x20, 0x230]

arrow_speed_offsets = offsets=[0x1E0, 0x58, 0x20, 0x70, 0x58, 0x20, 0xBD8]

player_speed_offsets = offsets=[0x1E0, 0x58, 0x20, 0x70, 0x58, 0x20, 0xB78]


#Where The Magic Happens
def getPointerAddress(base, offsets):
    remote_pointer = RemotePointer(pm.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(pm.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset


#Putting It Together
blood_gems = getPointerAddress(game_offset, blood_gems_offsets)

coins = getPointerAddress(game_offset, coins_offsets)

health = getPointerAddress(game_offset, health_offsets)

arrow_speed = getPointerAddress(game_offset, arrow_speed_offsets)

player_speed = getPointerAddress(game_offset, player_speed_offsets)
