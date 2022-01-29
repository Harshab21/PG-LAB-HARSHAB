##	Generate positive list of numbers from a given list of integers
   
list1 =[-10,20,35,-67,70]
re=[num for num in list1 if num>=0]
print(re)
##	Square of N number

n=int(input("enter limit:"))
squarelist= [ i**2 for i in range(1,n+1)]
print("Square of N numbers : ", squarelist)

##	Form a list of vowels selected from a given word

word =str(input("Enter the word :"))
print("The original string is : "+word)
print("The vowel are : ",end="")
for i in word:
   if i in 'aeiouAEIOU':
      print([i],end=" ")
      
##List ordinal value of each element of a word (Hint: use ord() to get ordinal values)
      

w=input("Enter a word:")
print("Ordinal values corresponding to each element is:")
for i in w:print(i,end=":")
print(ord(i),end=" ")


