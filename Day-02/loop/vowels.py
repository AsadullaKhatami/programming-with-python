str = "asadulla khatami";
length = len(str);
count = 0;

# print(str);
# print(length);

i = 0; 
while i < length:
    if(str[i] == 'a' or str == 'e' or str[i] == 'i' or str[i] == 'o' or str[i] == 'u'):
        count += 1;
    i += 1;

print("the number of vowels is: ", count);
