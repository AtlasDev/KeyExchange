import random, math, time, logging

logging.basicConfig(filename='RSA.log',level=logging.DEBUG);

def isPrime(p):
    if(p==2): return True
    if(not(p&1)): return False
    return pow(2,p-1,p)==1

def getPrime():
    while True:
        r = random.randint(1, 9);
        if isPrime(r):
            return r;

def getUniquePrime(other):
    while True:
        r = getPrime();
        if r is not other:
            return r;

def gcd(a, b):
    return gcd(b, a % b) if b else a

def isCoprime(a, b):
    return gcd(a, b) == 1
    
def getCoprime(number):
    isFound = False;
    while not isFound:
        r = random.randint(2, number);
        if isCoprime(number, r):
            return r;

def calcC(multiply, power, modulus):
    hugeStepLog2 = 32
    hugeStep = 2 ** hugeStepLog2
    hugeMultiply = multiply
    for i in range(hugeStepLog2):
        hugeMultiply = (hugeMultiply * hugeMultiply) % modulus

    largeStepLog2 = 16
    largeStep = 2 ** largeStepLog2
    largeMultiply = multiply
    for i in range(largeStepLog2):
        largeMultiply = (largeMultiply * largeMultiply) % modulus

    output = 1
    i = 0

    while i + hugeStep <= power:
        i += hugeStep
        output = (output * hugeMultiply) % modulus

    while i + largeStep <= power:
        i += largeStep
        output = (output * largeMultiply) % modulus

    while i < power:
        i += 1
        output = (output * multiply) % modulus

    return output    

def log(loc, msg):
    print(loc + " | " + msg);
    logging.info(loc + " | " + msg);
