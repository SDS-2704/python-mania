#Let's dive into the code for it!
# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
N, M= map(int,input().split())
assert ((5 < N < 101) and (15 < M < 303) and M == 3*N), "N should be greather than 5 and less than 101. M should be greater than 15 and less than 303."
c1, strn = '-', ".|."
wel = "WELCOME"
n = N//2
count1 = 1
dec1 = 1
count2 = int((M-6)/3)
#Upper half
for i in range(1, n+1):
print((c1*int((M-(3*dec1))/2) + (strn*count1) + (c1*int((M-(3*dec1))/2))))
count1 += 2
dec1 += 2
#Middle Line
print((c1*int((M-7)/2)) + wel + (c1*int((M-7)/2)))
#Lower half
for i in range(1, n+1):
print((c1*int(i*3)) + (strn*count2) + (c1*int(3*i)))
count2 -= 2
