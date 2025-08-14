import easygui

# current monsters in the program
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

# loop keeps people in the program until they want to quit
while True:
    print ("\nCurrent cards:")
    for key, value in my_dict.items():
        print (f"{key}:{value}")

    action = easygui.buttonbox ("\nDo you want to:", choices = ["add", "remove", "update", "search", "nothing"])
    # if user wants to add a new card
    if action == 'add':
        # make new card 
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
            #printing the new card
            print (f"{name}: strength={strength}, speed={speed}, stealth={stealth}, cunning={cunning}")
        
    # if user wants to remove a card in list
    elif action == 'remove':
        remove_card = easygui.enterbox ("enter key to remove")
        if remove_card in my_dict:
            del my_dict [remove_card]
        else:
            print ("key not found")
    # if user wants to update a card
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
            #prints off updated card
            print (f"{name}: strength={strength}, speed={speed}, stealth={stealth}, cunning={cunning}")
        
    # if the user wants to search a card in the list
    elif action == 'search':
        search_card = easygui.enterbox ("what card do you want to search?")
        if search_card in my_dict:
            easygui.msgbox ( my_dict[search_card])
            update = easygui.buttonbox ("do you want to update the card you searched?", choices = ["yes", "no"])
            if update == 'yes':
                #if the user wants to update the card after searching it
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
                 #prints out searched updated card
                 print (f"{name}: strength={strength}, speed={speed}, stealth={stealth}, cunning={cunning}")
            
                
                        
    # if the user decides to do nothing
    elif action == 'nothing':
        break
    
        
    
    


            

