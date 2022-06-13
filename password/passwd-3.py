from password_manager.vault import Vault


def set_1stkey():
    passwd = input('Set Protect Password: ')
    with Vault('fstkey') as vault:
        vault['fstkey'] = {
            'password': passwd
        }
        return vault['fstkey']['password']


def reset_1stkey():
    pass


def store_passwd():
    mark = input('Mark: ')
    password = input('Enter passwd: ')
    try:
        with Vault(mark) as vault:
            vault[mark] = {
                'password': password
            }
            return vault[mark]['password']
    except ValueError as e:
        return e


def get_passwd():
    mark = input('Mark: ')
    try:
        with Vault(mark) as vault:
            return vault[mark]['password']
    except ValueError as e:
        return e


def first_step():
    with Vault('fstkey') as vault:
        print(vault.data)
        if 'fstkey' in vault.data:
            return True
        else:
            return False


if __name__ == '__main__':
    # print(store_passwd())
    print(get_passwd())
    # print(first_step())
    # if not first_step():
    #     set_1stkey()
    # else:
    #     print(get_passwd())
