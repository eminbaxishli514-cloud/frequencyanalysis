# A script written for frequency analysis and basic decryption

letter_freq = {
    "e": 12.7020,
    "t": 9.0560,
    "a": 8.1670,
    "o": 7.5070,
    "i": 6.9660,
    "n": 6.7490,
    "s": 6.3270,
    "h": 6.0940,
    "r": 5.9870,
    "d": 4.2530,
    "l": 4.0250,
    "c": 2.7820,
    "u": 2.7580,
    "m": 2.4060,
    "w": 2.3600,
    "f": 2.2280,
    "g": 2.0150,
    "y": 1.9740,
    "p": 1.9290,
    "b": 1.4920,
    "v": 0.9780,
    "k": 0.7720,
    "j": 0.1530,
    "x": 0.1500,
    "q": 0.0950,
    "z": 0.0740
}

def counter(message, character):
    count = 0
    for i in message:
        if i == character:
            count += 1
    return count


y = """
lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi
bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx
ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr
yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk
lmird jk xjubt trmui jx ibndt wb wi kjb mk rmit bmiq bj rashmwk
rmvp yjeryrkb mkd wbi iwokwxwvmkvr mkd ijyr ynib urymwk
nkrashmwkrd bj ower m vjyshrbr rashmkmbwjk jkr cjnhd pmer
bj lr fnmhwxwrd mkd wkiswurd bj invp mk rabrkb bpmb pr
vjnhd urmvp bpr ibmbr jx rkhwopbrkrd ywkd vmsmlhr jx
urvjokwgwko ijnkdhrii ijnkd mkd ipmsrhrii ipmsr w dj kjb
drry ytirhx bpr xwkmh mnbpjuwbt lnb yt rasruwrkvr cwbp
qmbm pmi hrxb kj djnlb bpmb bpr xjhhjcwko wi bpr sujsru
msshwvmbwjk mkd wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr
pjsr bpmb bpr riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb
"""

# count total letters
total_letters = 0
for i in y:
    if i != " " and i != "\n":
        total_letters += 1

# cipher letter frequencies
cipher_freq = {}

for i in y:
    if i != " " and i != "\n":
        if i not in cipher_freq:
            cipher_freq[i] = counter(y, i) / total_letters * 100

# sort cipher frequencies (highest first)
cipher_sorted = {}
temp_cipher = cipher_freq.copy()

while temp_cipher:
    max_letter = ""
    max_value = -1
    for i in temp_cipher:
        if temp_cipher[i] > max_value:
            max_value = temp_cipher[i]
            max_letter = i
    cipher_sorted[max_letter] = max_value
    del temp_cipher[max_letter]

# sort English frequencies (highest first)
english_sorted = {}
temp_english = letter_freq.copy()

while temp_english:
    max_letter = ""
    max_value = -1
    for i in temp_english:
        if temp_english[i] > max_value:
            max_value = temp_english[i]
            max_letter = i
    english_sorted[max_letter] = max_value
    del temp_english[max_letter]

# build substitution mapping
mapping = {}

cipher_keys = list(cipher_sorted)
english_keys = list(english_sorted)

for i in range(len(cipher_keys)):
    mapping[cipher_keys[i]] = english_keys[i]

# decrypt text
decrypted = ""

for i in y:
    if i == " " or i == "\n":
        decrypted += i
    elif i in mapping:
        decrypted += mapping[i]
    else:
        decrypted += i

print("Cipher frequencies:")
print(cipher_freq)
print("\nSubstitution mapping:")
print(mapping)
print("\nDecrypted text:")
print(decrypted)