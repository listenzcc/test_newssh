
def brain_luck(code, input):
    # here is a wrong understanding of function
    inputlist = list(e for e in input)
    inputlist.reverse()
    idx_code = 0
    pointer = 0
    belt = [0]
    lefts = []
    output = ''

    while idx_code < len(code):

        # print(code[0:idx_code])
        # > increment data pointer
        if code[idx_code] == '>':
            if pointer == len(belt)-1:
                belt.append(0)
                pointer += 1
            else:
                pointer += 1
            idx_code += 1
            continue

        # < decrement data pointer
        if code[idx_code] == '<':
            if pointer == 0:
                belt.reverse()
                belt.append(0)
                belt.reverse()
                pointer += 1
            pointer -= 1
            idx_code += 1
            continue

        # , consume input at the data pointer
        if code[idx_code] == ',':
            if len(belt) == 0:
                belt.append(ord(inputlist.pop()))
            else:
                belt[pointer] = ord(inputlist.pop())
            idx_code += 1
            continue

        # . output the byte at the data pointer
        if code[idx_code] == '.':
            output += chr(belt[pointer])
            idx_code += 1
            continue

        # + increment data pointer
        if code[idx_code] == '+':
            belt[pointer] += 1
            belt[pointer] %= 256
            idx_code += 1
            continue

        # - increment data pointer
        if code[idx_code] == '-':
            try:
                belt[pointer] -= 1
            except:
                print(pointer)
                print(belt)
                print(output)
                return 0
            belt[pointer] %= 256
            idx_code += 1
            continue

        # [ store idx_code in lefts
        if code[idx_code] == '[':
            if belt[pointer] == 0:
                left_num = 0
                while True:
                    if code[idx_code] == '[':
                        left_num += 1
                    if code[idx_code] == ']':
                        left_num -= 1
                        if left_num == 0:
                            break
                    idx_code += 1
                idx_code += 1
                continue
            lefts.append(idx_code)
            idx_code += 1
            continue

        # ] retrace to last [
        if code[idx_code] == ']':
            if belt[pointer] == 0:
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

print(brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)))
print(chr(72))

print(brain_luck(
    '++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.', ''))

print(brain_luck(',>+>>>>++++++++++++++++++++++++++++++++++++++++++++>++++++++++++++++++++++++++++++++<<<<<<[>[>>>>>>+>+<<<<<<<-]>>>>>>>[<<<<<<<+>>>>>>>-]<[>++++++++++[-<-[>>+>+<<<-]>>>[<<<+>>>-]+<[>[-]<[-]]>[<<[>>>+<<<-]>>[-]]<<]>>>[>>+>+<<<-]>>>[<<<+>>>-]+<[>[-]<[-]]>[<<+>>[-]]<<<<<<<]>>>>>[++++++++++++++++++++++++++++++++++++++++++++++++.[-]]++++++++++<[->-<]>++++++++++++++++++++++++++++++++++++++++++++++++.[-]<<<<<<<<<<<<[>>>+>+<<<<-]>>>>[<<<<+>>>>-]<-[>>.>.<<<[-]]<<[>>+>+<<<-]>>>[<<<+>>>-]<<[<+>-]>[<+>-]<<<-]', chr(10)))
