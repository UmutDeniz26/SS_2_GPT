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


"""
prompt=""
prompt_elements = []
cnt_q=0
index_to_letters=['A','B','C','D','E','F','G','H','I','J']
prompt_index=0
def prompt_generator(text,index,current_prompt):
    global prompt_elements,index_to_letters
    if index==0:
        current_prompt+="Answer the Question Carefully : \n{}\n".format(text)
    else:
        current_prompt+="\n{}){}\n".format(index_to_letters[index-1],text)
    return current_prompt
"""
   
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
    
    """
    if key_q and pytesseract_include:
        if cnt_q%2==0:
            first_pos = pyautogui.position()
        elif cnt_q%2==1:
            second_pos = pyautogui.position()
            
            screenshot = takeSS(first_pos,second_pos)
            screenshot.save('screenshot.png')

            #change the path
            pytesseract.pytesseract.tesseract_cmd = r'C:\Users\umutc\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

            pyautogui.keyDown('capslock')
            pyautogui.keyUp('capslock')
            time.sleep(1.3)
            pyautogui.keyDown('capslock')
            pyautogui.keyUp('capslock')

            text = pytesseract.image_to_string(screenshot)

            prompt = prompt_generator(text,prompt_index,prompt)
            pyperclip.copy(prompt)
            prompt_index+=1

        cnt_q+=1
        time.sleep(1)
    """
        
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
            

            #change the path !!!!!nn
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
        
        """
        webbrowser.open("https://www.bing.com/search?form=WSBCPB&showconv=1&q=bing+AI")
        time.sleep(1.5)

        pyautogui.moveTo(1000,900)
        time.sleep(1.9)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.2)
        pyautogui.hotkey('enter')
        time.sleep(0.2)
        """
        time.sleep(1)


    if key_b :
        break
    

elapsed_time = datetime.datetime.now().timestamp() * 1000 - start_time
print("The elapsed time was", elapsed_time, "seconds.")
