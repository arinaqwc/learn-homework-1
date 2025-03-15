def compare_str(one, two):
    if not isinstance(one,str) or not isinstance(two,str):
        return 0
    if one == two:
        return 1
    if len(one)>len(two) and one != two:
        return 2
    if two=='learn' and one != two:
        return 3

print(compare_str('hello','gjrf'))
print(compare_str("longer_string", "short")) 
print(compare_str("short", "learn"))  
print(compare_str(123, "test"))