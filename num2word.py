spell = {1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9:'nine',
        10:'ten', 11:'eleven', 12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen', 16:'sixteen',
        17:'seventeen', 18:'eighteen', 19:'nineteen', 20:'twenty', 30:'thirty', 40:'forty', 50:'fifty',
        60:'sixty', 70:'seventy', 80:'eighty', 90:'ninety', '00':'hundred', '000':'thousand', '000000':'million'}

suffixes = {2:'thousand', 3:'million', 4:'billion', 5:'trillion', 6:'quadrillion', 7:'quintillion', 8:'sextillion', 9:'septillion',
            10:'octillion', 11:'nonillion', 12:'decillion',13:'undecillion', 14:'duodecillion', 15:'tredecillion', 16:'quattuordecillion',
            17:'quindecillion', 18:'sexdecillion', 19:'septendecillion', 20:'octodecillion', 21:'novemdecillion', 22:'vigintillion',
            23:'unvigintillion', 24:'duovigintillion', 25:'tresvigintillion', 26:'quattuorvigintillion', 27:'quinvigintillion',
            28:'sesvigintillion', 29:'septemvigintillion', 30:'octovigintillion', 31:'novemvigintillion', 32:'trigintillion', 33:'untrigintillion',
            34:'duotrigintillion', 35:'trestrigintillion', 36:'quattuotrigintillion', 37:'quintrigintillion', 38:'sestrigintillion', 39:'septentrigintillion',
            40:'octotrigintillion', 41:'noventrigintillion', 42:'quadragintillion'}

def num2word(num):
    num_arr = num_breakdown(num)
    suffix_len = len(num_arr)
    spelled = []
    if suffix_len > 42:
        return 'really large number'
    if num == 0:
        return 'zero'
    if num < 0 or type(num) != int:
        return 'please enter a non-negative integer'

    for i in range(suffix_len):
        p_index = suffix_len - i
        number = num_arr[i]
        if p_index > 1 and number != 0:
            spelled.append(assembler(sub_breakdown(number)) + ' ' + suffixes[p_index])
        elif number != 0:
            spelled.append(assembler(sub_breakdown(number)))
        
    if len(spelled) == 1:
        return spelled[0]
    output = ', '.join(spelled[:-1])
    if 'and' in spelled[-1]:
        output += ', ' + spelled[-1]
    else:
        output += ' and ' + spelled[-1]
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
    '''breaks down numbers into an array of three digits at a time'''
    num_array = []
    num_str = str(num)
    for i in range(len(num_str), 0, -3):
        start = max(i - 3, 0)
        num_array.insert(0, int(num_str[start:i]))
    return num_array

