# Algorithm Designed By Dixanta Bahadur Shrestha
# Creators Institute of Business & Technology [CIBT]
# https://creators.institute
# Purnachandi Marg, Lalitpur, Nepal

numbers=[
    'Zero','One','Two','Three','Four','Five',
    'Six','Seven','Eight','Nine'
]

less_20=["Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen",
"Sixteen","Seventeen","Eighteen","Nineteen"]

below_hundred=["Twenty","Thirty", 
"Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]

places = ['Hundred', 'Thousand']

def two_places(num_str):
    num = int(num_str)
    if num < 20:
        return less_20[int(num_str[-1])]
    elif num >= 20:
        if not int(num_str[-1]):
           return (below_hundred[int(num_str[0])-2])
        else:
            return(below_hundred[int(num_str[0])-2] +"-" + numbers[int(num_str[-1])])    
    return ""


def num2word(num):
    num_str = str(num)
    num_length = len(num_str)
    if num_length == 1:
        print(numbers[num])
    elif num_length == 2:
        print(two_places(num_str))
    elif num_length in [3, 4]:
        print(" ".join([numbers[int(num_str[0])] + " " + places[n-3] for n in range(num_length,2,-1)]) + " " + two_places(num_str[-2:]))


num2word(0)
num2word(10)
num2word(15)
num2word(20)
num2word(45)
num2word(165)
num2word(555)
num2word(9999)
