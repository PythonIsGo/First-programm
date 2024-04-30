from colorama import Fore, Back, Style
from random import randint, choice
import os
import datetime
import art
import webbrowser
from time import sleep
import getpass
import sys
import requests
serverl = 0
import shutil
import g4f
from re import search
from PIL import Image
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
        f = print(input("Time: "))
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
        else:
            print("InputError: not let")
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
        else:
            print("InputError: not biblio!")
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
            print("Downloading...")
    if t == "server.create(local)":
        servidl = input("ID: ")
        serverl = servidl
        serverinfl = input("Info: ")
        print(serverl, serverinfl)
    if t == "print(server(local))":
        print(serverl)
    if t == "println(server(local))":
        print(f"\n{serverl}")
    if t == "/n":
        print("\n")
    if t == "server.create(global)":
        global serverg
        serverg = input("ID: ")
        global serveridg
        serveridg = input("Info: ")
        print(serverg, serveridg)
    if t == "license":
        webbrowser.open_new_tab("LICENSE")
    if t == "list":
        whatlist = input("Word in list(max 6): ")
        if whatlist == "1":
            leste = input("List: ")
            list = [leste]
        if whatlist == "2":
            leste1 = input("List: ")
            leste2 = input("List(2): ")
            list = [leste1, leste2]
        if whatlist == "3":
            leste13 = input("List: ")
            leste23 = input("List(2): ")
            leste33 = input("List(3): ")
            list = [leste13, leste23, leste33]
        if whatlist == "4":
            leste14 = input("List: ")
            leste24 = input("List(2): ")
            leste34 = input("List(3): ")
            leste44 = input("List(4): ")
            list = [leste14, leste24, leste34, leste44]
        if whatlist == "5":
            leste15 = input("List: ")
            leste25 = input("List(2): ")
            leste35 = input("List(3): ")
            leste45 = input("List(4): ")
            leste55 = input("List(5): ")
            list = [leste15, leste25, leste35]
        if whatlist == "6":
            l16 = input("List: ")
            l26 = input("List(2): ")
            l36 = input("List(3): ")
            l46 = input("List(4): ")
            l56 = input("List(5): ")
            l66 = input("List(6): ")
            list = [l16, l26, l36, l46, l56, l66]
        else:
            print("InputError: write number(1, 2, 3, 4, 5, 6)")
    if t == "console.error()":
        error = input("Error: ")
        print(Fore.RED+"❌Error "+error+Fore.RESET)
    if t == "console.info()":
        info = input("Info: ")
        print(Fore.LIGHTWHITE_EX+"❕Info "+info+Fore.RESET)
    if t == "console.warn()":
        warn = input("Warn: ")
        print(Fore.YELLOW+"⚠️Warn "+warn+Fore.RESET)
    if t == "print(list)":
        print(list)
    if t == "println(list)":
        print(f"\n{list}")
    if t == "pip(linux)":
        webbrowser.open_new_tab("pl-pip(linux).sh")
    if t == "pip(windows)":
        webbrowser.open_new_tab("pl-pip(windows,macos).sh")
    if t == "pip(macos)":
        webbrowser.open_new_tab("pl-pip(windows,macos).sh")
    if t == "AVATAR":
        webbrowser.open_new_tab("avatar.png")
    if t == "BITS":
        webbrowser.open_new_tab("BITS.jpg")
    if t == "text":
        text = input("Txt: ")
        print(text)
    if t == "ai.create(new)":
        token = input("Token(max 9): ")[:9]
        model = input("Model: ")
        local = [token]
        if model == "gpt4":
            print("Чем могу помочь?")
            def ask_say(promt:str)->str:
                response = g4f.ChatCompletion.create(
                model=g4f.models.gpt_4,
                messages=[{"role": "user", "content": promt}],
    )
                return response

            i = input("")
            pechataet = "ChatGPT печатает..."
            print(pechataet)
            print(ask_say(i))
        if model == "gpt35_ultra_turbo":
            print("Чем могу помочь?")
            def ask_say(promt:str)->str:
                response = g4f.ChatCompletion.create(
                model=g4f.models.gpt_35_turbo_16k_0613,
                messages=[{"role": "user", "content": promt}],
    )
                return response

            i = input("")
            pechataet = "ChatGPT печатает..."
            print(pechataet)
            print(ask_say(i))
        if model == "gpt4_turbo":
            print("Чем могу помочь?")
            def ask_say(promt:str)->str:
                response = g4f.ChatCompletion.create(
                model=g4f.models.gpt_4_turbo,
                messages=[{"role": "user", "content": promt}],
    )
                return response

            i = input("")
            pechataet = "ChatGPT печатает..."
            print(pechataet)
            print(ask_say(i))
        if model == "gpt4_32k":
            print("Чем могу помочь?")
            def ask_say(promt:str)->str:
                response = g4f.ChatCompletion.create(
                model=g4f.models.gpt_4_32k,
                messages=[{"role": "user", "content": promt}],
    )
                return response

            i = input("")
            pechataet = "ChatGPT печатает..."
            print(pechataet)
            print(ask_say(i))
        if model == "gpt35_long":
            print("Чем могу помочь?")
            def ask_say(promt:str)->str:
                response = g4f.ChatCompletion.create(
                model=g4f.models.gpt_35_long,
                messages=[{"role": "user", "content": promt}],
    )
                return response

            i = input("")
            pechataet = "ChatGPT печатает..."
            print(pechataet)
            print(ask_say(i))
        if model == "gpt35_turbo":
            print("Чем могу помочь?")
            def ask_say(promt:str)->str:
                response = g4f.ChatCompletion.create(
                model=g4f.models.gpt_35_turbo_0613,
                messages=[{"role": "user", "content": promt}],
    )
                return response

            i = input("")
            pechataet = "ChatGPT печатает..."
            print(pechataet)
            print(ask_say(i))
        if model == "gpt4_32k_13":
            print("Чем могу помочь?")
            def ask_say(promt:str)->str:
                response = g4f.ChatCompletion.create(
                model=g4f.models.gpt_4_32k_0613,
                messages=[{"role": "user", "content": promt}],
    )
                return response

            i = input("")
            pechataet = "ChatGPT печатает..."
            print(pechataet)
            print(ask_say(i))
        if model == "gpt35_turbo_16k":
            print("Чем могу помочь?")
            def ask_say(promt:str)->str:
                response = g4f.ChatCompletion.create(
                model=g4f.models.gpt_35_turbo_16k,
                messages=[{"role": "user", "content": promt}],
    )
                return response

            i = input("")
            pechataet = "ChatGPT печатает..."
            print(pechataet)
            print(ask_say(i))
        print(token)
    if t == "ai.del()":
        del g4f
    if t == "ai.stop()":
        del g4f
    if t == "file.open(new)": 
        name = input("Name file: ")
        write = input("Write in file: ")
        with open(name, 'w') as file:
            file.write(write)
    if t == "off/on":
        os.system("reboot")
    if t == "off(+)":
        plus = input("+: ")
        os.system(f"shutdown +{plus}")
    if t == "off()":
        os.system("shutdown +0")
    if t == "let+":
        pluslet = input("+(string): ")
        let3 += pluslet
    if t == "let-":
        minuslet = input("-(string): ")
        let3 -= minuslet
    if t == "img.open()":
        imgop = input("Name file(or path to file): ")
        im = Image.open(imgop)
        im.show()
    else:
        print("CommandError: not your command")