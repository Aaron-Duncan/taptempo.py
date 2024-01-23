from pynput.keyboard import Key, Controller
import time
print("Use enter to tap, ctrl-C to quit")
inputList = [0,0,0,0]
key = 0
x = 0
y = 1
z = 2
w = 3
while True:
    begin = time.time()
    input() 
    end = time.time()
    elapsed = end - begin
    item = elapsed
    inputList.append(item)
    # print(inputList)
    x += 1
    y += 1
    z += 1
    w += 1
    quarternote = (inputList[x]+inputList[y]+inputList[z]+inputList[w])*1000/4
    BPM = 60000/quarternote
    count = len(inputList)
    Tempo = "Tempo: {:.2f}"
    print(Tempo.format(BPM))
   

    







    


 
    
    


