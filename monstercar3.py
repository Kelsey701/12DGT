import easygui
my_dict  =       {"stonling":
                 {
                 "Speed": 1,
                 "strength:": 7,
                 "stealth:": 25,
                 "cunning:" : 15
                 },
                 
                 "vexscream":
                 {
                 "strength:" : 1,
                 "speed:": 6,
                 "stealth:" :21,
                 "cunning:" : 19
                 },
                 "dawnmirage":
                 {
                  "strength": 5,
                  "speed": 15,
                  "stealth" : 18,
                  "cunning" : 22
                 },
                  "blazegolem":
                 {
                  "strength": 15,
                  "speed": 20,
                  "stealth": 23,
                  "cunning": 6
                  },
                  "websnake":
                 {
                  "strength": 7,
                  "speed": 15,
                  "stealth": 10,
                  "cunning": 5
                  },
                  "moldvine":
                 {
                  "strength": 21,
                  "speed": 18,
                  "stealth": 14,
                  "cunning": 5
                  },
                  "vortexwing":
                 {
                  "strength": 19,
                  "speed": 13,
                  "stealth": 19,
                  "cunning": 2
                  },
                  "rotthing":
                 {
                  "strength": 19,
                  "speed" : 7,
                  "stealth" : 4,
                  "cunning": 12
                  },
                  "froststep":
                 {
                  "strength": 14,
                  "speed": 14,
                  "stealth": 17,
                  "cunning": 4
                  },
                  "wispghoul":
                 {
                  "strength": 17,
                  "speed": 19,
                  "stealth": 3,
                  "cunning": 2
                  }}

while True:
    print ("\nCurrent cards:")
    for key, value in my_dict.items():
        print (f"{key}:{value}")

    action = easygui.buttonbox ("\nDo you want to:", choices = ["add", "remove", "update", "search", "nothing"])

    if action == 'add':
            name = easygui.enterbox ("Enter your monster name")
            strength = int(easygui.enterbox ("Enter your monsters strength (number 1 - 25)"))
            speed = int(easygui.enterbox ("Enter your monsters speed (number 1 - 25)"))
            stealth = int(easygui.enterbox ("Enter your monsters stealth (number 1 - 25)"))
            cunning =  int(easygui.enterbox ("Enter your monsters cunning (number 1 - 25)"))
            #add to dictionary
            my_dict [name] = {
                "strength": strength,
                "speed": speed,
                "stealth": stealth,
                "cunning": cunning}
            
            print (f"{name}: strength={strength}, speed={speed}, stealth={stealth}, cunning={cunning}")
        
         
    elif action == 'remove':
        remove_card = easygui.enterbox ("enter key to remove")
        if remove_card in my_dict:
            del my_dict [remove_card]
        else:
            print ("key not found")

    elif action == 'update':
            name = easygui.enterbox ("Enter your monster name to edits")
            strength = int(easygui.enterbox ("Enter your monsters strength (number 1 - 25)"))
            speed = int(easygui.enterbox ("Enter your monsters speed (number 1 - 25)"))
            stealth = int(easygui.enterbox ("Enter your monsters stealth (number 1 - 25)"))
            cunning =  int(easygui.enterbox ("Enter your monsters cunning (number 1 - 25)"))
            #add to dictionary
            my_dict [name] = {
                "strength": strength,
                "speed": speed,
                "stealth": stealth,
                "cunning": cunning}
            
            print (f"{name}: strength={strength}, speed={speed}, stealth={stealth}, cunning={cunning}")
        
    
    elif action == 'search':
        search_card = easygui.enterbox ("what card do you want to search?")
        if search_card in my_dict:
            easygui.msgbox ( my_dict[search_card])
            update = easygui.buttonbox ("do you want to update the card you searched?", choices = ["yes", "no"])
            if update == 'yes':
                 name = easygui.enterbox ("Enter your monster name to edits")
                 strength = int(easygui.enterbox ("Enter your monsters strength (number 1 - 25)"))
                 speed = int(easygui.enterbox ("Enter your monsters speed (number 1 - 25)"))
                 stealth = int(easygui.enterbox ("Enter your monsters stealth (number 1 - 25)"))
                 cunning =  int(easygui.enterbox ("Enter your monsters cunning (number 1 - 25)"))
                 #add to dictionary
                 my_dict [name] = {
                     "strength": strength,
                     "speed": speed,
                     "stealth": stealth,
                     "cunning": cunning}
                 print (f"{name}: strength={strength}, speed={speed}, stealth={stealth}, cunning={cunning}")
            else:
               break 
               

            

    elif action == 'nothing':
        break
    
        
    
    


            

