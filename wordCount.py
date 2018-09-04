import sys

nameInput = sys.argv[1]
nameOutput = sys.argv[2]

#Output text file - erase previous content
file = open(nameOutput, "w")
file.write("")
file .close()

#Extra output text file - erase previous content
file1 = open("myOutputSave.txt", "w")
file1.write("")
file.close()

#Reads input text file
file2 = open(nameInput, "r")
data = file2.read()

#Eliminates punctation and other signs 
word1 = data.split(".")
word2 = "".join(word1)
word3 = word2.split(",")
word4 = "".join(word3)
word4 = word4.lower()
word5 = word4.split(":")
word6 = "".join(word5)
word6a = word6.split("--")
word6b = "".join(word6a)
word6c = word6b.split(";")
word6d = "".join(word6c)
word7 = word6d.split()
word7.sort() #Sorted in descending order

for num in word7:
 word8 = word7.count(num) #Counts total of times each word occurs
 word9 =str(word8) #Transform (total) to string
 word10 = (num + " " + word9 + ", \n") #Word and total together

# print(word10)

#Write in extra file -temporary result
 file2a = open("myOutputSave.txt", "a")
 file2a.write(word10)
 file2a.close()
 
#Read extra file
file3 = open("myOutputSave.txt", "r")
word_new = file3.read()

#Eliminates signs
word_new3 = "".join(word_new)
word_new4 = {word_new3} 
word_new5 = word_new3.split(" \n")
word_new6 = set(word_new5) #Eliminate duplicates
word_new7 = list(word_new6)
word_new8 = "".join(word_new7)
word_new9 = word_new8.split(",")
word_new9.sort()

##print(word_new9)

for num1 in word_new9:
 word_new10 = (num1 + "\n") #Separate words
 print(word_new10)
 
#Write in output text file - result
 file5 = open(nameOutput, "a")
 file5.write(word_new10)
 file5.close()
 
