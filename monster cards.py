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
                  "cunning":2
                  }}

while True:
    print ("\nCurrent cards:")
    for key, value in my_dict.items():
        print (f"{key}:{value}")

    action = easygui.buttonbox ("\nDo you want to:", choices = ["add", "remove", "update", "search", "continue"])

    if action == 'add':
        add_new = easygui.enterbox ("enter new monster name:")
        catagory = easygui.enterbox ("what is the catagory you want to add")
        value = easygui.enterbox ("enter new value:")
        my_dict[add_new]= value

    elif action == 'remove':
        remove_card = easygui.enterbox ("enter key to remove")
        if remove_card in my_dict:
            del my_dict [remove_card]
        else:
            print ("key not found")

    elif action == 'update':
        update_card = easygui.enterbox ("enter the card you want to update:")
        if update_card in my_dict:                
            new_value = easygui.enterbox(f"Enter new value for '{key}':")
            my_dict[update_card] =  new_value
        else:
            print ("key not found")

    elif action == 'continue':
        break
    
        
    
    


            
