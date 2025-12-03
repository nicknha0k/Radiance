# !/bin/bash
# 
# ┌─────────────────────────────────────────────────────────────────────────┐
# │                            RADIANCE TOOLKIT                              │
# │                Multi-tool Cybersecurity & Discord Suite                  │
# │                        By w_ky - Est. 2024                             │
# └─────────────────────────────────────────────────────────────────────────┘
#
# 🌟 O QUE É?
# Ferramenta modular com 18+ utilitários para análise de segurança, 
# automação Discord, reconhecimento e testes de vulnerabilidade.
#
# 🚀 COMEÇAR:

# 1. Clone o repositório:
git clone https://github.com/nicknha0k/Radiance/
cd Radiance

# 2. Instale dependências (recomendado usar virtualenv):
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

# 3. Execute:
python3 main.py

# 🛠️ DETALHES TÉCNICOS:

# 📦 DEPENDÊNCIAS PRINCIPAIS:
# • discord.py     - API Discord completa
# • aiohttp        - Requests assíncronas
# • beautifulsoup4 - Parsing HTML
# • requests       - HTTP client
# • tkinter        - Interface gráfica (já vem com Python)

# 🎯 FUNCIONALIDADES PRINCIPAIS:

# 🔧 DISCORD TOOLS (01-06):
# • Raid Bot (Lecuio) - Automatização avançada de servidores
# • Webhook Tracker   - Análise e manipulação de webhooks
# • +4 slots para expansão

# ⚔️ HACK TOOLS (07-12):
# • Vulnerability Scanner - Scanner completo de vulnerabilidades web
# • DDoS Tool            - Ferramenta de teste de carga
# • LOG Cleaner          - Limpeza forense avançada
# • +3 slots para expansão

# 🔍 UTILITIES (13-18):
# • Password List (240k)    - Wordlist otimizada
# • IP Analysis             - Geolocalização e reconhecimento
# • Phone Number Analysis   - OSINT telefônico
# • IP/Phone Generators     - Geradores para testes

# ⚙️ EXECUÇÃO AVANÇADA:

# Modo terminal único (recomendado para maioria dos casos):
python3 main.py

# Modo múltiplos terminais (para operações paralelas):
# Terminal 1 - Menu principal:
# python3 main.py

# Terminal 2 - Executar ferramenta específica (ex: DDoS):
# python3 -c "from main import DDoS; DDoS()"

# Terminal 3 - Modo API (futura implementação):
# python3 -c "from modules.api import start_server; start_server()"

# 🐛 SOLUÇÃO DE PROBLEMAS:

# Erro: "ModuleNotFoundError"
# Solução: pip install discord.py aiohttp beautifulsoup4 requests

# Erro: Tkinter no Linux
# Solução: sudo apt-get install python3-tk

# Erro: SSL Certificate
# Solução: Desative verificação SSL ou configure certificados

# 🔒 SEGURANÇA:
# • Use em ambientes controlados
# • Não utilize para atividades ilegais
# • Algumas ferramentas requerem permissões elevadas
# • Mantenha o token do Bot Discord seguro

# 📁 ESTRUTURA DO PROJETO:
# Radiance/
# ├── main.py              # Entry point principal
# ├── requirements.txt     # Dependências Python
# ├── modules/            # Módulos separados (futuro)
# │   ├── discord_tools/  # Ferramentas Discord
# │   ├── security/       # Utilitários de segurança
# │   └── utils/          # Funções auxiliares
# ├── data/              # Arquivos de dados
# └── logs/              # Logs de operação

# 💻 COMPATIBILIDADE:
# • Python 3.8+
# • Windows 10/11, Linux, macOS
# • Conexão internet para algumas ferramentas
# • 2GB RAM mínimo recomendado

# 📞 SUPORTE:
# • Issues: https://github.com/nicknha0k/Radiance/issues
# • Discord: nicknha007
# • Email: via GitHub profile

# ⚠️ AVISO LEGAL:
# Esta ferramenta é para fins educacionais e de teste autorizado.
# O desenvolvedor não se responsabiliza por uso indevido.
# Use apenas em sistemas que você possui ou tem permissão para testar.

# 🎨 CRÉDITOS:
# Desenvolvido por w_ky com 10+ anos em segurança ofensiva
# Design de interface e otimizações por contributors
# Inspirado em ferramentas da comunidade infosec
