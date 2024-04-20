# write a program that takes a string and returns the most frequent character in it



def most_frequent_character(string):
    
    #create a dictonary to store the frequency of each character
    char_count={}

    #iterate through each each character in the string
    for character in string:

        #increment the count of the character in dictionary
        if character in char_count:
            char_count[character]+=1
        else:
            char_count[character]=1

    #initialize variables to keep track of most frequent character and its count
    most_frequent_char=None
    max_count=0

   #iterate through the dictionary to find the most frquent character
    for character,count in char_count.items():
        if count>max_count:
            max_count=count
            most_frequent_char=character

    return most_frequent_char

string="hello you are awesome"
freq_char=most_frequent_character(string)
print(f"The Most Frequent Character Is :  {freq_char}")         



