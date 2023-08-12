def swap_case(s):
    changed = ""
    for i in s:
        if i.islower():
            changed += i.upper()
        else:
            changed += i.lower()
    return changed

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
