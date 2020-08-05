if os.name == 'posix':
    # osx
    driver_path = '/usr/local/bin/chromedriver'
elif os.name == 'nt':
    # win32
    driver_path = 'C:\chromedriver\chromedriver'
else:
    print('Unknown operating system!!!')
    exit()