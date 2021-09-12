import os,time
os.system('cls') # linus -' clear'
filenames = ["animation1.txt"]

def animator(filesnames,delay = 1,repeat = 10):
       frames = []
       for name in filenames:
           with open(name,"r",encoding="utf8") as f:
              frames.append(f.readlines())
       for i in range(repeat):
           for frame in frames:
               print("".join(frame))
               time.sleep(5)
               os.system('cls')

animator(filenames,delay = 0.5, repeat = 5)

animator(filenames,delay = 0.1, repeat = 20)

animator(filenames,delay = 2, repeat = 5)
