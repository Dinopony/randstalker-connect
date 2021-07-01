function onItemTaken()
    -- Make a string out of the player inventory bytes
    local inventoryString = ''
    for address = 0xFF1040, 0xFF105C do
        inventoryString = inventoryString .. memory.readbyte(address) .. ','
    end
    comm.socketServerSend('inventoryChange=' .. inventoryString)
end

function onMapChange()
    local mapID = memory.read_u16_be(0xFF1204)
    comm.socketServerSend('mapChange=' .. mapID)
end

event.onmemoryexecute(onItemTaken, 0x29216)
event.onmemorywrite(onMapChange, 0xFF1204)