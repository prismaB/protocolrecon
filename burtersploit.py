try:
    import os
    import sys
    import subprocess
    import socket
    from datetime import datetime
    import pyfiglet
    import time
    from colorama import Fore,Back,init,Style
    init(autoreset=True)
except:
    pass

class brutesploits:
    banner = """
            dMMMMb  dMMMMMP .aMMMb  .aMMMb  dMMMMb 
            dMP.dMP dMP     dMP"VMP dMP"dMP dMP dMP 
            dMMMMK" dMMMP   dMP     dMP dMP dMP dMP  
            dMP"AMF dMP     dMP.aMP dMP.aMP dMP dMP   
            dMP dMP dMMMMMP  VMMMP"  VMMMP" dMP dMP    
            """
    print(banner)
    target = sys.argv[1]
    services = sys.argv[2]
    if target == "" or target == " " or target == "\r" or target == "\n":
        usage = """
        reconner.py 10.10.10.10 telnet
        reconner.py 10.10.10.10 smb
        reconner.py 10.10.10.10 portscan
        """
        print(usage)
    if len(sys.argv) < 2:
        usage = """
        reconner.py 10.10.10.10 telnet
        reconner.py 10.10.10.10 smb
        reconner.py 10.10.10.10 portscan
        """
        print(usage)
    elif services == "smb":
        try:
            subprocess.call("clear")
            print(Fore.RED + " " + " " + target + " " + Fore.RED)
            subprocess.call("clear")
            smbbanner = pyfiglet.figlet_format("SMB!")
            print(smbbanner)
            print("starting the nmap smb scan")
            os.system("nmap -p445 " + " " + target + " " + "-vv")
            time.sleep(0.10)
            print("starting nmap agressive smb scan")
            os.system("nmap -A -p445 " + " " + target + " " + "-vv")
            time.sleep(0.10)
            print("starting enum4linux")
            os.system("enum4linux" + " " + target)
            time.sleep(0.10)
            vulners = input("starting vulnscan [e]xit or [c]onite =>")
            if vulners == "E" or vulners == "e":
                print("bye!")
                sys.exit()
            elif vulners == "c" or vulners == "C":
                print("ok starting the vuln scan")
                print("starting the eternalblue scan")
                os.system("nmap -p445 --script smb-vuln-ms17-010" + " " + target)
                time.sleep(0.10)
                print("starting the nmap ms08-067 scanner")
                os.system("nmap --script smb-vuln-ms08-067.nse -p445" + " " + target)
                time.sleep(0.10)
                print("starting the smb-double-pulsar-backdoor script")
                os.system("nmap -p 445" + " " + target + " " + "--script=smb-double-pulsar-backdoor")
                time.sleep(0.10)
                print(Fore.RED +  " " + "scan finished" + Fore.RED)
        except KeyboardInterrupt:
            print("ok stopping the scan")
            os.system("sudo killall nmap")
            sys.exit()
    elif services == "telnet":
        try:
            subprocess.call("clear")
            telnetbanner = pyfiglet.figlet_format("TELNET!")
            print(telnetbanner)
            print("target is =>" + " " + target)
            print("starting the basic nmap scan")
            os.system("nmap -p23 " + " " + target)
            time.sleep(0.10)
            print("starting the nmap agressive scan")
            os.system("nmap -p23 -A" + " " + target)
            time.sleep(0.10)
            print("starting the telnet user enumation")
            os.system("nmap –script smtp-enum-users -p23" + " "  + target)
            brutetelnet = input("start bruteforce ? [e]xit or [c]onite =>")
            if brutetelnet == "c" or brutetelnet == "C":
                print("ok starting the brute force")
                bruteusername = input("add target username =>")
                print("username => " + " " + bruteusername)
                brutewordlists = input("add wordlists =>")
                print("wordlists =>" + " " + brutewordlists)
                os.system("hydra -l " + " " + bruteusername + " " + "-P" + " " + brutewordlists +" " + target + " " + "telnet" + " " + "-VV")
            elif brutetelnet == "e" or brutetelnet == "E":
                print("bye!")
                sys.exit()
        except KeyboardInterrupt:
            print("stopping the scan")
            os.system("killall hydra nmap")
            sys.exit()
    elif services == "portscan":
        try:
            print("target => " + " " + target)
            print("starting port scan")
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            for port in range(0,10001):
                s.connect_ex((target, port))
                if result ==0:
                    print("port open {} ".format(port))
        except KeyboardInterrupt:
            print("exitting the program")
            sys.exit()