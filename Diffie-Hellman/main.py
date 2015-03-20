#!/usr/bin/python

import functions

failed = False;
succeded = 0;

def runDiffie():
    global succeded;
    print("Generating random G...");
    g = functions.getPrime();
    print "G = %s." % g

    print("Generating random P...");
    p = functions.getPrime();
    while p == g:
        p = functions.getPrime();
    print "P = %s." % p

    print("Generating random Private Client Key...");
    pck = functions.getPrime();
    print "Private Client Key = %s." % pck

    print("Generating random Private Server Key...");
    psk = functions.getPrime();
    print "Private Server Key = %s." % psk

    print("Calculate Client Public Key...");
    cpk = functions.calcKey(g, pck, p);
    print "Client Public Key = %s." % cpk

    print("Calculate Server Public Key...");
    spk = functions.calcKey(g, psk, p);
    print "Server Public Key = %s." % spk

    print("Calculate Client Shared Secret...");
    css = functions.calcKey(spk, pck, p);
    print "Client Shared Secret = %s." % css

    print("Calculate Server Shared Secret...");
    sss = functions.calcKey(cpk, psk, p);
    print "Server Shared Secret = %s." % sss

    if(css == sss):
        print("Diffie-Hellman Key Exchange succeed!");
        succeded += 1;
        print "This is the", succeded, "time it has gone well."
        return True;
    else:
        print("Diffie-Hellman Key Exchange failed!");
        print "This been gone well for", succeded, "times."
        return False;

while runDiffie():
    print("Starting a new round!");
