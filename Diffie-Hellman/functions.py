import random, math, time, logging

def isPrime(p):
    if(p==2): return True
    if(not(p&1)): return False
    return pow(2,p-1,p)==1

def getPrime():
    isFound = False;
    while not isFound:
        keyLength = 309;
        r = random.randint(10**(keyLength-1), 10**keyLength - 1);
        if isPrime(r):
            return r;

def calcKey(g, pk, p):
    startTime = int(round(time.time() * 1000));
    key = long(pow(g,pk,p));
    endTime = int(round(time.time() * 1000)) - startTime;
    print("Key calculation took %s milliseconds." % endTime);
    logging.info("Key calculation took %s milliseconds." % endTime);
    return key;
