def solution(s):
    if len(s) == 1:
        return 1
    
    max_comp = len(s) // 2
    result = 1000
    
    for i in range(1, max_comp + 1):
        prev, count = s[:i], 0
        string = ""
        
        for j in range(i, len(s), i):
            curr = s[j:j + i]
            if prev != curr:
                if count:
                    string += f"{count+1}{prev}"
                else:
                    string += prev
                prev = curr
                count = 0
            else:
                count += 1
            
        if count:
            string += f"{count+1}{curr}"
        else:
            string += curr
        
        result = min(result, len(string))
        
    return result


def solution(s):
    max_comp = len(s) // 2
    result = 1000
    
    for i in range(1, max_comp + 1):
        prev, length = s[:i], 0
        count = 0
        
        for j in range(i, len(s), i):
            curr = s[j:j + i]
            count += 1
            
            if prev != curr:
                if count > 1:
                    length += i + 1
                else:
                    length += i
                prev = curr
                count = 0
            
        if count:
            length += i + 1
        else:
            length += len(curr)
        
        result = min(result, length)
        
    return result