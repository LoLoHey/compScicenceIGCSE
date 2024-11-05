# Calculation of the max positive and negative possible with sign 2's complement
# Return True if the conversion is possible or False if impossible
def checkPossible(denary, bits):
    max_pos = 2**(bits - 1) - 1
    max_neg = -2**(bits - 1)
    
    if max_neg <= denary <= max_pos :
        return True
    else:
        return False

# Conversion following the two's complement
def denaryToBinary(denary, bits):
    
    #Initialisation of the binary
    binary = ''
    
    #first case if the denary is positive:
    if denary < 0:
        # (<< bitwise operator) x << y: same as multiplying x by 2**y.
        # +(1 << bits) same as adding 2^bits
        denary = denary + (1 << bits)
 
    for i in range(bits):
        binary = str(denary%2) + binary
        denary = denary // 2

    return binary

# Conversion following the two's complement
def denaryTobinary_SAVE(denary, bits):
    
    #Initialisation of the binary
    binary = ''
    
    #first case if the denary is positive:
    if denary >= 0:
        for i in range(bits-1):
            binary = str(denary%2) + binary
            denary = denary // 2
        binary = '0' + binary
    #second case if the denary is negative
    elif denary < 0:
        denary = denary - 2**bits
        for i in range(bits-1):
            binary = str(denary%2) + binary
            denary = denary // 2
        binary = '1' + binary
    #The denary is not an int
    else:
        print('Conversion Error')
    return binary
# Get the input from the user + check if possible

def getInput():

    # Try a correct input to get the input from the user.
    try:
        denary_input, nb_of_bit = map(int, input("Enter the denary and the number of bits (separated by spaces): ").split())
    except:
        print('Error: Please follow the required format')
        return getInput()
    
    #check if it possible to do the conversion with the number of bits
    if checkPossible(denary_input, nb_of_bit):
        return denary_input, nb_of_bit
    else:
        print('overflow error, number of bits insufficient')
        return getInput()