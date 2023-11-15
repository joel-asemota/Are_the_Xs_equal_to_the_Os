def xo(s):
    x_count, o_count = 0, 0
    
    for i in s:
        if i == 'x' or i == 'X':
            x_count += 1
            
        elif i == 'o' or i == 'O':
            o_count += 1
            
    if x_count == o_count:
        s = True
    else: s = False
    
    return s
        
print(xo("ooxXm") == True)
print(xo("ooxm") == False)
print(xo("mmnbm") == True)
print(xo("xmnOm") == True)
