#!/usr/bin/python

a = 60
b = 13
c = 0


def binary_AND():
    c = a & b
    #first attempt
    #print(str(bin(a)[2:])+"\n&"+str(bin(b)[2:])+"\n="+str(bin(c)[2:]))

    #second attempt, much easier to read
    print("& (Binary AND) copies the bit if it exists in both \n")
    print("  "+format(a, '08b')+
        "\n& "+format(b, '08b')+
        "\n= "+format(c, '08b'))

    return

def binary_OR():
    c = a | b
    print("| (Binary OR) copies bit if it exists in either \n")
    print("  "+format(a, '08b')+
        "\n| "+format(b, '08b')+
        "\n= "+format(c, '08b'))

    return

def binary_XOR():
    c = a ^ b
    print("^ (Binary XOR) copies bit if it exists in one but not both \n")
    print("  "+format(a, '08b')+
        "\n^ "+format(b, '08b')+
        "\n= "+format(c, '08b'))

    return

def binary_ones_compliment():
    c = (~a)
    print("~ (Binary Ones Compliment) flips the bit \n")
    print(" (~"+format(a, '08b')+")"+
        "\n=  "+format(c, '08b'))
    return

def binary_left_shift():
    c = a << 2
    print("<< (Binary Left Shift) move left operand LEFT by right operand number of bits \n")
    print("  "+format(a, '08b')+" << 2"+
        "\n= "+format(c, '08b'))

    return

def binary_right_shift():
    c = a >> 2
    print(">> (Binary Right Shift) move left operand RIGHT by right operand number of bits \n")
    print("  "+format(a, '08b')+" >> 2"+
        "\n= "+format(c, '08b'))

    return

if __name__ == "__main__":
    binary_AND()
    print("\n####################\n")
    binary_OR()
    print("\n####################\n")
    binary_XOR()
    print("\n####################\n")
    binary_ones_compliment()
    print("\n####################\n")
    binary_left_shift()
    print("\n####################\n")
    binary_right_shift()
