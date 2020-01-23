
file = open("data1.txt");  #link to file

#A couple take aways

# 1.	With Python you can load a while file or load a file line by line
#		Initally, I loaded the whole file at once into a string, split the string
#		on "\n" and then worked with the array.  This was super messy. That said,
#		being able to split an array is very important.  So here is the code
#
#		dataStr = file.read();
#		dataArr = dataStr.split("\n")
#
# 2. 	You will notice that I used a try except here and you might wonder why
#		I did that instead of an if statement. First let me explain a difference
#		between Java and Python
#
#		Java: "happy".index("+") returns -1 program keeps going
#		Python: "happy".index("+") throws an error and program crashes
#		
#		What this means is that using an if will result in a crash of the program
#		unless the error is handled.  Because of this we can take the entire if 
#		statement out and put it in a try except.  If the line in the try fails
#		the program goes to the except and deals with what would habe been the 
#		if statement. 
#
# 3.	Sets LEARN THEM!  This program can be done without sets, however, it 
#		runs super slow and will not execture in the 30 section time limit.  
#		A set is like a list, but it DOES NOT allow duplicates.  That means 
#		if you add an element to a set that already exisits then nothing gets
#		added. 
#
#		What does that mean with this question?  
#		This question requires the program counts unique emails.  The process is
#		Step 1: read new email
#		Step 2: process email to standardize form
#		Step 3: add to set
#		Step 4: output size of set
#
#		If a set was not used Step 4 would be much more complex because you would
#		have to write an algorithm to count for duplicates.  Even done well, this 
#		will take a long time.  Some very smart programmers designed sets, you are
#		not going to be more efficent.
#
# 4.	
#
#

for i in range(0, 10, 1):

	x = file.readline();
	front = ""
	emailset = set([]) 

	for j in range(0,int(x),1):

		temp = file.readline().lower()

		try:
			front = temp[0:temp.index("+")] + temp[temp.index("@") + 1]
		except: 
			front = temp[0:temp.index("@")] + temp[temp.index("@") + 1]

		front = front.replace(".","")
		emailset.add(front)


	print(len(emailset))



