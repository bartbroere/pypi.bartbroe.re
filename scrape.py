import json
import os

import requests


def deobfuscate_download_url(ml, mi):
    mi = mi.replace('&lt;', '<')
    mi = mi.replace('&#62;', '>')
    mi = mi.replace('&#38;', '&')
    output = ''
    for i in range(len(mi)):
        output += chr(ml[ord(mi[i]) - 47])
    return output


gohlke_index = requests.get('https://www.lfd.uci.edu/~gohlke/pythonlibs/',
                            headers={'User-agent': 'Mozilla/5.0'}).text

packages = set()
for call_to_dl in gohlke_index.split("onclick")[1:-1]:
    ml = json.loads(call_to_dl.split("dl(")[1].split(", ")[0])
    mi = json.loads(call_to_dl.split(", ")[1].split(")")[0])
    download_url = 'https://download.lfd.uci.edu/pythonlibs/' + deobfuscate_download_url(ml, mi)
    download_filename = download_url.split("/")[-1]
    package_name = download_filename.split("-")[0]
    packages.add(package_name)
    if not os.path.exists(os.path.join('docs', package_name.lower())):
        os.mkdir(os.path.join('docs', package_name.lower()))
        with open(os.path.join('docs', package_name.lower(), 'index.html'), 'a') as package_index:
            package_index.write(f"""
            <html>
            <head>
                <title>{package_name}</title>
            </head>
            <body>
            """)
    with open(os.path.join('docs', package_name.lower(), 'index.html'), 'a') as package_index:
        package_index.write(f"""
            <a href="{download_url}">{download_filename}</a>
        """)

with open('docs/index.html', 'w') as main_package_index:
    main_package_index.write("""
    <html>
    <head>
    <title>pypi extra wheels</title>
    </head>
    <body>
    """)
    for package in packages:
        with open(os.path.join('docs', package.lower(), 'index.html'), 'a') as package_index:
            package_index.write(f"""
                </body>
                </html>
            """)
        main_package_index.write(f'<a href="{package}">{package}</a>')
        print(package)
    main_package_index.write("""
    </body>
    </html>
    """)
