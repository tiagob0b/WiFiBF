📡 WiFiBF

Simple brute-force tool for Wi-Fi (WPA/WPA2) passwords using Python and the pywifi library.
The project aims to demonstrate basic automation techniques for auditing wireless networks in controlled and laboratory environments.

⚠️ This project should only be used for educational purposes or authorized audits.

🚀 Features
Brute force attack via wordlist
Automatic connection to WPA/WPA2 networks
Windows compatible
Simple to use via CLI
Integration with pywifi library

🖥️ Requeriments
Python 3.9+
Windows (recommended)
Active Wi-Fi adapter
Permission to connect to the target network
Python dependencies:
pywifi
comtypes (required on Windows)

📦 Installation
Clone the repository:
````
git clone https://github.com/seuusuario/WifiBF.git
cd WifiBF"
````
Create a virtual environment:
````
python -m venv venv
````
Enable the environment:
Windows
````
venv\Scripts\activate
````
Install the dependencies:
````
pip install -r requirements.txt
````
⚡ Use
Example of execution:
````
python WiFiBF.py -s "Nome_of_SSID" -w wordlist.txt
````
Available parameters:
````
Parameter Description
-s	SSID of Wi-Fi network
-w	File wordlist
-v	Version
````
📌 Exemplo
````
python WiFiBF.py -s My_SSID -w wordlist.txt
````
Expected exit:

[~] Cracking...
[1] Crack Failed using 12345678
[2] Crack Failed using password
[*] Crack success!
[*] password is wifi123456

📂 Estrutura do Projeto
````
WifiBF
│
├── WiFiBF.py
├── requirements.txt
├── wordlist.txt
└── README.md
````
⚠️ Limitations

Works best on Windows
Does not replace professional wireless auditing tools
Speed ​​limited by the operating system's connection attempt time

🔒 Responsible Use
This software was developed for educational purposes only.
Do not use this tool to access networks without authorization.
Misuse may violate local information security laws.

Thank you!
This script was based on the Wacker tool, but the script was adjusted to work on Windows.

https://github.com/blunderbuss-wctf
