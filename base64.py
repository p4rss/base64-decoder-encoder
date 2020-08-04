import pybase64
def base64_encode(sayi,yazi):
    string = yazi
    for i in range(sayi):
        string = pybase64.b64encode(string.encode(encoding='utf-8', errors='strict')).decode(encoding="utf-8")
    print(string)
def base64_decode(sayi,yazi):
    string = yazi
    for i in range(sayi):
        string  = pybase64.b64decode(string)
    out_string = string.decode("UTF-8")
    print(out_string)








