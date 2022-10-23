#coding=utf-8
#!/usr/bin/python3
#Coded And Written By - X NOT FOUND X
try:
    import os,time,random,re,json,requests
except ImportError:
    os.system("pkg install nodejs")
    os.system("pkg install requests")
    os.system("pkg install random")
try:
    os.mkdir('.save')
except OSError:
    pass
# COLOUR 
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m'
m = '\x1b[1;91m'
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m'
u = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m'
p = '\x1b[0;34m' 
from requests.exceptions import ConnectionError


logo = """ \n\x1b[1;91m
          _        _______ _________
|\     /|( (    /|(  ___  )\__   __/
( \   / )|  \  ( || (   ) |   ) (   
 \ (_) / |   \ | || |   | |   | |   
  ) _ (  | (\ \) || |   | |   | |   
 / ( ) \ | | \   || |   | |   | |   
( /   \ )| )  \  || (___) |   | |   
|/     \||/    )_)(_______)   )_(   
                                    
X NOT FOUND X <> X NOT FOUND X <> X NOT FOUND X 
-------------------------------
\033[31;1m[^] AUTHOR    : X NOT FOUND X
\033[32;1m[~] Instagram : 44_hama_lordy_ezraily_44
\033[33;1m[~] Telegram  : @xXx_not_found_xXx
\033[34;1m[~] tiktok    : none
\033[35;1m[~] snapchat  : lordhackerencry
\033[36;1m[~] github    : hamalord4444
\033[32;1m[~] facebook  : Xnot Foundx
\033[33;1m[~] youtube   : HaMa LoRdy EzRaiLy
------------------------------------
X NOT FOUND X <> X NOT FOUND X <> X NOT FOUND X 
\n
 ------------------------------------------ """
def ex_id():
    global token
    try:
            token = open('/sdcard/token.txt','r').read()
            cookie = open('/sdcard/cookies.txt','r').read()
    except(KeyError , IOError):
        print(logo)
        print("\t    \033[1;31mLogin FB id continue\033[0;97m")
        print("")
        time.sleep(1)
        os.system("python2 guru.c")
    os.system("clear")
    print(logo)
    print("")
    print("\t    \033[1;32mDUMP IDS MENU\033[0;97m")
    print("")
    print("\033[97m[\033[92m01\033[97m] \033[92mDUMP FROM PUBLIC FRIENDS")
    print("\033[97m[\033[92m02\033[97m] \033[92mDUMP FROM PUBLIC FRIENDS OF FRIENDS")
    print("\033[97m[\033[92m03\033[97m] \033[92mDUMP FROM FOLLOWERS")
    print("\033[97m[\033[92m04\033[97m] \033[92mDUMP FROM FOLLOWERS OF FOLLOWERS")
    print("\033[97m[\033[92m05\033[97m] \033[92mDUMP FROM FOLLOWERS OF FRIENDS")
    print("\033[97m[\033[90m06\033[97m] \033[90m#DUMP FROM GROUPS MEMBERS (SOON...)")
    print("\033[97m[\033[90m07\033[97m] \033[90m#DUMP FROM REACTIONS && COMMENTS (SOON...)")
    print("\033[97m[\033[91m08\033[97m] \033[91mREMOVE COOKIES && TOKEN \033[97m(\033[91mLOGOUT\033[97m)")
    print("\033[97m[\033[93m00\033[97m] \033[93mEXIT")
    print("")
    exs()
