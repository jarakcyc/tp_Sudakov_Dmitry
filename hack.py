from ciphers import *


def get_gistagram(text):
    cnt = [0] * alpha
    for c in list(text):
        val = ord(c.lower())
        if (val >= ord('a') and val <= ord('z')):
            cnt[val - ord('a')] += 1
    return cnt


def get_base_gista(model):
    with open(model, 'r') as f:
        lines = f.readlines()
    base_gista = []
    for x in lines:
        base_gista.append(int(x))
    return base_gista


def match_gista(gista, base_gista):
    res = 0
    for i in range(alpha):
        res += abs(base_gista[i] - gista[i]) ** 2
    return res


def hack_caesar(text, model):
    base_gista = get_base_gista(model)
    best = -1
    shift = 0
    for key in range(alpha):
        cur = get_gistagram(encode_caesar(text, key))
        val = match_gista(cur, base_gista)
        if (best == -1 or val < best):
            best = val
            shift = key
    return encode_caesar(text, shift)

# ---------------------------------------------------------------------------


def get_symbols_count(text):
    cnt = [0] * alpha
    for c in list(text):
        s = c.lower()
        if (is_eng(s)):
            cnt[ord(s) - ord('a')] += 1
    return cnt


def get_match_index(text):
    cnt = get_symbols_count(text)
    n_symbols = 0
    for i in cnt:
        n_symbols += i
    res = 0
    for i in range(alpha):
        res += (cnt[i] / n_symbols) ** 2
    return res


def get_base_index(model):
    with open(model, 'r') as f:
        l = f.readlines()
        return float(f[0])


def compare_indexes(index, base_index):
    epsilon = 0.01
    return bool(abs(index - base_index) < epsilon)


def hack_vigenere(text, model):
    text = list(text)
    base_gista = []
    with open(model, 'r') as f:
        l = f.readlines()
        base_index = float(l[0])
        for x in range(1, alpha + 1):
            base_gista.append(int(l[x]))

    key_size = 1

    # берем каждый step-ый символ начиная с start
    def get_line(start, step, shift):
        line = ""
        i = start
        while (i < len(text)):
            line += shift_symbol(text[i], shift)
            i += step
        return line

    # находим длину ключа
    while True:
        good = 0
        for i in range(key_size):
            cur_line = get_line(i, key_size, 0)
            index = get_match_index(cur_line)
            if (compare_indexes(index, base_index)):
                good += 1
        if (good / key_size > 0.8):
            break
        key_size += 1

    # находим относительные сдвиги для всех строк 1...key_size-1 относительно
    # 0-ой
    first_line = get_line(0, key_size, 0)
    shifts = [0]
    for i in range(1, key_size):
        best_shift = 0
        max_index = 0
        for shift in range(0, alpha):
            cur_line = get_line(i, key_size, -shift)
            cnt_1 = get_symbols_count(first_line)
            cnt_2 = get_symbols_count(cur_line)
            n_1 = 0
            for j in cnt_1:
                n_1 += j
            n_2 = 0
            for j in cnt_2:
                n_2 += j
            cur_index = 0
            for j in range(alpha):
                cur_index += cnt_1[j] * cnt_2[j] / n_1 / n_2
            if (cur_index > max_index):
                max_index = cur_index
                best_shift = shift
        shifts.append(best_shift)

    # теперь, зная сдвиги всех строк относительно первой, задача превращается
    # в расшифровку шифра Цезаря
    result_text = ""
    for i in range(len(text)):
        result_text += shift_symbol(text[i], -shifts[i % key_size])
    best = -1
    shift = 0
    for key in range(alpha):
        cur = get_gistagram(encode_caesar(result_text, key))
        val = match_gista(cur, base_gista)
        if (best == -1 or val < best):
            best = val
            shift = key
    return encode_caesar(result_text, shift)
