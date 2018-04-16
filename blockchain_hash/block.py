import json, os, hashlib, binascii

blockchain_dir = os.curdir + '/blockchain/'

hashlenth = 4

def get_files():
    files = os.listdir(blockchain_dir)
    return sorted([int(i) for i in files])

def get_hash(filename):
    res = 0
    letter = ord('a')
    file = open(blockchain_dir + filename, 'rb').read()
    with open(blockchain_dir + filename, 'rb') as file:
        for line in file:
            for c in line:
                res += c
    res -= (10 + (32 * 3))#remove last line and 3 spaces
    res %= (10 ** hashlenth + 1)
    res = list(str(res))
    for i in range(int(hashlenth/2)):
        res[2*i+1] = chr(int(res[2*i+1], 16) + letter)
        letter += 1
    return ''.join(res)


def check_integrity():
    results = []
    files = get_files()

    for file in files[1:]:
        f = open(blockchain_dir + str(file))
        h = json.load(f)['hash']

        prev_file = str(file - 1)
        actual_hash = get_hash(prev_file)

        if h == actual_hash:
            res = 'Ok'
        else:
            res = 'Corrupted'

        results.append({'block' : prev_file, 'result' : res})

    return results

def write_block(name, prev_hash=''):
    files = get_files()
    prev_file = files[-1]
    filename = str(prev_file + 1)
    prev_hash = get_hash(str(prev_file))

    data = {'hash' : prev_hash,
            'name' : name}

    with open(blockchain_dir + filename, 'w') as file:
        json.dump(data, file, ensure_ascii=False)

def main():
    pass
    write_block(name='Mateusz')
    #print(check_integrity())

if __name__ == '__main__':
    main()
