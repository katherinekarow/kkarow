fp = open( "lab06_pre-lab_input.rtf" )
total = 0
letters = ''
for line in fp:
    for ch in line:
        if ch.isdigit():
            total += int(ch)
        elif ch.isalpha():
            letters += ch
            
print( total )    # Line 1
print( letters )  # Line 2
fp.close()