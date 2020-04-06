# pypi.bartbroere.eu
Collection of Python wheels, mostly for Raspberry Pi 4 (to avoid long waits) 
and Windows (to avoid the pain of building on Windows)

Use with
``python -m pip install --extra-index-url https://pypi.bartbroere.eu``

## Parsing Christoph Gohlke's / University of California pages
The page at https://www.lfd.uci.edu/~gohlke/pythonlibs/ performs some download URL generation
magic and obfuscation.

```javascript
function dc(ml, mi) {
    var ot = "";
    for (var j = 0; j < mi.length; j++) ot += String.fromCharCode(ml[mi.charCodeAt(j) - 47]);
    document.write(ot);
}

function dl1(ml, mi) {
    var ot = "https://download.lfd.uci.edu/pythonlibs/";
    for (var j = 0; j < mi.length; j++) ot += String.fromCharCode(ml[mi.charCodeAt(j) - 47]);
    location.href = ot;
}

function dl(ml, mi) {
    mi = mi.replace('&lt;', '<');
    mi = mi.replace('&#62;', '>');
    mi = mi.replace('&#38;', '&');
    setTimeout(function (l) {
        dl1(ml, mi)
    }, 1500, 1);
}

dl([101,53,106,110,46,105,118,50,115,104,97,100,99,49,116,54,108,51,119,95,112,52,109,113,45,47], "761FC50=H9:@G6363&lt;G;C@&#62;G;C@&#62;EGA42B9E:&#62;D3A8?");
// triggers download from: https://download.lfd.uci.edu/pythonlibs/s2jqpv5t/ad3-2.2.1-cp36-cp36m-win_amd64.whl
```

This code minimally in Python looks like:

```python
ml = [101, 53, 106, 110, 46, 105, 118, 50, 115, 104, 97, 100, 99, 49, 116, 54, 108, 51, 119, 95, 112, 52, 109, 113, 45,
      47]
mi = "761FC50=H9:@G6363&lt;G;C@&#62;G;C@&#62;EGA42B9E:&#62;D3A8?"


def deobfuscate_download_url(ml, mi):    
    mi = mi.replace('&lt;', '<')
    mi = mi.replace('&#62;', '>')
    mi = mi.replace('&#38;', '&')
    output = ''
    for i in range(len(mi)):
        output += chr(ml[ord(mi[i]) - 47])
    return output

print("https://download.lfd.uci.edu/pythonlibs/" + deobfuscate_download_url(ml, mi))
# https://download.lfd.uci.edu/pythonlibs/s2jqpv5t/ad3-2.2.1-cp36-cp36m-win_amd64.whl
```

It also seems to be checking for known automated User Agent strings, so I send "Mozilla/5.0" in each request.