The wordCount.py takes an input file and and an output file. The myOutput.txt file starts
with nothing inside. The myOutputSave.txt is an extra output file to save temporary results.
The wordCount.py reads the input file, eliminates punctuation, sorted the words in descending
order and counts the total number a word occurs, each word is putting together with its total number.The result is saved in myOutputSave.txt with duplications of the words. Then wordCount.py
uses myOutputSave.txt's content and eliminates the duplicates of the words, and put the result
in myOutput.txt.

 *wordCount.py takes input and output 
`$ python wordCount.py declaration.txt myOutput.txt` 
`$ python wordCount.py speech.txt myOutput.txt` 

 *Test 
`$ python wordCountTest.py declaration.txt myOutput.txt declarationKey.txt` 
`$ python wordCountTest.py speech.txt myOutput.txt speechKey.txt` 
