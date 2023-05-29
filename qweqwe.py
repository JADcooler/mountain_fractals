#diamond square method check
def avg(a):
    s = [0,0]
    for i in a:
        s[0] += i[0]
        s[1] += i[1]
    return (s[0]//len(a),s[1]//len(a))

MAX_LEN = 20

asd = [   [0 for i in range(MAX_LEN)        ] for i in range(MAX_LEN) ]

from pprint import pprint
def printit():
    pprint(asd)
    print()

def setit(c):
    asd[c[0]][c[1]] = 1




MASTER_Q = []

def addToQ(a):
    MASTER_Q.append(a)

def func(number):
    global MASTER_Q

    for i in range(number):
        a = MASTER_Q[0]
        MASTER_Q = MASTER_Q[1:]
        
        print("\nstuff ",a)
        s = avg(a)

        x = avg(a[:2] ) #0 and 1
        y = avg(a[1:2] + a[3:] ) #1 and 2
        z = avg(a[2:] ) #2 and 3
        w = avg(a[2:3] + a[:1] ) #3 and 0

        print("result is ",s, " with ",x,y,z,w,'\n')

        setit(s)
        setit(x)
        setit(y)
        setit(z)
        setit(w)

        printit()
    
        input()

        addToQ([a[0], x ,w, s])
        addToQ([x ,a[1] ,s, y])
        addToQ([w , s ,a[2], z])
        addToQ([s, y , z , a[3]])



start = [(0,0),(0,MAX_LEN-1), (MAX_LEN-1,0), (MAX_LEN-1,MAX_LEN-1)]
addToQ(start)
[setit(i) for i in start]
printit()
func(30)