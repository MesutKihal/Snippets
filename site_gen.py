import os

os.chdir('C:\\Users\\Diamond\\Desktop')

def Website_gen(site_name, author, js, css):
    os.makedirs(f'C:\\Users\\Diamond\\Desktop\\{site_name}')
    os.chdir(f'C:\\Users\\Diamond\\Desktop\\{site_name}')
    print(f'Created ./{site_name}')
    with open(('index.html'), '+w') as f:
        f.close()
    print(f'Created ./{site_name}/index.html')
    if js == 'y':
        os.makedirs('js')
        print(f'Created ./{site_name}/js/')
    else:
        pass
    if css == 'y':
        os.makedirs('css')
        print(f'Created ./{site_name}/css/')
    else:
        pass

    return 'Done'


result = Website_gen(str(input('Site name: ')),
                     str(input('Author: ')),
                     str(input('Do you want a folder for JavaScript? ')),
                     str(input('Do you want a folder for CSS? ')))

print(result)
    
