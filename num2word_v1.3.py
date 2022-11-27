def num2word(num):
    spell = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine',
             10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen',
             17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty',
             60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', '00':'hundred', '000':'thousand', '000000':'million'}
    if num >= 10000000:
        return 'really large number'
    
    output = []
    breakdown = num_breakdown(num) 
    # num_breakdown return format: [millions, thousands, hundreds, tens, ones]
    for i in breakdown:
        # Non empty thousands/millions
        if i != 0 and i > 999:
            prefix, suffix = num_slice(i)
            if prefix in spell:
                output.append(spell[prefix] + ' ' + spell[suffix])
            else:
                output.append(num2word(prefix) + ' ' + spell[suffix])
        # Non empty hundreds (will include and at the back)
        elif i != 0 and i > 99:
            prefix, suffix = num_slice(i)
            if prefix in spell:
                output.append(spell[prefix] + ' ' + spell[suffix])
            else:
                output.append(num2word(prefix) + ' ' + spell[suffix])
        # Non empty tens when the tens place is '10' as it could contain 'teen' values
        elif i == 10:
            output.append(spell[sum(breakdown[-2:])])
            break
        # Non empty digits
        elif i != 0:
            output.append(spell[i])

    combine_logic = breakdown[:2] + [sum(breakdown[2:])]
    str_out = ''
    for i in output:
        print(i, 'hi')
        if 'hundred' in i:
            str_out += i + ' and '
        else:
            str_out += i + ' '
    str_out = str_out[:-1]   
    return str_out

def num_slice(num):
    '''slices zeroes from the back, returns a tuple of prefix and zeros e.g. 100 > (1,'00').
       only works with trailing zeroes.
    '''
    str_num = str(num)
    if len(str_num) > 6:
        zeroes = '000000'
        prefix = int(str_num[:-6])
    elif len(str_num) > 3:
        zeroes = '000'
        prefix = int(str_num[:-3])
    else:
        zeroes = '00'
        prefix = int(str_num[:-2])
    return (prefix, zeroes)
    

def num_breakdown(num):
    divisors = [1000000, 1000, 100, 10, 1]
    breakdown = []
    r_total = 0
    for i in divisors:
        digit = num - (num % i) - r_total
        r_total += digit
        breakdown.append(digit)
    return breakdown
