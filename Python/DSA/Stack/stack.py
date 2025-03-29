class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if not self.is_empty():
            popped_item = self.items.pop()
            print(f"Popped: {popped_item}")
            return popped_item
        else:
            print("Stack is empty. Cannot pop.")
            return None
        
    def peek(self):
        if not self.is_empty():
            top_item = self.items[-1]
            print(f"Peek: {top_item}")
            return top_item
        else:
            print("Stack is empty. Cannot peek.")
            return None
        
    def size(self):
        return len(self.items)

    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack items: ", self.items)        



def parChecker(parantez):
     
    stack = Stack()
    open = "([{"
    close = "}])"

    for i in parantez:
        if i in open:
            stack.push(i)
        elif i in close:
            if stack.is_empty():
                return False
            son = stack.pop()

            if (son == "(" and i != ")" ) or (son == "[" and i != "]" ) or (son == "{" and i != "}" ):
                return False
    return stack.is_empty()


print(parChecker("{[]())}"))

            
def infix_to_postfix(infix_expr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    op_stack = Stack()
    postfix_list = []
    token_list = infix_expr.split()

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == "(":
            op_stack.push(token)
        elif token == ")":
            top_token = op_stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())

    return " ".join(postfix_list)

print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
#print(infix_to_postfix("A + B - C * D"))

a = [ 'a', ['b', ['c', None]]]
print(len(a))