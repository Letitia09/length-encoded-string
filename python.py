def encode(message):
    #Intialize the list with zero as value
    l=[0]*len(message)                            # returns a list of zeroes which has length that is equal to string length
    c=""                                           #intializing the variable 'c' as empty string
    for i in range(len(message)):
        if (l[i]!=1):                             #  this conditions helps in not looping the same element that is already compared 
            count=1    
            for j in range(i+1,len(message)):
                if message[i]==message[j]:       #check whether the adjacent element is equal to the previous element 
                    count+=1
                    l[j]=1                       #when the comparision is already done then assign value 1 to l[j]. so that there will no looping at the same index 
                else:
                    break
            c+=str(count)+message[i]             # concatenate all the characters
    return c                                      # returns 1A4B8C1A1B
    #Remove pass and write your logic here

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)
