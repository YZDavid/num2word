spell = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine',
             10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen',
             17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty',
             60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', '00':'hundred', '000':'thousand', '000000':'million'}

def num2word(num):
    if num >= 10000000:
        return 'really large number'
    
    mil, tho, hun = num_breakdown(num)
    output = []
    if mil != 0 and ((tho == 0) ^ (hun == 0)):
        output.append(spell[mil] + ' million and')
    elif mil != 0:
        output.append(spell[mil] + ' million,')
    if tho != 0:
        if tho in spell:
            output.append(spell[tho] + ' thousand,')
        else:
            output.append(assembler(sub_breakdown(tho)) + ' thousand,')
    if hun != 0:
        if hun in spell:
            output.append(spell[hun])
        else:
            output.append(assembler(sub_breakdown(hun)))

    output = ' '.join(output)
    if output[-1] == ',':
        output = output[:-1]
    return output
     
def assembler(tup):
    '''only works for numbers under a thousand in the format (hundreds, tens, ones)'''
    hundreds, tens, ones = tup
    output = []
    if hundreds != 0 and (tens == 0 and ones == 0):
        output.append(spell[hundreds] + ' hundred')
    elif hundreds != 0:
        output.append(spell[hundreds] + ' hundred and')
    if tens != 0:
        output.append(spell[tens])
    if ones != 0:
        output.append(spell[ones])
    return ' '.join(output)
    

def sub_breakdown(num):
    '''only works for numbers under a thousand'''
    ones = num % 10
    tens = (num % 100) - ones
    hundreds = (num // 100) % 10
    if tens == 10:
        tens += ones
        ones = 0
    return (hundreds, tens, ones)
    

def num_breakdown(num):
    mil = num // 1000000
    thousand = (num - (mil * 1000000)) // 1000
    hundred = num % 1000
    return (mil, thousand, hundred)

print(num2word(25406))
print(num2word(123))
print(num2word(9050327))
