nums = [10, 30, 20, 25, 5];
st = nums[0];

for i in nums:
    if st < i:
        st = i;

print("the max number is: ", st);