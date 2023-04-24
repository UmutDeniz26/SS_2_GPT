import pyautogui
import datetime
import keyboard
import time
from PIL import Image
import pyperclip
import webbrowser

pytesseract_include=True
try: 
    import pytesseract
except:
    pytesseract_include=False
#('n')#screenshot to imgbb and imgtotext
#('m')#skip imgbb
#('b')#exit
#('x')#ctrl v all bots
#('q')#prompt generator

prompt=""

# Get the current time
start_time = datetime.datetime.now().timestamp() * 1000

prompt_elements = []
prompt_index = 0
index_to_letters=['A','B','C','D','E','F','G','H','I','J']

screenshot_index=0

def prompt_generator(text,index,current_prompt):
    global prompt_elements,index_to_letters
    if index==0:
        current_prompt+="Answer the Question Carefully : \n{}\n".format(text)
    else:
        current_prompt+="\n{}){}\n".format(index_to_letters[index-1],text)
    return current_prompt

cnt=0
cnt_q=0

while True:
    
    # Get the current key that is pressed
    key_n = keyboard.is_pressed('n')#screenshot to imgbb and imgtotext
    key_m = keyboard.is_pressed('m')#skip imgbb
    key_b = keyboard.is_pressed('b')#exit
    key_x = keyboard.is_pressed('x')#ctrl v all bots
    key_q = keyboard.is_pressed('q')#prompt generator


    if key_q and pytesseract_include:
        if cnt_q%2==0:
            first_pos = pyautogui.position()
        elif cnt_q%2==1:
            second_pos = pyautogui.position()
            
            print(first_pos,second_pos)

            # Calculate the dimensions of the screenshot
            left = min(first_pos[0], second_pos[0])
            top = min(first_pos[1], second_pos[1])
            width = abs(first_pos[0] - second_pos[0])
            height = abs(first_pos[1] - second_pos[1])

            # Take the screenshot and save it as "screenshot.png" in the current directoryvv
            screenshot = pyautogui.screenshot(region=(left, top, width, height))
            screenshot.save('screenshot.png')

            #tesseract kullanmayacaksan sil(text to image)
            pytesseract.pytesseract.tesseract_cmd = r'C:\Users\umutc\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

            pyautogui.keyDown('capslock')
            pyautogui.keyUp('capslock')
            time.sleep(1.3)
            pyautogui.keyDown('capslock')
            pyautogui.keyUp('capslock')

            text = pytesseract.image_to_string(screenshot)

            prompt = prompt_generator(text,prompt_index,prompt)
            print(prompt)
            pyperclip.copy(prompt)
            prompt_index+=1
        cnt_q+=1
        time.sleep(1)

    if key_m :
        screenshot_index+=1
        print(screenshot_index)
        time.sleep(1)
        
        
    if key_n :

        if cnt%2==0:
            first_pos = pyautogui.position()
        elif cnt%2==1:
            second_pos = pyautogui.position()
            
            print(first_pos,second_pos)

            # Calculate the dimensions of the screenshot
            left = min(first_pos[0], second_pos[0])
            top = min(first_pos[1], second_pos[1])
            width = abs(first_pos[0] - second_pos[0])
            height = abs(first_pos[1] - second_pos[1])

            # Take the screenshot and save it as "screenshot.png" in the current directoryvv
            screenshot = pyautogui.screenshot(region=(left, top, width, height))
            screenshot.save('screenshot.png')


            if screenshot_index<1:
                webbrowser.open("https://tr.imgbb.com/")
                
                time.sleep(1.2)
                pyautogui.moveTo(950,450)

                pyautogui.leftClick()

                time.sleep(0.8)
                pyautogui.moveTo(500,595)
                pyautogui.leftClick()
                time.sleep(0.8)

                #change the path !!!!!
                pyperclip.copy(r'C:\Users\umutc\OneDrive\Masaüstü\Coding\screenshot.png')
                pyautogui.hotkey("ctrl", "v") 
                pyautogui.hotkey('enter')
                time.sleep(1.2)


                pyautogui.moveTo(950,880)
                pyautogui.leftClick()
                time.sleep(1.5)


                pyautogui.moveTo(1295,840)
                pyautogui.leftClick()
                time.sleep(0.2)

            else:
                webbrowser.open("https://www.imagetotext.info/")
                
                time.sleep(1.2)
                pyautogui.moveTo(750,710)

                pyautogui.leftClick()

                time.sleep(0.8)
                pyautogui.moveTo(500,595)
                pyautogui.leftClick()
                time.sleep(0.8)


                #change the path !!!!!
                pyperclip.copy(r'C:\Users\umutc\OneDrive\Masaüstü\Coding\screenshot.png')
                pyautogui.hotkey("ctrl", "v") 
                pyautogui.hotkey('enter')
                time.sleep(1.2)


                pyautogui.moveTo(800,930)
                pyautogui.leftClick()
                
                

            screenshot_index+=1

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
        

        webbrowser.open("https://www.bing.com/search?form=WSBCPB&showconv=1&q=bing+AI")
        time.sleep(1.5)

        pyautogui.moveTo(1000,900)
        time.sleep(1.9)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.2)
        pyautogui.hotkey('enter')
        time.sleep(0.2)


    if key_b :
        break


elapsed_time = datetime.datetime.now().timestamp() * 1000 - start_time
print("The elapsed time was", elapsed_time, "seconds.")
