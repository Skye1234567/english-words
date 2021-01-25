#App for ZP

import json
import random
import os
import platform

def main():
    slash = '\\'
    mode = platform.system()
    if mode == 'Darwin' or mode=='Linux' :
        slash='//'
    run(slash)
    
        
    
    
def run(s):
    
    yours=""
        
    while(yours.lower() not in {"no", "stop", "bye", "q"}):
        CURR_DIR = os.path.dirname(os.path.realpath(__file__))   
        yours = input("Your word?\n")
        f= open(CURR_DIR+s+ 'words_dictionary.json')
        mydic = json.load(f)
        mylist = list(mydic.keys())
        r = random.randint(0,len(mylist)-1)
        mine = mylist[r]
        print("Here's mine: \n "+mine)
    print("Goodbye")   
            
            
        
main()