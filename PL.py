from colorama import Fore, Back, Style
from random import randint, choice
import os
import datetime
import art
import webbrowser
from time import sleep
import getpass
import sys
serverl = 0
import shutil
local = []
print(Fore.LIGHTYELLOW_EX + Back.BLACK+ Style.BRIGHT+"")
art.tprint("Hello!")
print(Fore.LIGHTMAGENTA_EX+"")
imp = ['']
sleep(2)
art.tprint("E  L  E  C  T  R  O  B  R  A  I  N")
sleep(2)
inp = art.tprint("ElectroBrain")
print(Fore.RESET+"")
os.system("cls||clear")
while True:
    t = input("ElectroBrain(Programming Language): ")
    if t == "clear":
        os.system("cls||clear")
    if t == "print":
        say = input("Print: ")
        print(say)
    if t == "color red":
        print(Fore.RED+"Saved!")
    if t == "color green":
        print(Fore.GREEN+"Saved!")
    if t == "color yellow":
        print(Fore.YELLOW+"Saved!")
    if t == "color blue":
        print(Fore.BLUE+"Saved!")
    if t == "color pink":
        print(Fore.MAGENTA+"Saved!")
    if t == "color black":
        print(Fore.BLACK+"Saved!")
    if t == "color white":
        print(Fore.WHITE+"Saved!")
    if t == "color reset":
        print(Fore.RESET+"Saved!")
    if t == "color cyan":
        print(Fore.CYAN+"Saved!")
    if t ==  "time(now)":
        print(datetime.datetime.now())
    if t == "time":
        f = print(input("Time: "))[:9]
    if t == "input":
        input(input("Input: "))
    if t == "hw":
        print('Hello world!')
    if t == "let":
        let = input("Let name: ")
        let2 = input("Let info: ")
        let3 = let2
        print(let,"has attribute ",let2)
        print(let3)
    if t == "delete let(let)":
        dellet = input("Delete let(name): ")
        if dellet == let:
            del let3
            print("Delete!")
        if dellet != let:
            print("Sorry! Not let "+dellet+" !")
    if t == "println()":
        sayd = input("Println: ")
        print("\n", sayd)
    if t == "message.send()":
        message = input("Message: ")
        print(Fore.LIGHTRED_EX+"\n\n\n\n\n\n\n\n\n\n\n\n\n\n•New message!\n\n\n\n\n\n"+Fore.BLUE+message+Fore.RESET+"\n\n\n\n\n\n\n\n\n\n\n")
    if t == "art.print()":
        art1 = input("Art: ")
        art.tprint(art1)
    if t == "global(let)":
        let_glob = input("Let: ")
        global let_glob1
        let_glob1 = let_glob
        let_glob = let_glob1
        print(let_glob)
    if t == "df()":
        rmdir1 = input("Delete folder: ")
        os.rmdir(rmdir1)
        print("Delete!")
    if t == "pay":
        pay = input("Pay: ")
        print("\n\n\n\n\n\n\n\n\n"+Fore.LIGHTMAGENTA_EX+"You have been credited "+pay+Fore.RESET+"\n\n\n\n\n\n\n\n\n")
    if t == "pass":
        pass
    if t == "df(f)":
        RMTREE = input("Delete(folder and files(in folder)): ")
        shutil.rmtree(RMTREE)
        print("Delete!")
    if t == "df(file)":
        deletefiles = input("Delete(file): ")
        os.remove(deletefiles)
    if t == "help(site)":
        webbrowser.open_new_tab("help.html")
    if t == "site":
        webbrowser.open_new_tab("http://project9387299.tilda.ws/")
    if t == "print(let)":
        print(let3)
    if t == "println(let)":
        print(f"\n{let3}")
    if t == "import":
        impor = input("Import: ")
        if impor == "gp":
            impor = ["gp"]
            print("Import settings save")
    if t == "print(imports)":
        print(impor)
    if t == "println(imports)":
        print(f"\n{impor}")
    if t == "gp()":
        if "gp" in impor:
            gp = input("Input(gp(bg = 0%(getpass(pass))): ")
            getpass.getpass(gp)
        else:
            print("Not GP!")
    if t == "web":
        web = input("Open site: ")
        webbrowser.open(web)
    if t == "web_new":
        web1 = input("Open site: ")
        webbrowser.open_new(web1)
    if t == "web_new_tab":
        web2 = input("Open site: ")
        webbrowser.open_new_tab(web2)
    if t == "quit":
        exit("QUIT")
    if t == "nf":
        nw = input("New folder: ")
        os.mkdir(nw)
    if t == "nf(f)":
        nf = input("New file(name): ")
        open(f"{nf}.txt",'a').close()
    if t == "cd":
        cd = input("Cd: ")
        os.system(f"cd {cd}")
    if t == "help(avt)":
        webbrowser.open_new_tab("pay.html")
    if t == "let size":
        print(sys.getsizeof(let3))
        print("byte")
    if t == "math.pi":
        print("3.141592653589793")
    if t == "math.calc":
        print(eval(input("Calc: ")))
    if t == "infinite_fone":
        os.system("cls||clear")
        while True:
            print("Dowdonalding...")
    if t == "server.create(local)":
        servidl = input("ID: ")
        serverl = servidl
        print(serverl)
    if t == "print(server(local))":
        print(serverl)
    if t == "println(server(local))":
        print(f"\n{serverl}")
    if t == "/n":
        print("\n")
    if t == 'help':
        print(help)