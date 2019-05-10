myfile = open("fruits.txt")
fruits_read = myfile.read()
myfile.seek(0)
fruits_readline = myfile.readline()
myfile.seek(0)
fruits_readlines = myfile.readlines()
fruits_readlines_stripped = [line.strip() for line in fruits_readlines]

print(fruits_read)
myfile.close()

myfile = open("numbers.txt","w")
numbers = [1,2,3]
for i in numbers:
    myfile.write(str(i)+'\n')
    
myfile.close()