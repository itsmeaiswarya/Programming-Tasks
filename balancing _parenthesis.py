def pairs(open,close):
    if open=='{'and close=='}':
        return True
    if open=='['and close==']':
        return True
    if open=='('and close==')':
        return True
    return False

def balance_checking(exp):
    stack=[]
    for i in range(len(exp)):
        if exp[i]=='{' or exp[i]=='[' or exp[i]=='(':
            stack.append(exp[i])
        elif exp[i]=='}' or exp[i]==']' or exp[i]==')':
            if pairs(stack[-1],exp[i]) and len(stack)!=0:
                stack.pop()
            else:
                return False

    if len(stack)==0:
        return True
    else:
        return False

exp=input("Enter an expression to check balance parenthesis or not:")
print(balance_checking(exp))