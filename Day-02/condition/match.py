# grading system using match

# 80 - 100 => A+
# 70 - 79 => A-
# 60 - 69 => B
# 50 - 59 => C

mark = 55;

# print(mark/10);

match int(mark/10):
    case 8:
        print("A+");
    case 7:
        print("A-");
    case 6:
        print("B");
    case 5:
        print("C");
    case _:
        print("F");