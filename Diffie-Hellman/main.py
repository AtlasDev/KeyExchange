#!/usr/bin/python

import functions, logging

logging.basicConfig(filename='diffie-hellman.log',level=logging.DEBUG);
failed = False;
succeded = 0;

def runDiffie():
    global succeded;
    print("Generating random G...");
    logging.info("Generating random G...");
    g = functions.getPrime();
    print("G = %s." % g);
    logging.info("G = %s." % g);

    print("Generating random P...");
    logging.info("Generating random P...");
    p = functions.getPrime();
    while p == g:
        p = functions.getPrime();
    print("P = %s." % p);
    logging.info("P = %s." % p);

    print("Generating random Private Client Key...");
    logging.info("Generating random Private Client Key...");
    pck = functions.getPrime();
    print("Private Client Key = %s." % pck);
    logging.info("Private Client Key = %s." % pck);

    print("Generating random Private Server Key...");
    logging.info("Generating random Private Server Key...");
    psk = functions.getPrime();
    print("Private Server Key = %s." % psk);
    logging.info("Private Server Key = %s." % psk);

    print("Calculate Client Public Key...");
    logging.info("Calculate Client Public Key...");
    cpk = functions.calcKey(g, pck, p);
    print("Client Public Key = %s." % cpk);
    logging.info("Client Public Key = %s." % cpk);

    print("Calculate Server Public Key...");
    logging.info("Calculate Server Public Key...");
    spk = functions.calcKey(g, psk, p);
    print("Server Public Key = %s." % spk);
    logging.info("Server Public Key = %s." % spk);

    print("Calculate Client Shared Secret...");
    logging.info("Calculate Client Shared Secret...");
    css = functions.calcKey(spk, pck, p);
    print("Client Shared Secret = %s." % css);
    logging.info("Client Shared Secret = %s." % css);

    print("Calculate Server Shared Secret...");
    logging.info("Calculate Server Shared Secret...");
    sss = functions.calcKey(cpk, psk, p);
    print("Server Shared Secret = %s." % sss);
    logging.info("Server Shared Secret = %s." % sss);

    if(css == sss):
        print("Diffie-Hellman Key Exchange succeed!");
        logging.info("Diffie-Hellman Key Exchange succeed!");
        succeded += 1;
        print("This is the %s time it has gone well." % succeded);
        logging.info("This is the %s time it has gone well." % succeded);
        return True;
    else:
        print("Diffie-Hellman Key Exchange failed!");
        logging.info("Diffie-Hellman Key Exchange failed!");
        print("This been gone well for %s times." % succeded);
        logging.info("This been gone well for %s times." % succeded);
        return False;

while runDiffie():
    print("Starting a new round!");
    logging.info("Starting a new round!");
