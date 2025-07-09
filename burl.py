#!/usr/bin/python3
# Base64url encoder & decoder — Accepts n (multiple layer) encoding and decoding

from urllib.parse import quote_plus, unquote_plus
import sys, pyinputplus as pinp

def _help():
    print("""USAGE:  python3 burl.py -p [payload] -m [encode/decode] -n [optional] 
    where:
        -p  Specifies the payload to be encoded or decoded.
        -m  Specifies the mode. Either encode or decode.
        -n  Specifies the number of times to encode or decode. Default is set to 1.
              But in the case of decoding, if omitted, full decode would be used.
    """)
    sys.exit()
    
def encode(payload, n=1):
    '''Encode the payload/url n times'''
    for _ in range(n):
        payload = quote_plus(payload)
    return payload

def decode(payload, n=1):
    '''Decode the payload/url n times'''
    for _ in range(n):
        payload = unquote_plus(payload)
    return payload

def full_decode(payload):
    '''Fully decode an encoded payload/url until stable'''
    prev = ""
    while payload != prev:
        prev = payload
        payload = unquote_plus(payload)
    return payload

if __name__ == '__main__':
    args = sys.argv
    
    # Print Help
    if '-h' in args:
        _help()
        
    n = 1  # Default layer count

    # Get payload
    if '-p' in args:
        payload = args[args.index('-p') + 1]
    else:
        payload = pinp.inputStr("Enter the URL or payload: ")

    # Get mode
    if '-m' in args:
        mode = args[args.index('-m') + 1].lower()
    else:
        mode = pinp.inputMenu(['encode', 'decode'], prompt="What would you like to do?\n", numbered=True)

    # Get number of layers, else execute full decode if mode was set to decode
    if '-n' in args:
        try:
            n = int(args[args.index('-n') + 1])
        except:
            print("Invalid number for -n. Defaulting to 1.")
            n = 1
    elif mode == 'decode':
        # Run full decode
        result = full_decode(payload)
        print(result)
        sys.exit()
        
    # Execute
    if mode == 'encode':
        result = encode(payload, n)
    elif mode == 'decode':
        result = decode(payload, n)
    else:
        print("Invalid mode.")
        sys.exit(1)

    print(result)