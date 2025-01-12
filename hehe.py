# import turtle as t
# window = t.Screen()

# hey = t.Turtle()
# t.bgcolor('purple')


# window.exitonclick()
# turtle.done()


# WE PREP
# find missing no in an array of range [0,n]

def missingno(arr):
    n = len(arr)
    total = (n*(n+1))//2
    sum = 0
    for i in arr:
        sum+=i
    return total-sum

arr=[3,0,1]
print(missingno(arr))