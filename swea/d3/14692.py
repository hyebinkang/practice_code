t = int(input())

for i in range(t):
    N = int(input())

    if N%2 == 0:
        print("#{0}".format(i+1), "Alice")
    else:
        print("#{0}".format(i+1), "Bob")