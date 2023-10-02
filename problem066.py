from csv import reader


def caesar_cipher_cracker():
    """
    This function prints a message encrypted by caesar cipher encryption.
    Input data will contain the number of encrypted messages in the first
    line.
    Next lines will contain the encrypted lines themselves. Each line is
    encoded with separate key!
    Answer should contain three first words of each decrypted line followed
    by the value of the key. Several answers should be separated with spaces.
    :return:
    """
    arq = open("problem066.csv")
    l1 = reader(arq, delimiter="\n")
    l1 = list(l1)
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
                "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    l3, l4, l5, words = [], [], [], ""
    for i in range(0, len(l1)):
        for k in range(0, len(l1[i])):
            l3.append(l1[i][k].split(" "))
    print(l3)
    for i in range(0, len(l3)):
        for k in range(0, len(l3[i])):
            if k >= 3:
                break
            l4.append(l3[i][k])
        l5.append(l4)
        l4 = []
    print(l5)
    for i in range(0, len(l5)):
        for k in range(0, len(l5[i])):
            for j in range(0, len(l5[i][k])):
                if k >= 3:
                    words += str(i + 1)
                    break
                words += alphabet[alphabet.index(l5[i][k][j]) - i - 1]
            words += " "
    print(words)


caesar_cipher_cracker()

# 5
# PMZM LQMA QV UG JWAAWU EPW EIVBA BW TQDM NWZMDMZ QB QA JTIKS IVL EPQBM IVL ZML ITT WDMZ
# YMFY FQQ RJS FWJ HWJFYJI JVZFQ BMJS RD LZNYFW LJSYQD BJJUX HFWYMFLJ RZXY GJ IJXYWTDJI
# OCZ YZVY WPMT OCZDM JRI YZVY DA WGJJY WZ OCZ KMDXZ JA OCZ VYHDMVGOT
# DA FTGCOU GCEJ QPG KPVQ C UGXGTCN YQTNF UVQPG YCNNU FQ PQV C RTKUQP OCMG
# QZFC DNZCP LYO DPGPY JPLCD LRZ EFCYD LWW LCZFYO MFE OZPD YZE XZGP

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O",
            "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# HERE DIES IN 8 THAT ALL MEN 5 THE DEAD BURY 21 BY DREAMS EACH 2 FOUR SCORE AND 11
