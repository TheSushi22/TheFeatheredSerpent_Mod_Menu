import pymem
from pymem import Pymem
from pymem.ptypes import RemotePointer

#Game Name
pm = Pymem("TheFeatheredSerpent_KS_V1.7.exe")

#Offsets

blood_gems_offsets = offsets=[0x1E0, 0x58, 0x20, 0x70, 0x58, 0x20, 0xA28]
blood_gems_address = pm.base_address + 0x023D2BC0

coins_offsets = offsets=[0x1E0, 0x58, 0x20, 0x70, 0x58, 0x20, 0xA58]
coins_address = pm.base_address + 0x023D2BC0

health_offsets = offsets=[0x1E0, 0x58, 0x20, 0x70, 0x58, 0x20, 0x230]
health_address = pm.base_address + 0x023D2BC0

arrow_speed_offsets = offsets=[0x1E0, 0x58, 0x20, 0x70, 0x58, 0x20, 0xBD8]
arrow_speed_address = pm.base_address + 0x023D2BC0

#Where The Magic Happens

def getPointerAddress(base, offsets):
    remote_pointer = RemotePointer(pm.process_handle, base)
    for offset in offsets:
        if offset != offsets[-1]:
            remote_pointer = RemotePointer(pm.process_handle, remote_pointer.value + offset)
        else:
            return remote_pointer.value + offset
        
#Putting It Together

blood_gems = getPointerAddress(blood_gems_address, blood_gems_offsets)

coins = getPointerAddress(coins_address, coins_offsets)

health = getPointerAddress(health_address, health_offsets)

arrow_speed = getPointerAddress(arrow_speed_address, arrow_speed_offsets)
