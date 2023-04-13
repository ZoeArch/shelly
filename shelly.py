user_input = input("Enter a string: ")
print("Input string:", user_input)
explanation = ""

while len(user_input) > 0:
    if user_input.startswith("HE"):
        info_out ="High Explosive "
        user_input = user_input[2:]        
    elif user_input.startswith("BC"):
        info_out ="Balistic Capped "
        user_input = user_input[2:]
    elif user_input.startswith("AP"):
        info_out ="Armour Piercing "
        user_input = user_input[2:] 
    elif user_input.startswith("AC"):
        info_out ="Anti Concrete "
        user_input = user_input[2:]        
    elif user_input.startswith("DS"):
        info_out ="Discarding Sabot "
        user_input = user_input[2:]
    elif user_input.startswith("FS"):
        info_out ="Fin Stabilised "
        user_input = user_input[2:]        
    elif user_input.startswith("TF"):
        info_out ="Time Fuse "
        user_input = user_input[2:]        
    elif user_input.startswith("SH"):
        info_out ="Squash Head "
        user_input = user_input[2:]        
    elif user_input.startswith("AT"):
        info_out ="Anti Tank "
        user_input = user_input[2:]        
    elif user_input.startswith("C"):
        info_out ="Capped "
        user_input = user_input[1:]        
    elif user_input.startswith("CR"):
        info_out ="Composite Rigid "
        user_input = user_input[2:]        
    elif user_input.startswith("VOG"):
        info_out ="Anti personnel Fragmentation "
        user_input = user_input[3:]        
    elif user_input.startswith("GM"):
        info_out ="Guided Missile "
        user_input = user_input[2:]        
    elif user_input.startswith("R"):
        info_out ="Rocket Assisted "
        user_input = user_input[1:]        
    elif user_input.startswith("OTA"):
        info_out ="Overfly Top Attack "
        user_input = user_input[3:]        
    elif user_input.startswith("SAM"):
        info_out ="Surface to Air Missile "
        user_input = user_input[3:]        
    elif user_input.startswith("HV"):
        info_out ="High Velocity "
        user_input = user_input[2:]        
    elif user_input.startswith("DP"):
        info_out ="Dual Purpose "
        user_input = user_input[2:]               
    else:
        print("lmao error")
        user_input = user_input[1:]
    explanation += info_out

print(explanation)