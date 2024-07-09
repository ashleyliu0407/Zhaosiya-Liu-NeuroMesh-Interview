def minSub(source, target):
    count = 0
    target_index = 0
    
    while target_index < len(target):
        source_index = 0
        start_target_index = target_index 
        
        while source_index < len(source) and target_index < len(target):
            if source[source_index] == target[target_index]:
                target_index += 1
            source_index += 1
        
        if target_index == start_target_index:
            return -1
        
        count += 1 
    
    return count

print(minSub("abc", "abcbc")) 
print(minSub("abc", "acdbc"))
print(minSub("xyz", "xzyxz")) 
