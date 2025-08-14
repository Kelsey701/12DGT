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

    action = easygui.buttonbox ("\nDo you want to:", choices = ["add", "remove", "update", "search", "continue"])

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
         my_dict = {
                "strength": strength,
                "speed": speed,
                "stealth": stealth,
                "cunning": cunning}
         name = easygui.enterbox ("Enter monster card you want to change")
         update = easygui.buttonbox ("do you want to change the", choices = ["strength", "speed", "stealth", "cunning"])

         if update == 'strength':
                strength = int(easygui.enterbox ("Enter your monsters strength (number 1 - 25)"))
                #add to dictionary

         elif update == 'speed':
                speed = int(easygui.enterbox ("Enter your monsters speed (number 1 - 25)"))
                #add to dictionary

         elif update == 'stealth':
            stealth = int(easygui.enterbox ("Enter your monsters stealth (number 1 - 25)"))
            #add to dictionary

         elif update == 'cunning':
                cunning =  int(easygui.enterbox ("Enter your monsters cunning (number 1 - 25)"))
                #add to dictionary
                print (f"{name}: strength={strength}, speed={speed}, stealth={stealth}, cunning={cunning}")
        

    elif action == 'search':
        break
    elif action == 'continue':
        break
    
        
    
    


            

