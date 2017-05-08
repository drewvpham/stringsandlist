str = "It's thanksgiving day. It's my birthday,too!"
print str.find('day')

newstr=str.replace("day","month")
print newstr

x = [2,54,-2,7,12,98]

print min(x)
print max(x)

y = ["hello",2,54,-2,7,12,98,"world"]
print y[0]+" "+y[len(y)-1]


z = [19,2,54,-2,7,12,98,32,10,-3,6]
z.sort()
print z
first_half=z[:len(z)/2]
second_half=z[len(z)/2:]
print first_half
print second_half
solution=second_half
solution.insert(0,first_half)
print solution
print second_half
