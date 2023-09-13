import os
import pyautogui
import datetime
import keyboard
import time
import pyperclip
import webbrowser
#import pytesseract


#('n')#screenshot to imgbb and imgtotext
#('m')#skip imgbb
#('b')#exit
#('x')#ctrl v all bots
#('q')#prompt generator

# Get the current time
start_time = datetime.datetime.now().timestamp() * 1000
file_path = os.path.dirname(os.path.abspath(__file__))

cnt = 0


def takeSS(first_pos,second_pos):    
    left = min(first_pos[0], second_pos[0])
    top = min(first_pos[1], second_pos[1])
    width = abs(first_pos[0] - second_pos[0])
    height = abs(first_pos[1] - second_pos[1])
    
    screenshot = pyautogui.screenshot(region=(left, top, width, height))
    return screenshot

while 1:
    
    key_n = keyboard.is_pressed('n')#screenshot to imgtotext, to use this press n two times on different mouse position.
    key_b = keyboard.is_pressed('b')#exit
    key_x = keyboard.is_pressed('x')#ctrl v all bots
        
    if key_n :
        if cnt%2==0:
            first_pos = pyautogui.position()
        elif cnt%2==1:
            second_pos = pyautogui.position()

            screenshot = takeSS(first_pos,second_pos)
            screenshot.save('screenshot.png')

            
            webbrowser.open("https://www.imagetotext.info/")
            
            time.sleep(1.2)
            pyautogui.moveTo(750,710)
            pyautogui.leftClick()

            time.sleep(0.8)
            pyautogui.moveTo(500,595)
            pyautogui.leftClick()

            
            pyperclip.copy(r'{}\screenshot.png'.format(file_path))
            pyautogui.hotkey("ctrl", "v") 
            pyautogui.hotkey('enter')
            time.sleep(1.2)


            pyautogui.moveTo(800,930)
            pyautogui.leftClick()
        

        cnt+=1
        time.sleep(1)
        

    if key_x :
        webbrowser.open("https://bard.google.com/")
        time.sleep(2)
        
        pyautogui.moveTo(1000,900)
        time.sleep(0.2)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.2)
        pyautogui.hotkey('enter')
        time.sleep(0.2)

        
        webbrowser.open("https://chat.openai.com/")
        time.sleep(1)

        pyautogui.moveTo(950,450)
        time.sleep(0.2)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.2)
        pyautogui.hotkey('enter')
        time.sleep(0.2)
        
        time.sleep(1)


    if key_b :
        break
    

elapsed_time = datetime.datetime.now().timestamp() * 1000 - start_time
print("The elapsed time was", elapsed_time, "seconds.")
