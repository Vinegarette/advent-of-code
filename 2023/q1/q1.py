import math
filename = 'part2.txt'
with open(filename, 'r') as FILE:
    ans = 0
    
    num_words = {
        'one' : 1,
        'two' : 2,
        'three' : 3,
        'four' : 4,
        'five' : 5,
        'six' : 6,
        'seven' : 7,
        'eight' : 8,
        'nine' : 9,
        '1' : 1,
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5,
        '6' : 6,
        '7' : 7,
        '8' : 8,
        '9' : 9
    }
    
    
    for line in FILE.readlines():
        
        
        # Find Digits...
        
        # Find indexes of all nums...
        l, r = math.inf, -1
        first, last = -1, -1
        indexes = {}
        for key in num_words:
            indexes[key] = (line.find(key), line.rfind(key))
            
        # Scrape thru all vals, find leftmost and rightmost indexes/nums
        for key in indexes:
            left, right = indexes[key]
            
            
            if left < l and left != -1:
                l = left
                first = num_words[key]
                
            if right > r and right != -1:
                r = right
                last = num_words[key]
        
        # Concat together
        ans += int(str(first) + str(last))
    print(ans)