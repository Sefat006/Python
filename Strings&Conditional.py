str = "This is a string. \n we are creating it in python"
print(str)

str1 = "Sefatur"
len1 = len(str1)
print(len1)


str2 = "Rahman"
len2 = len(str2)
print(len2)

print(str1 + str2)

final_str = str1 + " " + str2
print(final_str) #attach both string
print(len(final_str)) # print the length of the string


# indexing and slicing

str3 = "sefatur rahman"
ch = str3[2]
print(ch) # print(str3[2])

# slicing
print(str3[8:14]) # from index 8 to 13; 8 = r and 13 = n; rahman
# (str3[8:len(str3)]) # print(str3[8:])


# some more function is 
# str.find("") // to find anything in string
# str.count("") // to count occurance of any value
# str.replace("","") // replace any word





#  conditional statement ------------------

light = "green"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")

print("end of code")

