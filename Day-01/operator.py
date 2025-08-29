x = ['appel', 'banana'];
y = ['appel', 'banana'];
z = x;

# print(x is not y); # true
# print(x is not z); # false
# print(x == y); # true

print("banana" in x); # true
print("abcd" in y); # false

def function():
    global num;
    num = 30;
# print(num);
function();
print(num);