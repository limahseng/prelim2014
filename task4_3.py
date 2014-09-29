def hex2dec(hexnum):
    if len(hexnum) == 1: # terminating case position 0
        return int(hexnum)
    else: # recursive case positions 1 to 3
        return hex2dec(hexnum[0:len(hexnum)-1]) + int(hexnum[len(hexnum)-1]) * 2

def bin2dec(bin):
    dec = 0
    factor = 1
    while bin > 0:
        if bin % 10 == 1:
            dec += factor
        bin //= 10
        factor *= 2
    return dec

def bin2decs(bin):
    dec = 0
    factor = 1
    while len(bin) > 0:
        dec += factor * int(bin[-1])
        bin = bin[0:-1]
        factor *= 2
    return dec

def bin2decr(bin):
    if len(bin) == 1:
        return int(bin)
    else:
        return bin2decr(bin[0:-1]) * 2 + int(bin[-1])

def ipv6_bin2dec(ipv6addr):
    # separate into sections of 4 hexadecimal digits after uppercase conversion
    sections = ipv6addr.upper().split(':')
    result = ''
    for section in sections:
        group = ''
        for digit in section:
            group += hexmap[digit]
        result += str(bin2decr(group)) + ':'
    print(result)


def ipv6r(address):
    if len(address) == 1: # terminating case
        group = ''
        for digit in address[0]:
            group += hexmap[digit]
        return str(bin2decr(group))
    else:
        mid = len(address) // 2
        return ipv6r(address[:mid]) + ipv6r(address[mid:])

def ipv6_bin2decr(ipv6addr):
    # separate into sections of 4 hexadecimal digits after uppercase conversion
    sections = ipv6addr.upper().split(':')
    print(ipv6r(sections))

# set up hexadecimal to binary mapping dictionary
hexmap = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', \
          '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}

# main
print(bin2dec(1011))
print(bin2decs('1011'))
print(bin2decr('1011'))
ipv6_bin2dec('2001:0db8:0000:0000:0000:ff00:0042:8329')
ipv6_bin2decr('2001:0db8:0000:0000:0000:ff00:0042:8329')
