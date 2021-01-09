

if __name__ == "__main__":

    last_name = ''
    with open('storage/saves.txt', 'r', encoding='utf-8') as file:
        file.seek(0)
        last_name = file.readline()
        file.close()
        pass
    print('last_name == {0}'.format(last_name))

    print('Enter the additional name:')
    name = ''
    name = input()
    if name != '' or name != last_name:
        with open('storage/saves.txt', 'w', encoding='utf-8') as file:
            file.truncate()
            file.seek(0)
            file.write(name.lower())
            file.close()
            pass
        pass

    print('Name is {0} \t Period is {1}'.format(name, period))

    pass