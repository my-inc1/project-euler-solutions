#PROJECT EULER PROBLEM 1

#Setting up an empty array to store the numbers
nums = []

#loop through all numbers between 1 and 1000 
for i in range(1, 1000):
    #find numbers which are multiples of 5 or 3 using the modulo function
    if i % 5 == 0 or i % 3 == 0:
        #After finding those numbers add them to the empty "nums array"
        nums.append(i)
#print out the sum of numbers in the "nums array"       
print(sum(nums))

#OUTPUT = 233168