def seconds_since_noon(ore, minuti , secondi):
    
    new_ore= ore*3600
    new_minuti= minuti*60
    new_time= new_ore+new_minuti+secondi
    return new_time
    





secondi= seconds_since_noon(3, 15, 50)    
print(secondi)