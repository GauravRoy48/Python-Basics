#-----------------------------------------BEFORE------------------------------------------------------
#myfile = open("fruits.txt")
#fruits_read = myfile.read()
#myfile.seek(0)
#fruits_readline = myfile.readline()
#myfile.seek(0)
#fruits_readlines = myfile.readlines()
#fruits_readlines_stripped = [line.strip() for line in fruits_readlines]
#
#print(fruits_read)
#myfile.close()
#-----------------------------------------AFTER------------------------------------------------------
with open("fruits.txt") as myfile:
    fruits_read = myfile.read()
    myfile.seek(0)
    fruits_readline = myfile.readline()
    myfile.seek(0)
    fruits_readlines = myfile.readlines()
    fruits_readlines_stripped = [line.strip() for line in fruits_readlines]

    print(fruits_read)


#-----------------------------------------BEFORE------------------------------------------------------
#myfile = open("numbers.txt","w")
#numbers = [1,2,3]
#for i in numbers:
#    myfile.write(str(i)+'\n')
#
#myfile.close()
#-----------------------------------------AFTER------------------------------------------------------
with open("numbers.txt","w") as myfile:
    numbers = [1,2,3]
    for i in numbers:
        myfile.write(str(i)+'\n')
