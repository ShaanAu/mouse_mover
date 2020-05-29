import  time, random
import pyautogui, sys

print('determine how many seconds to wait before moving the cursor')
v =input()
print('Press Ctrl-C to quit')

try:
    while True:
        x,y = pyautogui.position()
        time.sleep(int(v))
        a = random.randint(300, 1000) #width 0,10 assuming 1920px
        b = random.randint(300, 1000) #height 0,10 assuming 1080px height
        pyautogui.moveTo(a, b, 2) #2 is the time from x,y to a,b
except KeyboardInterrupt:
    print("\n")