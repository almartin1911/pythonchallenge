# ex1.py
# http://www.pythonchallenge.com/pc/def/map.html

cryptic_text = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq
ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm
jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''

url = "map"
cryptic_text = url

decrypted_text = ""

for char in cryptic_text:
    char_int = ord(char)
    # print(char_int, end=' ')
    if char_int != 46 and char_int != 32 and char_int != 10:
        char_int += 2
        if char_int > 122:
            char_int -= 26
    decrypted_text += chr(char_int)

print(f"Original: {cryptic_text}")
print(f"Decrypted: {decrypted_text}")

# TODO: Implement with string.maketrans()
# TODO: Optimize the char rotation for punctuation symbols
# Solution: Rotate chars, then apply the algorithm to the URL
# Result: http://www.pythonchallenge.com/pc/def/ocr.html