def exs():
    id=[]
    tokenku=[]
    uid=[]
    uid2=[]
    s = input("\033[1;33m ▄︻̷̿┻̿═━一 \033[0;97m ")
    if s in ["1",'01']:
        os.system('rm -rf /sdcard/idsfriends.txt')
        try:
            token = open('/sdcard/token.txt','r').read()
            cookie = open('/sdcard/cookies.txt','r').read()
            tokenku.append(token)
        except IOError:
            exit()
        try:
            jum = int(input('[?] CRACK ID LIMIT : '))
        except ValueError:
            print('{k}[✘] NOT PUBLIC ID ')
            exs()
        if jum<1:
            print('[✘] Your limit error')
            exs()
        ses=requests.Session()
        yz = 0
        for met in range(jum):
            yz+=1		
            kl = input('[➤] INPUT PUBLIC '+str(yz)+' : ')
            uid.append(kl)
        for userr in uid:
            try:
                rgi1 = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cookie}).json()
                ids = open("/sdcard/idsfriends.txt", "w")
                for mi in rgi1['friends']['data']:
                    uid = mi["id"]
                    na = mi["name"]
                    print(uid+"|"+na)
                    id.append(uid+"|"+na)
                    ids.write(uid+"|"+na+"\n")
            except (KeyError,IOError):
                pass
            except requests.exceptions.ConnectionError:
                print('{k}[✘] Error  ')
                exit()
        try:
            print('')
            print(f'[•] Total Id :{b}'+str(len(id)))
        except requests.exceptions.ConnectionError:
            print(f'{u}')
            print('[✘] No Internet connection ')
        except (KeyError,IOError):
            print(f'[✘] Not Public  {u}')
            time.sleep(3)
            print("")
            print(" ------------------------------------------ ")
            print("")
            print(" The process has completed")
            print(" Total ids: "+str(len(id)))
            print("")
            print(" ------------------------------------------ ")
            print("")
            input(" Press enter to download file ")
            os.system("cp /sdcard/idsfriends.txt /sdcard && rm -rf /sdcard/idsfriends.txt")
            print(" File downloaded successfully")
            time.sleep(1)
            ex_id()
    elif s in ["2",'02']:
        try:
            token = open('/sdcard/token.txt','r').read()
            cookie = open('/sdcard/cookies.txt','r').read()
            tokenku.append(token)
        except IOError:
            exit()
        try:
            jum = int(input('[?] CRACK ID LIMIT : '))
        except ValueError:
            print('{k}[✘] NOT PUBLIC ID ')
            exs()
        if jum<1:
            print('[✘] Your limit error')
            exs()
        ses=requests.Session()
        yz = 0
        for met in range(jum):
            yz+=1		
            kl = input('[➤] INPUT PUBLIC '+str(yz)+' : ')
            uid.append(kl)
        for userr in uid:
            try:
                rgi2 = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cookie}).json()
                ids = open("/sdcard/idsfriends.txt", "w")
                for mi in rgi2['friends']['data']:
                    uid = mi["id"]
                    na = mi["name"]
                    print(uid+"|"+na)
                    id.append(uid+"|"+na)
                    ids.write(uid+"|"+na+"\n")
            except (KeyError,IOError):
                pass
            except requests.exceptions.ConnectionError:
                print('{k}[✘] Error  ')
                exit()
            
        ii = open("/sdcard/idsfriends.txt", "r").read().splitlines()
        for ur in ii:
            try:
                user2=ur.split('|')[0]
                rgi3 = ses.get('https://graph.facebook.com/v2.0/'+user2+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cookie}).json()
                for mi in rgi3['friends']['data']:
                    uidd2 = mi["id"]
                    name = mi["name"]
                    print(uidd2+"|"+name)
                    id.append(uidd2+"|"+name)
                    ids.write(uidd2+"|"+name+"\n")
            except (KeyError,IOError):
                pass
            except requests.exceptions.ConnectionError:
                print('{k}[✘] Error  ')
                exit()
        try:
            print('')
            print(f'[•] Total Id :{b}'+str(len(id)))
        except requests.exceptions.ConnectionError:
            print(f'{u}')
            print('[✘] No Internet connection ')
        except (KeyError,IOError):
            print(f'[✘] Not Public  {u}')
            time.sleep(3)
            print("")
            print(" ------------------------------------------ ")
            print("")
            print(" The process has completed")
            print(" Total ids: "+str(len(id)))
            print("")
            print(" ------------------------------------------ ")
            print("")
            input(" Press enter to download file ")
            os.system("cp /sdcard/idsfriends.txt /sdcard && rm -rf /sdcard/idsfriends.txt")
            print(" File downloaded successfully")
            time.sleep(1)
            ex_id()
    elif s in ["3",'03']:
        os.system('rm -rf /sdcard/idsfriends.txt')
        try:
            token = open('/sdcard/token.txt','r').read()
            cookie = open('/sdcard/cookies.txt','r').read()
        except IOError:
            exs()
        try:
            jum = int(input('[?] CRACK ID LIMIT : '))
        except ValueError:
            print('{k}[✘] NOT PUBLIC ID ')
            time.sleep(3)
            exs()
        if jum<1:
            print('[✘] Your limit error')
            time.sleep(3)
            exs()
        ses=requests.Session()
        yz = 0
        for met in range(jum):
            yz+=1		
            kl = input('[➤] INPUT FOLLOWERS ID '+str(yz)+' : ')
            uid.append(kl)
        for userr in uid:
            try:
                rgi4 = ses.get('https://graph.facebook.com/'+userr+'?fields=subscribers.limit(99999)&access_token='+tokenku[0],cookies={'cookie': cookie}).json()
                ids = open("/sdcard/idsfriends.txt", "w")
                for mi in rgi4['subscribers']['data']:
                    uid = mi["id"]
                    na = mi["name"]
                    print(uid+"|"+na)
                    id.append(uid+"|"+na)
                    ids.write(uid+"|"+na+"\n")
                print('[•] Total Id :{h} '+str(len(id)))
            except requests.exceptions.ConnectionError:
                print('[✘] No Connection  ')
                exit()
            except (KeyError,IOError):
                print('[✘] Id Is Not Public')
                time.sleep(3)
    elif s in ["4",'04']:
        os.system('rm -rf /sdcard/idsfriends.txt')
        try:
            token = open('/sdcard/token.txt','r').read()
            cookie = open('/sdcard/cookies.txt','r').read()
            tokenku.append(token)
        except IOError:
            exit()
        try:
            jum = int(input('[?] CRACK ID LIMIT : '))
        except ValueError:
            print('{k}[✘] NOT PUBLIC ID ')
            exs()
        if jum<1:
            print('[✘] Your limit error')
            exs()
        ses=requests.Session()
        yz = 0
        for met in range(jum):
            yz+=1		
            kl = input('[➤] INPUT FOLLOWERS ID '+str(yz)+' : ')
            uid.append(kl)
        for userr in uid:
            try:
                rgi5 = ses.get('https://graph.facebook.com/'+userr+'?fields=subscribers.limit(999999)&access_token='+tokenku[0],cookies={'cookie': cookie}).json()
                ids = open("/sdcard/idsfriends.txt", "w")
                for mi in rgi5['subscribers']['data']:
                    uid = mi["id"]
                    na = mi["name"]
                    print(uid+"|"+na)
                    id.append(uid+"|"+na)
                    ids.write(uid+"|"+na+"\n")
            except (KeyError,IOError):
                pass
            except requests.exceptions.ConnectionError:
                print('{k}[✘] Error  ')
                exit()
            
        ii = open("/sdcard/idsfriends.txt", "r").read().splitlines()
        for ur in ii:
            try:
                user2=ur.split('|')[0]
                rgi6 = ses.get('https://graph.facebook.com/'+user2+'?fields=subscribers.limit(999999)&access_token='+tokenku[0],cookies={'cookie': cookie}).json()
                for mi in rgi6['subscribers']['data']:
                    uid = mi["id"]
                    na = mi["name"]
                    print(uid+"|"+na)
                    id.append(uid+"|"+na)
                    ids.write(uid+"|"+na+"\n")
            except (KeyError,IOError):
                pass
            except requests.exceptions.ConnectionError:
                print('{k}[✘] Error  ')
                exit()
        try:
            print('')
            print(f'[•] Total Id :{b}'+str(len(id)))
        except requests.exceptions.ConnectionError:
            print(f'{u}')
            print('[✘] No Internet connection ')
        except (KeyError,IOError):
            print(f'[✘] Not Public  {u}')
            time.sleep(3)
            print("")
            print(" ------------------------------------------ ")
            print("")
            print(" The process has completed")
            print(" Total ids: "+str(len(id)))
            print("")
            print(" ------------------------------------------ ")
            print("")
            input(" Press enter to download file ")
            os.system("cp idsfollowers.txt /sdcard && rm -rf /sdcard/idsfriends.txt")
            print(" File downloaded successfully")
            time.sleep(1)
            ex_id()
    elif s in ["5",'05']:
        os.system('rm -rf /sdcard/idsfriends.txt')
        try:
            token = open('/sdcard/token.txt','r').read()
            cookie = open('/sdcard/cookies.txt','r').read()
            tokenku.append(token)
        except IOError:
            exit()
        try:
            jum = int(input('[?] CRACK ID LIMIT : '))
        except ValueError:
            print('{k}[✘] NOT PUBLIC ID ')
            exs()
        if jum<1:
            print('[✘] Your limit error')
            exs()
        ses=requests.Session()
        yz = 0
        for met in range(jum):
            yz+=1		
            kl = input('[➤] INPUT FOLLOWERS ID '+str(yz)+' : ')
            uid.append(kl)
        for userr in uid:
            try:
                rgi7 = ses.get('https://graph.facebook.com/'+userr+'?fields=subscribers.limit(999999)&access_token='+tokenku[0],cookies={'cookie': cookie}).json()
                ids = open("/sdcard/idsfriends.txt", "w")
                for mi in rgi7['subscribers']['data']:
                    uid = mi["id"]
                    na = mi["name"]
                    print(uid+"|"+na)
                    id.append(uid+"|"+na)
                    ids.write(uid+"|"+na+"\n")
            except (KeyError,IOError):
                pass
            except requests.exceptions.ConnectionError:
                print('{k}[✘] Error  ')
                exit()
            
        ii = open("/sdcard/idsfriends.txt", "r").read().splitlines()
        for ur in ii:
            try:
                user2=ur.split('|')[0]
                rgi8 = ses.get('https://graph.facebook.com/v2.0/'+user2+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cookie}).json()
                for mi in rgi8['friends']['data']:
                    uidd2 = mi["id"]
                    name = mi["name"]
                    print(uidd2+"|"+name)
                    id.append(uidd2+"|"+name)
                    ids.write(uidd2+"|"+name+"\n")
            except (KeyError,IOError):
                pass
            except requests.exceptions.ConnectionError:
                print('{k}[✘] Error  ')
                exit()
        try:
            print('')
            print(f'[•] Total Id :{b}'+str(len(id)))
        except requests.exceptions.ConnectionError:
            print(f'{u}')
            print('[✘] No Internet connection ')
        except (KeyError,IOError):
            print(f'[✘] Not Public  {u}')
            time.sleep(3)
            print("")
            print(" ------------------------------------------ ")
            print("")
            print(" The process has completed")
            print(" Total ids: "+str(len(id)))
            print("")
            print(" ------------------------------------------ ")
            print("")
            input(" Press enter to download file ")
            os.system("cp idsfollowers.txt /sdcard && rm -rf /sdcard/idsfriends.txt")
            print(" File downloaded successfully")
            time.sleep(1)
            ex_id()
    elif s in ["6",'06']:
        os.system('rm -rf /sdcard/idsfriends.txt')
        print('\033[90m#DUMP FROM GROUPS MEMBERS SOON...')
        exit()
    elif s in ['7','07']:
        os.system('rm -rf /sdcard/idsfriends.txt')
        print('\033[90m#DUMP FROM REACTIONS && COMMENTS SOON...')
    elif s in ["8",'08']:
        os.system("rm -rf /sdcard/token.txt")
        os.system("rm -rf /sdcard/cookies.txt")
        print('Successful Removed Token & Cookies')
    elif s in ["0",'00']:
        exit()
try:
    open("/sdcard/token.txt", "r").read()
    open("/sdcard/cookies.txt", "r").read()
    ex_id()
except Exception as e:
    os.system("rm -rf /sdcard/token.txt")
    os.system("rm -rf /sdcard/cookies.txt")
    print(f'  %s[%s✘%s]%s LOGIN Error %s'%(x,k,x,m,x))
    os.system('clear')
    asu = random.choice([m,k,h,b,u])
    cookie=input(f'%s[%s√%s]%s Enter fresh Cookie : '%(P,H,P,H))
    data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
    find_token = re.search("(EAAG\w+)", data.text)
    ken=open("/sdcard/token.txt", "w").write(find_token.group(1))
    cookie=open("/sdcard/cookies.txt", "w").write(cookie)
    print('%s[%s✔%s]%s Login successful run again \033[1;97m\033[1;41m  \033[0m\033[1;93m'%(N,H,N,H));time.sleep(1)
    ex_id()

