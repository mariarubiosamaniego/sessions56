s = "Red Roses run no risk, sir, on nurses order"
#prove that this sentence is a palindrome
#1. sanitize (remove space and punctuation)
#2. make it all the same case with .lower() method
#3. compare that the slice of reverse is the same as the original

punctuation = " !.,;?:"
for p in punctuation:
    s = s.replace(p, "")
print(s)
s = s.lower()
print(s)

if s == s[::-1]:    #string is the same in reverse
    print("f{s} is a palindrome")
else:
    print("f{s} is not a palindrome")

