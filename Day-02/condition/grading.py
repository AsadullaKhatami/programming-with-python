mark = 18;

# 80 - 100 => A+
# 70 - 79 => A-
# 60 - 69 => B
# 50 - 59 => C

if mark >= 80 and mark <= 100:
    print("A+");
elif mark >= 70 and mark <= 79:
    print("A-");
elif mark >= 60 and mark <= 69:
    print("B");
elif mark >= 50 and mark <= 59:
    print("C");
else:
    print("F");