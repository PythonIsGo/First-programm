from colorama import Fore, Back, Style
from ursina import Ursina, Entity, color, held_keys
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
serverl = ""
serverp = ""
import playsound
import shutil
import g4f
from tkinter import *
messages = ""
from re import search
from PIL import Image
privacy = ""
mains = ""
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
os.system("clear")
run = True
while run:
    t = input(">>>")
    if t == "clear":
        os.system("clear")
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
        if impor == "win4Tools":
            print("Import settings save")
            imp += "win4Tools"
        if impor == "egame":
            print("Import settings save")
            imp += "egame"
    if t == "print(imports)":
        print(imp)
    if t == "println(imports)":
        print(f"\n{imp}")
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
        whatlist = input("List name: ")
        list = ""
    if t == "list.add()":
        listadd = input("List add: ")
        list += listadd
        print(list)
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
        systemget = os.system(f"{sysget}")
    if t == "print(messages)":
        print(messages)
    if t == "println(messages)":
        print(f"\n{messages}")
    if t == "/":
        print("\n")
    if t == "//":
        print("\n\n")
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
    if t == "ai.update()":
        os.system("pip install -U g4f")
    if t == "/":
        print("\n")
    if t == "////":
        print("\n\n\n\n")
    if t == "{main}":
        mainname = input("Name: ")
        mains += mainname
        print(f"""static public main__{mainname}:
              CREATE
        """)
    if t == "win4.create(window)":
        if "win4Tools" in imp:
            win4geometry = input("Geometry(geometry1 x geometry2): ")
            win4title = input("Title: ")
            win = Tk()
            win.geometry(f"{win4geometry}")
            win.title(f"{win4title}")
            print("compiling...")
            sleep(randint(1,5))
            win.mainloop()
        if "win4Tools" not in imp:
            print("Win4Tools not installed")
    if t == "win4.create(window(setbg))":
            if "win4Tools" in imp:
                win4geometry = input("Geometry(geometry1 x geometry2): ")
                win4title = input("Title: ")
                win = Tk()
                win4bg = input("BgColor: ")
                win['bg'] = win4bg
                win.geometry(f"{win4geometry}")
                win.title(f"{win4title}")
                print("compiling...")
                sleep(randint(1,5))
                win.mainloop()
            if "win4Tools" not in imp:
                print("Win4Tools not installed")
    if t == "win4.create(window, label)"or t == "win4.create(window,label)":
        if "win4Tools" in imp:
            win4geometry = input("Geometry(geometry1 x geometry2): ")
            win4title = input("Title: ")
            win4label = input("Label(text): ")
            win4labelplacex = input("Label place(x): ")
            win4placelabely = input("Label place(y): ")
            win = Tk()
            win.geometry(f"{win4geometry}")
            win.title(f"{win4title}")
            winlabel = Label(win, text=f"{win4label}")
            winlabel.place(x = win4labelplacex, y = win4placelabely)
            print("compiling...")
            sleep(randint(1,5))
            win.mainloop()
        if "win4Tools" not in imp:
            print("Win4Tools not installed")
    if t == "win4.create(window, label, (setbg))"or t == "win4.create(window,label,(setbg))":
        if "win4Tools" in imp:
            win4geometry = input("Geometry(geometry1 x geometry2): ")
            win4title = input("Title: ")
            win = Tk()
            win4bg = input("BgColor: ")
            win['bg'] = f"{win4bg}"
            win4label = input("Label(text): ")
            win4labelplacex = input("Label place(x): ")
            win4placelabely = input("Label place(y): ")
            win.geometry(f"{win4geometry}")
            win.title(f"{win4title}")
            winlabel = Label(win, text=f"{win4label}")
            winlabel.place(x = win4labelplacex, y = win4placelabely)
            print("compiling...")
            sleep(randint(1,5))
            win.mainloop()
        if "win4Tools" not in imp:
            print("Win4Tools not installed")
    if t == "win4.create(window, label, button)"or t == "win4.create(window,label,button)"or t == "win4.create(window,button,label)" or t == "win4.create(window, button, label)":
        if "win4Tools" in imp:
            win4geometry = input("Geometry(geometry1 x geometry2): ")
            win4title = input("Title: ")
            win4button = input("Button(text): ")
            win4label = input("Label(text): ")
            win4labelplacex = input("Label place(x): ")
            win4placelabely = input("Label place(y): ")
            win4buttonplacex = input("Button place(x): ")
            win4buttonplacey = input("Button place(y): ")
            win = Tk()
            winbutton = Button(win, text=f"{win4button}")
            winbutton.place(x = win4buttonplacex, y = win4buttonplacey)
            win.geometry(f"{win4geometry}")
            win.title(f"{win4title}")
            winlabel = Label(win, text=f"{win4label}")
            winlabel.place(x = win4labelplacex, y = win4placelabely)
            print("compiling...")
            sleep(randint(1,5))
            win.mainloop()
        if "win4Tools" not in imp:
            print("Win4Tools not installed")
    if t == "win4.create(window, label, button, (setbg))"or t == "win4.create(window,label,button,(setbg))"or t == "win4create(window,button,label,(setbg))" or t == "win4.create(window, button, label, (setbg))":
        if "win4Tools" in imp:
            win4geometry = input("Geometry(geometry1 x geometry2): ")
            win4title = input("Title: ")
            win = Tk()
            win4bg = input("BgColor: ")
            win['bg'] = f"{win4bg}"
            win4button = input("Button(text): ")
            win4label = input("Label(text): ")
            win4labelplacex = input("Label place(x): ")
            win4placelabely = input("Label place(y): ")
            win4buttonplacex = input("Button place(x): ")
            win4buttonplacey = input("Button place(y): ")
            winbutton = Button(win, text=f"{win4button}")
            winbutton.place(x = win4buttonplacex, y = win4buttonplacey)
            win.geometry(f"{win4geometry}")
            win.title(f"{win4title}")
            winlabel = Label(win, text=f"{win4label}")
            winlabel.place(x = win4labelplacex, y = win4placelabely)
            print("compiling...")
            sleep(randint(1,5))
            win.mainloop()
        if "win4Tools" not in imp:
            print("Win4Tools not installed")
    if t == "win4.create(window, label, button, entry)"or t == "win4.create(window,label,button,entry)":
        if "win4Tools" in imp:
            win4geometry = input("Geometry(geometry1 x geometry2): ")
            win4title = input("Title: ")
            win = Tk()
            win4button = input("Button(text): ")
            win4label = input("Label(text): ")
            win4labelplacex = input("Label place(x): ")
            win4placelabely = input("Label place(y): ")
            win4buttonplacex = input("Button place(x): ")
            win4buttonplacey = input("Button place(y): ")
            win4entryname = input("Entry(text): ")
            win4entryplacex = input("Entry place(x): ")
            win4entryplacey = input("Entry place(y): ")
            winbutton = Button(win, text=f"{win4button}")
            winbutton.place(x = win4buttonplacex, y = win4buttonplacey)
            winentry = Entry(win, text=f"{win4entryname}")
            winentry.place(x = win4entryplacex, y = win4entryplacey)
            win.geometry(f"{win4geometry}")
            win.title(f"{win4title}")
            winlabel = Label(win, text=f"{win4label}")
            winlabel.place(x = win4labelplacex, y = win4placelabely)
            print("compiling...")
            sleep(randint(1,5))
            win.mainloop()
        if "win4Tools" not in imp:
            print("Win4Tools not installed")
    if t == "win4.create(window, label, button, entry, (setbg))"or t == "win4.create(window,label,button,entry,(setbg))":
        if "win4Tools" in imp:
            win4geometry = input("Geometry(geometry1 x geometry2): ")
            win4title = input("Title: ")
            win = Tk()
            win4bg = input("BgColor: ")
            win['bg'] = f"{win4bg}"
            win4button = input("Button(text): ")
            win4label = input("Label(text): ")
            win4labelplacex = input("Label place(x): ")
            win4placelabely = input("Label place(y): ")
            win4buttonplacex = input("Button place(x): ")
            win4buttonplacey = input("Button place(y): ")
            win4entryname = input("Entry(text): ")
            win4entryplacex = input("Entry place(x): ")
            win4entryplacey = input("Entry place(y): ")
            winbutton = Button(win, text=f"{win4button}")
            winbutton.place(x = win4buttonplacex, y = win4buttonplacey)
            winentry = Entry(win, text = f"{win4entryname}")
            winentry.place(x = win4entryplacex, y = win4entryplacey)
            win.geometry(f"{win4geometry}")
            win.title(f"{win4title}")
            winlabel = Label(win, text=f"{win4label}")
            winlabel.place(x = win4labelplacex, y = win4placelabely)
            print("compiling...")
            sleep(randint(1,5))
            win.mainloop()
        if "win4Tools" not in imp:
            print("Win4Tools not installed")
    if t == "win4.create(window, entry)":
        if "win4Tools" in imp:
            win4geometry = input("Geometry(geometry1 x geometry2): ")
            win4title = input("Title: ")
            win = Tk()
            win4entryname = input("Entry(text): ")
            win4entryplacex = input("Entry place(x): ")
            win4entryplacey = input("Entry place(y): ")
            winentry = Entry(win, text = f"{win4entryname}")
            winentry.place(x = win4entryplacex, y = win4entryplacey)
            win.geometry(f"{win4geometry}")
            win.title(f"{win4title}")
            print("compiling...")
            sleep(randint(1,5))
            win.mainloop()
        if "win4Tools" not in imp:
            print("Win4Tools not installed")
    if t == "win4.create(window, entry, (setbg))"or t == "win4.create(window,entry,(setbg))":
        if "win4Tools" in imp:
            win4geometry = input("Geometry(geometry1 x geometry2): ")
            win4title = input("Title: ")
            win = Tk()
            win4bg = input("BgColor: ")
            win['bg'] = f"{win4bg}"
            win4entryname = input("Entry(text): ")
            win4entryplacex = input("Entry place(x): ")
            win4entryplacey = input("Entry place(y): ")
            winentry = Entry(win, text = f"{win4entryname}")
            winentry.place(x = win4entryplacex, y = win4entryplacey)
            win.geometry(f"{win4geometry}")
            win.title(f"{win4title}")
            print("compiling...")
            sleep(randint(1,5))
            win.mainloop()
        if "win4Tools" not in imp:
            print("Win4Tools not installed")
    if t == "win4.create(window, entry, label)"or t == "win4.create(window,entry,label)":
        if "win4Tools" in imp:
            win4geometry = input("Geometry(geometry1 x geometry2): ")
            win4title = input("Title: ")
            win = Tk()
            win4entryname = input("Entry(text): ")
            win4entryplacex = input("Entry place(x): ")
            win4entryplacey = input("Entry place(y): ")
            win4label = input("Label(text): ")
            win4labelplacex = input("Label place(x): ")
            win4placelabely = input("Label place(y): ")
            winentry = Entry(win, text = f"{win4entryname}")
            winentry.place(x = win4entryplacex, y = win4entryplacey)
            winlabel = Label(win, text=f"{win4label}")
            winlabel.place(x = win4labelplacex, y = win4placelabely)
            win.geometry(f"{win4geometry}")
            win.title(f"{win4title}")
            print("compiling...")
            sleep(randint(1,5))
            win.mainloop()
        if "win4Tools" not in imp:
            print("Win4Tools not installed")
    if t == "win4.create(window, entry, label, (setbg))"or t == "win4.create(window,entry,label,(setbg))":
        if "win4Tools" in imp:
            win4geometry = input("Geometry(geometry1 x geometry2): ")
            win4title = input("Title: ")
            win = Tk()
            win4bg = input("BgColor: ")
            win['bg'] = f"{win4bg}"
            win4entryname = input("Entry(text): ")
            win4entryplacex = input("Entry place(x): ")
            win4entryplacey = input("Entry place(y): ")
            win4label = input("Label(text): ")
            win4labelplacex = input("Label place(x): ")
            win4placelabely = input("Label place(y): ")
            winentry = Entry(win, text = f"{win4entryname}")
            winentry.place(x = win4entryplacex, y = win4entryplacey)
            winlabel = Label(win, text=f"{win4label}")
            winlabel.place(x = win4labelplacex, y = win4placelabely)
            win.geometry(f"{win4geometry}")
            win.title(f"{win4title}")
            print("compiling...")
            sleep(randint(1,5))
            win.mainloop()
        if "win4Tools" not in imp:
            print("Win4Tools not installed")
    if t == "win4.create(window, button)"or t == "win4.create(window,button)":
        if "win4Tools" in imp:
            win4geometry = input("Geometry(geometry1 x geometry2): ")
            win4title = input("Title: ")
            win = Tk()
            win4button = input("Button(text): ")
            win4buttonplacex = input("Button place(x): ")
            win4buttonplacey = input("Button place(y): ")
            winbutton = Button(win, text=f"{win4button}")
            winbutton.place(x = win4buttonplacex, y = win4buttonplacey)
            win.geometry(f"{win4geometry}")
            win.title(f"{win4title}")
            print("compiling...")
            sleep(randint(1,5))
            win.mainloop()
        if "win4Tools" not in imp:
            print("Win4Tools not installed")
    if t == "win4.create(window, button, (setbg))"or t == "win4.create(window,button,(setbg))":
        if "win4Tools" in imp:
            win4geometry = input("Geometry(geometry1 x geometry2): ")
            win4title = input("Title: ")
            win = Tk()
            win4bg = input("BgColor: ")
            win['bg'] = f"{win4bg}"
            win4button = input("Button(text): ")
            win4buttonplacex = input("Button place(x): ")
            win4buttonplacey = input("Button place(y): ")
            winbutton = Button(win, text=f"{win4button}")
            winbutton.place(x = win4buttonplacex, y = win4buttonplacey)
            win.geometry(f"{win4geometry}")
            win.title(f"{win4title}")
            print("compiling...")
            sleep(randint(1,5))
            win.mainloop()
        if "win4Tools" not in imp:
            print("Win4Tools not installed")
    if t == "playsound.play()":
        path = input("Path(or name.mp3): ")
        playsound.playsound(f"{path}")
    if t == "zip.open()":
        namezip = input("Name: ")
        files = input("File: ")
        os.system(f"zip {namezip}.zip {files}") 
    if t == "create.boot()":
        with open("boot.py", '+w') as file:
            file.write("""
import os
print("rebooting")
print("BOOT")
os.system("./start.sh")""")
    if t == "egame.start()":
            if imp in "egame":
                engine = Tk()
                engine.geometry("900x900")
                engine.title("EGame.menu")
                btn_start_engine = Button(engine, text="")