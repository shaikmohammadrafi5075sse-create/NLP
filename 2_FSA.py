def ends_with_ab(s):
    # States: 0 = start, 1 = seen 'a', 2 = seen 'ab' (accept)
    state = 0
    for char in s:
        if state == 0:
            if char == 'a':
                state = 1
            else:
                state = 0
        elif state == 1:
            if char == 'b':
                state = 2
            elif char == 'a':
                state = 1
            else:
                state = 0
        elif state == 2:
            if char == 'a':
                state = 1
            else:
                state = 0
    # Accept if final state is 2 (string ends with 'ab')
    return state == 2

# Test cases
test_strings = ["ab", "aab", "babab", "abc", "helloab", "cab"]
for s in test_strings:
    if ends_with_ab(s):
        print(f"'{s}' is accepted (ends with 'ab').")
    else:
        print(f"'{s}' is rejected (does not end with 'ab').")


#---------------------------OutPut--------------------------

C:\Users\HP\OneDrive\Desktop\NLP Programs>python 2_FSA.py
'ab' is accepted (ends with 'ab').
'aab' is accepted (ends with 'ab').
'babab' is accepted (ends with 'ab').
'abc' is rejected (does not end with 'ab').
'helloab' is accepted (ends with 'ab').
'cab' is accepted (ends with 'ab').