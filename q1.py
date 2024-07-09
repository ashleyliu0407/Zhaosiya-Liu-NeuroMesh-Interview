def minSub(input, target):
    count = 0
    index = 0
    
    while index < len(target):
        index = 0
        start_index = index 
        
        while index < len(input) and index < len(target):
            if input[index] == target[index]:
                index += 1
            index += 1
        
        if index == start_index:
            return -1
        
        count += 1 
    
    return count

print(minSub("abc", "abcbc")) 
print(minSub("abc", "acdbc"))
print(minSub("xyz", "xzyxz")) 
