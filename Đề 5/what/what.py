stri = str(input())
if len(stri) >= 3:
    if stri.endswith('ing') == False:
        res = ''.join([stri,'ing'])
    else:
        if stri.endswith('ly') == False:
            res = ''.join([stri,'ly'])
else:
    res = stri

print(res)