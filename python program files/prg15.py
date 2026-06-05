stack=[]
def push(element):
    stack.append(element)
    print('element pushed to stack.')
def pop():
    if stack == []:
        print('Underflow,no element in stack')
    else:
        element = stack.pop()
        print('element popped from stack.',element)
def peek():
    if stack == []:
        print('Underflow,no element in stack')
    else:
        print('Top element is' ,stack[-1])
def display_stack():
    if stack == []:
        print('Underflow,no element in stack.')
    else:
        print('Stack status:', stack)
def menu():
    while True:
        print('\nMenu')
        print('1. Push')
        print('2. Pop')
        print('3. Peek')
        print('4. Display Stack Status')
        print('5. Exit')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            element = int(input('Enter the element to push: '))
            push(element)
        elif choice == 2:
            pop()
        elif choice == 3:
            peek()
        elif choice == 4:
            display_stack()
        elif choice == 5:
            print('Exited.')
            break
        else:
            print('Invalid choice. Please try again.')

menu()
