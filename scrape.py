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
                <style>
                body{{margin:40px auto;max-width:650px;line-height:1.6;font-size:18px;color:#444;padding:0 10px}}
                h1,h2,h3{{line-height:1.2}}
                </style>
                <title>{package_name.lower()}</title>
            </head>
            <body>
            """)
    with open(os.path.join('docs', package_name.lower(), 'index.html'), 'a') as package_index:
        package_index.write(f"""
            <a href="{download_url}">{download_filename}</a>
        """)

with open('docs/index.html', 'w') as main_package_index:
    main_package_index.write(f"""
    <html>
    <head>
    <style>
    body{{margin:40px auto;max-width:650px;line-height:1.6;font-size:18px;color:#444;padding:0 10px}}
    h1,h2,h3{{line-height:1.2}}
    </style>
    <title>PyPI Windows wheels</title>
    </head>
    <body>
    <header>PyPI Windows wheels</header>
    """)
    for package in sorted(packages):
        with open(os.path.join('docs', package.lower(), 'index.html'), 'a') as package_index:
            package_index.write(f"""
                </body>
                </html>
            """)
        main_package_index.write(f'<a href="{package.lower()}">{package.lower()}</a>\n\n')
        print(package)
    main_package_index.write("""
    </body>
    </html>
    """)
