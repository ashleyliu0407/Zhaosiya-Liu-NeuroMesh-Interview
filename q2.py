def parenthesesTest(string):
    stack = []
    output = [' '] * len(string)
    
    for i, char in enumerate(string):
        if char == '(':
            stack.append(i)
        elif char == ')':
            if stack:
                stack.pop()
            else:
                output[i] = '?'
    
    while stack:
        output[stack.pop()] = 'x'
    
    return ''.join(output)

def main():
    print("Please enter your string: ")
    inputStrings = []
    while True:
        line = input().strip()
        if line == "":
            break
        inputStrings.append(line)
    
    for string in inputStrings:
        print(string)
        print(parenthesesTest(string))


if __name__ == "__main__":
    main()