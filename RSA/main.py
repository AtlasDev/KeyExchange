#!/usr/bin/python

import functions, random, math, time

succeded = 0;

def runRSA():
    startTime = int(round(time.time() * 1000));
    global succeded;
    functions.log("GLOBAL", "===== Generating keys =====");
    
    functions.log("SERVER", "Generating random P...");
    p = functions.getPrime();
    functions.log("SERVER", "P = %s." % p);
    
    functions.log("SERVER", "Generating random Q...");
    q = functions.getUniquePrime(p);
    functions.log("SERVER", "Q = %s." % q);
    
    functions.log("SERVER", "Calculating N...");
    n = p*q;
    functions.log("SERVER", "N = %s." % n);
    
    functions.log("SERVER", "Calculating phi of N...");
    phiN = (p-1)*(q-1);
    functions.log("SERVER", "phiN = %s." % phiN);

    functions.log("SERVER", "Generating E...");
    e = functions.getCoprime(n);
    functions.log("SERVER", "E = %s." % e);

    functions.log("SERVER", "Generating K...");
    k = 2;
    functions.log("SERVER", "K = %s." % k);

    functions.log("SERVER", "Calculating D...");
    d = (k*phiN+1)/e;
    functions.log("SERVER", "D = %s." % d);

    functions.log("GLOBAL", "===== Key calculation finished =====");

    functions.log("GLOBAL", "===== starting encrypting message =====");

    m = random.randint(100000000000000, 999999999999999);
    functions.log("CLIENT", "Number to encrypt (M): %s" % m);

    functions.log("CLIENT", "Encrypting the message...");
    c = functions.calcC(m, e, n);
    functions.log("CLIENT", "C = %s." % c);

    functions.log("SERVER", "Decrypting the message...");
    decMsg = math.pow(c, d);
    functions.log("SERVER", "Decrypted MSG = %s." % decMsg);

    if m == decMsg:
        functions.log("SERVER", "RSA succeded!");
    else:
        functions.log("SERVER", "RSA failed...");
        
    endTime = int(round(time.time() * 1000));
    totalTime = endTime - startTime;
    functions.log("GLOBAL", "Calculations took %d milliseconds" % totalTime);
    
runRSA();
