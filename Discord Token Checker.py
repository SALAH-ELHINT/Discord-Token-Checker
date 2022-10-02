'''
by SALAH-ELHINT "https://github.com/SALAH-ELHINT/Discord-Token-Checker.git"
'''
import pip

install = [
    'requests'
    'os'
]

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])


for i in range(2):
    try:
        import requests
        import time
        import json
        import os
    except:
        for i in range(len(install)):
            import_or_install(install[i])

print()
print('''\033[1;31;40m 
                              ____   _                              _     ____  _                  _                                                        
                             |  _ \ (_) ___   ___   ___   _ __   __| |   / ___|| |__    ___   ___ | | __  ___  _ __ 
                             | | | || |/ __| / __| / _ \ | '__| / _` |  | |    | '_ \  / _ \ / __|| |/ / / _ \| '__|
                             | |_| || |\__ \| (__ | (_) || |   | (_| |  | |___ | | | ||  __/| (__ |   < |  __/| | 
                             |____/ |_||___/ \___| \___/ |_|    \__,_|   \____||_| |_| \___| \___||_|\_\ \___||_|

             © Discord Token Checker by SALAH-ELHINT
\033''')
while True:
    print('''\033[1;34;40m''', end='')
    combo_name = input('Entry Combo: \033[1;33;40m')
    print('''\033[1;34;40m''', end='')
    # combo_name=input('Entry Proxy: \033[1;33;40m')
    # print('''\033[1;34;40m''',end='')
    if os.path.exists(f'{combo_name}.txt'):  # and os.path.exists(f'{proxy_name}.txt')
        break
print()
file_combo = open(f'{combo_name}.txt', 'r+')
# file_proxy = open(f'{proxy_name}.txt', 'r+')
file_combo_details = open('tokens_details.txt', 'a+')
file_combo_successful = open('tokens_successful.txt', 'a+')
n, bad_acc, good_acc = -1, 0, 0

def line_num(name_file, line_count=0):
    for line in name_file:
        if len(line)>=20 and '.' in line and ' - ' not in line:
            if line != '\n':
                line_count = line_count + 1
    return line_count

print(f'''\033[1;32;40m _________ Settings _______________________________________________\n\
|\n| \033[1;34;40m[INFO]\033[0;0m\033[1;32;40m [>>] {combo_name}.txt Loaded : \033[1;33;40m{line_num(file_combo)}\033[0;0m\033[1;32;40m
|\n\
|\n| \033[1;34;40m[INFO]\033[0;0m\033[1;32;40m [>>] proxy.txt Loaded : \033[1;33;40m0\033[0;0m\033[1;32;40m
|\n\
|\n\
|_________________________________________________________________\033\n''')
time.sleep(2)
file_combo = open(f'{combo_name}.txt', 'a+')
file_combo.writelines('\n')
file_combo.close()
file_combo = open(f'{combo_name}.txt', 'r+')
# file_proxy = open(f'{proxy_name}.txt', 'r+')

try:
    for line_combo in file_combo:
        file_combo = open(f'{combo_name}.txt', 'r+')
        n = n + 1
        if len(line_combo) >= 20 and '.' in line_combo and ' - ' not in line_combo:
            print(
                f'\033[1;33;40m Checker is running - \033[1;32;40m[+] Good tokens  : [{good_acc}] \033[1;33;40m~~~ \033[1;31;40m[-] Bad tokens  :  [{bad_acc}] ',
                end='\r')
            token = line_combo.rstrip()
            header = {
                'authorization': token
            }
            r = requests.get(f"https://discordapp.com/api/v7/users/@me",
                             headers=header)
            if r.reason != 'Unauthorized':
                t = f'token: {token}'
                print(f'\033[1;32;40m{t}')
                file_combo_details.writelines(t + '\n')
                file_combo_successful.writelines(token + '\n')
                file_combo = open(f'{combo_name}.txt', "r+")
                line_combo = file_combo.readlines()
                line_combo[n] = (f'{token} - Token is valid\n')
                file_combo = open(f'{combo_name}.txt', "w+")
                file_combo.writelines(line_combo)
                file_combo.close()
                e = r.json()
                good_acc = good_acc + 1
                for i in e:
                    y = str(i)
                    yy = f'{i}: {e[y]}'
                    print(yy)
                    file_combo_details.writelines(yy + '\n')
                file_combo_details.writelines('#' * 80 + '\n')
            else:
                file_combo = open(f'{combo_name}.txt', "r+")
                line_combo = file_combo.readlines()
                line_combo[n] = (f'{token} - Connection error\n')
                file_combo = open(f'{combo_name}.txt', "w+")
                file_combo.writelines(line_combo)
                file_combo.close()
                print(f'\033[1;31;40m{token} | Invalid token')
                bad_acc = bad_acc + 1
            print('\033[1;34;40m#' * 80)
except:
    print()
    print('\033[1;33;40m\n                  #############################                  HTTP ERROR 403                  #############################\n\033[1;31;40m')
finally:
    print()
    print(f'\n\033[1;33;40m Checker result - \033[1;32;40m[+] Good tokens  : [{good_acc}] \033[1;33;40m~~~ \033[1;31;40m[-] Bad tokens  :  [{bad_acc}] ')

'''
by SALAH-ELHINT "https://github.com/SALAH-ELHINT/Discord-Token-Checker.git"
'''