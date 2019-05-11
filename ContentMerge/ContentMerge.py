from datetime import datetime
import glob2

files = glob2.glob('*.txt')
with open(datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt","w") as writeFile:
    for file in files:
        with open(file,"r") as readFile:
            writeFile.write(readFile.read() + "\n")
