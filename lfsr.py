from hashlib import sha256

from time import time, sleep


def xor(a, b):
    if a == b:
        return 0
    return 1


def lfsr():  # vor fi alese pozitiile 1, 2, 4, 5 si 8
    password = []
    seed = int(time() * 1000.0)
    hashObj = sha256()
    hashObj.update(bytes(str(seed), encoding="ascii"))
    hashed_seed = hashObj.hexdigest()
    hashed_seed_binary = [bin(ord(d)) for d in hashed_seed]
    seed_digits = []
    for each in hashed_seed_binary:
        for bit in each[2:]:
            seed_digits.append(bit)
    for each in range(16):
        password.append(seed_digits.pop())
        seed_digits.insert(0, xor(xor(xor(xor(seed_digits[1], seed_digits[2]), seed_digits[4]), seed_digits[5]),
                                  seed_digits[8]))
    return int("".join(str(x) for x in password), 2)


def shuffle(lst):
    for each in range(len(lst)):
        sleep(0.1)
        index_to_swap = lfsr() % len(lst)
        aux = lst[index_to_swap]
        lst[index_to_swap] = lst[each]
        lst[each] = aux
    return lst
