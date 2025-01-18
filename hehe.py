# import turtle as t
# window = t.Screen()

# hey = t.Turtle()
# t.bgcolor('purple')


# window.exitonclick()
# turtle.done()


# WE PREP
# find missing no in an array of range [0,n]

# def missingno(arr):
#     n = len(arr)
#     total = (n*(n+1))//2
#     sum = 0
#     for i in arr:
#         sum+=i
#     return total-sum

# arr=[3,0,1]
# print(missingno(arr))

# remove parenthesis
def removeOuterParentheses(s: str) -> str:
        result = []
        c = 0
        for i in s:
            if i == '(':
                if c>0:
                    result.append(i)
                c+=1
            elif i == ')':
                c -= 1
                if c>0:
                    result.append(i)
        return "".join(result)

s = "(()())(())"
print(removeOuterParentheses(s))