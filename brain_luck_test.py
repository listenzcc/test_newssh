
def brain_luck(code, input):
    # here is a wrong understanding of function
    inputlist = list(e for e in input)
    idx_code = 0
    idx_input = 0
    pointer = 0
    lefts = []
    output = ''

    while idx_code < len(code):

        # print(idx_code)
        # print(code[idx_code])
        # print(output)
        # print(''.join(inputlist).encode('utf-8'))

        # > increment data pointer
        if code[idx_code] == '>':
            idx_input += 1
            idx_code += 1
            continue

        # < decrement data pointer
        if code[idx_code] == '<':
            idx_input -= 1
            idx_code += 1
            continue

        # , consume input at the data pointer
        if code[idx_code] == ',':
            pointer = ord(inputlist.pop(idx_input))
            idx_code += 1
            continue

        # . output the byte at the data pointer
        if code[idx_code] == '.':
            output += chr(pointer)
            idx_code += 1
            continue

        # + increment data pointer
        if code[idx_code] == '+':
            pointer += 1
            pointer %= 256
            idx_code += 1
            continue

        # - increment data pointer
        if code[idx_code] == '-':
            pointer -= 1
            pointer %= 256
            idx_code += 1
            continue

        # [ store idx_code in lefts
        if code[idx_code] == '[':
            if pointer == 0:
                while code[idx_code] != ']':
                    idx_code += 1
                idx_code += 1
                continue
            lefts.append(idx_code)
            idx_code += 1
            continue

        # ] retrace to last [
        if code[idx_code] == ']':
            if pointer == 0:
                lefts.pop()
                idx_code += 1
                continue
            idx_code = lefts.pop()
            continue

        idx_code += 1

    return output


print(brain_luck(',+[-.,+]', 'Codewars' + chr(255)))
print('Codewars')

print(brain_luck(',[.[-],]', 'Codewars' + chr(0)))
print('Codewars')

#print(brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)))
print(chr(72))
