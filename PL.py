from colorama import Fore, Back, Style
from random import randint, choice
import os
import datetime
import art
import webbrowser
from time import sleep
import getpass
import psutil
messageserver = ""
import sys
serverl = 0
serverp = ""
import playsound
import shutil
import g4f
messages = ""
from re import search
from PIL import Image
privacy = ""
pgs = ""
local = []
email = ""
get = ""
system = ""
print(Fore.LIGHTYELLOW_EX + Back.BLACK+ Style.BRIGHT+"")
art.tprint("Hello!")
playsound.playsound('zapusk.mp3')
print(Fore.LIGHTMAGENTA_EX+"")
imp = ''
sleep(2)
art.tprint("E  L  E  C  T  R  O  B  R  A  I  N")
sleep(2)
inp = art.tprint("ElectroBrain")
print(Fore.RESET+"")
os.system("cls||clear")
run = True
while run:
    t = input("ElectroBrain(Programming Language): ")
    if t == "clear":
        os.system("cls||clear")
    if t == "print()":
        say = input("Print: ")
        print(say)
    if t == "color red()":
        print(Fore.RED+"Saved!")
    if t == "color green()":
        print(Fore.GREEN+"Saved!")
    if t == "color yellow()":
        print(Fore.YELLOW+"Saved!")
    if t == "color blue()":
        print(Fore.BLUE+"Saved!")
    if t == "color pink()":
        print(Fore.MAGENTA+"Saved!")
    if t == "color black()":
        print(Fore.BLACK+"Saved!")
    if t == "color white()":
        print(Fore.WHITE+"Saved!")
    if t == "color reset()":
        print(Fore.RESET+"Saved!")
    if t == "color cyan()":
        print(Fore.CYAN+"Saved!")
    if t ==  "time(now)":
        print(datetime.datetime.now())
    if t == "time()":
        f = print(input("Time: "))
    if t == "input()":
        input(input("Input: "))
    if t == "hw":
        print('Hello world!')
    if t == "let.create()":
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
    if t == "send.message()":
        message = input("Message: ")
        print(Fore.LIGHTRED_EX+"\n\n\n\n\n\n\n\n\n•New message!\n\n\n\n\n\n"+Fore.BLUE+message+Fore.RESET+"\n\n\n\n\n\n\n\n\n")
        messages += message
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
    if t == "pay()":
        pay = input("Pay: ")
        print("\n\n\n\n\n\n\n\n\n"+Fore.LIGHTMAGENTA_EX+"You have been credited "+pay+Fore.RESET+"\n\n\n\n\n\n\n\n\n")
    if t == "pass()":
        pass
    if t == "df(f)":
        RMTREE = input("Delete(folder and files(in folder)): ")
        shutil.rmtree(RMTREE)
        print("Delete!")
    if t == "df(file)":
        deletefiles = input("Delete(file): ")
        os.remove(deletefiles)
    if t == "site(my)":
        webbrowser.open_new_tab("https://electrobrainmygit.tilda.ws")
    if t == "print(let)":
        print(let3)
    if t == "println(let)":
        print(f"\n{let3}")
    if t == "import":
        impor = input("Import: ")
        if impor == "gp":
            imp += "gp"
            print("Import settings save")
        if impor == "chat":
            imp += "chat"
            print("Import setting save")
        else:
            print("InputError: not biblio")
    if t == "print(imports)":
        print(impor)
    if t == "println(imports)":
        print(f"\n{impor}")
    if t == "gp()":
        if "gp" in imp:
            gp = input("Input(gp(bg = 0%(getpass(pass))): ")
            getpass.getpass(gp)
        else:
            print("ImportError: Not GP!")
    if t == "web()":
        web = input("Open site: ")
        webbrowser.open(web)
    if t == "web_new()":
        web1 = input("Open site: ")
        webbrowser.open_new(web1)
    if t == "web_new_tab()":
        web2 = input("Open site: ")
        webbrowser.open_new_tab(web2)
    if t == "quit":
        exit("QUIT")
    if t == "nf()":
        nw = input("New folder: ")
        os.mkdir(nw)
    if t == "nf(f)":
        nf = input("New file(name): ")
        open(f"{nf}.txt",'a').close()
    if t == "cd()":
        cd = input("Cd: ")
        os.system(f"cd {cd}")
    if t == "let size()":
        print(sys.getsizeof(let3))
        print("byte")
    if t == "math.pi()":
        print("3.141592653589793")
    if t == "math.calc()":
        print(eval(input("Calc: ")))
    if t == "infinite_fone()":
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
    if t == "print(server(global))":
        print(f"ID: {serverg}, info: {serveridg}")
    if t == "println(server(global))":
        print(f"\nID: {serverg}, info: {serveridg}")
    if t == "license()":
        webbrowser.open_new_tab("LICENSE")
    if t == "list()":
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
        webbrowser.open_new_tab("piplinux.sh")
    if t == "AVATAR()":
        webbrowser.open_new_tab("avatar.png")
    if t == "text()":
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
    if t == "off/on()":
        os.system("reboot")
    if t == "off(+)":
        plus = input("+: ")
        os.system(f"shutdown +{plus}")
    if t == "off()":
        os.system("shutdown +0")
    if t == "let+()":
        pluslet = input("+(string): ")
        let3 += pluslet
    if t == "let-()":
        minuslet = input("-(string): ")
        let3 -= minuslet
    if t == "img.open()":
        imgop = input("Name file(or path to file): ")
        im = Image.open(imgop)
        im.show()
    if t == "bg green()":
        print(Back.GREEN+"Saved!")
    if t == "bg red()":
        print(Back.RED+"Saved!")
    if t == "bg blue()":
        print(Back.BLUE+"Saved!")
    if t == "bg pink()":
        print(Back.MAGENTA+"Saved!")
    if t == "bg cyan()":
        print(Back.CYAN+"Saved!")
    if t == "bg yellow()":
        print(Back.YELLOW+"Saved!")
    if t == "bg black()":
        print(Back.BLACK+"Saved!")
    if t == "bg white()":
        print(Back.WHITE+"Saved!")
    if t == "bg reset()":
        print(Back.RESET+"Saved!")
    if t == "list+()":
        liisplus = input("+: ")
        list += liisplus
    if t == "list-()":
        listminus = input("-: ")
    if t == "send.message(email)":
        messageemail = input('Message: ')
        email += messageemail
    if t == "print(email)":
        print(email)
    if t == "println(email)":
        print(f"\n{email}")
    if t == "send.get()":
        g1 = input("Get: ")
        get += g1
        print("get...")
        sleep(randint(1,5))
        print(f"GET: {get}")
    if t == "print(get)":
        print("get...")
        sleep(randint(1,5))
        print(f"GET: {get}")
    if t == "println(get)":
        print("get...")
        sleep(randint(1,5))
        print(f"\nGET: {get}")
    if t == "send.get(server(local))":
        inf = input("Get: ")
        serverinfl += inf
        get += f"local: {inf}"
    if t == "send.get(server(global)":
        getg = input("Get: ")
        serveridg += getg
        get += f"global: {getg}"
    if t == "send.sysget()":
        sysget = input("System get: ")
        system += sysget
        print(f"\n\n\n\n\n\n\n\n SYSTEM GET:  {sysget}\n\n\n\n\n\n\n\n\n\n")
    if t == "print(messages)":
        print(messages)
    if t == "println(messages)":
        print(f"\n{messages}")
    if t == "/":
        print("\n")
    if t == "//":
        print("\n\n")
    if t == "chat.online()":
        if imp in "chat":
            print("Open file chat.py")
        else:
            print("ImportError: Not chat!")
    if t == "send.message(server)":
        sendms = input("Message: ")
        messageserver += sendms
    if t == "print(server(message))":
        print(messageserver)
    if t == "println(server(message))":
        print(f"\n{messageserver}")
    if t == "package()":
        pack = input("Package: ")
        if pack == "SyntaxS":
            while True:
                print("S")
        else:
            print("PackageError: not package")
    if t == "Ruby.create.code()":
        with open('file.ru','w'):
            print("Save ruby file")
    if t == "ping()":
        webbrowser.open_new_tab("https://2ip.ru/speed/")
    if t == "setpass()":
        passsword = getpass.getpass("Your password: ")
        passwordinput = getpass.getpass()
        if passwordinput == f"{passsword}":
            print("Password save")
            privacy += passsword
        if passwordinput != passsword:
            print("This is different password")
    if t == "print(privacy)":
        print(privacy)
    if t == "println(privacy)":
        print(f"\n{privacy}")
    if t == "server.create(privacy)":
        priv = webbrowser.open_new_tab("https://2ip.io/ru/privacy/")
        privc = input("Privacy: ")
        privacy += privc
    if t == "print(server(privacy))":
        print(privacy)
    if t == 'println(server(privacy))':
        print(f"\n{privacy}")
    if t == "delete server(privacy)":
        del privacy
    if t == "delete server(local)":
        del serverl
        del serverinfl
    if t == "delete server(global)":
        del serveridg
        del serverg
    if t == "send.alert()":
        text = input("Text: ")
        close = input("CLose func: ")
        ok = input("Ok func: ")
        os.system("cls||clear")
        alert = input(f"{text} [{ok}] or [{close}] ")
        if alert == ok:
            print("Confirmed")
            sleep(1.5)
            os.system('cls||clear')
        if alert == close:
            os.system("cls||clear")
    if t == "ps()":
        webbrowser.open_new_tab("https://2ip.ru/port-scaner/")
        dan = input("Port-scanner info: ")
        system += dan
    if t == "print(ps)":
        print(dan)
    if t == "println(ps)":
        print(f"\n{dan}")
    if t == "cpu":
        print("Number of CPUs:", os.cpu_count())
    if t == "pc.info()":
        p = psutil.virtual_memory()
        util = p
        print(util)
    if t == "cpu_time()":
        print(psutil.cpu_times())
    if t == "pc.info()":
        print(psutil.cpu_count(), psutil.boot_time, psutil.cpu_freq(), psutil.cpu_percent(), psutil.cpu_times(), psutil.disk_usage, psutil.disk_io_counters(), psutil.cpu_stats(), psutil.cpu_times_percent(), psutil.disk_partitions(), psutil.net_if_addrs(), psutil.pid_exists)
        print("")
    if t == "print(not)":
        print("Error!")
    if t == "creator()":
        print("Привет! Меня зовут Кирилл. И я создал этот язык. Он создавался довольно таки долгое время, и я прошу: если можешь, то поддержи меня: 2200 7005 2653 0208. спасибо за то что пользуйтесь языком ;)")
    if t == "send.confirm()":
        text1 = input("Text: ")
        ok1 = input("Ok func: ")
        close1 = input("Close func: ")
        notf = input("NotOk func: ")
        os.system("cls||clear")
        alert1 = input(f"{text1} [{ok1}] or [{close1}] or [{notf}] ")
        if alert1 == ok1:
            print("Confirmed")
            sleep(1.5)
            os.system("cls||clear")
        if alert1 == close1:
            os.system("cls||clear")
        if alert1 == notf:
            print("Not confirmed")
            sleep(1.5)
            os.system("cls||clear")
    if t == "server.delete(local)":
        del serverinfl
        del serverl
    if t == "server.delete(global)":
        del serveridg
        del serverg
    if t == "server.delete(all)":
        del serveridg
        del serverg
        del serverinfl
        del serverl
    