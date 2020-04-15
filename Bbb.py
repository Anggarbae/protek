# Tutuy's
import linepy
from linepy import *
from akad.ttypes import *
from datetime import datetime
import pytz, pafy, time, asyncio, random, multiprocessing, timeit, sys, json, ctypes, codecs, tweepy, threading, glob, re, ast, six, os, subprocess, wikipedia, atexit, urllib, urllib.parse, urllib3, string, tempfile, shutil, unicodedata
from humanfriendly import format_timespan, format_size, format_number, format_length
import html5lib
import requests,json,urllib3
from random import randint
from bs4 import BeautifulSoup
from gtts import gTTS
from googletrans import Translator
import youtube_dl
from time import sleep
from zalgo_text import zalgo
from threading import Thread,Event
import wikipedia as wiki
requests.packages.urllib3.disable_warnings()
#=============================================
cl = LINE("olengkiller@gmail.com","olengkiller")
cl.log("Auth Token : " + str(cl.authToken))

ki = LINE("olengkiller@gmail.com","olengkiller")
ki.log("Auth Token : " + str(ki.authToken))

kk = LINE("olengkiller@gmail.com","olengkiller")
kk.log("Auth Token : " + str(kk.authToken))

kc = LINE("olengkiller@gmail.com","olengkiller")
kc.log("Auth Token : " + str(kc.authToken))

kb = LINE("olengkiller@gmail.com","olengkiller")
kb.log("Auth Token : " + str(kb.authToken))

kd = LINE("olengkiller@gmail.com","olengkiller")
kd.log("Auth Token : " + str(kd.authToken))

ke = LINE("olengkiller@gmail.com","olengkiller")
ke.log("Auth Token : " + str(ke.authToken))

kf = LINE("olengkiller@gmail.com","olengkiller")
kf.log("Auth Token : " + str(kf.authToken))

kg = LINE("olengkiller@gmail.com","olengkiller")
kg.log("Auth Token : " + str(kg.authToken))

kh = LINE("olengkiller@gmail.com","olengkiller")
kh.log("Auth Token : " + str(kh.authToken))

so = LINE("olengkiller@gmail.com","olengkiller")
so.log("Auth Token : " + str(so.authToken))

sw = LINE("olengkiller@gmail.com","olengkiller")
sw.log("Auth Token : " + str(sw.authToken))
#=============================================
print ("=====Login sukses=====")
#=============================================
poll = OEPoll(cl)
owner = ["Ubb1949ac6f0ec0e6a40c08a0ee845690"]
admin = ["Ubb1949ac6f0ec0e6a40c08a0ee845690"]
staff = ["u0c9a54e812e96da0944b2e3d59e9b6d4","uf2d4d56738a1d800df2f6e00ad8f49da","u90b8684efc5a350a749ab475edfb1c74","u65c87f2471f5399ebba8f242ad46253c"]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = kb.getProfile().mid
Emid = kd.getProfile().mid
Fmid = ke.getProfile().mid
Gmid = kf.getProfile().mid
Hmid = kg.getProfile().mid
Imid = kh.getProfile().mid
Jmid = so.getProfile().mid
Zmid = sw.getProfile().mid
AbiMuhajir = [cl,ki,kk,kc,kb,kd,ke,kf,kg,kh]
OlengBot = [cl,ki,kk,kc,kb,kd,ke,kf,kg,kh]
AbiOleng = [so,sw]
Abi = [mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,Jmid,Zmid]
OlengKiller = admin + staff
#=============================================
protectqr = []
protectkick = []
protectjoin = []
protectinvite = []
protectcancel = []
protectantijs = []
ghost = []
welcome = []
left = []
msg_dict = {}
msg_dict1 = {}
#=============================================
responsename1 = ki.getProfile().displayName
responsename2 = kk.getProfile().displayName
responsename3 = kc.getProfile().displayName
responsename4 = kb.getProfile().displayName
responsename5 = kd.getProfile().displayName
responsename6 = ke.getProfile().displayName
responsename7 = kf.getProfile().displayName
responsename8 = kg.getProfile().displayName
responsename9 = kh.getProfile().displayName
#=============================================
settings = {
    "Picture":False,
    "group":{},
    "SpamInvite":False,
    "changeCover":False,
    "changeVideo":False,
    "groupPicture":False,
    "changePicture":False,
    "autoJoinTicket":False,
    "userMention":{},
    "timeRestart": {},
    "server": {},
    "simiSimi":{},
    "userAgent": [
        "Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
        "Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
        "Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
        "Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
        "Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
    ]
}
#=============================================
wait = {
    "limit": 1,
    "owner":{},
    "admin":{},
    "addadmin":False,
    "delladmin":False,
    "staff":{},
    "addstaff":False,
    "dellstaff":False,
    "bots":{},
    "addbots":False,
    "dellbots":False,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Talkblacklist":{},
    "Talkwblacklist":False,
    "Talkdblacklist":False,
    "talkban":True,
    "contact":False,
    "invite":False,
    'autoJoin':True,
    'autoAdd':True,
    'autoLeave':False,
    'autoLeave1':False,
    "detectMention":False,
    "Mentionkick":False,
    "responOn":False,
    "welcomeOn":True,
    'autoBlock':True,
    'Timeline':True,
    "sticker":False,
    "selfbot":True,
    "Addsticker":{
            "name": "",
            "status":False
            },
    "stk":{},
    "selfbot":True,
    "Images":{},
    "Img":{},
    "Addimage":{
            "name": "",
            "status":False
            },
    "Videos":{},
    "Addaudio":{
            "name": "",
            "status":False
            },
    "Addvideo":{
            "name": "",
            "status":False
            },
    "myProfile": {
            "displayName": "",
            "coverId": "",
            "pictureStatus": "",
            "statusMessage": ""
            },
    "unsend":True,
    "mention":"gabung sini cok\nJangan Colay terus awokwkwk",
    "Respontag":"Kalo Kangen Pm aja kak\nhehe",
    "welcome":"welcome to the hell\njangan sider cok\nBukan grup bokep",
     "left":"kalo mau left pamit dulu lah bego",
    "comment":"Tenkyu for add me",
    "message":"Tenkyu for add me",
    }
#=============================================
read = {
    "readPoint":{},
    "readMember":{},
    "readTime":{},
    "ROM":{},
}

cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}
#=============================================
with open('creator.json', 'r') as fp:
    creator = json.load(fp)
with open('owner.json', 'r') as fp:
    owner = json.load(fp)
#=============================================
Setbot = codecs.open("setting.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
videosOpen = codecs.open("video.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
audiosOpen = codecs.open("audio.json","r","utf-8")
Setmain = json.load(Setbot)
images = json.load(imagesOpen)
videos = json.load(videosOpen)
stickers = json.load(stickersOpen)
audios = json.load(audiosOpen)
#=============================================
mulai = time.time()

tz = pytz.timezone("Asia/Jakarta")
timeNow = datetime.now(tz=tz)

def restart_program(): 
    python = sys.executable
    os.execl(python, python, * sys.argv)

def restartBot():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)

def runtime(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours, 24)
    return '%02d Hari %02d Jam %02d Menit %02d Detik' % (days, hours, mins, secs)
    
def sendAudioWithURL(self, to_, url):
        path = self.downloadFileWithURL(url)
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise Exception(e)

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))
        r = requests.get(url, stream=True, verify=False)
        if r.status_code == 200:
           with open(path, 'w') as f:
              shutil.copyfileobj(r.raw, f)
        else:
           raise Exception('Download audio failure.')
        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise e   

def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Mention User「{}」\n\n  [ Mention ]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def siderMembers(to, mid):
    try:
        arrData = ""
        textx = "Heh cok ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["mention"]+"\n\n✒Group name: "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
        contact = cl.getContact(op.param2).picturePath
        image = 'http://dl.profile.line.naver.jp'+contact
        cl.sendImageWithURL(op.param1, image)
        cl.sendMessage(to, None, contentMetadata={"STKID":"73760366","STKPKGID":"12228","STKVER":"2"}, contentType=7)
    except Exception as error:
        cl.sendMessage(msg.to, None, contentMetadata={"STKID":"73760366","STKPKGID":"12228","STKVER":"2"}, contentType=7)

def welcomeMembers(to, mid):
    try:
        arrData = ""
        textx = "Total Member Masuk「{}」\nheh cok  ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            ginfo = cl.getGroup(to)
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention+wait["welcome cok"]+"\nNama grup : "+str(ginfo.name)
            if no < len(mid):
                no += 1
                textx += "%i " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n[ {} ]".format(str(cl.getGroup(to).name))
                except:
                    no = "\n[ Success ]"
        cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(msg.to, None, contentMetadata={"STKID":"73760366","STKPKGID":"12228","STKVER":"2"}, contentType=7)

def sendMention1(to, mid, firstmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmiessage))
        arr = []
        mention = "@x \n"
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        today = datetime.today()
        future = datetime(2018,3,1)
        hari = (str(future - today))
        comma = hari.find(",")
        hari = hari[:comma]
        teman = cl.getAllContactIds()
        gid = cl.getGroupIdsJoined()
        tz = pytz.timezone("Asia/Jakarta")
        timeNow = datetime.now(tz=tz)
        eltime = time.time() - mulai
        bot = runtime(eltime)
        text += mention+"✒ Jam : "+datetime.strftime(timeNow,'%H:%M:%S')+" Wib\n✒ Group : "+str(len(gid))+"\n✒ Teman : "+str(len(teman))+"\n✒ Expired : In "+hari+"\n✒ Version : ReyPro Bot's v1.57\n✒ Tanggal : "+datetime.strftime(timeNow,'%Y-%m-%d')+"\n✒ Runtime : \n • "+bot
        cl.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        cl.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def sendMention(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@zeroxyuuki "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    cl.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)

def command(text):
    pesan = text.lower()
    if pesan.startswith(Setmain["keyCommand"]):
        cmd = pesan.replace(Setmain["keyCommand"],"")
    else:
        cmd = "command"
    return cmd
    
#message.createdTime -> 00:00:00
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')

#delete log if pass more than 24 hours
def delete_log1():
    ndt = datetime.now()
    for data in msg_dict1:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict1[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict1[msg_id]

def atend1():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict1, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")
    
def sendImage(to, path, name="image"):
    try:
        if setttings["server"] == "VPS":
            cl.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)    

def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')


def delete_log():
    ndt = datetime.now()
    for data in msg_dict:
        if (datetime.utcnow() - cTime_to_datetime(msg_dict[data]["createdTime"])) > datetime.timedelta(1):
            del msg_dict[msg_id]

def atend():
    print("Saving")
    with open("Log_data.json","w",encoding='utf8') as f:
        json.dump(msg_dict, f, ensure_ascii=False, indent=4,separators=(',', ': '))
    print("BYE")    

def help():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage = "xxxxxxxxxxxxxx" + "\n" + \
                  " Hayang Tutuy's" + "\n" + \
                  "xxxxxxxxxxxxxx" + "\n" + \
                  "____________" + "\n" + \
                  -"Me\n" + \
                  -"Mid「@」\n" + \
                  -"Cipok「@」\n" + \
                  -"Abi1-10「@」\n" + \
                  -"Cleanse \n" + \
                  -"Sikat「@」\n" + \
                  -"About\n" + \
                  -"Restart\n" + \
                  -"Runtime\n" + \
                  -"Creator\n" + \
                  -"Sp\n" + \
                  -"Sptime\n" + \
                  -"Mention/Kiss\n" + \
                  -"Join\n" + \
                  -"Out\n" + \
                  -"Js stay\n" + \
                  -"Bye\n" + \
                  -"Leave「Namagrup」\n" + \
                  -"Ginfo\n" + \
                  -"Open\n" + \
                  -"Close\n" + \
                  -"Remove chat\n" + \
                  -"Js「in/out」\n" + \
                  -"Intip 「on/off」\n" + \
                  -"Updatebot\n" + \
                  -"Broadcast:「Text」\n" + \
                  -"Setkey「New Key」\n" + \
                  -"Mykey\n" + \
                  -"Resetkey\n" + \
                  -"Spamcall:「jumlahnya」\n" + \
                  -"Spamcall\n" + \
                  "HELP+\n" + \
                  -"Notag「on/off」\n" + \
                  -"Allpro「on/off」\n" + \
                  -"Proqr「on/off」\n" + \
                  -"Proinvite「on/off」\n" + \
                  -"Projoin「on/off」\n" + \
                  -"Prokick「on/off」\n" + \
                  -"Procancel「on/off」\n" + \
                  "HELP++ \n" + \
                  -"Sticker「on/off」\n" + \
                  -"Respon「on/off」\n" + \
                  -"Contact「on/off」\n" + \
                  -"Autojoin「on/off」\n" + \
                  -"Autoadd「on/off」\n" + \
                  -"Welcome「on/off」\n" + \
                  -"Autoleave「on/off」\n" + \
                  "HELP+++\n" + \
                  -"Admin:on\n" + \
                  -"Admin:repeat\n" + \
                  -"Staff:on\n" + \
                  -"Staff:repeat\n" + \
                  -"Bot:on\n" + \
                  -"Bot:repeat\n" + \
                  -"Adminadd「@」\n" + \
                  -"Admindell「@」\n" + \
                  -"Staffadd「@」\n" + \
                  -"Staffdell「@」\n" + \
                  -"Botadd「@」\n" + \
                  -"Botdell「@」\n" + \
                  -"Refresh\n" + \
                  -"Listbot\n" + \
                  -"Listadmin\n" + \
                  -"Listprotect\n"+ \
                  "xxxxxxxxxxxx" + "\n" + \
                  "Dah lah mlz\nTutuy dulu"
    return helpMessage

def helpbot():
    key = Setmain["keyCommand"]
    key = key.title()
    helpMessage1 = "xxxxxxxxxxxx" + "\n" + \
                  "Hayang Tutuy's" + "\n" + \
                  "xxxxxxxxxxxx" + "\n" + \
                  "____________" + "\n" + \
                  -"Blc\n" + \
                  -"Ban:on\n" + \
                  -"Unban:on\n" + \
                  -"Ban「@」\n" + \
                  -"Unban「@」\n" + \
                  -"Talkban「@」\n" + \
                  -"Untalkban「@」\n" + \
                  - "Talkban:on\n" + \
                  -"Untalkban:on\n" + \
                  - "Banlist\n" + \
                  -"Talkban「on/off」\n" + \
                  -"Talkbanlist\n" + \
                  -"Clearban\n" + \
                  -"Refresh\n" + \
                  - "Cek sider\n" + \
                  -"Cek spam\n" + \
                  -"Cek pesan \n" + \
                  -"Cek respon \n" + \
                  -"Cek welcome\n" + \
                  -"Set sider:「Text」\n" + \
                  -"Set spam:「Text」\n" + \
                  -"Set pesan:「Text」\n" + \
                  -"Set respon:「Text」\n" + \
                  -"Set welcome:「Text」\n" + \
                  -"Myname:「Nama」\n" + \
                  -"Rname:「Nama」\n" + \
                  -"R1name:「Nama」\n" + \
                  -"R2name:「Nama」\n" + \
                  -"GhostCname:「Nama」\n" + \
                  -"abi1Up「Image」\n" + \
                  -"abi2Up「Image」\n" + \
                  -"abi3Up「Image」\n" + \
                  -"GhostUp「Image」\n" + \
                  -"Gift:「Mid」「Result」\n" + \
                  -"Spam:「Mid」「Result」\n" + \
                  "xxxxxxxxxxxx" + "\n" + \
                  "Dah lah mlz\nTutuy dulu"
                  
    return helpMessage1

def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        
        if op.type == 11:
            if op.param1 in protectqr:
                try:
                    if cl.getGroup(op.param1).preventedJoinByTicket == False:
                        if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            cl.reissueGroupTicket(op.param1)
                            X = cl.getGroup(op.param1)
                            X.preventJoinByTicket = False
                            cl.updateGroup(X)
                            Ti = cl.reissueGroupTicket(op.param1)
                            so.acceptGroupInvitationByTicket(op.param1,Ti)
                            so.sendMessage(op.param1,"wah kiker mainan qr minta di cipok")
                            so.kickoutFromGroup(op.param1,[op.param2])
                            wait["blacklist"][op.param2] = True
                            X = so.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            so.updateGroup(X)
                            so.leaveGroup(op.param1)
                            cl.findAndAddContactsByMid(op.param1,[Jmid])
                            cl.inviteIntoGroup(op.param1,[Jmid])
                except:
                    try:
                        if ki.getGroup(op.param1).preventedJoinByTicket == False:
                            if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                ki.reissueGroupTicket(op.param1)
                                X = ki.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                ki.updateGroup(X)
                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                    except:
                        try:
                            if kk.getGroup(op.param1).preventedJoinByTicket == False:
                                if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    kk.reissueGroupTicket(op.param1)
                                    X = kk.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    kk.updateGroup(X)
                                    cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                        except:
                            try:
                                if kc.getGroup(op.param1).preventedJoinByTicket == False:
                                    if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        kc.reissueGroupTicket(op.param1)
                                        X = kc.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        kc.updateGroup(X)
                                        cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                            except:
                                try:
                                    if kb.getGroup(op.param1).preventedJoinByTicket == False:
                                        if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            kb.reissueGroupTicket(op.param1)
                                            X = kb.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            kb.updateGroup(X)
                                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                except:
                                    try:
                                        if kd.getGroup(op.param1).preventedJoinByTicket == False:
                                            if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                kd.reissueGroupTicket(op.param1)
                                                X = kd.getGroup(op.param1)
                                                X.preventedJoinByTicket = True
                                                kd.updateGroup(X)
                                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)
                                    except:
                                        try:
                                            if ke.getGroup(op.param1).preventedJoinByTicket == False:
                                                if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                    ke.reissueGroupTicket(op.param1)
                                                    X = ke.getGroup(op.param1)
                                                    X.preventedJoinByTicket = True
                                                    ke.updateGroup(X)
                                                    cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)            
                                        except:
                                            try:
                                                if kf.getGroup(op.param1).preventedJoinByTicket == False:
                                                    if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                        kf.reissueGroupTicket(op.param1)
                                                        X = kf.getGroup(op.param1)
                                                        X.preventedJoinByTicket = True
                                                        kf.updateGroup(X)
                                                        cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)           
                                            except:
                                                try:
                                                    if kg.getGroup(op.param1).preventedJoinByTicket == False:
                                                        if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                            kg.reissueGroupTicket(op.param1)
                                                            X = kg.getGroup(op.param1)
                                                            X.preventedJoinByTicket = True
                                                            kg.updateGroup(X)
                                                            cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)          
                                                except:
                                                    try:
                                                        if kh.getGroup(op.param1).preventedJoinByTicket == False:
                                                            if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                                                kh.reissueGroupTicket(op.param1)
                                                                X = kh.getGroup(op.param1)
                                                                X.preventedJoinByTicket = True
                                                                kh.updateGroup(X)
                                                                cl.sendMessage(op.param1, None, contentMetadata={'mid': op.param2}, contentType=13)             
                                                    except:
                                                        pass
                                                        
        if op.type == 13:
            if mid in op.param3:
                if wait["autoLeave"] == True:
                    if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                        cl.leaveGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)

        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                        ginfo = cl.getGroup(op.param1)
            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.leaveGroup(op.param1)
                    else:
                        ki.acceptGroupInvitation(op.param1)
                        ginfo = ki.getGroup(op.param1)
                        ki.sendMessage(op.param1,"Hai cok " + str(ginfo.name))
            if Bmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
                        kk.leaveGroup(op.param1)
                    else:
                        kk.acceptGroupInvitation(op.param1)
                        ginfo = kk.getGroup(op.param1)
            if Cmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
                        kc.sendMessage(op.param1,"bye cok\n Group " +str(ginfo.name))
                        kc.leaveGroup(op.param1)
                    else:
                        kc.acceptGroupInvitation(op.param1)
                        ginfo = kc.getGroup(op.param1)
            if Dmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
                        kb.leaveGroup(op.param1)
                    else:
                        kb.acceptGroupInvitation(op.param1)
                        ginfo = kb.getGroup(op.param1)
            if Emid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kd.acceptGroupInvitation(op.param1)
                        ginfo = kd.getGroup(op.param1)
                        kd.leaveGroup(op.param1)
                    else:
                        kd.acceptGroupInvitation(op.param1)
                        ginfo = kd.getGroup(op.param1)
            if Fmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)
                        ke.leaveGroup(op.param1)
                    else:
                        ke.acceptGroupInvitation(op.param1)
                        ginfo = ke.getGroup(op.param1)   
            if Gmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kf.acceptGroupInvitation(op.param1)
                        ginfo = kf.getGroup(op.param1)
                        kf.leaveGroup(op.param1)
                    else:
                        kf.acceptGroupInvitation(op.param1)
                        ginfo = kf.getGroup(op.param1) 
            if Hmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kg.acceptGroupInvitation(op.param1)
                        ginfo = kg.getGroup(op.param1)
                        kg.leaveGroup(op.param1)
                    else:
                        kg.acceptGroupInvitation(op.param1)
                        ginfo = kg.getGroup(op.param1)
            if Imid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        kh.acceptGroupInvitation(op.param1)
                        ginfo = kh.getGroup(op.param1)
                        kh.leaveGroup(op.param1)
                    else:
                        kh.acceptGroupInvitation(op.param1)
                        ginfo = kh.getGroup(op.param1)
            if Jmid in op.param3:
                if wait["autoJoin"] == True:
                    if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        so.acceptGroupInvitation(op.param1)
                        ginfo = so.getGroup(op.param1)
                        so.leaveGroup(op.param1)
                    else:
                        so.acceptGroupInvitation(op.param1)
                        ginfo = so.getGroup(op.param1)
                        
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        random.choice(OlengBot).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        pass
                        
        if op.type == 13:
            if op.param1 in protectinvite:
                if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    try:
                        group = cl.getGroup(op.param1)
                        gMembMids = [contact.mid for contact in group.invitee]
                        for op.param3 in gMembMids:
                            cl.cancelGroupInvitation(op.param1, gMembMids)
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.sendMessage(op.param1,"lu nginvite siapa cok")
                    except:
                        try:
                            group = ki.getGroup(op.param1)
                            gMembMids = [contact.mid for contact in group.invitee]
                            for op.param3 in gMembMids:
                                ki.cancelGroupInvitation(op.param1, gMembMids)
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.sendMessage(op.param1,"lu nginvite siapa cok")
                        except:
                            try:
                                group = kk.getGroup(op.param1)
                                gMembMids = [contact.mid for contact in group.invitee]
                                for op.param3 in gMembMids:
                                    kk.cancelGroupInvitation(op.param1, gMembMids)
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kk.sendMessage(op.param1,"lu nginvite siapa cok")
                            except:
                                try:
                                    group = kc.getGroup(op.param1)
                                    gMembMids = [contact.mid for contact in group.invitee]
                                    for op.param3 in gMembMids:
                                        kc.cancelGroupInvitation(op.param1, gMembMids)
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                        kc.sendMessage(op.param1,"lu nginvite siapa cok")
                                except:
                                    try:
                                        group = kb.getGroup(op.param1)
                                        gMembMids = [contact.mid for contact in group.invitee]
                                        for op.param3 in gMembMids:
                                            kb.cancelGroupInvitation(op.param1, gMembMids)
                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                            kb.sendMessage(op.param1,"lu nginvite siapa cok")
                                    except:
                                        try:
                                            group = kd.getGroup(op.param1)
                                            gMembMids = [contact.mid for contact in group.invitee]
                                            for op.param3 in gMembMids:
                                                kd.cancelGroupInvitation(op.param1, gMembMids)
                                                kd.kickoutFromGroup(op.param1,[op.param2])
                                                kd.sendMessage(op.param1,"lu nginvite siapa cok")
                                        except:
                                            try:
                                                group = ke.getGroup(op.param1)
                                                gMembMids = [contact.mid for contact in group.invitee]
                                                for op.param3 in gMembMids:
                                                    ke.cancelGroupInvitation(op.param1, gMembMids)
                                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                                    ke.sendMessage(op.param1,"lu nginvite siapa cok")
                                            except:
                                                try:
                                                    group = kf.getGroup(op.param1)
                                                    gMembMids = [contact.mid for contact in group.invitee]
                                                    for op.param3 in gMembMids:
                                                        kf.cancelGroupInvitation(op.param1, gMembMids)
                                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                                        kf.sendMessage(op.param1,"lu nginvite siapa cok")
                                                except:
                                                    try:
                                                        group = kg.getGroup(op.param1)
                                                        gMembMids = [contact.mid for contact in group.invitee]
                                                        for op.param3 in gMembMids:
                                                            kg.cancelGroupInvitation(op.param1, gMembMids)
                                                            kg.kickoutFromGroup(op.param1,[op.param2])
                                                            kg.sendMessage(op.param1,"lu nginvite siapa cok")
                                                    except:
                                                        try:
                                                            group = kh.getGroup(op.param1)
                                                            gMembMids = [contact.mid for contact in group.invitee]
                                                            for op.param3 in gMembMids:
                                                                kh.cancelGroupInvitation(op.param1, gMembMids)
                                                                kh.kickoutFromGroup(op.param1,[op.param2])
                                                                kh.sendMessage(op.param1,"lu nginvite siapa cok")       
                                                        except:
                                                            pass

        if op.type == 17:
            if op.param2 in wait["blacklist"]:
                random.choice(OlengBot).kickoutFromGroup(op.param1,[op.param2])
                random.choice(OlengBot).cancelGroupInvitation(op.param1,[op.param2])
            else:
                pass

        if op.type == 17:
            if op.param1 in welcome:
                if op.param2 in Abi:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                welcomeMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)
                
        if op.type == 17:
            if op.param1 in left:
                if op.param2 in Abi:
                    pass
                ginfo = cl.getGroup(op.param1)
                contact = cl.getContact(op.param2).picturePath
                image = 'http://dl.profile.line.naver.jp'+contact
                leftMembers(op.param1, [op.param2])
                cl.sendImageWithURL(op.param1, image)
                sendMention(to, "Si jones Baper«@!", [sender])
                cl.sendContact(to, sender)
                
                return

        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if (wait["message"] in [" "," ","\n",None]):
                        pass
                    else:
                        cl.sendMessage(op.param1, wait["message"])
                        ki.sendMessage(op.param1, wait["message"])
                        kk.sendMessage(op.param1, wait["message"])
                        kc.sendMessage(op.param1, wait["message"])
                        kd.sendMessage(op.param1, wait["message"])
                        kb.sendMessage(op.param1, wait["message"])
                        ke.sendMessage(op.param1, wait["message"])
                        kf.sendMessage(op.param1, wait["message"])
                        kg.sendMessage(op.param1, wait["message"])
                        kh.sendMessage(op.param1, wait["message"])
                        so.sendMessage(op.param1, wait["message"])
                        sw.sendMessage(op.param1, wait["message"])

        if op.type == 19:
            if op.param1 in protectkick:
                if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    random.choice(OlengBot).kickoutFromGroup(op.param1,[op.param2])
                    random.choice(OlengBot).cancelGroupInvitation(op.param1,[op.param2])
                else:
                	pass
                
        if op.type == 19:
            if op.param1 in ghost:
                try:
                    if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        G = cl.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        cl.updateGroup(G)
                        invsend = 0
                        Ticket = cl.reissueGroupTicket(op.param1)
                        sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                        sw.cancelGroupInvitation(op.param1,[op.param2])
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                        sw.sendMessage(op.param1,"Wah kicket bgst awokwok")
                        sw.leaveGroup(op.param1)
                        X = cl.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        cl.updateGroup(X)
                except:
                    try:
                        if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                            G = ki.getGroup(op.param1)
                            G.preventedJoinByTicket = False
                            ki.updateGroup(G)
                            invsend = 0
                            Ticket = ki.reissueGroupTicket(op.param1)
                            so.acceptGroupInvitationByTicket(op.param1,Ticket)
                            so.cancelGroupInvitation(op.param1,[op.param2])
                            so.kickoutFromGroup(op.param1,[op.param2])
                            wait["blacklist"][op.param2] = True
                            so.sendMessage(op.param1,"hajar sini cok")
                            so.leaveGroup(op.param1)
                            X = ki.getGroup(op.param1)
                            X.preventedJoinByTicket = True
                            ki.updateGroup(X)
                    except:
                        try:
                            if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                G = kk.getGroup(op.param1)
                                G.preventedJoinByTicket = False
                                kk.updateGroup(G)
                                invsend = 0
                                Ticket = kk.reissueGroupTicket(op.param1)
                                so.acceptGroupInvitationByTicket(op.param1,Ticket)
                                so.cancelGroupInvitation(op.param1,[op.param2])
                                so.kickoutFromGroup(op.param1,[op.param2])
                                wait["blacklist"][op.param2] = True
                                so.sendMessage(op.param1,"hajar sini cok")
                                so.leaveGroup(op.param1)
                                X = kk.getGroup(op.param1)
                                X.preventedJoinByTicket = True
                                kk.updateGroup(X)
                        except:
                            try:
                                if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                    G = kc.getGroup(op.param1)
                                    G.preventedJoinByTicket = False
                                    kc.updateGroup(G)
                                    invsend = 0
                                    Ticket = kc.reissueGroupTicket(op.param1)
                                    so.acceptGroupInvitationByTicket(op.param1,Ticket)
                                    so.cancelGroupInvitation(op.param1,[op.param2])
                                    so.kickoutFromGroup(op.param1,[op.param2])
                                    wait["blacklist"][op.param2] = True
                                    so.sendMessage(op.param1,"hajar sini cok")
                                    so.leaveGroup(op.param1)
                                    X = kc.getGroup(op.param1)
                                    X.preventedJoinByTicket = True
                                    kc.updateGroup(X)
                            except:
                                try:
                                    if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                        G = kb.getGroup(op.param1)
                                        G.preventedJoinByTicket = False
                                        kb.updateGroup(G)
                                        invsend = 0
                                        Ticket = kb.reissueGroupTicket(op.param1)
                                        so.acceptGroupInvitationByTicket(op.param1,Ticket)
                                        so.cancelGroupInvitation(op.param1,[op.param2])
                                        so.kickoutFromGroup(op.param1,[op.param2])
                                        wait["blacklist"][op.param2] = True
                                        so.sendMessage(op.param1,"hajar sini cok")
                                        so.leaveGroup(op.param1)
                                        X = kb.getGroup(op.param1)
                                        X.preventedJoinByTicket = True
                                        kb.updateGroup(X)
                                except:
                                    try:
                                        if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                                            G = ke.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            ke.updateGroup(G)
                                            invsend = 0
                                            Ticket = ke.reissueGroupTicket(op.param1)
                                            so.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            so.cancelGroupInvitation(op.param1,[op.param2])
                                            so.kickoutFromGroup(op.param1,[op.param2])
                                            wait["blacklist"][op.param2] = True
                                            so.sendMessage(op.param1,"hajar sini cok")
                                            so.leaveGroup(op.param1)
                                            X = ke.getGroup(op.param1)
                                            X.preventedJoinByTicket = True
                                            ke.updateGroup(X)       
                                    except:
                                        pass
      
        if op.type == 19:
            try:
                if op.param1 in protectantijs:
                  if op.param3 in mid:
                    if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        sw.acceptGroupInvitation(op.param1)
                        sw.cancelGroupInvitation(op.param1,[op.param2])
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        G = sw.getGroup(op.param1)
                        G.preventedJoinByTicket = False
                        sw.updateGroup(G)
                        invsend = 0
                        Ticket = sw.reissueGroupTicket(op.param1)
                        cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                        ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                        kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                        so.acceptGroupInvitationByTicket(op.param1,Ticket)
                        wait["blacklist"][op.param2] = True
                        X = sw.getGroup(op.param1)
                        X.preventedJoinByTicket = True
                        sw.updateGroup(X)       
                        sw.inviteIntoGroup(op.param1,[admin])
                        sw.leaveGroup(op.param1)
                        cl.findAndAddContactsByMid(op.param1,[Jmid,Zmid])
                        cl.inviteIntoGroup(op.param1,[Jmid,Zmid])
                        cl.inviteIntoGroup(op.param1,[admin])
                    else:
                        pass
                        
                if op.param3 in Zmid:
                    if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.cancelGroupInvitation(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        cl.sendMessage(op.param1,"hajar sini cok")
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.cancelGroupInvitation(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.inviteIntoGroup(op.param1,[Zmid])
                        cl.sendMessage(op.param1,"hajar sini cok")
                        
                if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if op.param3 in admin:
                        if op.param1 in protectantijs:
                            wait["blacklist"][op.param2] = True
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.cancelGroupInvitation(op.param1,[op.param2])
                            cl.findAndAddContactsByMid(op.param3)
                            cl.inviteIntoGroup(op.param1,[op.param3])
                else:
                    pass
            except:
                pass
                
        if op.type == 19:
            try:
                if op.param1 in protectantijs:
                  if op.param3 in mid:
                    if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        so.acceptGroupInvitation(op.param1)
                        so.kickoutFromGroup(op.param1,[op.param2])
                        so.cancelGroupInvitation(op.param1,[op.param2])
                        wait["blacklist"][op.param2] = True
                        so.leaveGroup(op.param1)
                        cl.findAndAddContactsByMid(op.param1,[Jmid])
                        cl.inviteIntoGroup(op.param1,[Jmid])
                        cl.inviteIntoGroup(op.param1,[admin])
                    else:
                        pass
                        
                if op.param3 in Jmid:
                    if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.cancelGroupInvitation(op.param1,[op.param2])
                        cl.inviteIntoGroup(op.param1,[Jmid])
                    else:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param3)
                        cl.cancelGroupInvitation(op.param1,[op.param2])
                        cl.inviteIntoGroup(op.param1,[Jmid])
                        
                if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    if op.param3 in admin:
                        if op.param1 in protectantijs:
                            wait["blacklist"][op.param2] = True
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.findAndAddContactsByMid(op.param3)
                            cl.inviteIntoGroup(op.param1,[op.param3])
                else:
                    pass
            except:
                pass   
        
        if op.type == 32:
            if op.param1 in protectcancel:
              if op.param3 in Abi:    
                if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param3 not in wait["blacklist"]:
                            random.choice(OlengBot).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(OlengBot).inviteIntoGroup(op.param1,[Jmid,Zmid])
                    except:
                        pass
         
        if op.type == 32:
            if op.param1 in protectcancel:
              if op.param3 in Abi:    
                if op.param2 not in Abi and op.param2 not in owner and op.param2 not in admin and op.param2 not in staff:
                    wait["blacklist"][op.param2] = True
                    try:
                        if op.param2 not in wait["blacklist"]:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            if op.param2 not in wait["blacklist"]:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                if op.param2 not in wait["blacklist"]:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    if op.param2 not in wait["blacklist"]:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        if op.param2 not in wait["blacklist"]:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            if op.param2 not in wait["blacklist"]:
                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                                ke.cancelGroupInvitation(op.param1,[op.param2])
                                        except:
                                            try:
                                                if op.param2 not in wait["blacklist"]:
                                                    kf.kickoutFromGroup(op.param1,[op.param2])
                                                    kf.cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                try:
                                                    if op.param2 not in wait["blacklist"]:
                                                        kg.kickoutFromGroup(op.param1,[op.param2])
                                                        kg.cancelGroupInvitation(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        if op.param2 not in wait["blacklist"]:
                                                            kh.kickoutFromGroup(op.param1,[op.param2])
                                                            kh.cancelGroupInvitation(op.param1,[op.param2])
                                                    except:
                                                        pass
                                                        
                return

        if op.type == 19:
            if mid in op.param3:
                if op.param2 in Abi:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        ki.kickoutFromGroup(op.param1,[op.param2])
                        ki.inviteIntoGroup(op.param1,[op.param3])
                        cl.acceptGroupInvitation(op.param1)
                        ki.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            kk.kickoutFromGroup(op.param1,[op.param2])
                            kk.inviteIntoGroup(op.param1,[op.param3])
                            cl.acceptGroupInvitation(op.param1)
                            kk.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                kc.kickoutFromGroup(op.param1,[op.param2])
                                kc.inviteIntoGroup(op.param1,[op.param3])
                                cl.acceptGroupInvitation(op.param1)
                                kc.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                    cl.acceptGroupInvitation(op.param1)
                                    kb.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                        cl.acceptGroupInvitation(op.param1)
                                        kd.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = ki.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            ki.updateGroup(G)
                                            Ticket = ki.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            so.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            random.choice(OlengBot).kickoutFromGroup(op.param1,[op.param2])
                                            random.choice(OlengBot).cancelGroupInvitation(op.param1,[op.param2])
                                        except:
                                            try:
                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                                ke.inviteIntoGroup(op.param1,[op.param3])
                                                cl.acceptGroupInvitation(op.param1)
                                                ke.cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                try:
                                                    kf.kickoutFromGroup(op.param1,[op.param2])
                                                    kf.inviteIntoGroup(op.param1,[op.param3])
                                                    cl.acceptGroupInvitation(op.param1)
                                                    kf.cancelGroupInvitation(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        kg.kickoutFromGroup(op.param1,[op.param2])
                                                        kg.inviteIntoGroup(op.param1,[op.param3])
                                                        cl.acceptGroupInvitation(op.param1)
                                                        kg.cancelGroupInvitation(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            kh.kickoutFromGroup(op.param1,[op.param2])
                                                            kh.inviteIntoGroup(op.param1,[op.param3])
                                                            cl.acceptGroupInvitation(op.param1)
                                                            kh.cancelGroupInvitation(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                sw.kickoutFromGroup(op.param1,[op.param2])
                                                                sw.inviteIntoGroup(op.param1,[op.param3])
                                                                cl.acceptGroupInvitation(op.param1)
                                                                sw.cancelGroupInvitation(op.param1,[op.param2])
                                                            except:
                                                                try:
                                                                    so.kickoutFromGroup(op.param1,[op.param2])
                                                                    so.inviteIntoGroup(op.param1,[op.param3])
                                                                    cl.acceptGroupInvitation(op.param1)
                                                                    so.cancelGroupInvitation(op.param1,[op.param2])
                                                                except:
                                                                    pass
                                                                    
                return

        if op.type == 19:
            if Amid in op.param3:
                if op.param2 in Abi:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kk.inviteIntoGroup(op.param1,[op.param3])
                        ki.acceptGroupInvitation(op.param1)
                        kk.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            kc.kickoutFromGroup(op.param1,[op.param2])
                            kc.inviteIntoGroup(op.param1,[op.param3])
                            ki.acceptGroupInvitation(op.param1)
                            kc.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                kb.kickoutFromGroup(op.param1,[op.param2])
                                kb.inviteIntoGroup(op.param1,[op.param3])
                                ki.acceptGroupInvitation(op.param1)
                                kb.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                    ki.acceptGroupInvitation(op.param1)
                                    kd.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        ki.acceptGroupInvitation(op.param1)
                                        cl.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = ki.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            ki.updateGroup(G)
                                            Ticket = ki.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            so.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            random.choice(OlengBot).kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                so.kickoutFromGroup(op.param1,[op.param2])
                                                so.inviteIntoGroup(op.param1,[op.param3])
                                                ki.acceptGroupInvitation(op.param1)
                                                so.cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                try:
                                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                                    ki.acceptGroupInvitation(op.param1)
                                                    ke.cancelGroupInvitation(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                                        kf.inviteIntoGroup(op.param1,[op.param3])
                                                        ki.acceptGroupInvitation(op.param1)
                                                        kf.cancelGroupInvitation(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            kg.kickoutFromGroup(op.param1,[op.param2])
                                                            kg.inviteIntoGroup(op.param1,[op.param3])
                                                            ki.acceptGroupInvitation(op.param1)
                                                            kg.cancelGroupInvitation(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                kh.kickoutFromGroup(op.param1,[op.param2])
                                                                kh.inviteIntoGroup(op.param1,[op.param3])
                                                                ki.acceptGroupInvitation(op.param1)
                                                                kh.cancelGroupInvitation(op.param1,[op.param2])
                                                            except:
                                                                try:
                                                                    sw.kickoutFromGroup(op.param1,[op.param2])
                                                                    sw.inviteIntoGroup(op.param1,[op.param3])
                                                                    ki.acceptGroupInvitation(op.param1)
                                                                    sw.cancelGroupInvitation(op.param1,[op.param2])
                                                                except:
                                                                    pass
                                            
                return

        if op.type == 19:
            if Bmid in op.param3:
                if op.param2 in Abi:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kc.kickoutFromGroup(op.param1,[op.param2])
                        kc.inviteIntoGroup(op.param1,[op.param3])
                        kk.acceptGroupInvitation(op.param1)
                        kc.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            kb.kickoutFromGroup(op.param1,[op.param2])
                            kb.inviteIntoGroup(op.param1,[op.param3])
                            kk.acceptGroupInvitation(op.param1)
                            kb.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                kd.kickoutFromGroup(op.param1,[op.param2])
                                kd.inviteIntoGroup(op.param1,[op.param3])
                                kk.acceptGroupInvitation(op.param1)
                                kd.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                    kk.acceptGroupInvitation(op.param1)
                                    ke.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                        kf.inviteIntoGroup(op.param1,[op.param3])
                                        kk.acceptGroupInvitation(op.param1)
                                        kf.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = kk.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kk.updateGroup(G)
                                            Ticket = kk.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            so.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            random.choice(OlengBot).kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                kg.kickoutFromGroup(op.param1,[op.param2])
                                                kg.inviteIntoGroup(op.param1,[op.param3])
                                                kk.acceptGroupInvitation(op.param1)
                                                kg.cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                try:
                                                    kh.kickoutFromGroup(op.param1,[op.param2])
                                                    kh.inviteIntoGroup(op.param1,[op.param3])
                                                    kk.acceptGroupInvitation(op.param1)
                                                    kh.cancelGroupInvitation(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                                        kk.acceptGroupInvitation(op.param1)
                                                        cl.cancelGroupInvitation(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            ki.kickoutFromGroup(op.param1,[op.param2])
                                                            ki.inviteIntoGroup(op.param1,[op.param3])
                                                            kk.acceptGroupInvitation(op.param1)
                                                            ki.cancelGroupInvitation(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                sw.kickoutFromGroup(op.param1,[op.param2])
                                                                sw.inviteIntoGroup(op.param1,[op.param3])
                                                                kk.acceptGroupInvitation(op.param1)
                                                                sw.cancelGroupInvitation(op.param1,[op.param2])
                                                            except:
                                                                try:
                                                                   so.kickoutFromGroup(op.param1,[op.param2])
                                                                   so.inviteIntoGroup(op.param1,[op.param3])
                                                                   kk.acceptGroupInvitation(op.param1)
                                                                   so.cancelGroupInvitation(op.param1,[op.param2])
                                                                except:
                                                                    pass
                                            
                return

        if op.type == 19:
            if Cmid in op.param3:
                if op.param2 in Abi:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kb.kickoutFromGroup(op.param1,[op.param2])
                        kb.inviteIntoGroup(op.param1,[op.param3])
                        kc.acceptGroupInvitation(op.param1)
                        kb.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            kd.kickoutFromGroup(op.param1,[op.param2])
                            kd.inviteIntoGroup(op.param1,[op.param3])
                            kc.acceptGroupInvitation(op.param1)
                            kd.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                ke.kickoutFromGroup(op.param1,[op.param2])
                                ke.inviteIntoGroup(op.param1,[op.param3])
                                kc.acceptGroupInvitation(op.param1)
                                ke.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kf.kickoutFromGroup(op.param1,[op.param2])
                                    kf.inviteIntoGroup(op.param1,[op.param3])
                                    kc.acceptGroupInvitation(op.param1)
                                    kf.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        kg.kickoutFromGroup(op.param1,[op.param2])
                                        kg.inviteIntoGroup(op.param1,[op.param3])
                                        kc.acceptGroupInvitation(op.param1)
                                        kg.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = kc.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kc.updateGroup(G)
                                            Ticket = kc.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            so.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            random.choice(OlengBot).kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                kh.kickoutFromGroup(op.param1,[op.param2])
                                                kh.inviteIntoGroup(op.param1,[op.param3])
                                                kc.acceptGroupInvitation(op.param1)
                                                kh.cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                try:
                                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                                    cl.inviteIntoGroup(op.param1,[op.param3])
                                                    kc.acceptGroupInvitation(op.param1)
                                                    cl.cancelGroupInvitation(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                                        kc.acceptGroupInvitation(op.param1)
                                                        ki.cancelGroupInvitation(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            kk.kickoutFromGroup(op.param1,[op.param2])
                                                            kk.inviteIntoGroup(op.param1,[op.param3])
                                                            kc.acceptGroupInvitation(op.param1)
                                                            kk.cancelGroupInvitation(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                sw.kickoutFromGroup(op.param1,[op.param2])
                                                                sw.inviteIntoGroup(op.param1,[op.param3])
                                                                kc.acceptGroupInvitation(op.param1)
                                                                sw.cancelGroupInvitation(op.param1,[op.param2])
                                                            except:
                                                                try:
                                                                   so.kickoutFromGroup(op.param1,[op.param2])
                                                                   so.inviteIntoGroup(op.param1,[op.param3])
                                                                   kc.acceptGroupInvitation(op.param1)
                                                                   so.cancelGroupInvitation(op.param1,[op.param2])
                                                                except:
                                                                    pass
                                    
                return

        if op.type == 19:
            if Dmid in op.param3:
                if op.param2 in Abi:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kd.kickoutFromGroup(op.param1,[op.param2])
                        kd.inviteIntoGroup(op.param1,[op.param3])
                        kb.acceptGroupInvitation(op.param1)
                        kd.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            ke.kickoutFromGroup(op.param1,[op.param2])
                            ke.inviteIntoGroup(op.param1,[op.param3])
                            kb.acceptGroupInvitation(op.param1)
                            ke.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                kf.kickoutFromGroup(op.param1,[op.param2])
                                kf.inviteIntoGroup(op.param1,[op.param3])
                                kb.acceptGroupInvitation(op.param1)
                                kf.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kg.kickoutFromGroup(op.param1,[op.param2])
                                    kg.inviteIntoGroup(op.param1,[op.param3])
                                    kb.acceptGroupInvitation(op.param1)
                                    kg.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        kh.kickoutFromGroup(op.param1,[op.param2])
                                        kh.inviteIntoGroup(op.param1,[op.param3])
                                        kb.acceptGroupInvitation(op.param1)
                                        kh.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = kb.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kb.updateGroup(G)
                                            Ticket = kb.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            so.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            random.choice(OlengBot).kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                cl.kickoutFromGroup(op.param1,[op.param2])
                                                cl.inviteIntoGroup(op.param1,[op.param3])
                                                kb.acceptGroupInvitation(op.param1)
                                                cl.cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                try:
                                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                                    kb.acceptGroupInvitation(op.param1)
                                                    ki.cancelGroupInvitation(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                                        kb.acceptGroupInvitation(op.param1)
                                                        kk.cancelGroupInvitation(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            kc.kickoutFromGroup(op.param1,[op.param2])
                                                            kc.inviteIntoGroup(op.param1,[op.param3])
                                                            kb.acceptGroupInvitation(op.param1)
                                                            kc.cancelGroupInvitation(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                sw.kickoutFromGroup(op.param1,[op.param2])
                                                                sw.inviteIntoGroup(op.param1,[op.param3])
                                                                kb.acceptGroupInvitation(op.param1)
                                                                sw.cancelGroupInvitation(op.param1,[op.param2])
                                                            except:
                                                                try:
                                                                   so.kickoutFromGroup(op.param1,[op.param2])
                                                                   so.inviteIntoGroup(op.param1,[op.param3])
                                                                   kb.acceptGroupInvitation(op.param1)
                                                                   so.cancelGroupInvitation(op.param1,[op.param2])
                                                                except:
                                                                    pass            

                return

        if op.type == 19:
            if Emid in op.param3:
                if op.param2 in Abi:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try: 
                        ke.kickoutFromGroup(op.param1,[op.param2])
                        ke.inviteIntoGroup(op.param1,[op.param3])
                        kd.acceptGroupInvitation(op.param1)
                        ke.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            kf.kickoutFromGroup(op.param1,[op.param2])
                            kf.inviteIntoGroup(op.param1,[op.param3])
                            kd.acceptGroupInvitation(op.param1)
                            kf.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                kg.kickoutFromGroup(op.param1,[op.param2])
                                kg.inviteIntoGroup(op.param1,[op.param3])
                                kd.acceptGroupInvitation(op.param1)
                                kg.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kh.kickoutFromGroup(op.param1,[op.param2])
                                    kh.inviteIntoGroup(op.param1,[op.param3])
                                    kd.acceptGroupInvitation(op.param1)
                                    kh.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        cl.kickoutFromGroup(op.param1,[op.param2])
                                        cl.inviteIntoGroup(op.param1,[op.param3])
                                        kd.acceptGroupInvitation(op.param1)
                                        cl.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = kd.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kd.updateGroup(G)
                                            Ticket = kd.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            so.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            random.choice(OlengBot).kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                ki.kickoutFromGroup(op.param1,[op.param2])
                                                ki.nviteIntoGroup(op.param1,[op.param3])
                                                kd.acceptGroupInvitation(op.param1)
                                                ki.cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                try:
                                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                                    kd.acceptGroupInvitation(op.param1)
                                                    kk.cancelGroupInvitation(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                                        kd.acceptGroupInvitation(op.param1)
                                                        kc.cancelGroupInvitation(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            kb.kickoutFromGroup(op.param1,[op.param2])
                                                            kb.inviteIntoGroup(op.param1,[op.param3])
                                                            kd.acceptGroupInvitation(op.param1)
                                                            kb.cancelGroupInvitation(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                sw.kickoutFromGroup(op.param1,[op.param2])
                                                                sw.inviteIntoGroup(op.param1,[op.param3])
                                                                kd.acceptGroupInvitation(op.param1)
                                                                sw.cancelGroupInvitation(op.param1,[op.param2])
                                                            except:
                                                                try:
                                                                   so.kickoutFromGroup(op.param1,[op.param2])
                                                                   so.inviteIntoGroup(op.param1,[op.param3])
                                                                   kd.acceptGroupInvitation(op.param1)
                                                                   so.cancelGroupInvitation(op.param1,[op.param2])
                                                                except:
                                                                    pass
                                                                   
                return

        if op.type == 19:
            if Fmid in op.param3:
                if op.param2 in Abi:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try: 
                        kf.kickoutFromGroup(op.param1,[op.param2])
                        kf.inviteIntoGroup(op.param1,[op.param3])
                        ke.acceptGroupInvitation(op.param1)
                        kf.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            kg.kickoutFromGroup(op.param1,[op.param2])
                            kg.inviteIntoGroup(op.param1,[op.param3])
                            ke.acceptGroupInvitation(op.param1)
                            kg.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                kh.kickoutFromGroup(op.param1,[op.param2])
                                kh.inviteIntoGroup(op.param1,[op.param3])
                                ke.acceptGroupInvitation(op.param1)
                                kh.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    cl.kickoutFromGroup(op.param1,[op.param2])
                                    cl.inviteIntoGroup(op.param1,[op.param3])
                                    ke.acceptGroupInvitation(op.param1)
                                    cl.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        ki.kickoutFromGroup(op.param1,[op.param2])
                                        ki.inviteIntoGroup(op.param1,[op.param3])
                                        ke.acceptGroupInvitation(op.param1)
                                        ki.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = ke.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            ke.updateGroup(G)
                                            Ticket = ke.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            so.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            random.choice(OlengBot).kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                kk.kickoutFromGroup(op.param1,[op.param2])
                                                kk.inviteIntoGroup(op.param1,[op.param3])
                                                ke.acceptGroupInvitation(op.param1)
                                                kk.cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                try:
                                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                                    ke.acceptGroupInvitation(op.param1)
                                                    kc.cancelGroupInvitation(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                                        kb.inviteIntoGroup(op.param1,[op.param3])
                                                        ke.acceptGroupInvitation(op.param1)
                                                        kb.cancelGroupInvitation(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                                            kd.inviteIntoGroup(op.param1,[op.param3])
                                                            ke.acceptGroupInvitation(op.param1)
                                                            kd.cancelGroupInvitation(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                sw.kickoutFromGroup(op.param1,[op.param2])
                                                                sw.inviteIntoGroup(op.param1,[op.param3])
                                                                ke.acceptGroupInvitation(op.param1)
                                                                sw.cancelGroupInvitation(op.param1,[op.param2])
                                                            except:
                                                                try:
                                                                   so.kickoutFromGroup(op.param1,[op.param2])
                                                                   so.inviteIntoGroup(op.param1,[op.param3])
                                                                   ke.acceptGroupInvitation(op.param1)
                                                                   so.cancelGroupInvitation(op.param1,[op.param2])
                                                                except:
                                                                    pass 

                return

        if op.type == 19:
            if Gmid in op.param3:
                if op.param2 in Abi:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kg.kickoutFromGroup(op.param1,[op.param2])
                        kg.inviteIntoGroup(op.param1,[op.param3])
                        kf.acceptGroupInvitation(op.param1)
                        kg.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            kh.kickoutFromGroup(op.param1,[op.param2])
                            kh.inviteIntoGroup(op.param1,[op.param3])
                            kf.acceptGroupInvitation(op.param1)
                            kh.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                cl.kickoutFromGroup(op.param1,[op.param2])
                                cl.inviteIntoGroup(op.param1,[op.param3])
                                kf.acceptGroupInvitation(op.param1)
                                cl.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    ki.kickoutFromGroup(op.param1,[op.param2])
                                    ki.inviteIntoGroup(op.param1,[op.param3])
                                    kf.acceptGroupInvitation(op.param1)
                                    ki.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        kk.kickoutFromGroup(op.param1,[op.param2])
                                        kk.inviteIntoGroup(op.param1,[op.param3])
                                        kf.acceptGroupInvitation(op.param1)
                                        kk.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = kf.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kf.updateGroup(G)
                                            Ticket = kf.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            so.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            random.choice(OlengBot).kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                kc.kickoutFromGroup(op.param1,[op.param2])
                                                kc.inviteIntoGroup(op.param1,[op.param3])
                                                kf.acceptGroupInvitation(op.param1)
                                                kc.cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                try:
                                                    kb.kickoutFromGroup(op.param1,[op.param2])
                                                    kb.inviteIntoGroup(op.param1,[op.param3])
                                                    kf.acceptGroupInvitation(op.param1)
                                                    kb.cancelGroupInvitation(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        kd.kickoutFromGroup(op.param1,[op.param2])
                                                        kd.inviteIntoGroup(op.param1,[op.param3])
                                                        kf.acceptGroupInvitation(op.param1)
                                                        kd.cancelGroupInvitation(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            ke.kickoutFromGroup(op.param1,[op.param2])
                                                            ke.inviteIntoGroup(op.param1,[op.param3])
                                                            kf.acceptGroupInvitation(op.param1)
                                                            ke.cancelGroupInvitation(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                sw.kickoutFromGroup(op.param1,[op.param2])
                                                                sw.inviteIntoGroup(op.param1,[op.param3])
                                                                kf.acceptGroupInvitation(op.param1)
                                                                sw.cancelGroupInvitation(op.param1,[op.param2])
                                                            except:
                                                                try:
                                                                   so.kickoutFromGroup(op.param1,[op.param2])
                                                                   so.inviteIntoGroup(op.param1,[op.param3])
                                                                   kf.acceptGroupInvitation(op.param1)
                                                                   so.cancelGroupInvitation(op.param1,[op.param2])
                                                                except:
                                                                    pass

                return

        if op.type == 19:
            if Hmid in op.param3:
                if op.param2 in Abi:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        kh.kickoutFromGroup(op.param1,[op.param2])
                        kh.inviteIntoGroup(op.param1,[op.param3])
                        kg.acceptGroupInvitation(op.param1)
                        kh.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            kg.acceptGroupInvitation(op.param1)
                            cl.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                kg.acceptGroupInvitation(op.param1)
                                ki.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                    kg.acceptGroupInvitation(op.param1)
                                    kk.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                        kg.acceptGroupInvitation(op.param1)
                                        kc.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = kg.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kg.updateGroup(G)
                                            Ticket = kg.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            so.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            random.choice(OlengBot).kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                kb.kickoutFromGroup(op.param1,[op.param2])
                                                kb.inviteIntoGroup(op.param1,[op.param3])
                                                kg.acceptGroupInvitation(op.param1)
                                                kb.cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                try:
                                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                                    kg.acceptGroupInvitation(op.param1)
                                                    kd.cancelGroupInvitation(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                                        kg.acceptGroupInvitation(op.param1)
                                                        ke.cancelGroupInvitation(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                                            kf.inviteIntoGroup(op.param1,[op.param3])
                                                            kg.acceptGroupInvitation(op.param1)
                                                            kf.cancelGroupInvitation(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                sw.kickoutFromGroup(op.param1,[op.param2])
                                                                sw.inviteIntoGroup(op.param1,[op.param3])
                                                                kg.acceptGroupInvitation(op.param1)
                                                                sw.cancelGroupInvitation(op.param1,[op.param2])
                                                            except:
                                                                try:
                                                                   so.kickoutFromGroup(op.param1,[op.param2])
                                                                   so.inviteIntoGroup(op.param1,[op.param3])
                                                                   kg.acceptGroupInvitation(op.param1)
                                                                   so.cancelGroupInvitation(op.param1,[op.param2])
                                                                except:
                                                                    pass 

                return

        if op.type == 19:
            if Imid in op.param3:
                if op.param2 in Abi:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.inviteIntoGroup(op.param1,[op.param3])
                        kh.acceptGroupInvitation(op.param1)
                        cl.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.inviteIntoGroup(op.param1,[op.param3])
                            kh.acceptGroupInvitation(op.param1)
                            ki.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.inviteIntoGroup(op.param1,[op.param3])
                                kh.acceptGroupInvitation(op.param1)
                                kk.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.inviteIntoGroup(op.param1,[op.param3])
                                    kh.acceptGroupInvitation(op.param1)
                                    kc.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.inviteIntoGroup(op.param1,[op.param3])
                                        kh.acceptGroupInvitation(op.param1)
                                        kb.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = kh.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            kh.updateGroup(G)
                                            Ticket = kh.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            so.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            random.choice(OlengBot).kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                kd.kickoutFromGroup(op.param1,[op.param2])
                                                kd.inviteIntoGroup(op.param1,[op.param3])
                                                kh.acceptGroupInvitation(op.param1)
                                                kd.cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                try:
                                                    ke.kickoutFromGroup(op.param1,[op.param2])
                                                    ke.inviteIntoGroup(op.param1,[op.param3])
                                                    kh.acceptGroupInvitation(op.param1)
                                                    ke.cancelGroupInvitation(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        kf.kickoutFromGroup(op.param1,[op.param2])
                                                        kf.inviteIntoGroup(op.param1,[op.param3])
                                                        kh.acceptGroupInvitation(op.param1)
                                                        kf.cancelGroupInvitation(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            kg.kickoutFromGroup(op.param1,[op.param2])
                                                            kg.inviteIntoGroup(op.param1,[op.param3])
                                                            kh.acceptGroupInvitation(op.param1)
                                                            kg.cancelGroupInvitation(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                sw.kickoutFromGroup(op.param1,[op.param2])
                                                                sw.inviteIntoGroup(op.param1,[op.param3])
                                                                kh.acceptGroupInvitation(op.param1)
                                                                sw.cancelGroupInvitation(op.param1,[op.param2])
                                                            except:
                                                                try:
                                                                   so.kickoutFromGroup(op.param1,[op.param2])
                                                                   so.inviteIntoGroup(op.param1,[op.param3])
                                                                   kh.acceptGroupInvitation(op.param1)
                                                                   so.cancelGroupInvitation(op.param1,[op.param2])
                                                                except:
                                                                    pass

                return

        if op.type == 19:
            if Jmid in op.param3:
                if op.param2 in Abi:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        sw.kickoutFromGroup(op.param1,[op.param2])
                        sw.inviteIntoGroup(op.param1,[op.param3])
                        so.acceptGroupInvitation(op.param1)
                        sw.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            so.acceptGroupInvitation(op.param1)
                            cl.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                so.acceptGroupInvitation(op.param1)
                                ki.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                    so.acceptGroupInvitation(op.param1)
                                    kk.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                        so.acceptGroupInvitation(op.param1)
                                        kc.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = so.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            so.updateGroup(G)
                                            Ticket = so.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            so.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            random.choice(OlengBot).kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                kb.kickoutFromGroup(op.param1,[op.param2])
                                                kb.inviteIntoGroup(op.param1,[op.param3])
                                                so.acceptGroupInvitation(op.param1)
                                                kb.cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                try:
                                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                                    so.acceptGroupInvitation(op.param1)
                                                    ke.cancelGroupInvitation(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                                        so.acceptGroupInvitation(op.param1)
                                                        ke.cancelGroupInvitation(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                                            kf.inviteIntoGroup(op.param1,[op.param3])
                                                            so.acceptGroupInvitation(op.param1)
                                                            kf.cancelGroupInvitation(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                kg.kickoutFromGroup(op.param1,[op.param2])
                                                                kg.inviteIntoGroup(op.param1,[op.param3])
                                                                so.acceptGroupInvitation(op.param1)
                                                                kg.cancelGroupInvitation(op.param1,[op.param2])
                                                            except:
                                                                try:
                                                                   kh.kickoutFromGroup(op.param1,[op.param2])
                                                                   kh.inviteIntoGroup(op.param1,[op.param3])
                                                                   so.acceptGroupInvitation(op.param1)
                                                                   kh.cancelGroupInvitation(op.param1,[op.param2])
                                                                except:
                                                                    pass

                return

        if op.type == 19:
            if Zmid in op.param3:
                if op.param2 in Abi:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        so.kickoutFromGroup(op.param1,[op.param2])
                        so.inviteIntoGroup(op.param1,[op.param3])
                        sw.acceptGroupInvitation(op.param1)
                        so.cancelGroupInvitation(op.param1,[op.param2])
                    except:
                        try:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                            cl.inviteIntoGroup(op.param1,[op.param3])
                            sw.acceptGroupInvitation(op.param1)
                            cl.cancelGroupInvitation(op.param1,[op.param2])
                        except:
                            try:
                                ki.kickoutFromGroup(op.param1,[op.param2])
                                ki.inviteIntoGroup(op.param1,[op.param3])
                                sw.acceptGroupInvitation(op.param1)
                                ki.cancelGroupInvitation(op.param1,[op.param2])
                            except:
                                try:
                                    kk.kickoutFromGroup(op.param1,[op.param2])
                                    kk.inviteIntoGroup(op.param1,[op.param3])
                                    sw.acceptGroupInvitation(op.param1)
                                    kk.cancelGroupInvitation(op.param1,[op.param2])
                                except:
                                    try:
                                        kc.kickoutFromGroup(op.param1,[op.param2])
                                        kc.inviteIntoGroup(op.param1,[op.param3])
                                        sw.acceptGroupInvitation(op.param1)
                                        kc.cancelGroupInvitation(op.param1,[op.param2])
                                    except:
                                        try:
                                            G = sw.getGroup(op.param1)
                                            G.preventedJoinByTicket = False
                                            sw.updateGroup(G)
                                            Ticket = sw.reissueGroupTicket(op.param1)
                                            cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ki.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kk.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kc.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kb.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kd.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            ke.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kf.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kg.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            kh.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            so.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            sw.acceptGroupInvitationByTicket(op.param1,Ticket)
                                            random.choice(OlengBot).kickoutFromGroup(op.param1,[op.param2])
                                        except:
                                            try:
                                                kb.kickoutFromGroup(op.param1,[op.param2])
                                                kb.inviteIntoGroup(op.param1,[op.param3])
                                                sw.acceptGroupInvitation(op.param1)
                                                kb.cancelGroupInvitation(op.param1,[op.param2])
                                            except:
                                                try:
                                                    kd.kickoutFromGroup(op.param1,[op.param2])
                                                    kd.inviteIntoGroup(op.param1,[op.param3])
                                                    sw.acceptGroupInvitation(op.param1)
                                                    ke.cancelGroupInvitation(op.param1,[op.param2])
                                                except:
                                                    try:
                                                        ke.kickoutFromGroup(op.param1,[op.param2])
                                                        ke.inviteIntoGroup(op.param1,[op.param3])
                                                        sw.acceptGroupInvitation(op.param1)
                                                        ke.cancelGroupInvitation(op.param1,[op.param2])
                                                    except:
                                                        try:
                                                            kf.kickoutFromGroup(op.param1,[op.param2])
                                                            kf.inviteIntoGroup(op.param1,[op.param3])
                                                            sw.acceptGroupInvitation(op.param1)
                                                            kf.cancelGroupInvitation(op.param1,[op.param2])
                                                        except:
                                                            try:
                                                                kg.kickoutFromGroup(op.param1,[op.param2])
                                                                kg.inviteIntoGroup(op.param1,[op.param3])
                                                                sw.acceptGroupInvitation(op.param1)
                                                                kg.cancelGroupInvitation(op.param1,[op.param2])
                                                            except:
                                                                try:
                                                                   kh.kickoutFromGroup(op.param1,[op.param2])
                                                                   kh.inviteIntoGroup(op.param1,[op.param3])
                                                                   sw.acceptGroupInvitation(op.param1)
                                                                   kh.cancelGroupInvitation(op.param1,[op.param2])
                                                                except:
                                                                    pass   
                                            
                return

            if admin in op.param3:
                if op.param2 in Abi:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.cancelGroupInvitation(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.cancelGroupInvitation(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.cancelGroupInvitation(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.cancelGroupInvitation(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.cancelGroupInvitation(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.cancelGroupInvitation(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                            try:
                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                                ke.cancelGroupInvitation(op.param1,[op.param2])
                                                ke.findAndAddContactsByMid(op.param1,admin)
                                                ke.inviteIntoGroup(op.param1,admin)
                                            except:
                                                try:
                                                    kf.kickoutFromGroup(op.param1,[op.param2])
                                                    kf.cancelGroupInvitation(op.param1,[op.param2])
                                                    kf.findAndAddContactsByMid(op.param1,admin)
                                                    kf.inviteIntoGroup(op.param1,admin)
                                                except:
                                                    try:
                                                        kg.kickoutFromGroup(op.param1,[op.param2])
                                                        kg.cancelGroupInvitation(op.param1,[op.param2])
                                                        kg.findAndAddContactsByMid(op.param1,admin)
                                                        kg.inviteIntoGroup(op.param1,admin)  
                                                    except:
                                                        try:
                                                            kh.kickoutFromGroup(op.param1,[op.param2])
                                                            kh.cancelGroupInvitation(op.param1,[op.param2])
                                                            kh.findAndAddContactsByMid(op.param1,admin)
                                                            kh.inviteIntoGroup(op.param1,admin)  
                                                        except:
                                                            try:
                                                                so.kickoutFromGroup(op.param1,[op.param2])
                                                                so.cancelGroupInvitation(op.param1,[op.param2])
                                                                so.findAndAddContactsByMid(op.param1,admin)
                                                                so.inviteIntoGroup(op.param1,admin)  
                                                            except:
                                                                try:
                                                                    sw.kickoutFromGroup(op.param1,[op.param2])
                                                                    sw.cancelGroupInvitation(op.param1,[op.param2])
                                                                    sw.findAndAddContactsByMid(op.param1,admin)
                                                                    sw.inviteIntoGroup(op.param1,admin)  
                                                                except:
                                                                    pass

                return

            if staff in op.param3:
                if op.param2 in Abi:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.cancelGroupInvitation(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,staff)
                        cl.inviteIntoGroup(op.param1,staff)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.cancelGroupInvitation(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,staff)
                            ki.inviteIntoGroup(op.param1,staff)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.cancelGroupInvitation(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,staff)
                                kk.inviteIntoGroup(op.param1,staff)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.cancelGroupInvitation(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,staff)
                                    kc.inviteIntoGroup(op.param1,staff)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.cancelGroupInvitation(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,staff)
                                        kb.inviteIntoGroup(op.param1,staff)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.cancelGroupInvitation(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,staff)
                                            kd.nviteIntoGroup(op.param1,staff)
                                        except:
                                            try:
                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                                ke.cancelGroupInvitation(op.param1,[op.param2])
                                                ke.findAndAddContactsByMid(op.param1,staff)
                                                ke.inviteIntoGroup(op.param1,staff)
                                            except:
                                                try:
                                                    kf.kickoutFromGroup(op.param1,[op.param2])
                                                    kf.cancelGroupInvitation(op.param1,[op.param2])
                                                    kf.findAndAddContactsByMid(op.param1,staff)
                                                    kf.inviteIntoGroup(op.param1,staff)
                                                except:
                                                    try:
                                                        kg.kickoutFromGroup(op.param1,[op.param2])
                                                        kg.cancelGroupInvitation(op.param1,[op.param2])
                                                        kg.findAndAddContactsByMid(op.param1,staff)
                                                        kg.inviteIntoGroup(op.param1,staff)  
                                                    except:
                                                        try:
                                                            kh.kickoutFromGroup(op.param1,[op.param2])
                                                            kh.cancelGroupInvitation(op.param1,[op.param2])
                                                            kh.findAndAddContactsByMid(op.param1,staff)
                                                            kh.inviteIntoGroup(op.param1,staff)  
                                                        except:
                                                            try:
                                                                so.kickoutFromGroup(op.param1,[op.param2])
                                                                so.cancelGroupInvitation(op.param1,[op.param2])
                                                                so.findAndAddContactsByMid(op.param1,staff)
                                                                so.inviteIntoGroup(op.param1,staff)  
                                                            except:
                                                                try:
                                                                    sw.kickoutFromGroup(op.param1,[op.param2])
                                                                    sw.cancelGroupInvitation(op.param1,[op.param2])
                                                                    sw.findAndAddContactsByMid(op.param1,staff)
                                                                    sw.inviteIntoGroup(op.param1,staff)  
                                                                except:
                                                                    pass    
                                            
                return

            if staff in op.param3:
                if op.param2 in Abi:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.cancelGroupInvitation(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,staff)
                        cl.inviteIntoGroup(op.param1,staff)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.cancelGroupInvitation(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,staff)
                            ki.inviteIntoGroup(op.param1,staff)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.cancelGroupInvitation(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,staff)
                                kk.inviteIntoGroup(op.param1,staff)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.cancelGroupInvitation(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,staff)
                                    kc.inviteIntoGroup(op.param1,staff)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.cancelGroupInvitation(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,staff)
                                        kb.inviteIntoGroup(op.param1,staff)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.cancelGroupInvitation(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,staff)
                                            kd.nviteIntoGroup(op.param1,staff)
                                        except:
                                            try:
                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                                ke.cancelGroupInvitation(op.param1,[op.param2])
                                                ke.findAndAddContactsByMid(op.param1,staff)
                                                ke.inviteIntoGroup(op.param1,staff)
                                            except:
                                                try:
                                                    kf.kickoutFromGroup(op.param1,[op.param2])
                                                    kf.cancelGroupInvitation(op.param1,[op.param2])
                                                    kf.findAndAddContactsByMid(op.param1,staff)
                                                    kf.inviteIntoGroup(op.param1,staff)
                                                except:
                                                    try:
                                                        kg.kickoutFromGroup(op.param1,[op.param2])
                                                        kg.cancelGroupInvitation(op.param1,[op.param2])
                                                        kg.findAndAddContactsByMid(op.param1,staff)
                                                        kg.inviteIntoGroup(op.param1,staff)  
                                                    except:
                                                        try:
                                                            kh.kickoutFromGroup(op.param1,[op.param2])
                                                            kh.cancelGroupInvitation(op.param1,[op.param2])
                                                            kh.findAndAddContactsByMid(op.param1,staff)
                                                            kh.inviteIntoGroup(op.param1,staff)  
                                                        except:
                                                            try:
                                                                so.kickoutFromGroup(op.param1,[op.param2])
                                                                so.cancelGroupInvitation(op.param1,[op.param2])
                                                                so.findAndAddContactsByMid(op.param1,staff)
                                                                so.inviteIntoGroup(op.param1,staff)  
                                                            except:
                                                                try:
                                                                    sw.kickoutFromGroup(op.param1,[op.param2])
                                                                    sw.cancelGroupInvitation(op.param1,[op.param2])
                                                                    sw.findAndAddContactsByMid(op.param1,staff)
                                                                    sw.inviteIntoGroup(op.param1,staff)  
                                                                except:
                                                                     pass   
                                            
                return

            if member in op.param3:
                if op.param2 in Abi:
                    pass
                if op.param2 in member:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.cancelGroupInvitation(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,member)
                        cl.inviteIntoGroup(op.param1,member)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.cancelGroupInvitation(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,member)
                            ki.inviteIntoGroup(op.param1,member)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.cancelGroupInvitation(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,member)
                                kk.inviteIntoGroup(op.param1,member)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.cancelGroupInvitation(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,member)
                                    kc.inviteIntoGroup(op.param1,member)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.cancelGroupInvitation(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,member)
                                        kb.inviteIntoGroup(op.param1,member)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.cancelGroupInvitation(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,member)
                                            kd.nviteIntoGroup(op.param1,member)
                                        except:
                                            try:
                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                                ke.cancelGroupInvitation(op.param1,[op.param2])
                                                ke.findAndAddContactsByMid(op.param1,member)
                                                ke.inviteIntoGroup(op.param1,member)
                                            except:
                                                try:
                                                    kf.kickoutFromGroup(op.param1,[op.param2])
                                                    kf.cancelGroupInvitation(op.param1,[op.param2])
                                                    kf.findAndAddContactsByMid(op.param1,member)
                                                    kf.inviteIntoGroup(op.param1,member)
                                                except:
                                                    try:
                                                        kg.kickoutFromGroup(op.param1,[op.param2])
                                                        kg.cancelGroupInvitation(op.param1,[op.param2])
                                                        kg.findAndAddContactsByMid(op.param1,member)
                                                        kg.inviteIntoGroup(op.param1,member)  
                                                    except:
                                                        try:
                                                            kh.kickoutFromGroup(op.param1,[op.param2])
                                                            kh.cancelGroupInvitation(op.param1,[op.param2])
                                                            kh.findAndAddContactsByMid(op.param1,member)
                                                            kh.inviteIntoGroup(op.param1,member)  
                                                        except:
                                                            pass         
                                            
                return

            if admin in op.param3:
                if op.param2 in Abi:
                    pass
                if op.param2 in owner:
                    pass
                if op.param2 in admin:
                    pass
                if op.param2 in staff:
                    pass
                else:
                    wait["blacklist"][op.param2] = True
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
                        cl.cancelGroupInvitation(op.param1,[op.param2])
                        cl.findAndAddContactsByMid(op.param1,admin)
                        cl.inviteIntoGroup(op.param1,admin)
                    except:
                        try:
                            ki.kickoutFromGroup(op.param1,[op.param2])
                            ki.cancelGroupInvitation(op.param1,[op.param2])
                            ki.findAndAddContactsByMid(op.param1,admin)
                            ki.inviteIntoGroup(op.param1,admin)
                        except:
                            try:
                                kk.kickoutFromGroup(op.param1,[op.param2])
                                kk.cancelGroupInvitation(op.param1,[op.param2])
                                kk.findAndAddContactsByMid(op.param1,admin)
                                kk.inviteIntoGroup(op.param1,admin)
                            except:
                                try:
                                    kc.kickoutFromGroup(op.param1,[op.param2])
                                    kc.cancelGroupInvitation(op.param1,[op.param2])
                                    kc.findAndAddContactsByMid(op.param1,admin)
                                    kc.inviteIntoGroup(op.param1,admin)
                                except:
                                    try:
                                        kb.kickoutFromGroup(op.param1,[op.param2])
                                        kb.cancelGroupInvitation(op.param1,[op.param2])
                                        kb.findAndAddContactsByMid(op.param1,admin)
                                        kb.inviteIntoGroup(op.param1,admin)
                                    except:
                                        try:
                                            kd.kickoutFromGroup(op.param1,[op.param2])
                                            kd.cancelGroupInvitation(op.param1,[op.param2])
                                            kd.findAndAddContactsByMid(op.param1,admin)
                                            kd.nviteIntoGroup(op.param1,admin)
                                        except:
                                            try:
                                                ke.kickoutFromGroup(op.param1,[op.param2])
                                                ke.cancelGroupInvitation(op.param1,[op.param2])
                                                ke.findAndAddContactsByMid(op.param1,admin)
                                                ke.inviteIntoGroup(op.param1,admin)
                                            except:
                                                try:
                                                    kf.kickoutFromGroup(op.param1,[op.param2])
                                                    kf.cancelGroupInvitation(op.param1,[op.param2])
                                                    kf.findAndAddContactsByMid(op.param1,admin)
                                                    kf.inviteIntoGroup(op.param1,admin)
                                                except:
                                                    try:
                                                        kg.kickoutFromGroup(op.param1,[op.param2])
                                                        kg.cancelGroupInvitation(op.param1,[op.param2])
                                                        kg.findAndAddContactsByMid(op.param1,admin)
                                                        kg.inviteIntoGroup(op.param1,admin)  
                                                    except:
                                                        try:
                                                            kh.kickoutFromGroup(op.param1,[op.param2])
                                                            kh.cancelGroupInvitation(op.param1,[op.param2])
                                                            kh.findAndAddContactsByMid(op.param1,admin)
                                                            kh.inviteIntoGroup(op.param1,admin)  
                                                        except:
                                                            pass
                                        
                return

        if op.type == 55:
            try:
                if op.param1 in Setmain["RAreadPoint"]:
                   if op.param2 in Setmain["RAreadMember"][op.param1]:
                       pass
                   else:
                       Setmain["RAreadMember"][op.param1][op.param2] = True
                else:
                   pass
            except:
                pass
                
        if op.type == 15:
            if op.param1 in welcome:
                if op.param2 in Abi:
                    pass
                ginfo = cl.getGroup(op.param1)
                leaveMembers(op.param1, [op.param2])            

        if op.type == 55:
            if op.param2 in wait["blacklist"]:
                random.choice(OlengBot).kickoutFromGroup(op.param1,[op.param2])
            else:
                pass

            if cctv['cyduk'][op.param1]==True:
                if op.param1 in cctv['point']:
                    Name = cl.getContact(op.param2).displayName
                    if Name in cctv['sidermem'][op.param1]:
                        pass
                    else:
                        cctv['sidermem'][op.param1] += "\n~ " + Name
                        siderMembers(op.param1, [op.param2])
                        
        if op.type == 0:
            return
        if op.type == 5:
              if wait["autoAdd"] == True:
                  cl.findAndAddContactsByMid(op.param1)
                  ki.findAndAddContactsByMid(op.param1)
                  kk.findAndAddContactsByMid(op.param1)
                  kc.findAndAddContactsByMid(op.param1)
                  kd.findAndAddContactsByMid(op.param1)
                  kb.findAndAddContactsByMid(op.param1)
                  ke.findAndAddContactsByMid(op.param1)
                  kf.findAndAddContactsByMid(op.param1)
                  kg.findAndAddContactsByMid(op.param1)
                  kh.findAndAddContactsByMid(op.param1)
                  so.findAndAddContactsByMid(op.param1)
                  sw.findAndAddContactsByMid(op.param1)
                  sendMention(op.param1, op.param1, "Haii ", ", terimakasih sudah add saya")
                  cl.sendText(op.param1, wait["message"])               
                        
        if op.type == 5:
            print ("[ 5 ] NOTIFIED AUTO BLOCK CONTACT")
            if wait["autoBlock"] == True:
                cl.blockContact(op.param1)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                           if msg_dict[msg_id]["text"] == 'Gambarnya dibawah':
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                zx = ""
                                zxc = ""
                                zx2 = []
                                xpesan =  "| gambar dihapus  |\n sender : "
                                ret_ = " grup: {}".format(str(ginfo.name))
                                ret_ += "\nwaktu sent : {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\nnub"
                                ret_ += "\nnub" 
                                ry = str(ryan.displayName)
                                pesan = ''
                                pesan2 = pesan+"@x \n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':ryan.mid}
                                zx2.append(zx)
                                zxc += pesan2
                                text = xpesan + zxc + ret_ + ""
                                cl.sendMessage(at, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                cl.sendImage(at, msg_dict[msg_id]["data"])
                           else:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict[msg_id]["from"])
                                ret_ =  "pesan dihapus\n"
                                ret_ += "sender: {}".format(str(ryan.displayName))
                                ret_ += "\ngrup: {}".format(str(ginfo.name))
                                ret_ += "\nwaktu sent: {}".format(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"])))
                                ret_ += "\nisi pesan: {}".format(str(msg_dict[msg_id]["text"]))
                                ret_ += "\nnub"
                                ret_ += "\nnub" 
                                cl.sendMessage(at, str(ret_))
                        del msg_dict[msg_id]
                except Exception as e:
                    print(e)

        if op.type == 65:
            if wait["unsend"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict1:
                        if msg_dict1[msg_id]["from"]:
                                ginfo = cl.getGroup(at)
                                ryan = cl.getContact(msg_dict1[msg_id]["from"])
                                ret_ =  "sticker dihapus\n"
                                ret_ += "sender : {}".format(str(ryan.displayName))
                                ret_ += "\ngrup: {}".format(str(ginfo.name))
                                ret_ += "\nwaktu sent: {}".format(dt_to_str(cTime_to_datetime(msg_dict1[msg_id]["createdTime"])))
                                ret_ += "\nnub"
                                ret_ += "\nnub" 
                                ret_ += "{}".format(str(msg_dict1[msg_id]["text"]))
                                cl.sendMessage(at, str(ret_))
                                cl.sendImage(at, msg_dict1[msg_id]["data"])
                        del msg_dict1[msg_id]
                except Exception as e:
                    print(e)          

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 2:
               if msg.toType == 0:
                    to = msg._from
               elif msg.toType == 2:
                    to = msg.to
               if msg.contentType == 16:
                    if wait["Timeline"] == True:
                            ret_ = "「 ᴅᴇᴛᴀɪʟ ᴘᴏsᴛɪɴɢᴀɴ 」"
                            if msg.contentMetadata["serviceType"] == "GB":
                                contact = cl.getContact(sender)
                                auth = "\nsender: {}".format(str(contact.displayName))
                            else:
                                auth = "\nsender: {}".format(str(msg.contentMetadata["serviceName"]))
                            ret_ += auth
                            if "stickerId" in msg.contentMetadata:
                                stck = "\nsᴛɪᴄᴋᴇʀ : https://line.me/R/shop/detail/{}".format(str(msg.contentMetadata["packageId"]))
                                ret_ += stck
                            if "mediaOid" in msg.contentMetadata:
                                object_ = msg.contentMetadata["mediaOid"].replace("svc=myhome|sid=h|","")
                                if msg.contentMetadata["mediaType"] == "V":
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\nObjek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                        murl = "\nMedia URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\nObjek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                        murl = "\nMedia URL : https://obs-us.line-apps.com/myhome/h/download.nhn?{}".format(str(object_))
                                    ret_ += murl
                                else:
                                    if msg.contentMetadata["serviceType"] == "GB":
                                        ourl = "\nObjek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(msg.contentMetadata["mediaOid"]))
                                    else:
                                        ourl = "\nObjek URL : https://obs-us.line-apps.com/myhome/h/download.nhn?tid=612w&{}".format(str(object_))
                                ret_ += ourl
                            if "text" in msg.contentMetadata:
                                text = "\ntulisan: {}".format(str(msg.contentMetadata["text"]))
                                purl = "\nPost URL : {}".format(str(msg.contentMetadata["postEndUrl"]).replace("line://","https://line.me/R/"))
                                ret_ += purl
                                ret_ += text
                            cl.sendMessage(to, str(ret_))
                            cl.like(url[25:58], url[66:], likeType=1005)
                            cl.comment(url[25:58], url[66:], wait["message"])
                            cl.sendMessage(msg.to,"Like sukses cok")
               if msg.contentType == 0:
                    msg_dict[msg.id] = {"text":msg.text,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 1:
                    path = cl.downloadObjectMsg(msg_id)
                    msg_dict[msg.id] = {"text":'Gambar ada dibawah cok',"data":path,"from":msg._from,"createdTime":msg.createdTime}
               if msg.contentType == 7:
                   stk_id = msg.contentMetadata["STKID"]
                   stk_ver = msg.contentMetadata["STKVER"]
                   pkg_id = msg.contentMetadata["STKPKGID"]
                   ret_ = "\n\n「 tikel info 」"
                   ret_ += "\ntikel id: {}".format(stk_id)
                   ret_ += "\ntikel versi: {}".format(stk_ver)
                   ret_ += "\ntikel package: {}".format(pkg_id)
                   ret_ += "\ntikel url: line://shop/detail/{}".format(pkg_id)
                   query = int(stk_id)
                   if type(query) == int:
                            data = 'https://stickershop.line-scdn.net/stickershop/v1/sticker/'+str(query)+'/ANDROID/sticker.png'
                            path = cl.downloadFileURL(data)
                            msg_dict1[msg.id] = {"text":str(ret_),"data":path,"from":msg._from,"createdTime":msg.createdTime}       

        if op.type == 26:
           if wait["selfbot"] == True:
               msg = op.message
               if msg._from not in Abi:
                 if wait["talkban"] == True:
                   if msg._from in wait["Talkblacklist"]:
                      try:
                          random.choice(OlengBot).kickoutFromGroup(msg.to, [msg._from])
                      except:
                          try:
                              random.choice(OlengBot).kickoutFromGroup(msg.to, [msg._from])
                          except:
                              random.choice(OlengBot).kickoutFromGroup(msg.to, [msg._from])
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                   contact = cl.getContact(msg._from)
                   image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Abi:
                           cl.sendMessage(msg.to, wait["Respontag"])
                           cl.sendImageWithURL(msg.to,image)
                           #rnd = ["dilarang ngetag bang abi"]
                           #p = random.choice(rnd)
                           #lang = 'id'
                           #tts = gTTS(text=p, lang=lang)
                           #tts.save("hasil.mp3")
                           #cl.sendAudio(msg.to,"hasil.mp3")
                           cl.sendMessage(msg.to, None, contentMetadata={"STKID":"73760366","STKPKGID":"12228","STKVER":"2"}, contentType=7)
                           break
               if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["Mentionkick"] == True:
                   name = re.findall(r'@(\w+)', msg.text)
                   mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                   mentionees = mention['MENTIONEES']
                   for mention in mentionees:
                        if mention ['M'] in Abi:
                           cl.mentiontag(msg.to,[msg._from])
                           cl.sendMessage(msg.to, "Crooottttt....")
                           cl.kickoutFromGroup(msg.to, [msg._from])
                           break
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"「Cek ID Sticker」\nSTKID : " + msg.contentMetadata["STKID"] + "\n STKPKGID : " + msg.contentMetadata["STKPKGID"] + "\n STKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"✒ Nama : " + msg.contentMetadata["displayName"] + "\n MID : " + msg.contentMetadata["mid"] + "\n Status Msg : " + contact.statusMessage + "\n Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)

        if op.type == 25 or op.type == 26:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            if msg.toType == 0 or msg.toType == 2:
               if msg.toType == 0:
                    to = receiver
               elif msg.toType == 2:
                    to = receiver
               if msg.contentType == 7:
                 if wait["sticker"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,"STKID : " + msg.contentMetadata["STKID"] + "\nSTKPKGID : " + msg.contentMetadata["STKPKGID"] + "\nSTKVER : " + msg.contentMetadata["STKVER"]+ "\n\n「Link Sticker」" + "\nline://shop/detail/" + msg.contentMetadata["STKPKGID"])
               if msg.contentType == 13:
                 if wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        path = cl.getContact(msg.contentMetadata["mid"]).picturePath
                        image = 'http://dl.profile.line.naver.jp'+path
                        cl.sendMessage(msg.to,"✒ Nama : " + msg.contentMetadata["displayName"] + "\n MID : " + msg.contentMetadata["mid"] + "\n Status Msg : " + contact.statusMessage + "\n Picture URL : http://dl.profile.line-cdn.net/" + contact.pictureStatus)
                        cl.sendImageWithURL(msg.to, image)
#ADD Bots
               if msg.contentType == 13:
                 if msg._from in admin:
                  if wait["addbots"] == True:
                    if msg.contentMetadata["mid"] in Abi:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi anggota bot")
                        wait["addbots"] = True
                    else:
                        Abi.append(msg.contentMetadata["mid"])
                        wait["addbots"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke anggota bot")
                 if wait["dellbots"] == True:
                    if msg.contentMetadata["mid"] in Abi:
                        Abi.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari anggota bot")
                    else:
                        wait["dellbots"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan anggota bot")
#ADD STAFF
                 if msg._from in admin:
                  if wait["addstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi staff")
                        wait["addstaff"] = True
                    else:
                        staff.append(msg.contentMetadata["mid"])
                        wait["addstaff"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke staff")
                 if wait["dellstaff"] == True:
                    if msg.contentMetadata["mid"] in staff:
                        staff.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari staff")
                        wait["dellstaff"] = True
                    else:
                        wait["dellstaff"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan staff")
#ADD ADMIN
                 if msg._from in admin:
                  if wait["addadmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        cl.sendMessage(msg.to,"Contact itu sudah jadi admin")
                        wait["addadmin"] = True
                    else:
                        admin.append(msg.contentMetadata["mid"])
                        wait["addadmin"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke admin")
                 if wait["delladmin"] == True:
                    if msg.contentMetadata["mid"] in admin:
                        admin.remove(msg.contentMetadata["mid"])
                        cl.sendMessage(msg.to,"Berhasil menghapus dari admin")
                    else:
                        wait["delladmin"] = True
                        cl.sendMessage(msg.to,"Contact itu bukan admin")
#ADD BLACKLIST
                 if msg._from in admin:
                  if wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendMessage(msg.to,"Contact itu sudah ada di blacklist")
                        wait["wblacklist"] = True
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke blacklist user")
                  if wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Berhasil menghapus dari blacklist user")
                    else:
                        wait["dblacklist"] = True
                        cl.sendMessage(msg.to,"Contact itu tidak ada di blacklist")
#TALKBAN
                 if msg._from in admin:
                  if wait["Talkwblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        cl.sendMessage(msg.to,"Contact itu sudah ada di Talkban")
                        wait["Talkwblacklist"] = True
                    else:
                        wait["Talkblacklist"][msg.contentMetadata["mid"]] = True
                        wait["Talkwblacklist"] = True
                        cl.sendMessage(msg.to,"Berhasil menambahkan ke Talkban user")
                  if wait["Talkdblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["Talkblacklist"]:
                        del wait["Talkblacklist"][msg.contentMetadata["mid"]]
                        cl.sendMessage(msg.to,"Berhasil menghapus dari Talkban user")
                    else:
                        wait["Talkdblacklist"] = True
                        cl.sendMessage(msg.to,"Contact itu tidak ada di Talkban")
#UPDATE FOTO
               if msg.contentType == 1:
                 if msg._from in admin:
                    if wait["Addimage"]["status"] == True:
                        path = cl.downloadObjectMsg(msg.id)
                        images[wait["Addimage"]["name"]] = str(path)
                        f = codecs.open("image.json","w","utf-8")
                        json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(msg.to, "Berhasil menambahkan gambar {}".format(str(wait["Addimage"]["name"])))
                        wait["Addimage"]["status"] = False                
                        wait["Addimage"]["name"] = ""
               if msg.contentType == 2:
                 if msg._from in admin:
                    if wait["Addvideo"]["status"] == True:
                        path = cl.downloadObjectMsg(msg.id)
                        videos[wait["Addvideo"]["name"]] = str(path)
                        f = codecs.open("video.json","w","utf-8")
                        json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(msg.to, "Berhasil menambahkan video {}".format(str(wait["Addvideo"]["name"])))
                        wait["Addvideo"]["status"] = False                
                        wait["Addvideo"]["name"] = ""
               if msg.contentType == 7:
                 if msg._from in admin:
                    if wait["Addsticker"]["status"] == True:
                        stickers[wait["Addsticker"]["name"]] = {"STKID":msg.contentMetadata["STKID"],"STKPKGID":msg.contentMetadata["STKPKGID"]}
                        f = codecs.open("sticker.json","w","utf-8")
                        json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(msg.to, "Berhasil menambahkan sticker {}".format(str(wait["Addsticker"]["name"])))
                        wait["Addsticker"]["status"] = False                
                        wait["Addsticker"]["name"] = ""
               if msg.contentType == 3:
                 if msg._from in admin:
                    if wait["Addaudio"]["status"] == True:
                        path = cl.downloadObjectMsg(msg.id)
                        audios[wait["Addaudio"]["name"]] = str(path)
                        f = codecs.open("audio.json","w","utf-8")
                        json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                        cl.sendMessage(msg.to, "Berhasil menambahkan mp3 {}".format(str(wait["Addaudio"]["name"])))
                        wait["Addaudio"]["status"] = False                
                        wait["Addaudio"]["name"] = ""
               if msg.toType == 2:
                 if msg._from in admin:
                   if settings["groupPicture"] == True:
                     path = cl.downloadObjectMsg(msg_id)
                     settings["groupPicture"] = False
                     cl.updateGroupPicture(msg.to, path)
                     cl.sendMessage(msg.to, "Berhasil mengubah foto group")

               if msg.contentType == 1:
                   if msg._from in admin:
                       if mid in Setmain["ARfoto"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][mid]
                            cl.updateProfilePicture(path)
                            cl.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                        if Amid in Setmain["ARfoto"]:
                            path = ki.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Amid]
                            ki.updateProfilePicture(path)
                            ki.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Bmid in Setmain["ARfoto"]:
                            path = kk.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Bmid]
                            kk.updateProfilePicture(path)
                            kk.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Cmid in Setmain["ARfoto"]:
                            path = kc.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Cmid]
                            kc.updateProfilePicture(path)
                            kc.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Dmid in Setmain["ARfoto"]:
                            path = kb.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Dmid]
                            kb.updateProfilePicture(path)
                            kb.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Emid in Setmain["ARfoto"]:
                            path = kd.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Emid]
                            kd.updateProfilePicture(path)
                            kd.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Fmid in Setmain["ARfoto"]:
                            path = ke.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Fmid]
                            ke.updateProfilePicture(path)
                            ke.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Gmid in Setmain["ARfoto"]:
                            path = kf.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Gmid]
                            kf.updateProfilePicture(path)
                            kf.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Hmid in Setmain["ARfoto"]:
                            path = kg.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Hmid]
                            kg.updateProfilePicture(path)
                            kg.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Imid in Setmain["ARfoto"]:
                            path = kh.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Imid]
                            kh.updateProfilePicture(path)
                            kh.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Jmid in Setmain["ARfoto"]:
                            path = so.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Jmid]
                            so.updateProfilePicture(path)
                            so.sendMessage(msg.to,"Foto berhasil dirubah")
                        elif Zmid in Setmain["ARfoto"]:
                            path = sw.downloadObjectMsg(msg_id)
                            del Setmain["ARfoto"][Zmid]
                            sw.updateProfilePicture(path)
                            sw.sendMessage(msg.to,"Foto berhasil dirubah")

               if msg.contentType == 1:
                 if msg._from in admin:
                   if settings["changePicture"] == True:
                     path1 = ki.downloadObjectMsg(msg_id)
                     path2 = kk.downloadObjectMsg(msg_id)
                     path3 = kc.downloadObjectMsg(msg_id)
                     path4 = kb.downloadObjectMsg(msg_id)
                     path5 = kd.downloadObjectMsg(msg_id)
                     path6 = ke.downloadObjectMsg(msg_id)
                     path7 = kf.downloadObjectMsg(msg_id)
                     path8 = kg.downloadObjectMsg(msg_id)
                     path9 = kh.downloadObjectMsg(msg_id)
                     path10 = so.downloadObjectMsg(msg_id)
                     path11 = sw.downloadObjectMsg(msg_id)
                     tings["changePicture"] = False
                     ki.updateProfilePicture(path1)
                     ki.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kk.updateProfilePicture(path2)
                     kk.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kc.updateProfilePicture(path3)
                     kc.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kb.updateProfilePicture(path4)
                     kb.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kd.updateProfilePicture(path5)
                     kd.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     ke.updateProfilePicture(path6)
                     ke.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kf.updateProfilePicture(path7)
                     kf.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kg.updateProfilePicture(path8)
                     kg.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     kh.updateProfilePicture(path9)
                     kh.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     so.updateProfilePicture(path10)
                     so.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
                     sw.updateProfilePicture(path11)
                     sw.sendMessage(msg.to, "Berhasil mengubah foto profile bot")
               if msg.contentType == 2:
                   if msg._from in admin:
                       if mid in Setmain["ARvideo"]:
                            path = cl.downloadObjectMsg(msg_id)
                            del Setmain["ARvideo"][mid]
                            cl.updateProfileVideoPicture(path)
                            cl.sendMessage(msg.to,"Foto berhasil dirubah jadi video")
                            
               if msg.contentType == 0:
                 if Setmain["autoRead"] == True:
                     cl.sendChatChecked(msg.to, msg_id)
                 if text is None:
                     return
                 else:
                        for sticker in stickers:
                         if msg._from in admin:
                           if text.lower() == sticker:
                              sid = stickers[text.lower()]["STKID","73760366"]
                              spkg = stickers[text.lower()]["STKPKGID","12228"]
                              cl.sendSticker(to, spkg, sid)
                        for image in images:
                         if msg._from in admin:
                           if text.lower() == image:
                              cl.sendImage(msg.to, images[image])
                        for audio in audios:
                         if msg._from in admin:
                           if text.lower() == audio:
                              cl.sendAudio(msg.to, audios[audio])
                        for video in videos:
                         if msg._from in admin:
                           if text.lower() == video:
                              cl.sendVideo(msg.to, videos[video])
                        cmd = command(text)
                        if cmd == "help":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage = help()
                               cl.sendMessage(msg.to, str(helpMessage))
                                                                                       
                        if cmd == "self on":
                            if msg._from in admin:
                                wait["selfbot"] = True
                                cl.sendMessage(msg.to, "Selfbot diaktifkan")
                                
                        elif cmd == "self off":
                            if msg._from in admin:
                                wait["selfbot"] = False
                                cl.sendMessage(msg.to, "Selfbot dinonaktifkan")
                                            
                        elif cmd == "helpself":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               helpMessage1 = helpbot()
                               cl.sendMessage(msg.to, str(helpMessage1))

                        elif cmd == "set":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                md = "╭─〔™AbiOleng™〕──\n│Tanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\n│Jam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]\n╰───────────────\n    •─{Protect Status}─•\n╭───────────────\n"
                                if wait["sticker"] == True: md+="│ Sticker\n"
                                else: md+="│ Sticker(x)\n"
                                if wait["contact"] == True: md+="│ Contact\n"
                                else: md+="│ Contact(x)\n"
                                if wait["talkban"] == True: md+="│ Talkban\n"
                                else: md+="│ Talkban(x」\n"
                                if wait["Mentionkick"] == True: md+="│ Notag\n"
                                else: md+="│ Notag(x)\n"
                                if wait["detectMention"] == True: md+="│ Respon"
                                else: md+="│ Respon(x)\n"
                                if wait["autoJoin"] == True: md+="│ Autojoin\n"
                                else: md+="│ Autojoin(x)\n"
                                if wait["autoAdd"] == True: md+="│ Autoadd\n"
                                else: md+="│ Autoadd(x)\n"
                                if msg.to in welcome: md+="│ Welcome\n"
                                else: md+="│ Welcome(x)\n"
                                if wait["autoLeave"] == True: md+="│ Autoleave\n"
                                else: md+="│ Autoleave(x)\n"
                                if msg.to in protectqr: md+="│ Protecturl\n"
                                else: md+="│ Protecturl(x)\n"
                                if msg.to in protectqr: md+="│ Protectinvitel\n"
                                else: md+="│ Protecturl(x)\n"
                                if msg.to in protectjoin: md+="│ Protectjoin\n"
                                else: md+="│ Protectjoin(x)\n"
                                if msg.to in protectkick: md+="│ Protectkick\n"
                                else: md+="│ Protectkick(x)\n"
                                if msg.to in protectcancel: md+="│ Protectcancel"
                                else: md+="│ Protectcancel(x)"
                                cl.sendMessage(msg.to, md)

                        elif cmd == "owner" or text.lower() == 'creator':
                            if msg._from in admin:
                                cl.sendMessage(msg.to,"bot protect cok") 
                                ma = ""
                                for i in creator:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)
                                    cl.sendMessage(msg.to, None, contentMetadata={"STKID":"73760366","STKPKGID":"12228","STKVER":"2"}, contentType=7)

                        elif cmd == "mie":
                                channel = Channel(cl, '1526709289')
                                kie = channel.getChannelResult()
                                url = "https://game.linefriends.com/jbp-lcs-ranking/lcs/SendMessage"
                                data = {
                                    "cc": "{}".format(str(kie.token)),
                                    "to": to,
                                    "messages": [
                                        {
                                            "type": "template",
                                            "altText": "RAT",
                                            "template": {
                                                "type": "buttons",
                                                "thumbnailImageUrl": "https://os.line.naver.jp/os/p/{}".format(sender),
                                                "title": "RAT",
                                                "text": "SOAK BOT~",
                                                "actions": [
                                                    {
                                                        "type": "uri",
                                                        "label": "ChatMe",
                                                        "uri": "line://ti/p/~sadis101"
                                                    },
                                                    {
                                                        "type": "uri",
                                                        "label": "AddMe",
                                                        "uri": "line://ti/p/~olengkiller"
                                                    }                                                    
                                                ],
                                                "imageAspectRatio": "square",
                                                "imageSize": "contain"
                                            }
                                        }
                                    ]
                                }
                                headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 5.0.2; SM-G530H Build/LRX22G; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Line/8.9.1', 'Content-Type': 'application/json', 'Connection': 'keep-alive', 'Accept':'*/*', 'Accept-Encoding':'gzip, deflate'}
                                result = requests.session().post(url, headers=headers, data=json.dumps(data))
                                result.text  

                        elif cmd == "abot" or cmd == "informasi":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention1(msg.to, sender, "「 Type Selfbot 」\n")
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': mid}, contentType=13)

                        elif cmd == "me" or text.lower() == 'aku':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sendMention(to, "「Auto Mention」\n@!", [sender])
                               cl.sendContact(to, sender)

                        elif text.lower() == "mid":
                               cl.sendMessage(msg.to, msg._from)
                               cl.sendMessage(msg.to,"Mid mele apa js cok")
                               cl.sendMessage(msg.to, None, contentMetadata={"STKID":"73760366","STKPKGID":"12228","STKVER":"2"}, contentType=7)
                               
                        elif text.lower() == "nah":
                               cl.sendMessage(msg.to,"Nah bego lu")
                               cl.sendMessage(msg.to, None, contentMetadata={"STKID":"73760366","STKPKGID":"12228","STKVER":"2"}, contentType=7)
                               
                        elif text.lower() == "naik":
                               cl.sendMessage(msg.to,"Naik ke mana cok")
                               cl.sendMessage(msg.to, None, contentMetadata={"STKID":"73760366","STKPKGID":"12228","STKVER":"2"}, contentType=7)
                               
                        elif text.lower() == "malam":
                               cl.sendMessage(msg.to,"Dah malam cok mati sana")
                               cl.sendMessage(msg.to, None, contentMetadata={"STKID":"73760366","STKPKGID":"12228","STKVER":"2"}, contentType=7)
                               
                        elif text.lower() == "pagi":
                               cl.sendMessage(msg.to,"pagi enak buat cuddle")
                               cl.sendMessage(msg.to, None, contentMetadata={"STKID":"73760366","STKPKGID":"12228","STKVER":"2"}, contentType=7)

                        elif text.lower() == "typo":
                               cl.sendMessage(msg.to,"ngetik aja blm khatam")
                               cl.sendMessage(msg.to, None, contentMetadata={"STKID":"73760366","STKPKGID":"12228","STKVER":"2"}, contentType=7)
                               
                        elif text.lower() == "asalamualaikum":
                               cl.sendMessage(msg.to,"waalaikumsayang")
                               cl.sendMessage(msg.to, None, contentMetadata={"STKID":"73760366","STKPKGID":"12228","STKVER":"2"}, contentType=7)
                               
                        elif text.lower() == "susu":
                               cl.sendMessage(msg.to,"ngocok susu ya cok")
                               cl.sendMessage(msg.to, None, contentMetadata={"STKID":"73760366","STKPKGID":"12228","STKVER":"2"}, contentType=7)

                        elif text.lower() == "kopi":
                               cl.sendMessage(msg.to,"kopi dalgoblok")
                               cl.sendMessage(msg.to, None, contentMetadata={"STKID":"73760366","STKPKGID":"12228","STKVER":"2"}, contentType=7)
                               
                        elif text.lower() == "pantek":
                               cl.sendMessage(msg.to,"papapapapantek")
                               cl.sendMessage(msg.to, None, contentMetadata={"STKID":"16083755","STKPKGID":"1419343","STKVER":"1"}, contentType=7)

                        elif text.lower() == "sepi":
                               cl.sendMessage(msg.to,"enak buat tutuy")
                               cl.sendMessage(msg.to, None, contentMetadata={"STKID":"16083751","STKPKGID":"1419343","STKVER":"1"}, contentType=7)
                               
                        elif text.lower() == "atto":
                               cl.sendMessage(msg.to,"sejenis anjing kan ya")
                               cl.sendMessage(msg.to, None, contentMetadata={"STKID":"16083747","STKPKGID":"1419343","STKVER":"1"}, contentType=7)

                        elif text.lower() == "kangen":
                               cl.sendMessage(msg.to,"dih lu siapa")
                               cl.sendMessage(msg.to, None, contentMetadata={"STKID":"16083749","STKPKGID":"1419343","STKVER":"1"}, contentType=7)
                               
                        elif text.lower() == "cium":
                               cl.sendMessage(msg.to,"cium babi sana")
                               cl.sendMessage(msg.to, None, contentMetadata={"STKID":"16083746","STKPKGID":"1419343","STKVER":"1"}, contentType=7)

                        elif text.lower() == "gblk":
                               cl.sendMessage(msg.to,"lu goblok")
                               cl.sendMessage(msg.to, None, contentMetadata={"STKID":"16083746","STKPKGID":"1419343","STKVER":"1"}, contentType=7)
                               
                        elif text.lower() == "bego":
                               cl.sendMessage(msg.to,"bego lu ya")
                               cl.sendMessage(msg.to, None, contentMetadata={"STKID":"18532723","STKPKGID":"9061","STKVER":"2"}, contentType=7)

                        elif text.lower() == "mandi":
                               cl.sendMessage(msg.to,"mandi junub ya")
                               cl.sendMessage(msg.to, None, contentMetadata={"STKID":"18532723","STKPKGID":"9061","STKVER":"2"}, contentType=7)

                        elif text.lower() == "sayang":
                               cl.sendMessage(msg.to,"palalu peyang")
                               cl.sendMessage(msg.to, None, contentMetadata={"STKID":"13835585","STKPKGID":"7451","STKVER":"4"}, contentType=7)

                        elif text.lower() == "bot":
                               cl.sendMessage(msg.to,"lu yg bot")
                               cl.sendMessage(msg.to, None, contentMetadata={"STKID":"13835585","STKPKGID":"7451","STKVER":"4"}, contentType=7)    

                        elif text.lower() == "ajg":
                               cl.sendMessage(msg.to,"atto dipanggil tuh")
                               cl.sendMessage(msg.to, None, contentMetadata={"STKID":"38489980","STKPKGID":"11129","STKVER":"4"}, contentType=7)

                        elif text.lower() == "baper":
                               cl.sendMessage(msg.to,"lemah lu cok")
                               cl.sendMessage(msg.to, None, contentMetadata={"STKID":"13835600","STKPKGID":"7451","STKVER":"4"}, contentType=7)     

                        elif text.lower() == "anjing":
                               cl.sendMessage(msg.to,"atto dipanggil tuh")
                               cl.sendMessage(msg.to, None, contentMetadata={"STKID":"127833632","STKPKGID":"13207","STKVER":"1"}, contentType=7)

                        elif text.lower() == "nyanyi":
                               cl.sendMessage(msg.to,"aku suka susumu meskipun gede satu,aku suka anumu meskipun belum tumbuh bulu~")
                               cl.sendMessage(msg.to, None, contentMetadata={"STKID":"38489960","STKPKGID":"11129","STKVER":"4"}, contentType=7)   
                               
                        elif text.lower() == "asu":
                               cl.sendMessage(msg.to,"asu kok teriak asu")
                               cl.sendMessage(msg.to, None, contentMetadata={"STKID":"18532723","STKPKGID":"9061","STKVER":"2"}, contentType=7)     

                        elif text.lower() == "asw":
                               cl.sendMessage(msg.to,"asw kok teriak asw")
                               cl.sendMessage(msg.to, None, contentMetadata={"STKID":"18532723","STKPKGID":"9061","STKVER":"2"}, contentType=7)         

                        elif text.lower() == "goblok":
                               cl.sendMessage(msg.to,"lu goblok")
                               cl.sendMessage(msg.to, None, contentMetadata={"STKID":"13835582","STKPKGID":"7451","STKVER":"4"}, contentType=7)
                               
                        elif cmd == "tig tog":
                          if msg.toType == 2:
                             group = cl.getGroup(msg.to)
                             nama = [contact.mid for contact in group.members]
                             k = len(nama)//20
                             for a in range(k+1):
                                txt = u''
                                s=0
                                b=[]
                                for i in group.members[a*20 : (a+1)*20]:
                                    b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                    s += 7
                                    txt += u'@Zero \n'
                                cl.sendMessage(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)

                        elif ("Mid " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "Nama : "+str(mi.displayName)+"\nMID : " +key1)
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)

                        elif ("Info " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               cl.sendMessage(msg.to, "✒ Nama : "+str(mi.displayName)+"\n✒ Mid : " +key1+"\n✒ Status Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))

                        elif text.lower() == "clear chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   cl.removeAllMessages(op.param2)
                                   cl.sendMessage(msg.to,"Chat akun utama dibersihkan...")
                               except:
                                   pass

                        elif text.lower() == "remove chat":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               try:
                                   ki.removeAllMessages(op.param2)
                                   kk.removeAllMessages(op.param2)
                                   kc.removeAllMessages(op.param2)
                                   kb.removeAllMessages(op.param2)
                                   kd.removeAllMessages(op.param2)
                                   ke.removeAllMessages(op.param2)
                                   kf.removeAllMessages(op.param2)
                                   kg.removeAllMessages(op.param2)
                                   kh.removeAllMessages(op.param2)
                                   so.removeAllMessages(op.param2)
                                   sw.removeAllMessages(op.param2)
                                   cl.sendMessage(msg.to,"Chat akun bot dibersihkan...")
                               except:
                                   pass

                        elif cmd.startswith("broadcast: "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               pesan = text.replace(sep[0] + " ","")
                               saya = cl.getGroupIdsJoined()
                               for group in saya:
                                   cl.sendMessage(group,"[ Broadcast ]\n" + str(pesan))

                        elif text.lower() == "mykey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Mykey」\nSetkey bot mu「 " + str(Setmain["keyCommand"]) + " 」")
                               
                        elif cmd.startswith("setkey "):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               sep = text.split(" ")
                               key = text.replace(sep[0] + " ","")
                               if key in [""," ","\n",None]:
                                   cl.sendMessage(msg.to, "Gagal mengganti key")
                               else:
                                   Setmain["keyCommand"] = str(key).lower()
                                   cl.sendMessage(msg.to, "「Setkey」\nSetkey diganti jadi「{}」".format(str(key).lower()))
                                   
                        elif cmd.startswith("/al quran "):
                            query = text.replace("/al quran ","")
                            text = query.split("-")
                            surah = int(text[0])
                            ayat1 = int(text[1])
                            ayat2 = int(text[2])
                            result = requests.get("https://farzain.xyz/api/alquran.php?id={}&from={}&to={}".format(surah, ayat1, ayat2))
                            data = result.text
                            data = json.loads(data)
                            if data["status"] == "success":
                                hasil = "Al-Qur'an\n"
                                hasil += "\nName : {}".format(str(data["nama_surat"]))
                                hasil += "\nMeaning : {}".format(str(data["arti_surat"]))
                                hasil += "\nAyat :"
                                for ayat in data["ayat"]:
                                    hasil += "\n{}".format(str(ayat))
                                hasil += "\nMeaning Ayat :"
                                for arti in data["arti"]:
                                    hasil += "\n{}".format(str(arti))
                                cl.sendMessage(to, str(hasil))
                                
                        elif ("Steal " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key1 = key["MENTIONEES"][0]["M"]
                               mi = cl.getContact(key1)
                               a = channel.getProfileCoverURL(mid=key1)
                               cl.sendMessage(msg.to, " Contact Info \n• Nama : "+str(mi.displayName)+"\n Mid : " +key1+"\n Status Msg"+str(mi.statusMessage))
                               cl.sendMessage(msg.to, None, contentMetadata={'mid': key1}, contentType=13)
                               if "videoProfile='{" in str(cl.getContact(key1)):
                                   cl.sendVideoWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath)+'/vp.small')
                                   cl.sendImageWithURL(receiver, a)
                               else:
                                   cl.sendImageWithURL(msg.to, 'http://dl.profile.line.naver.jp'+str(mi.picturePath))
                                   cl.sendImageWithURL(receiver, a)

                        elif ("Cover " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    u = key["MENTIONEES"][0]["M"]
                                    a = channel.getProfileCoverURL(mid=u)
                                    cl.sendImageWithURL(receiver, a)
                                except Exception as e:
                                    cl.sendText(receiver, str(e))
#CLONE
                        elif cmd.startswith("clone "):
                          if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    cl.cloneContactProfile(ls)
                                    cl.sendContact(to, sender)
                                    cl.sendMessage(to, "➧ Berhasil clone profile")

                        elif cmd == "restoreprofile":
                            try:
                                lineProfile = cl.getProfile()
                                lineProfile.displayName = str(wait["myProfile"]["displayName"])
                                lineProfile.statusMessage = str(wait["myProfile"]["statusMessage"])
                                lineProfile.pictureStatus = str(wait["myProfile"]["pictureStatus"])
                                cl.updateProfileAttribute(8, lineProfile.pictureStatus)
                                cl.updateProfile(lineProfile)
                                coverId = str(wait["myProfile"]["coverId"])
                                cl.updateProfileCoverById(coverId)
                                cl.sendMessage(to, "ʀᴇsᴛᴏʀᴇ ᴘʀᴏғɪʟᴇ sᴜᴄᴄᴇs, ᴡᴀɪᴛ ᴀ ғᴇᴡ ᴍɪɴᴜᴛᴇs")
                            except Exception as e:
                                cl.sendMessage(to, "ʀᴇsᴛᴏʀᴇ ᴘʀᴏғɪʟᴇ ғᴀɪʟᴇᴅ")

                        elif cmd == "backupprofile":
                            try:
                                profile = cl.getProfile()
                                wait["myProfile"]["displayName"] = str(profile.displayName)
                                wait["myProfile"]["statusMessage"] = str(profile.statusMessage)
                                wait["myProfile"]["pictureStatus"] = str(profile.pictureStatus)
#                                coverId = ririn.getProfileDetail()["result"]["objectId"]
#                                wait["myProfile"]["coverId"] = str(coverId)
                                cl.sendMessage(to, "ʙᴀᴄᴋᴜᴘ ᴘʀᴏғɪʟᴇ sᴜᴄᴄᴇs")
                            except Exception as e:
                                cl.sendMessage(to, "ʙᴀᴄᴋᴜᴘ ᴘʀᴏғɪʟᴇ ғᴀɪʟᴇᴅ")

                        elif ("Sticker: " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    query = msg.text.replace("Sticker: ", "")
                                    query = int(query)
                                    if type(query) == int:
                                        cl.sendImageWithURL(receiver, 'https://stickershop.line-scdn.net/stickershop/v1/product/'+str(query)+'/ANDROID/main.png')
                                        cl.sendText(receiver, 'https://line.me/S/sticker/'+str(query))
                                    else:
                                        cl.sendText(receiver, 'gunakan key sticker angka bukan huruf')
                                except Exception as e:
                                    cl.sendText(receiver, str(e))        

                        elif text.lower() == "resetkey":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               Setmain["keyCommand"] = ""
                               cl.sendMessage(msg.to, "「Setkey」\nSetkey mu kembali ke awal")
                               
                        elif cmd == "reject":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              ginvited = cl.getGroupIdsInvited()
                              if ginvited != [] and ginvited != None:
                                  for gid in ginvited:
                                      cl.rejectGroupInvitation(gid)
                                      ki.rejectGroupInvitation(gid)
                                      kk.rejectGroupInvitation(gid)
                                      kc.rejectGroupInvitation(gid)
                                      kb.rejectGroupInvitation(gid)
                                      kd.rejectGroupInvitation(gid)
                                      ke.rejectGroupInvitation(gid)
                                      kf.rejectGroupInvitation(gid)
                                      kg.rejectGroupInvitation(gid)
                                      kh.rejectGroupInvitation(gid)
                                  cl.sendMessage(to, "Berhasil tolak sebanyak {} undangan grup".format(str(len(ginvited))))
                              else:
                                  cl.sendMessage(to, "Tidak ada undangan yang tertunda")        

                        elif cmd == "restart":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "Tunggu sebentar...")
                               Setmain["restartPoint"] = msg.to
                               restartBot()
                               cl.sendMessage(msg.to, "Silahkan gunakan seperti semula")
                            
                        elif cmd == "runtime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               eltime = time.time() - mulai
                               bot = "Aktif " +waktu(eltime)
                               cl.sendMessage(msg.to,bot)
                            
                        elif cmd == "ginfo":
                          if msg._from in admin:
                            try:
                                G = cl.getGroup(msg.to)
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                cl.sendMessage(msg.to, "✒ ReyPro Grup Info\n\n✒ Nama Group : {}".format(G.name)+ "\n✒ ID Group : {}".format(G.id)+ "\n✒ Pembuat : {}".format(G.creator.displayName)+ "\n✒ Waktu Dibuat : {}".format(str(timeCreated))+ "\n✒ Jumlah Member : {}".format(str(len(G.members)))+ "\n✒ Jumlah Pending : {}".format(gPending)+ "\n✒ Group Qr : {}".format(gQr)+ "\n✒ Group Ticket : {}".format(gTicket))
                                cl.sendMessage(msg.to, None, contentMetadata={'mid': G.creator.mid}, contentType=13)
                                cl.sendImageWithURL(msg.to, 'http://dl.profile.line-cdn.net/'+G.pictureStatus)
                            except Exception as e:
                                cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("infogrup "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            number = text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                try:
                                    gCreator = G.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if G.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(G.invitee))
                                if G.preventedJoinByTicket == True:
                                    gQr = "Tertutup"
                                    gTicket = "Tidak ada"
                                else:
                                    gQr = "Terbuka"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(G.id)))
                                timeCreated = []
                                timeCreated.append(time.strftime("%d-%m-%Y [ %H:%M:%S ]", time.localtime(int(G.createdTime) / 1000)))
                                ret_ += " ReyPro Grup Info\n"
                                ret_ += "\n Nama Group : {}".format(G.name)
                                ret_ += "\n ID Group : {}".format(G.id)
                                ret_ += "\n Pembuat : {}".format(gCreator)
                                ret_ += "\n Waktu Dibuat : {}".format(str(timeCreated))
                                ret_ += "\n Jumlah Member : {}".format(str(len(G.members)))
                                ret_ += "\n Jumlah Pending : {}".format(gPending)
                                ret_ += "\n Group Qr : {}".format(gQr)
                                ret_ += "\n Group Ticket : {}".format(gTicket)
                                ret_ += ""
                                cl.sendMessage(to, str(ret_))
                            except:
                                pass

                        elif cmd.startswith("infomem "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            ret_ = ""
                            try:
                                group = groups[int(number)-1]
                                G = cl.getGroup(group)
                                no = 0
                                ret_ = ""
                                for mem in G.members:
                                    no += 1
                                    ret_ += "\n " "- "+ str(no) + ". " + mem.displayName
                                cl.sendMessage(to," Group Name : [ " + str(G.name) + " ]\n\n   [ List Member ]\n" + ret_ + "\n\n「Total %i Members」" % len(G.members))
                            except: 
                                pass

                        elif cmd.startswith("leave: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            number = msg.text.replace(separate[0] + " ","")
                            groups = cl.getGroupIdsJoined()
                            group = groups[int(number)-1]
                            for i in group:
                                ginfo = cl.getGroup(i)
                                if ginfo == group:
                                    ki.leaveGroup(i)
                                    kk.leaveGroup(i)
                                    kc.leaveGroup(i)
                                    kb.leaveGroup(i)
                                    ke.leaveGroup(i)
                                    kd.leaveGroup(i)
                                    kf.leaveGroup(i)
                                    kg.leaveGroup(i)
                                    kh.leaveGroup(i)
                                    cl.sendMessage(msg.to,"Berhasil keluar di grup " +str(ginfo.name))

                        elif cmd == "fiendlist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getAllContactIds()
                               for i in gid:
                                   G = cl.getContact(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "|" + str(a) + ". " +G.displayName+ "\n"
                               cl.sendMessage(msg.to,"[ FRIEND LIST ]\n|\n"+ma+"|\n[ Total >"+str(len(gid))+"< Friends ]")

                        elif cmd == "gruplist":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = cl.getGroupIdsJoined()
                               for i in gid:
                                   G = cl.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "| " + str(a) + ". " +G.name+ "\n"
                               cl.sendMessage(msg.to,"[ GROUP LIST ]\n|\n"+ma+"|\n[ Total >"+str(len(gid))+"< Groups ]")

                        elif cmd == "gruplist1":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ki.getGroupIdsJoined()
                               for i in gid:
                                   G = ki.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "| " + str(a) + ". " +G.name+ "\n"
                               ki.sendMessage(msg.to,"[ GROUP LIST ]\n|\n"+ma+"|\n[ Total >"+str(len(gid))+"< Groups ]")

                        elif cmd == "gruplist2":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kk.getGroupIdsJoined()
                               for i in gid:
                                   G = kk.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "| " + str(a) + ". " +G.name+ "\n"
                               kk.sendMessage(msg.to,"[ GROUP LIST ]\n|\n"+ma+"|\n[ Total >"+str(len(gid))+"< Groups ]")

                        elif cmd == "gruplist3":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kc.getGroupIdsJoined()
                               for i in gid:
                                   G = kc.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "| " + str(a) + ". " +G.name+ "\n"
                               kc.sendMessage(msg.to,"[ GROUP LIST ]\n|\n"+ma+"|\n[ Total >"+str(len(gid))+"< Groups ]")
                               
                        elif cmd == "gruplist4":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = kb.getGroupIdsJoined()
                               for i in gid:
                                   G = kb.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "| " + str(a) + ". " +G.name+ "\n"
                               kb.sendMessage(msg.to,"[ GROUP LIST ]\n|\n"+ma+"|\n[ Total >"+str(len(gid))+"< Groups ]")       
                               
                        elif cmd == "gruplist5":
                            if msg._from in admin:
                               ma = ""
                               a = 0
                               gid = ke.getGroupIdsJoined()
                               for i in gid:
                                   G = ke.getGroup(i)
                                   a = a + 1
                                   end = "\n"
                                   ma += "| " + str(a) + ". " +G.name+ "\n"
                               ke.sendMessage(msg.to,"[ GROUP LIST ]\n|\n"+ma+"|\n[ Total >"+str(len(gid))+"< Groups ]")
                        elif cmd == "open":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = False
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Opened")

                        elif cmd == "close":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   X = cl.getGroup(msg.to)
                                   X.preventedJoinByTicket = True
                                   cl.updateGroup(X)
                                   cl.sendMessage(msg.to, "Url Closed")

                        elif cmd == "qr grup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                if msg.toType == 2:
                                   x = cl.getGroup(msg.to)
                                   if x.preventedJoinByTicket == True:
                                      x.preventedJoinByTicket = False
                                      cl.updateGroup(x)
                                   gurl = cl.reissueGroupTicket(msg.to)
                                   cl.sendMessage(msg.to, "Nama : "+str(x.name)+ "\nUrl grup : http://line.me/R/ti/g/"+gurl)

#===========BOT UPDATE============#
                        elif cmd == "updategrup":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if msg.toType == 2:
                                settings["groupPicture"] = True
                                cl.sendMessage(msg.to,"Send your images.....")

                        elif cmd == "updatebot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["changePicture"] = True
                                cl.sendMessage(msg.to,"Send your images.....")
                                
                        elif cmd == "bot up":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                Setmain["ARfoto"][mid] = True
                                cl.sendMessage(msg.to,"Send your images.....")
                                
                        elif cmd == "bot1up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Amid] = True
                                ki.sendMessage(msg.to,"Send your images.....")
                                
                        elif cmd == "bot2up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Bmid] = True
                                kk.sendMessage(msg.to,"Send your images.....")
                                
                        elif cmd == "botl3up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Cmid] = True
                                kc.sendMessage(msg.to,"Send your images.....")
                                
                        elif cmd == "bot4up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Dmid] = True
                                kb.sendMessage(msg.to,"Send your images.....")
        
                        elif cmd == "bot5up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Emid] = True
                                kd.sendMessage(msg.to,"Send your images.....")
                                
                        elif cmd == "bot6up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Fmid] = True
                                ke.sendMessage(msg.to,"Send your images.....")
                                
                        elif cmd == "bot7up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Gmid] = True
                                kf.sendMessage(msg.to,"Send your images.....")
                                
                        elif cmd == "bot8up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Hmid] = True
                                kg.sendMessage(msg.to,"Send your images.....")
                                
                        elif cmd == "bot9up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Imid] = True
                                kh.sendMessage(msg.to,"Send your images.....")
        
                        elif cmd == "bot10up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Jmid] = True
                                so.sendMessage(msg.to,"Send your images.....")        
     
                        elif cmd == "bot11up":
                            if msg._from in admin:
                                Setmain["ARfoto"][Zmid] = True
                                sw.sendMessage(msg.to,"Send your images.....")

                        elif cmd.startswith("botname: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = cl.getProfile()
                                profile.displayName = string
                                cl.updateProfile(profile)
                                cl.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot1name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ki.getProfile()
                                profile.displayName = string
                                ki.updateProfile(profile)
                                ki.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot2name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kk.getProfile()
                                profile.displayName = string
                                kk.updateProfile(profile)
                                kk.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot3name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kc.getProfile()
                                profile.displayName = string
                                kc.updateProfile(profile)
                                kc.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                
                        elif cmd.startswith("bot4name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kb.getProfile()
                                profile.displayName = string
                                kb.updateProfile(profile)
                                kb.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                
                        elif cmd.startswith("bot5name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kd.getProfile()
                                profile.displayName = string
                                kd.updateProfile(profile)
                                kd.sendMessage(msg.to,"Nama diganti jadi " + string + "") 

                        elif cmd.startswith("bot6name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = ke.getProfile()
                                profile.displayName = string
                                ke.updateProfile(profile)
                                ke.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                
                        elif cmd.startswith("bot7name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kf.getProfile()
                                profile.displayName = string
                                kf.updateProfile(profile)
                                kf.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot8name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kg.getProfile()
                                profile.displayName = string
                                kg.updateProfile(profile)
                                kg.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot9name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = kh.getProfile()
                                profile.displayName = string
                                kh.updateProfile(profile)
                                kh.sendMessage(msg.to,"Nama diganti jadi " + string + "")

                        elif cmd.startswith("bot10name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = so.getProfile()
                                profile.displayName = string
                                so.updateProfile(profile)
                                so.sendMessage(msg.to,"Nama diganti jadi " + string + "")
                                
                        elif cmd.startswith("bot11name: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 10000000000:
                                profile = sw.getProfile()
                                profile.displayName = string
                                sw.updateProfile(profile)
                                sw.sendMessage(msg.to,"Nama diganti jadi " + string + "")

#=========== [ Add Image ] ============#
                        elif cmd.startswith("imgadd img "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in images:
                                wait["Addimage"]["status"] = True
                                wait["Addimage"]["name"] = str(name.lower())
                                images[str(name.lower())] = ""
                                f = codecs.open("image.json","w","utf-8")
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendMessage(msg.to, "Silahkan kirim fotonya...") 
                            else:
                                cl.sendMessage(msg.to, "Foto itu sudah dalam list") 
                                
                        elif cmd.startswith("imgdell img "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in images:
                                cl.deleteFile(images[str(name.lower())])
                                del images[str(name.lower())]
                                f = codecs.open("image.json","w","utf-8")
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendMessage(msg.to, "Berhasil menghapus {}".format( str(name.lower())))
                            else:
                                cl.sendMessage(msg.to, "Foto itu tidak ada dalam list") 
                                 
                        elif text.lower() == "listimage":
                           if msg._from in admin:
                             no = 0
                             ret_ = "「 Daftar Image 」\n\n"
                             for image in images:
                                 no += 1
                                 ret_ += str(no) + ". " + image.title() + "\n"
                             ret_ += "\nTotal「{}」Images".format(str(len(images)))
                             cl.sendMessage(to, ret_)
#=========== [ Add Video ] ============#                               
                        elif cmd.startswith("addvideo "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in videos:
                                wait["Addvideo"]["status"] = True
                                wait["Addvideo"]["name"] = str(name.lower())
                                videos[str(name.lower())] = ""
                                f = codecs.open("video.json","w","utf-8")
                                json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendMessage(msg.to, "Silahkan kirim videonya...") 
                            else:
                                cl.sendMessage(msg.to, "Video itu sudah dalam list") 
                                
                        elif cmd.startswith("dellvideo "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in videos:
                                cl.deleteFile(videos[str(name.lower())])
                                del videos[str(name.lower())]
                                f = codecs.open("video.json","w","utf-8")
                                json.dump(videos, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendMessage(msg.to, "Berhasil menghapus video {}".format( str(name.lower())))
                            else:
                                cl.sendMessage(msg.to, "Video itu tidak ada dalam list") 
                                 
                        elif text.lower() == "listvideo":
                           if msg._from in admin:
                             no = 0
                             ret_ = "「 Daftar Video 」\n\n"
                             for video in videos:
                                 no += 1
                                 ret_ += str(no) + ". " + video.title() + "\n"
                             ret_ += "\nTotal「{}」Videos".format(str(len(videos)))
                             cl.sendMessage(to, ret_)
                             sendMention(msg.to, msg._from,"","\nJika ingin play video nya,\nSilahkan ketik nama - judul\nBisa juga ketik namanya saja")
#=========== [ Add Video ] ============#                               
                        elif cmd.startswith("addmp3 "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in audios:
                                wait["Addaudio"]["status"] = True
                                wait["Addaudio"]["name"] = str(name.lower())
                                audios[str(name.lower())] = ""
                                f = codecs.open("audio.json","w","utf-8")
                                json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendText(msg.to, "Silahkan kirim mp3 nya...") 
                            else:
                                cl.sendMessage(msg.to, "Mp3 itu sudah dalam list") 
                                
                        elif cmd.startswith("dellmp3 "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in audios:
                                cl.deleteFile(audios[str(name.lower())])
                                del audios[str(name.lower())]
                                f = codecs.open("audio.json","w","utf-8")
                                json.dump(audios, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendMessage(msg.to, "Berhasil menghapus mp3 {}".format( str(name.lower())))
                            else:
                                cl.sendMessage(msg.to, "Mp3 itu tidak ada dalam list") 
                                 
                        elif cmd == "listmp3":
                             no = 0
                             ret_ = "「 Daftar Lagu 」\n\n"
                             for audio in audios:
                                 no += 1
                                 ret_ += str(no) + ". " + audio.title() + "\n"
                             ret_ += "\nTotal「{}」Lagu".format(str(len(audios)))
                             cl.sendMessage(to, ret_)
                             sendMention(msg.to, msg._from,"","\nJika ingin play mp3 nya,\nSilahkan ketik nama - judul\nBisa juga ketik namanya saja")
#=========== [ Add Sticker ] ============#                                            
                        elif cmd.startswith("addsticker "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in stickers:
                                wait["Addsticker"]["status"] = True
                                wait["Addsticker"]["name"] = str(name.lower())
                                stickers[str(name.lower())] = ""
                                f = codecs.open("sticker.json","w","utf-8")
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendMessage(msg.to, "Silahkan kirim stickernya...") 
                            else:
                                cl.sendMessage(msg.to, "Sticker itu sudah dalam list") 
                                
                        elif cmd.startswith("dellsticker "):
                          if msg._from in admin:
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in stickers:
                                del stickers[str(name.lower())]
                                f = codecs.open("sticker.json","w","utf-8")
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                cl.sendMessage(msg.to, "Berhasil menghapus sticker {}".format( str(name.lower())))
                            else:
                                cl.sendMessage(msg.to, "Sticker itu tidak ada dalam list") 
                                 
                        elif text.lower() == "liststicker":
                           if msg._from in admin:
                             no = 0
                             ret_ = "「 Daftar Sticker 」\n\n"
                             for sticker in stickers:
                                 no += 1
                                 ret_ += str(no) + ". " + sticker.title() + "\n"
                             ret_ += "\nTotal「{}」Stickers".format(str(len(stickers)))
                             cl.sendMessage(to, ret_)

#===========BOT UPDATE============#
                        elif cmd == "mention" or text.lower() == 'kiss':
                           if wait["selfbot"] == True:
                            if msg._from in Abi:
                             group = cl.getGroup(msg.to)
                            nama = [contact.mid for contact in group.members]
                            k = len(nama)//20
                            for a in range(k+1):
                                txt = u''
                                s=0
                                b=[]
                                for i in group.members[a*20 : (a+1)*20]:
                                    b.append({"S":str(s), "E" :str(s+6), "M":i.mid})
                                    s += 7
                                    txt += u'@Zero \n'
                                cl.sendMessage(msg.to, text=txt, contentMetadata={u'MENTION': json.dumps({'MENTIONEES':b})}, contentType=0)  

                        elif cmd == "listbot":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                a = 0
                                for m_id in Abi:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"✒ Abi bot\n\n"+ma+"\nTotal「%s」Bots" %(str(len(Abi))))

                        elif cmd == "listadmin":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                ma = ""
                                mb = ""
                                mc = ""
                                a = 0
                                b = 0
                                c = 0
                                for m_id in Abi:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in admin:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getContact(m_id).displayName + "\n"
                                for m_id in staff:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"✒ Abi admin\n\nSuper admin:\n"+ma+"\nAdmin:\n"+mb+"\nStaff:\n"+mc+"\nTotal「%s」Abi staff" %(str(len(owner)+len(admin)+len(staff))))

                        elif cmd == "listprotect":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                ma = ""
                                mb = ""
                                mc = ""
                                md = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                gid = protectqr
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectkick
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    mb += str(b) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectjoin
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    md += str(d) + ". " +cl.getGroup(group).name + "\n"
                                gid = protectcancel
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    mc += str(c) + ". " +cl.getGroup(group).name + "\n"
                                cl.sendMessage(msg.to,"protect\n\n PROTECT URL :\n"+ma+"\n PROTECT KICK :\n"+mb+"\n PROTECT JOIN :\n"+md+"\n PROTECT CANCEL:\n"+mc+"\nTotal「%s」Grup yg dijaga" %(str(len(protectqr)+len(protectkick)+len(protectjoin)+len(protectcancel))))

                        elif cmd == "respon" or cmd == "pasukan":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                cl.sendMessage(msg.to, "aku disini cok")
                                ki.sendMessage(msg.to, "aku disini cok")
                                kk.sendMessage(msg.to, "aku disini cok")
                                kc.sendMessage(msg.to, "aku disini cok")
                                kb.sendMessage(msg.to, "aku disini cok")
                                kd.sendMessage(msg.to, "aku disini cok")
                                ke.sendMessage(msg.to, "aku disini cok")
                                kf.sendMessage(msg.to, "aku disini cok")
                                kg.sendMessage(msg.to, "aku disini cok")
                                kh.sendMessage(msg.to, "aku disini cok")
                                
                        elif msg.text.lower().startswith("addbot"):
                           if msg._from in Abi:
                                try:
                                    cl.findAndAddContactsByMid(Amid)
                                    cl.findAndAddContactsByMid(Bmid)
                                    cl.findAndAddContactsByMid(Cmid)
                                    cl.findAndAddContactsByMid(Dmid)
                                    cl.findAndAddContactsByMid(Emid)
                                    cl.findAndAddContactsByMid(Fmid)
                                    cl.findAndAddContactsByMid(Gmid)
                                    cl.findAndAddContactsByMid(Hmid)
                                    cl.findAndAddContactsByMid(Imid)
                                    cl.findAndAddContactsByMid(Jmid)
                                    cl.findAndAddContactsByMid(Zmid)
                                    cl.sendMessage(msg.to,"Success!!!")
                                    ki.findAndAddContactsByMid(mid)
                                    ki.findAndAddContactsByMid(Bmid)
                                    ki.findAndAddContactsByMid(Cmid)
                                    ki.findAndAddContactsByMid(Dmid)
                                    ki.findAndAddContactsByMid(Emid)
                                    ki.findAndAddContactsByMid(Fmid)
                                    ki.findAndAddContactsByMid(Gmid)
                                    ki.findAndAddContactsByMid(Hmid)
                                    ki.findAndAddContactsByMid(Imid)
                                    ki.findAndAddContactsByMid(Jmid)
                                    ki.findAndAddContactsByMid(Zmid)
                                    ki.sendMessage(msg.to,"Success!!!")
                                    kk.findAndAddContactsByMid(mid)
                                    kk.findAndAddContactsByMid(Amid)
                                    kk.findAndAddContactsByMid(Cmid)
                                    kk.findAndAddContactsByMid(Dmid)
                                    kk.findAndAddContactsByMid(Emid)
                                    kk.findAndAddContactsByMid(Fmid)
                                    kk.findAndAddContactsByMid(Gmid)
                                    kk.findAndAddContactsByMid(Hmid)
                                    kk.findAndAddContactsByMid(Imid)
                                    kk.findAndAddContactsByMid(Jmid)
                                    kk.findAndAddContactsByMid(Zmid)
                                    kk.sendMessage(msg.to,"Success!!!")
                                    kc.findAndAddContactsByMid(mid)
                                    kc.findAndAddContactsByMid(Amid)
                                    kc.findAndAddContactsByMid(Bmid)
                                    kc.findAndAddContactsByMid(Dmid)
                                    kc.findAndAddContactsByMid(Emid)
                                    kc.findAndAddContactsByMid(Fmid)
                                    kc.findAndAddContactsByMid(Gmid)
                                    kc.findAndAddContactsByMid(Hmid)
                                    kc.findAndAddContactsByMid(Imid)
                                    kc.findAndAddContactsByMid(Jmid)
                                    kc.findAndAddContactsByMid(Zmid)
                                    kc.sendMessage(msg.to,"Success!!!")
                                    kb.findAndAddContactsByMid(mid)
                                    kb.findAndAddContactsByMid(Amid)
                                    kb.findAndAddContactsByMid(Bmid)
                                    kb.findAndAddContactsByMid(Cmid)
                                    kb.findAndAddContactsByMid(Emid)
                                    kb.findAndAddContactsByMid(Fmid)
                                    kb.findAndAddContactsByMid(Gmid)
                                    kb.findAndAddContactsByMid(Hmid)
                                    kb.findAndAddContactsByMid(Imid)
                                    kb.findAndAddContactsByMid(Jmid)
                                    kb.findAndAddContactsByMid(Zmid)
                                    kb.sendMessage(msg.to,"Success!!!")
                                    kd.findAndAddContactsByMid(mid)
                                    kd.findAndAddContactsByMid(Amid)
                                    kd.findAndAddContactsByMid(Bmid)
                                    kd.findAndAddContactsByMid(Cmid)
                                    kd.findAndAddContactsByMid(Dmid)
                                    kd.findAndAddContactsByMid(Fmid)
                                    kd.findAndAddContactsByMid(Gmid)
                                    kd.findAndAddContactsByMid(Hmid)
                                    kd.findAndAddContactsByMid(Imid)
                                    kd.findAndAddContactsByMid(Jmid)
                                    kd.findAndAddContactsByMid(Zmid)
                                    kd.sendMessage(msg.to,"Success!!!")
                                    ke.findAndAddContactsByMid(mid)
                                    ke.findAndAddContactsByMid(Amid)
                                    ke.findAndAddContactsByMid(Bmid)
                                    ke.findAndAddContactsByMid(Cmid)
                                    ke.findAndAddContactsByMid(Dmid)
                                    ke.findAndAddContactsByMid(Emid)
                                    ke.findAndAddContactsByMid(Gmid)
                                    ke.findAndAddContactsByMid(Hmid)
                                    ke.findAndAddContactsByMid(Imid)
                                    ke.findAndAddContactsByMid(Jmid)
                                    ke.findAndAddContactsByMid(Zmid)
                                    ke.sendMessage(msg.to,"Success!!!")
                                    kf.findAndAddContactsByMid(mid)
                                    kf.findAndAddContactsByMid(Amid)
                                    kf.findAndAddContactsByMid(Bmid)
                                    kf.findAndAddContactsByMid(Cmid)
                                    kf.findAndAddContactsByMid(Dmid)
                                    kf.findAndAddContactsByMid(Emid)
                                    kf.findAndAddContactsByMid(Fmid)
                                    kf.findAndAddContactsByMid(Hmid)
                                    kf.findAndAddContactsByMid(Imid)
                                    kf.findAndAddContactsByMid(Jmid)
                                    kf.findAndAddContactsByMid(Zmid)
                                    kf.sendMessage(msg.to,"Success!!!")
                                    kg.findAndAddContactsByMid(mid)
                                    kg.findAndAddContactsByMid(Amid)
                                    kg.findAndAddContactsByMid(Bmid)
                                    kg.findAndAddContactsByMid(Cmid)
                                    kg.findAndAddContactsByMid(Dmid)
                                    kg.findAndAddContactsByMid(Emid)
                                    kg.findAndAddContactsByMid(Fmid)
                                    kg.findAndAddContactsByMid(Gmid)
                                    kg.findAndAddContactsByMid(Imid)
                                    kg.findAndAddContactsByMid(Jmid)
                                    kg.findAndAddContactsByMid(Zmid)
                                    kg.sendMessage(msg.to,"Success!!!")
                                    kh.findAndAddContactsByMid(mid)
                                    kh.findAndAddContactsByMid(Amid)
                                    kh.findAndAddContactsByMid(Bmid)
                                    kh.findAndAddContactsByMid(Cmid)
                                    kh.findAndAddContactsByMid(Dmid)
                                    kh.findAndAddContactsByMid(Emid)
                                    kh.findAndAddContactsByMid(Fmid)
                                    kh.findAndAddContactsByMid(Gmid)
                                    kh.findAndAddContactsByMid(Hmid)
                                    kh.findAndAddContactsByMid(Jmid)
                                    kh.findAndAddContactsByMid(Zmid)
                                    kh.sendMessage(msg.to,"Success!!!")
                                    so.findAndAddContactsByMid(mid)
                                    so.findAndAddContactsByMid(Amid)
                                    so.findAndAddContactsByMid(Bmid)
                                    so.findAndAddContactsByMid(Cmid)
                                    so.findAndAddContactsByMid(Dmid)
                                    so.findAndAddContactsByMid(Emid)
                                    so.findAndAddContactsByMid(Fmid)
                                    so.findAndAddContactsByMid(Gmid)
                                    so.findAndAddContactsByMid(Hmid)
                                    so.findAndAddContactsByMid(Imid)
                                    so.findAndAddContactsByMid(Zmid)
                                    so.sendMessage(msg.to,"Success!!!")
                                    sw.findAndAddContactsByMid(mid)
                                    sw.findAndAddContactsByMid(Amid)
                                    sw.findAndAddContactsByMid(Bmid)
                                    sw.findAndAddContactsByMid(Cmid)
                                    sw.findAndAddContactsByMid(Dmid)
                                    sw.findAndAddContactsByMid(Emid)
                                    sw.findAndAddContactsByMid(Fmid)
                                    sw.findAndAddContactsByMid(Gmid)
                                    sw.findAndAddContactsByMid(Hmid)
                                    sw.findAndAddContactsByMid(Imid)
                                    sw.findAndAddContactsByMid(Jmid)
                                    sw.sendMessage(msg.to,"Success!!!")
                                except:
                                    pass
                                    
                        elif msg.text.lower() == "cek add":
                          if msg._from in Abi:
                          #if msg._from in Creator or msg._from in Owner:  
                            contactlist = cl.getAllContactIds()
                            kontak = cl.getContacts(contactlist)
                            num=1
                            msgs="「 Friend List 」\n"
                            for ids in kontak:
                                msgs+="\n%i. %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n\nTotal Friend : %i" % len(kontak)
                            cl.sendMessage(to, msgs)
                    
                            contactlist = ki.getAllContactIds()
                            kontak = ki.getContacts(contactlist)
                            num=1
                            msgs="「 Friend List 」\n"
                            for ids in kontak:
                                msgs+="\n%i. %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n\nTotal Friend : %i" % len(kontak)
                            ki.sendMessage(to, msgs)
                    
                            contactlist = kk.getAllContactIds()
                            kontak = kk.getContacts(contactlist)
                            num=1
                            msgs="「 Friend List 」\n"
                            for ids in kontak:
                                msgs+="\n%i. %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n\nTotal Friend : %i" % len(kontak)
                            kk.sendMessage(to, msgs)
                    
                            contactlist = kc.getAllContactIds()
                            kontak = kc.getContacts(contactlist)
                            num=1
                            msgs="「 Friend List 」\n"
                            for ids in kontak:
                                msgs+="\n%i. %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n\nTotal Friend : %i" % len(kontak)
                            kc.sendMessage(to, msgs)
                    
                            contactlist = kb.getAllContactIds()
                            kontak = kb.getContacts(contactlist)
                            num=1
                            msgs="「 Friend List 」\n"
                            for ids in kontak:
                                msgs+="\n%i. %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n\nTotal Friend : %i" % len(kontak)
                            kb.sendMessage(to, msgs)
                    
                            contactlist = kd.getAllContactIds()
                            kontak = kd.getContacts(contactlist)
                            num=1
                            msgs="「 Friend List 」\n"
                            for ids in kontak:
                                msgs+="\n%i. %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n\nTotal Friend : %i" % len(kontak)
                            kd.sendMessage(to, msgs)
                    
                            contactlist = ke.getAllContactIds()
                            kontak = ke.getContacts(contactlist)
                            num=1
                            msgs="「 Friend List 」\n"
                            for ids in kontak:
                                msgs+="\n%i. %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n\nTotal Friend : %i" % len(kontak)
                            ke.sendMessage(to, msgs)

                            contactlist = kf.getAllContactIds()
                            kontak = kf.getContacts(contactlist)
                            num=1
                            msgs="「 Friend List 」\n"
                            for ids in kontak:
                                msgs+="\n%i. %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n\nTotal Friend : %i" % len(kontak)
                            kf.sendMessage(to, msgs)
                    
                            contactlist = kg.getAllContactIds()
                            kontak = kg.getContacts(contactlist)
                            num=1
                            msgs="「 Friend List 」\n"
                            for ids in kontak:
                                msgs+="\n%i. %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n\nTotal Friend : %i" % len(kontak)
                            kg.sendMessage(to, msgs)
                    
                            contactlist = kh.getAllContactIds()
                            kontak = kh.getContacts(contactlist)
                            num=1
                            msgs="「 Friend List 」\n"
                            for ids in kontak:
                                msgs+="\n%i. %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n\nTotal Friend : %i" % len(kontak)
                            kh.sendMessage(to, msgs)
                    
                            contactlist = so.getAllContactIds()
                            kontak = so.getContacts(contactlist)
                            num=1
                            msgs="「 Friend List 」\n"
                            for ids in kontak:
                                msgs+="\n%i. %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n\nTotal Friend : %i" % len(kontak)
                            so.sendMessage(to, msgs)
                    
                            contactlist = sw.getAllContactIds()
                            kontak = sw.getContacts(contactlist)
                            num=1
                            msgs="「 Friend List 」\n"
                            for ids in kontak:
                                msgs+="\n%i. %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n\nTotal Friend : %i" % len(kontak)
                            sw.sendMessage(to, msgs)

                        elif cmd == "cek limit":
                            if msg._from in Abi:
                                try:cl.inviteIntoGroup(to, ["uc5abb77929c76b5f91f4beaecd88e5e2"]);has = "OK"
                                except:has = "NOT"
                                try:cl.kickoutFromGroup(to, ["uc5abb77929c76b5f91f4beaecd88e5e2"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "fresh"
                                else:sil = "limit"
                                if has1 == "OK":sil1 = "fresh"
                                else:sil1 = "limit"
                                cl.sendMessage(to, "limit\nKick : {} \nInvite : {}".format(sil1,sil))
                                try:ki.inviteIntoGroup(to, ["u7abc6bc75b34fc0c545fe46c43cff380"]);has = "OK"
                                except:has = "NOT"
                                try:ki.kickoutFromGroup(to, ["u7abc6bc75b34fc0c545fe46c43cff380"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "fresh"
                                else:sil = "limit"
                                if has1 == "OK":sil1 = "fresh"
                                else:sil1 = "limit"
                                ki.sendMessage(to, "limit\nKick : {} \nInvite : {}".format(sil1,sil))
                                try:kk.inviteIntoGroup(to, ["ub4b2144cb807203fe8ab26ee90ea3804"]);has = "OK"
                                except:has = "NOT"
                                try:kk.kickoutFromGroup(to, ["ub4b2144cb807203fe8ab26ee90ea3804"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "fresh"
                                else:sil = "limit"
                                if has1 == "OK":sil1 = "fresh"
                                else:sil1 = "limit"
                                kk.sendMessage(to, "limit\nKick : {} \nInvite : {}".format(sil1,sil))
                                try:kc.inviteIntoGroup(to, ["uae95a5f98fec6ca04407a4fba451662f"]);has = "OK"
                                except:has = "NOT"
                                try:kc.kickoutFromGroup(to, ["uae95a5f98fec6ca04407a4fba451662f"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "fresh"
                                else:sil = "limit"
                                if has1 == "OK":sil1 = "fresh"
                                else:sil1 = "limit"
                                kc.sendMessage(to, "limit\nKick : {} \nInvite : {}".format(sil1,sil))
                                try:kb.inviteIntoGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has = "OK"
                                except:has = "NOT"
                                try:kb.kickoutFromGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "fresh"
                                else:sil = "limit"
                                if has1 == "OK":sil1 = "fresh"
                                else:sil1 = "limit"
                                kb.sendMessage(to, "limit\nKick : {} \nInvite : {}".format(sil1,sil))
                                try:kd.inviteIntoGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has = "OK"
                                except:has = "NOT"
                                try:kd.kickoutFromGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "fresh"
                                else:sil = "limit"
                                if has1 == "OK":sil1 = "fresh"
                                else:sil1 = "limit"
                                kd.sendMessage(to, "limit\nKick : {} \nInvite : {}".format(sil1,sil))
                                try:ke.inviteIntoGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has = "OK"
                                except:has = "NOT"
                                try:ke.kickoutFromGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "fresh"
                                else:sil = "limit"
                                if has1 == "OK":sil1 = "fresh"
                                else:sil1 = "limit"
                                ke.sendMessage(to, "limit\nKick : {} \nInvite : {}".format(sil1,sil))
                                try:kf.inviteIntoGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has = "OK"
                                except:has = "NOT"
                                try:kf.kickoutFromGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "fresh"
                                else:sil = "limit"
                                if has1 == "OK":sil1 = "fresh"
                                else:sil1 = "limit"
                                kf.sendMessage(to, "limit\nKick : {} \nInvite : {}".format(sil1,sil))
                                try:kg.inviteIntoGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has = "OK"
                                except:has = "NOT"
                                try:kg.kickoutFromGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "fresh"
                                else:sil = "limit"
                                if has1 == "OK":sil1 = "fresh"
                                else:sil1 = "limit"
                                kg.sendMessage(to, "limit\nKick : {} \nInvite : {}".format(sil1,sil))
                                try:kh.inviteIntoGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has = "OK"
                                except:has = "NOT"
                                try:kh.kickoutFromGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "fresh"
                                else:sil = "limit"
                                if has1 == "OK":sil1 = "fresh"
                                else:sil1 = "limit"
                                kh.sendMessage(to, "limit\nKick : {} \nInvite : {}".format(sil1,sil))
                                try:so.inviteIntoGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has = "OK"
                                except:has = "NOT"
                                try:so.kickoutFromGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "fresh"
                                else:sil = "limit"
                                if has1 == "OK":sil1 = "fresh"
                                else:sil1 = "limit"
                                so.sendMessage(to, "limit\nKick : {} \nInvite : {}".format(sil1,sil))
                                try:sw.inviteIntoGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has = "OK"
                                except:has = "NOT"
                                try:sw.kickoutFromGroup(to, ["ub1371df988ca044ac372d4ad9d21b22b"]);has1 = "OK"
                                except:has1 = "NOT"
                                if has == "OK":sil = "fresh"
                                else:sil = "limit"
                                if has1 == "OK":sil1 = "fresh"
                                else:sil1 = "limit"
                                sw.sendMessage(to, "limit\nKick : {} \nInvite : {}".format(sil1,sil))
                                
                        elif cmd == "invite":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                try:
                                    anggota = [Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid]
                                    cl.inviteIntoGroup(msg.to, anggota)
                                    ki.acceptGroupInvitation(msg.to)
                                    kk.acceptGroupInvitation(msg.to)
                                    kc.acceptGroupInvitation(msg.to)
                                    kb.acceptGroupInvitation(msg.to)
                                    kd.acceptGroupInvitation(msg.to)
                                    ke.acceptGroupInvitation(msg.to)
                                    kf.acceptGroupInvitation(msg.to)
                                    kg.acceptGroupInvitation(msg.to)
                                    kh.acceptGroupInvitation(msg.to)
                                    cl.sendMessage(msg.to,"Grup"+str(ginfo.name)+"Aman Dari kiker cok")
                                except:
                                    pass
                                    
                        elif cmd == "js stay":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                try:
                                    ginfo = cl.getGroup(msg.to)
                                    cl.inviteIntoGroup(msg.to, [Jmid,Zmid])
                                    cl.sendMessage(msg.to,"Grup"+str(ginfo.name)+"Stay di luar bos")
                                except:
                                    pass 

                        elif cmd == "bos1":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = ki.getGroup(msg.to)
                                    ki.inviteIntoGroup(msg.to, [mid])
                                    cl.sendMessage(msg.to,"Invite bos sukses")
                                except:
                                    pass 
                                    
                        elif cmd == "bos2":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = kk.getGroup(msg.to)
                                    kk.inviteIntoGroup(msg.to, [mid])
                                    kk.sendMessage(msg.to,"Invite bos sukses")
                                except:
                                    pass            
 
                        elif cmd == "bos3":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                try:
                                    ginfo = kk.getGroup(msg.to)
                                    kk.inviteIntoGroup(msg.to, [mid])
                                    kk.sendMessage(msg.to,"Invite bos sukses")
                                except:
                                    pass 
                                    
                        elif cmd == "join":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kf.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kg.acceptGroupInvitationByTicket(msg.to,Ticket)
                                kh.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                cl.updateGroup(G)

                        elif cmd == "out":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                G = cl.getGroup(msg.to)
                                ki.leaveGroup(msg.to)
                                kk.leaveGroup(msg.to)
                                kc.leaveGroup(msg.to)
                                kb.leaveGroup(msg.to)
                                kd.leaveGroup(msg.to)
                                ke.leaveGroup(msg.to)
                                kf.leaveGroup(msg.to)
                                kg.leaveGroup(msg.to)
                                kh.leaveGroup(msg.to)
                                
                        elif cmd == "bye":
                          if wait["selfbot"] == True:
                            if msg._from in creator:
                                G = cl.getGroup(msg.to)
                                cl.sendMessage(msg.to, "ijin lep ya cok,bye"+str(G.name))
                                cl.leaveGroup(msg.to)

                        elif cmd.startswith("leave: "):
                            if msg._from in admin:
                                proses = text.split(" ")
                                ng = text.replace(proses[0] + " ","")
                                gid = cl.getGroupIdsJoined()
                                for i in gid:
                                    h = cl.getGroup(i).name
                                    if h == ng:
                                        ki.sendMessage(i, "dah lah mlz")
                                        ki.leaveGroup(i)
                                        kk.leaveGroup(i)
                                        kc.leaveGroup(i)
                                        kb.leaveGroup(i)
                                        kd.leaveGroup(i)
                                        ke.leaveGroup(i)
                                        kf.leaveGroup(i)
                                        kg.leaveGroup(i)
                                        kh.leaveGroup(i)
                                        cl.sendMessage(to,"dah keluar cok" +h)

                        elif cmd == "m1":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ki.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ki.updateGroup(G)

                        elif cmd == "m2":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kk.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kk.updateGroup(G)

                        elif cmd == "m3":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kc.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kc.updateGroup(G)
                                
                        elif cmd == "m4":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = kb.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                kb.updateGroup(G)
                                
                        elif cmd == "m5":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                kd.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = ke.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                ke.updateGroup(G)

                        elif cmd == "js in":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                ginfo = cl.getGroup(msg.to)
                                G.preventedJoinByTicket = False
                                cl.updateGroup(G)
                                invsend = 0
                                Ticket = cl.reissueGroupTicket(msg.to)
                                so.acceptGroupInvitationByTicket(msg.to,Ticket)
                                sw.acceptGroupInvitationByTicket(msg.to,Ticket)
                                G = sw.getGroup(msg.to)
                                G.preventedJoinByTicket = True
                                sw.updateGroup(G)

                        elif cmd == "js out":
                            if msg._from in admin:
                                G = cl.getGroup(msg.to)
                                so.leaveGroup(msg.to)
                                sw.leaveGroup(msg.to)

                        elif cmd == "sptime":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                get_profile_time_start = time.time()
                                get_profile = cl.getProfile()
                                get_profile_time = time.time() - get_profile_time_start
                                get_group_time_start = time.time()
                                get_group = cl.getGroupIdsJoined()
                                get_group_time = time.time() - get_group_time_start
                                get_contact_time_start = time.time()
                                get_contact = cl.getContact(mid)
                                get_contact_time = time.time() - get_contact_time_start
                                cl.sendMessage(msg.to, "speed respon\n\n - Get Profile\n   %.10f\n - Get Contact\n   %.10f\n - Get Group\n   %.10f" % (get_profile_time/3,get_contact_time/3,get_group_time/3))

                        elif cmd == "sp" or cmd == "sk":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               start = time.time()
                               cl.sendMessage(msg.to, "Progres speed...")
                               elapsed_time = time.time() - start
                               cl.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               ki.sendMessage(msg.to, "Progres speed...")
                               ki.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               kk.sendMessage(msg.to, "Progres speed...")
                               kk.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               kc.sendMessage(msg.to, "Progres speed...")
                               kc.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               kb.sendMessage(msg.to, "Progres speed...")
                               kb.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               kd.sendMessage(msg.to, "Progres speed...")
                               kd.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               ke.sendMessage(msg.to, "Progres speed...")
                               ke.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               kf.sendMessage(msg.to, "Progres speed...")
                               kf.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               kg.sendMessage(msg.to, "Progres speed...")
                               kg.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               kh.sendMessage(msg.to, "Progres speed...")
                               kh.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               so.sendMessage(msg.to, "Progres speed...")
                               so.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))
                               sw.sendMessage(msg.to, "Progres speed...")
                               sw.sendMessage(msg.to, "{} detik".format(str(elapsed_time)))

                        elif cmd == "lurking on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 Setmain['RAreadPoint'][msg.to] = msg_id
                                 Setmain['RAreadMember'][msg.to] = {}
                                 cl.sendMessage(msg.to, "Lurking on\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurking off":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                 tz = pytz.timezone("Asia/Jakarta")
                                 timeNow = datetime.now(tz=tz)
                                 del Setmain['RAreadPoint'][msg.to]
                                 del Setmain['RAreadMember'][msg.to]
                                 cl.sendMessage(msg.to, "Lurking off\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                            
                        elif cmd == "lurkers":
                          if msg._from in admin:
                            if msg.to in Setmain['RAreadPoint']:
                                if Setmain['RAreadMember'][msg.to] != {}:
                                    aa = []
                                    for x in Setmain['RAreadMember'][msg.to]:
                                        aa.append(x)
                                    try:
                                        arrData = ""
                                        textx = "  [ Result {} member ]    \n\n  [ Lurkers ]\n1. ".format(str(len(aa)))
                                        arr = []
                                        no = 1
                                        b = 1
                                        for i in aa:
                                            b = b + 1
                                            end = "\n"
                                            mention = "@x\n"
                                            slen = str(len(textx))
                                            elen = str(len(textx) + len(mention) - 1)
                                            arrData = {'S':slen, 'E':elen, 'M':i}
                                            arr.append(arrData)
                                            tz = pytz.timezone("Asia/Jakarta")
                                            timeNow = datetime.now(tz=tz)
                                            textx += mention
                                            if no < len(aa):
                                                no += 1
                                                textx += str(b) + ". "
                                            else:
                                                try:
                                                    no = "[ {} ]".format(str(cl.getGroup(msg.to).name))
                                                except:
                                                    no = "  "
                                        msg.to = msg.to
                                        msg.text = textx+"\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]"
                                        msg.contentMetadata = {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}
                                        msg.contentType = 0
                                        cl.sendMessage(msg)
                                    except:
                                        pass
                                    try:
                                        del Setmain['RAreadPoint'][msg.to]
                                        del Setmain['RAreadMember'][msg.to]
                                    except:
                                        pass
                                    Setmain['RAreadPoint'][msg.to] = msg.id
                                    Setmain['RAreadMember'][msg.to] = {}
                                else:
                                    cl.sendMessage(msg.to, "User kosong...")
                            else:
                                cl.sendMessage(msg.to, "Ketik lurking on cok")

                        elif cmd == "intip on":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              try:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cl.sendMessage(msg.to, "Cek sider on\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                                  del cctv['point'][msg.to]
                                  del cctv['sidermem'][msg.to]
                                  del cctv['cyduk'][msg.to]
                              except:
                                  pass
                              cctv['point'][msg.to] = msg.id
                              cctv['sidermem'][msg.to] = ""
                              cctv['cyduk'][msg.to]=True

                        elif cmd == "intip off":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              if msg.to in cctv['point']:
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  cctv['cyduk'][msg.to]=False
                                  cl.sendMessage(msg.to, "Cek sider off\n\nTanggal : "+ datetime.strftime(timeNow,'%Y-%m-%d')+"\nJam [ "+ datetime.strftime(timeNow,'%H:%M:%S')+" ]")
                              else:
                                  cl.sendMessage(msg.to, "udah off cok")
                                  
                        elif cmd == "promo":
                          if msg._from in admin:
                             cl.sendMessage(msg.to,"──────┅❇͜͡❇͜͡☆͜͡❇͜͡❇┅──────\nᴼᴾᴱᴺ ᴼᴿᴰᴱᴿ\n────────┅┅───────\n➣ꜱᴇʟꜰʙᴏᴛ ᴏɴʟʏ\n➣ᴄᴏɪɴ ʟɪɴᴇ  / ꜱᴛɪᴄκᴇʀ ᴘᴇʀᴍᴀɴᴇɴ\n➣ꜱᴇᴡᴀ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ / ꜱᴇʟꜰʙᴏᴛ / ᴛᴇᴍᴘʟᴀᴛᴇ\n➣ɴᴇᴡ ꜱᴄʀɪᴘᴛ ꜱʙ / ᴛᴇᴍᴘʟᴀᴛᴇ\n➣ɴᴇᴡ vᴘꜱ ɢᴄʟᴏᴜᴰ jᴀᴘᴀɴ\n➣ᴍᴇɴᴇʀɪᴍᴀ ʙᴇʟᴀjᴀʀ ʙᴏᴛ\n➣ꜱᴏɴɢʙᴏᴏκ\n➣ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ ʀᴏᴏᴍ ꜱᴍᴜʟᴇ\n➣ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ ʀᴏᴏᴍ ᴇvᴇɴᴛ\n➣ᴏʀᴅᴇʀ & ʜᴀʀɢᴀ\n─────────┅┅─────────\n  ʟᴀɴɢꜱᴜɴɢ κʟɪκ ᴡᴀʀɴᴀ ʙɪʀᴜ\nline.me/ti/p/~sadis101\n➣ѕєʟғвот κɪcκєʀ_+_ᴘʀᴏᴛᴇᴄᴛ\n────────┅❇͜͡❇͜͡☆͜͡❇͜͡❇┅────────")
                             msg.contentType = 13
                             msg.contentMetadata = {'mid': admin}
                             tanya = msg.text.replace("promo ","")
                             jawab = ("──────┅❇͜͡❇͜͡☆͜͡❇͜͡❇┅──────\nᴼᴾᴱᴺ ᴼᴿᴰᴱᴿ\n────────┅┅───────\n➣ꜱᴇʟꜰʙᴏᴛ ᴏɴʟʏ\n➣ᴄᴏɪɴ ʟɪɴᴇ  / ꜱᴛɪᴄκᴇʀ ᴘᴇʀᴍᴀɴᴇɴ\n➣ꜱᴇᴡᴀ ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ / ꜱᴇʟꜰʙᴏᴛ / ᴛᴇᴍᴘʟᴀᴛᴇ\n➣ɴᴇᴡ ꜱᴄʀɪᴘᴛ ꜱʙ / ᴛᴇᴍᴘʟᴀᴛᴇ\n➣ɴᴇᴡ vᴘꜱ ɢᴄʟᴏᴜᴰ Jᴀᴘᴀɴ\n➣ᴍᴇɴᴇʀɪᴍᴀ ʙᴇʟᴀjᴀʀ ʙᴏᴛ\n➣ꜱᴏɴɢʙᴏᴏκ\n➣ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ ʀᴏᴏᴍ ꜱᴍᴜʟᴇ\n➣ʙᴏᴛ ᴘʀᴏᴛᴇᴄᴛ ʀᴏᴏᴍ ᴇvᴇɴᴛ\n➣ᴏʀᴅᴇʀ & ʜᴀʀɢᴀ\n─────────┅┅─────────\n  ʟᴀɴɢꜱᴜɴɢ κʟɪκ ᴡᴀʀɴᴀ ʙɪʀᴜ\nline.me/ti/p/~sadis101\n➣ѕєʟғвот κɪcκєʀ_+_ᴘʀᴏᴛᴇᴄᴛ\n────────┅❇͜͡❇͜͡☆͜͡❇͜͡❇┅────────")
                             jawaban = random.choice(jawab)
                             tts = gTTS(text=jawaban, lang='pm id line ya')
                             tts.save('tts.mp3')
                             cl.sendAudio(msg.to,'tts.mp3')
                             cl.sendMessage(msg)         
                             cl.sendMessage(msg.to,"Jika Berminat Langsung Hubungi Kami Ya Trima Kasih😊😊")       
#===========Hiburan============#
                        elif cmd.startswith("sholat: "):
                          if msg._from in admin:
                             sep = text.split(" ")
                             location = text.replace(sep[0] + " ","")
                             with requests.session() as web:
                                  web.headers["user-agent"] = random.choice(settings["userAgent"])
                                  r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                                  data = r.text
                                  data = json.loads(data)
                                  tz = pytz.timezone("Asia/Jakarta")
                                  timeNow = datetime.now(tz=tz)
                                  if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isha : ":
                                         ret_ = "「Jadwal Sholat」"
                                         ret_ += "\n Lokasi : " + data[0]
                                         ret_ += "\n " + data[1]
                                         ret_ += "\n " + data[2]
                                         ret_ += "\n " + data[3]
                                         ret_ += "\n " + data[4]
                                         ret_ += "\n " + data[5]
                                         ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                         ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                  cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("cuaca: "):
                          if msg._from in admin:
                            separate = text.split(" ")
                            location = text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if "result" not in data:
                                    ret_ = "「Status Cuaca」"
                                    ret_ += "\n Lokasi : " + data[0].replace("Temperatur di kota ","")
                                    ret_ += "\n Suhu : " + data[1].replace("Suhu : ","") + " C"
                                    ret_ += "\n Kelembaban : " + data[2].replace("Kelembaban : ","") + " %"
                                    ret_ += "\n Tekanan udara : " + data[3].replace("Tekanan udara : ","") + " HPa"
                                    ret_ += "\n Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + " m/s"
                                    ret_ += "\n\nTanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\nJam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                cl.sendMessage(msg.to, str(ret_))

                        elif cmd.startswith("lokasi: "):
                          if msg._from in admin:
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if data[0] != "" and data[1] != "" and data[2] != "":
                                    link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                    ret_ = "「Info Lokasi」"
                                    ret_ += "\n Location : " + data[0]
                                    ret_ += "\n Google Maps : " + link
                                else:
                                    ret_ = "[Details Location] Error : Location not found"
                                cl.sendMessage(msg.to,str(ret_))

                        elif cmd.startswith("?"):
                           if msg._from in admin:
                               try:
                                   txt = text.replace('?','').split(' ')
                                   btype,ttype = random.choice([1,2,3,4,5]),random.choice([1,2,3,4])
                                   path = 'http://corrykalam.gq/retrowave.php?'
                                   if len(txt) == 1:
                                       params = {'text1': txt[0],'text2': '','text3': '','btype': str(btype),'ttype': str(ttype)}
                                   elif len(txt) == 2:
                                       params = {'text1': txt[0],'text2': txt[1],'text3': '','btype': str(btype),'ttype': str(ttype)}
                                   elif len(txt) == 3:
                                       params = {'text1': txt[0],'text2': txt[1],'text3': txt[2],'btype': str(btype),'ttype': str(ttype)}
                                   data = requests.get(path, params=params).json()
                                   cl.sendImageWithURL(receiver, data['image'])
                               except Exception as e:
                                   cl.sendMessage(receiver, str(e))

                        elif cmd.startswith("lirik: "):
                           if msg._from in admin:
                               sep = msg.text.split(" ")
                               search = msg.text.replace(sep[0] + " ","")
                               params = {'songname': search}
                               with requests.session() as web:
                                   web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                   r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                   try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          songs = song[5]
                                          lyric = songs.replace('ti:','Title - ')
                                          lyric = lyric.replace('ar:','Artist - ')
                                          lyric = lyric.replace('al:','Album - ')
                                          removeString = "[1234567890.:]"
                                          for char in removeString:
                                              lyric = lyric.replace(char,'')
                                          ret_ = "[ Lyric ]"
                                          ret_ += "\n Nama lagu : {}".format(str(song[0]))
                                          ret_ += "\n Durasi : {}".format(str(song[1]))
                                          ret_ += "\n Link : {}".format(str(song[3]))
                                          ret_ += "\n[ Finish ]\n\nLirik nya :\n{}".format(str(lyric))
                                          cl.sendMessage(msg.to, str(ret_))
                                   except:
                                       cl.sendMessage(to, "Lirik ga ketemu cok")
                            
                        elif cmd.startswith("music: "):
                           if msg._from in admin:
                              sep = msg.text.split(" ")
                              search = msg.text.replace(sep[0] + " ","")
                              params = {'songname': search}
                              with requests.session() as web:
                                  web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                  r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?{}".format(urllib.parse.urlencode(params)))
                                  try:
                                      data = json.loads(r.text)
                                      for song in data:
                                          ret_ = "[ Music ]"
                                          ret_ += "\n Nama lagu : {}".format(str(song[0]))
                                          ret_ += "\n Durasi : {}".format(str(song[1]))
                                          ret_ += "\n Link : {}".format(str(song[3]))
                                          ret_ += "\n[ Waiting Audio ]"
                                      cl.sendMessage(msg.to, str(ret_))
                                      cl.sendMessage(msg.to, "sabar asw")
                                      cl.sendAudioWithURL(msg.to, song[3])
                                  except:
                                      cl.sendMessage(to, "Musik ga ketemu cok")

                        elif cmd.startswith("gimage: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            search = msg.text.replace(sep[0] + " ","")
                            url = "https://api.xeonwz.ga/api/image/google?q={}".format(urllib.parse.quote(search))
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get(url)
                                data = r.text
                                data = json.loads(data)
                                if data["data"] != []:
                                    start = timeit.timeit()
                                    items = data["data"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    cl.sendMessage(msg.to,"「Google Image」\nType : Search Image\nTime taken : %seconds" % (start))
                                    cl.sendImageWithURL(msg.to, str(path))

                        elif cmd.startswith("ytmp4: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                textToSearch = msg.text.replace(sep[0] + " ","")
                                query = urllib.parse.quote(textToSearch)
                                search_url="https://www.youtube.com/results?search_query="
                                mozhdr = {'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.9.0.3) Gecko/2008092417 Firefox/3.0.3'}
                                sb_url = search_url + query
                                sb_get = requests.get(sb_url, headers = mozhdr)
                                soupeddata = BeautifulSoup(sb_get.content, "html.parser")
                                yt_links = soupeddata.find_all("a", class_ = "yt-uix-tile-link")
                                x = (yt_links[1])
                                yt_href =  x.get("href")
                                yt_href = yt_href.replace("watch?v=", "")
                                qx = "https://youtu.be" + str(yt_href)
                                vid = pafy.new(qx)
                                stream = vid.streams
                                best = vid.getbest()
                                best.resolution, best.extension
                                for s in stream:
                                    me = best.url
                                    hasil = ""
                                    title = "Judul [ " + vid.title + " ]"
                                    author = '\n\n Author : ' + str(vid.author)
                                    durasi = '\n Duration : ' + str(vid.duration)
                                    suka = '\n Likes : ' + str(vid.likes)
                                    rating = '\n Rating : ' + str(vid.rating)
                                    deskripsi = '\n Deskripsi : ' + str(vid.description)
                                cl.sendVideoWithURL(msg.to, me)
                                cl.sendMessage(msg.to,title+ author+ durasi+ suka+ rating+ deskripsi)
                            except Exception as e:
                                cl.sendMessage(msg.to,str(e))

                        elif cmd.startswith("abi: "):
                          if msg._from in admin:
                            try:
                                proses = text.split(" ")
                                urutan = text.replace(proses[0] + " ","")
                                r = requests.get("http://api.zicor.ooo/joox.php?song={}".format(str(urllib.parse.quote(urutan))))
                                data = r.text
                                data = json.loads(data)
                                b = data
                                c = str(b["title"])
                                d = str(b["singer"])
                                e = str(b["url"])
                                g = str(b["image"])
                                hasil = "Penyanyi: "+str(d)
                                hasil += "\nJudul : "+str(c)
                                cl.sendImageWithURL(to,g)
                                cl.sendAudioWithURL(to,e)
                                cl.sendMessage(msg.to,hasil)
                            except Exception as error:
                                 cl.sendMessage(to, "error\n" + str(error))

                        elif cmd.startswith("profileig: "):
                          if msg._from in admin:
                            try:
                                sep = msg.text.split(" ")
                                instagram = msg.text.replace(sep[0] + " ","")
                                response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                                data = response.json()
                                namaIG = str(data['user']['full_name'])
                                bioIG = str(data['user']['biography'])
                                mediaIG = str(data['user']['media']['count'])
                                verifIG = str(data['user']['is_verified'])
                                usernameIG = str(data['user']['username'])
                                followerIG = str(data['user']['followed_by']['count'])
                                profileIG = data['user']['profile_pic_url_hd']
                                privateIG = str(data['user']['is_private'])
                                followIG = str(data['user']['follows']['count'])
                                link = "✒ Link : " + "https://www.instagram.com/" + instagram
                                text = "✒ Name : "+namaIG+"\n Username : "+usernameIG+"\n Biography : "+bioIG+"\n Follower : "+followerIG+"\n Following : "+followIG+"\n Post : "+mediaIG+"\n Verified : "+verifIG+"\n Private : "+privateIG+"" "\n" + link
                                cl.sendImageWithURL(msg.to, profileIG)
                                cl.sendMessage(msg.to, str(text))
                            except Exception as e:
                                    cl.sendMessage(msg.to, str(e))

                        elif cmd.startswith("cekdate: "):
                          if msg._from in admin:
                            sep = msg.text.split(" ")
                            tanggal = msg.text.replace(sep[0] + " ","")
                            r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                            data=r.text
                            data=json.loads(data)
                            lahir = data["data"]["lahir"]
                            usia = data["data"]["usia"]
                            ultah = data["data"]["ultah"]
                            zodiak = data["data"]["zodiak"]
                            cl.sendMessage(msg.to,"⚫ I N F O R M A S I ⚫\n\n"+" Date Of Birth : "+lahir+"\n Age : "+usia+"\n Ultah : "+ultah+"\n Zodiak : "+zodiak)

                        elif cmd.startswith("spamtag: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                Setmain["RAlimit"] = num
                                cl.sendText(msg.to,"「 Status Spamtag 」\nBerhasil diubah jadi {} kali".format(str(strnum)))

                        elif cmd.startswith("spamcall: "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                proses = text.split(":")
                                strnum = text.replace(proses[0] + ":","")
                                num =  int(strnum)
                                wait["limit"] = num
                                cl.sendMessage(msg.to,"Total Spamcall Diubah Menjadi " +strnum)

                        elif cmd.startswith("spamtag "):
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                                if 'MENTION' in msg.contentMetadata.keys()!=None:
                                    key = eval(msg.contentMetadata["MENTION"])
                                    key1 = key["MENTIONEES"][0]["M"]
                                    zx = ""
                                    zxc = " "
                                    zx2 = []
                                    pesan2 = "@a"" "
                                    xlen = str(len(zxc))
                                    xlen2 = str(len(zxc)+len(pesan2)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':key1}
                                    zx2.append(zx)
                                    zxc += pesan2
                                    msg.contentType = 0
                                    msg.text = zxc
                                    lol = {'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                                    msg.contentMetadata = lol
                                    jmlh = int(Setmain["RAlimit"])
                                    if jmlh <= 1000:
                                        for x in range(jmlh):
                                            try:
                                                cl.sendMessage1(msg)
                                            except Exception as e:
                                                cl.sendText(msg.to,str(e))
                                    else:
                                        cl.sendText(msg.to,"Jumlah melebihi 1000")
                                        
                        elif cmd == "spamcall":
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                             if msg.toType == 2:
                                group = cl.getGroup(to)
                                members = [mem.mid for mem in group.members]
                                jmlh = int(wait["limit"])
                                cl.sendMessage(msg.to, "Berhasil mengundang {} undangan Call Grup".format(str(wait["limit"])))
                                if jmlh <= 100000:
                                  for x in range(jmlh):
                                     try:
                                        cl.acquireGroupCallRoute(to)
                                        cl.inviteIntoGroupCall(to, contactIds=members)
                                     except Exception as e:
                                        cl.sendMessage(msg.to,str(e))
                                else:
                                    cl.sendMessage(msg.to,"Jumlah melebihi batas")

                        elif 'Gift: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Gift: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 100000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      ki.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kk.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kc.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kb.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kd.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      ke.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kf.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kg.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      kh.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      so.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      sw.sendMessage(midd, None, contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58', 'PRDTYPE': 'THEME', 'MSGTPL': '6'}, contentType=9)
                                      cl.sendMessage(msg.to, "tuh gip buat lu")

                        elif 'Spam: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              korban = msg.text.replace('Spam: ','')
                              korban2 = korban.split()
                              midd = korban2[0]
                              jumlah = int(korban2[1])
                              if jumlah <= 100000:
                                  for var in range(0,jumlah):
                                      cl.sendMessage(midd, str(Setmain["RAmessage1"]))
                                      ki.sendMessage(midd, str(Setmain["RAmessage1"]))
                                      kk.sendMessage(midd, str(Setmain["RAmessage1"]))
                                      kc.sendMessage(midd, str(Setmain["RAmessage1"]))
                                      kb.sendMessage(midd, str(Setmain["RAmessage1"]))
                                      kd.sendMessage(midd, str(Setmain["RAmessage1"]))
                                      kesendMessage(midd, str(Setmain["RAmessage1"]))
                                      kf.sendMessage(midd, str(Setmain["RAmessage1"]))
                                      kg.sendMessage(midd, str(Setmain["RAmessage1"]))
                                      kh.sendMessage(midd, str(Setmain["RAmessage1"]))
                                      so.sendMessage(midd, str(Setmain["RAmessage1"]))
                                      sw.sendMessage(midd, str(Setmain["RAmessage1"]))
                                      
                        elif 'ID line: ' in msg.text:
                          if wait["selfbot"] == True:
                           if msg._from in admin:
                              msgs = msg.text.replace('ID line: ','')
                              conn = cl.findContactsByUserid(msgs)
                              if True:
                                  cl.sendMessage(msg.to, "http://line.me/ti/p/~" + msgs)
                                  cl.sendMessage(msg.to, None, contentMetadata={'mid': conn.mid}, contentType=13)

#===========Protection============#
                        elif 'Welcome ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Welcome ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Welcome on"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Welcome on\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Diaktifkan\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Welcome off\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Welcome off"
                                    cl.sendMessage(msg.to, "Dinonaktifkan\n" + msgs)
                                    
                        elif 'Left ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Left ','')
                              if spl == 'on':
                                  if msg.to in welcome:
                                       msgs = "Left on"
                                  else:
                                       welcome.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Left on\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Diaktifkan\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in welcome:
                                         welcome.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Left off\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Left off"
                                    cl.sendMessage(msg.to, "Dinonaktifkan\n" + msgs)
                                    
                        elif 'Proqr ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Proqr ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = "Protect url on"
                                  else:
                                       protectqr.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect url on\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Diaktifkan\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect url off\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect url off"
                                    cl.sendMessage(msg.to, "Dinonaktifkan\n" + msgs)

                        elif 'Prokick ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Prokick ','')
                              if spl == 'on':
                                  if msg.to in protectkick:
                                       msgs = "Protect kick on"
                                  else:
                                       protectkick.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect kick on\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Diaktifkan\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect kick off\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect kick off"
                                    cl.sendMessage(msg.to, "Dinonaktifkan\n" + msgs)
                                    
                        elif 'Proinvite ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Proinvite ','')
                              if spl == 'on':
                                  if msg.to in protectinvite:
                                       msgs = "Protect invite on"
                                  else:
                                       protectinvite.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect invite on\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Diaktifkan\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect invite off\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect invite off"
                                    cl.sendMessage(msg.to, "Dinonaktifkan\n" + msgs)           

                        elif 'Projoin ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Projoin ','')
                              if spl == 'on':
                                  if msg.to in protectjoin:
                                       msgs = "Protect join on"
                                  else:
                                       protectjoin.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect join on\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Diaktifkan\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect join off\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect join off"
                                    cl.sendMessage(msg.to, "Dinonaktifkan\n" + msgs)

                        elif 'Procancel ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Procancel ','')
                              if spl == 'on':
                                  if msg.to in protectcancel:
                                       msgs = "Protect cancel on"
                                  else:
                                       protectcancel.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Protect cancel on\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Diaktifkan\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Protect cancel off\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Protect cancel off"
                                    cl.sendMessage(msg.to, "Dinonaktifkan\n" + msgs)
                                    
                        elif 'Js ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Js ','')
                              if spl == 'on':
                                  if msg.to in protectantijs:
                                       msgs = "Anti JS on"
                                  else:
                                       protectantijs.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Anti JS on\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Diaktifkan\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectantijs:
                                         protectantijs.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Anti JS off\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Anti JS off"
                                    cl.sendMessage(msg.to, "Dinonaktifkan\n" + msgs)
                                    
                        elif 'Ghost ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Ghost ','')
                              if spl == 'on':
                                  if msg.to in ghost:
                                       msgs = "Ghost on"
                                  else:
                                       ghost.append(msg.to)
                                       ginfo = cl.getGroup(msg.to)
                                       msgs = "Ghost on\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Diaktifkan\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in ghost:
                                         ghost.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Ghost off\nDi Group : " +str(ginfo.name)
                                    else:
                                         msgs = "Ghost off"
                                    cl.sendMessage(msg.to, "Dinonaktifkan\n" + msgs)
                                    
                        elif 'Allpro ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Allpro ','')
                              if spl == 'on':
                                  if msg.to in protectqr:
                                       msgs = ""
                                  else:
                                       protectqr.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                  	protectinvite.append(msg.to)
                                  if msg.to in protectkick:
                                      msgs = ""
                                  else:
                                      protectkick.append(msg.to)
                                  if msg.to in protectjoin:
                                      msgs = ""
                                  else:
                                      protectjoin.append(msg.to)
                                  if msg.to in protectcancel:
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Semua protect sudah on\nDi Group : " +str(ginfo.name)
                                  else:
                                      protectcancel.append(msg.to)
                                      ginfo = cl.getGroup(msg.to)
                                      msgs = "Berhasil mengaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                  cl.sendMessage(msg.to, "Diaktifkan\n" + msgs)
                              elif spl == 'off':
                                    if msg.to in protectqr:
                                         protectqr.remove(msg.to)
                                    else:
                                    	msgs = ""
                                    if msg.to in protectinvite:
                                         protectinvite.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectkick:
                                         protectkick.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectjoin:
                                         protectjoin.remove(msg.to)
                                    else:
                                         msgs = ""
                                    if msg.to in protectcancel:
                                         protectcancel.remove(msg.to)
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Berhasil menonaktifkan semua protect\nDi Group : " +str(ginfo.name)
                                    else:
                                         ginfo = cl.getGroup(msg.to)
                                         msgs = "Semua protect sudah off\nDi Group : " +str(ginfo.name)
                                    cl.sendMessage(msg.to, "Dinonaktifkan\n" + msgs)

#===========KICKOUT============#
                        elif ("Cipok " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Abi:
                                       try:
                                           G = cl.getGroup(msg.to)
                                           G.preventedJoinByTicket = False
                                           cl.updateGroup(G)
                                           invsend = 0
                                           Ticket = cl.reissueGroupTicket(msg.to)
                                           so.acceptGroupInvitationByTicket(msg.to,Ticket)
                                           so.kickoutFromGroup(msg.to, [target])
                                           so.leaveGroup(msg.to)
                                           X = cl.getGroup(msg.to)
                                           X.preventedJoinByTicket = True
                                           cl.updateGroup(X)
                                       except:
                                           pass
                                           
                        elif "Cleanse" in msg.text:
                           if msg._from in Abi:
                            if msg.toType == 2:
                             #  print "Otw cleanse"
                               _name = msg.text.replace("Cleanse","")
                               gs = cl.getGroup(msg.to)
                               gs = ki.getGroup(msg.to)
                               gs = kk.getGroup(msg.to)
                               gs = kc.getGroup(msg.to) 
                               gs = kb.getGroup(msg.to)
                               gs = kd.getGroup(msg.to)
                               gs = ke.getGroup(msg.to)
                               gs = kf.getGroup(msg.to)
                               gs = kg.getGroup(msg.to) 
                               gs = kh.getGroup(msg.to)
                               ki.sendMessage(msg.to,"yaudah iya")
                               targets = []
                               for g in gs.members:
                                   if _name in g.displayName:
                                       targets.append(g.mid)
                               if targets == []:
                                  ki.sendMessage(msg.to,"Not found")
                              #    else:
                               for target in targets:
                                     if target not in Abi:
                                      try:
                                          klist=[cl,ki,kk,kc,kb,kd,ke,kf,kg,kh]
                                          kicker=random.choice(klist)
                                          kicker.kickoutFromGroup(msg.to,[target])
                                          print (msg.to,[g.mid])
                                      except:
                                          ki.sendMessage(msg.to,"maap ya :(")
                                          
                        elif ("Abi " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Abi:
                                       try:
                                           cl.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass
                                           
                        elif ("Abi1 " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Abi:
                                       try:
                                           ki.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass
                                           
                        elif ("Abi2 " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Abi:
                                       try:
                                           kk.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass
                                           
                        elif ("Abi3 " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Abi:
                                       try:
                                           kc.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass

                        elif ("Abi4 " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Abi:
                                       try:
                                           kb.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass
                                           
                        elif ("Abi5 " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Abi:
                                       try:
                                           kd.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass
                                           
                        elif ("Abi6 " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Abi:
                                       try:
                                           ke.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass
                                           
                        elif ("Abi7 " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Abi:
                                       try:
                                           kf.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass 

                        elif ("Abi8 " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Abi:
                                       try:
                                           kg.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass
                                           
                        elif ("Abi9 " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Abi:
                                       try:
                                           kh.kickoutFromGroup(msg.to, [target])
                                       except:
                                           pass         
                                                   
#===========ADMIN ADD============#
                        elif ("Adminadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           admin.append(target)
                                           cl.sendMessage(msg.to,"Berhasil menambahkan admin")
                                       except:
                                           pass

                        elif ("Staffadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           staff.append(target)
                                           cl.sendMessage(msg.to,"Berhasil menambahkan staff")
                                       except:
                                           pass

                        elif ("Botadd " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           Abi.append(target)
                                           cl.sendMessage(msg.to,"Berhasil menambahkan bot")
                                       except:
                                           pass

                        elif ("Admindell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Oleng:
                                       try:
                                           admin.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Staffdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Oleng:
                                       try:
                                           staff.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif ("Botdell " in msg.text):
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                   if target not in Oleng:
                                       try:
                                           Abi.remove(target)
                                           cl.sendMessage(msg.to,"Berhasil menghapus admin")
                                       except:
                                           pass

                        elif cmd == "admin:on" or text.lower() == 'admin:on':
                            if msg._from in admin:
                                wait["addadmin"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "admin:repeat" or text.lower() == 'admin:repeat':
                            if msg._from in admin:
                                wait["delladmin"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "staff:on" or text.lower() == 'staff:on':
                            if msg._from in admin:
                                wait["addstaff"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "staff:repeat" or text.lower() == 'staff:repeat':
                            if msg._from in admin:
                                wait["dellstaff"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "bot:on" or text.lower() == 'bot:on':
                            if msg._from in admin:
                                wait["addbots"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "bot:repeat" or text.lower() == 'bot:repeat':
                            if msg._from in admin:
                                wait["dellbots"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "refresh" or text.lower() == 'refresh':
                            if msg._from in admin:
                                wait["addadmin"] = False
                                wait["delladmin"] = False
                                wait["addstaff"] = False
                                wait["dellstaff"] = False
                                wait["addbots"] = False
                                wait["dellbots"] = False
                                wait["wblacklist"] = False
                                wait["dblacklist"] = False
                                wait["Talkwblacklist"] = False
                                wait["Talkdblacklist"] = False
                                cl.sendMessage(msg.to,"Berhasil di Refresh...")

                        elif cmd == "myadmin" or text.lower() == 'contact admin':
                            if msg._from in admin:
                                ma = ""
                                for i in admin:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "mystaff" or text.lower() == 'contact staff':
                            if msg._from in admin:
                                ma = ""
                                for i in staff:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "mybot" or text.lower() == 'mybojo':
                            if msg._from in admin:
                                ma = ""
                                for i in Abi:
                                    ma = cl.getContact(i)
                                    cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

#===========COMMAND ON OFF============#
                        elif cmd == "spaminvite on":
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                settings["SpamInvite"] = True
                                cl.sendMessage(msg.to,"Send Contact to spam grup..")

                        elif cmd == "spaminvite off":
                          if wait["selfbot"] == False:
                            if msg._from in admin:
                                settings["SpamInvite"] = False
                                cl.sendMessage(msg.to,"Send Contact to send grup Off..")

                        elif cmd == "unsend on" or text.lower() == 'unsend on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["unsend"] = True
                                sendMention(msg.to, sender, " Status Unsend \nUser ", "\nSilahkan unsend pesannya,\nKetik unsend off jika sudah slesai")

                        elif cmd == "unsend off" or text.lower() == 'unsend off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["unsend"] = False
                                sendMention(msg.to, sender, " Status Unsend \nUser ", " \nDeteksi unsend dinonaktifkan")

                        elif cmd == "timeline on" or text.lower() == 'timeline on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Timeline"] = True
                                sendMention(msg.to, sender, " Status Timeline \nUser ", "\nSilahkan kirim postingannya,\nKetik timeline off jika sudah slesai")

                        elif cmd == "timeline off" or text.lower() == 'timeline off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Timeline"] = False
                                sendMention(msg.to, sender, " Status Timeline \nUser ", " \nDeteksi timeline dinonaktifkan")
                                
                        elif cmd == "invite on" or text.lower() == 'invite on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = True
                                sendMention(msg.to, sender, " Status Invite \nUser ", "\nSilahkan kirim kontaknya,\nKetik invite off jika sudah slesai")

                        elif cmd == "invite off" or text.lower() == 'invite off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["invite"] = False
                                sendMention(msg.to, sender, " Status Invite \nUser ", " \nInvite via contact dinonaktifkan")
                                
                        elif cmd == "notag on" or text.lower() == 'notag on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Mentionkick"] = True
                                cl.sendMessage(msg.to,"Notag diaktifkan")

                        elif cmd == "notag off" or text.lower() == 'notag off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["MentionKick"] = False
                                cl.sendMessage(msg.to,"Notag dinonaktifkan")

                        elif cmd == "contact on" or text.lower() == 'contact on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = True
                                cl.sendMessage(msg.to,"Deteksi contact diaktifkan")

                        elif cmd == "contact off" or text.lower() == 'contact off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["contact"] = False
                                cl.sendMessage(msg.to,"Deteksi contact dinonaktifkan")

                        elif cmd == "respon on" or text.lower() == 'respon on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = True
                                cl.sendMessage(msg.to,"Auto respon diaktifkan")

                        elif cmd == "respon off" or text.lower() == 'respon off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["detectMention"] = False
                                cl.sendMessage(msg.to,"Auto respon dinonaktifkan")
                                
                        elif cmd == "talkban on" or text.lower() == 'talkban on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["talkban"] = True
                                cl.sendMessage(msg.to,"Talk Ban diaktifkan")

                        elif cmd == "talkban off" or text.lower() == 'talkban off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["talkban"] = False
                                cl.sendMessage(msg.to,"Talk Ban dinonaktifkan")

                        elif cmd == "autojoin on" or text.lower() == 'autojoin on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = True
                                cl.sendMessage(msg.to,"Autojoin diaktifkan")

                        elif cmd == "autojoin off" or text.lower() == 'autojoin off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoin"] = False
                                cl.sendMessage(msg.to,"Autojoin dinonaktifkan")

                        elif cmd == "autoleave on" or text.lower() == 'autoleave on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = True
                                cl.sendMessage(msg.to,"Autoleave diaktifkan")

                        elif cmd == "autoleave off" or text.lower() == 'autoleave off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoLeave"] = False
                                cl.sendMessage(msg.to,"Autoleave dinonaktifkan")

                        elif cmd == "autoadd on" or text.lower() == 'autoadd on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = True
                                cl.sendMessage(msg.to,"Auto add diaktifkan")

                        elif cmd == "autoadd off" or text.lower() == 'autoadd off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoAdd"] = False
                                cl.sendMessage(msg.to,"Auto add dinonaktifkan")

                        elif cmd == "sticker on" or text.lower() == 'sticker on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = True
                                cl.sendMessage(msg.to,"Deteksi sticker diaktifkan")

                        elif cmd == "sticker off" or text.lower() == 'sticker off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["sticker"] = False
                                cl.sendMessage(msg.to,"Deteksi sticker dinonaktifkan")

                        elif cmd == "jointicket on" or text.lower() == 'jointicket on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = True
                                cl.sendMessage(msg.to,"Join ticket diaktifkan")

                        elif cmd == "jointicket off" or text.lower() == 'jointicket off':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["autoJoinTicket"] = False
                                cl.sendMessage(msg.to,"Notag dinonaktifkan")

#===========COMMAND BLACKLIST============#
                        elif ("Talkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["Talkblacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Untalkban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["Talkblacklist"][target]
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "talkban:on" or text.lower() == 'talkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkwblacklist"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "untalkban:on" or text.lower() == 'untalkban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["Talkdblacklist"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif ("Ban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           wait["blacklist"][target] = True
                                           cl.sendMessage(msg.to,"Berhasil menambahkan blacklist")
                                       except:
                                           pass

                        elif ("Unban " in msg.text):
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                               key = eval(msg.contentMetadata["MENTION"])
                               key["MENTIONEES"][0]["M"]
                               targets = []
                               for x in key["MENTIONEES"]:
                                    targets.append(x["M"])
                               for target in targets:
                                       try:
                                           del wait["blacklist"][target]
                                           cl.sendMessage(msg.to,"Berhasil menghapus blacklist")
                                       except:
                                           pass

                        elif cmd == "ban:on" or text.lower() == 'ban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["wblacklist"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "unban:on" or text.lower() == 'unban:on':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                                wait["dblacklist"] = True
                                cl.sendMessage(msg.to,"Please send to contact...")

                        elif cmd == "banlist" or text.lower() == 'banlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["blacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"✒ Blacklist User\n\n"+ma+"\nTotal「%s」Blacklist User" %(str(len(wait["blacklist"]))))

                        elif cmd == "talkbanlist" or text.lower() == 'talkbanlist':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["Talkblacklist"] == {}:
                                cl.sendMessage(msg.to,"Tidak ada Talkban user")
                              else:
                                ma = ""
                                a = 0
                                for m_id in wait["Talkblacklist"]:
                                    a = a + 1
                                    end = '\n'
                                    ma += str(a) + ". " +cl.getContact(m_id).displayName + "\n"
                                cl.sendMessage(msg.to,"✒ Talkban User\n\n"+ma+"\nTotal「%s」Talkban User" %(str(len(wait["Talkblacklist"]))))

                        elif cmd == "buron" or text.lower() == 'blc':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if wait["blacklist"] == {}:
                                    cl.sendMessage(msg.to,"Tidak ada blacklist")
                                    ki.sendMessage(msg.to,"Tidak ada blacklist")
                                    kk.sendMessage(msg.to,"Tidak ada blacklist")
                                    kc.sendMessage(msg.to,"Tidak ada blacklist")
                                    kb.sendMessage(msg.to,"Tidak ada blacklist")
                                    kd.sendMessage(msg.to,"Tidak ada blacklist")
                                    ke.sendMessage(msg.to,"Tidak ada blacklist")
                                    kf.sendMessage(msg.to,"Tidak ada blacklist")
                                    kg.sendMessage(msg.to,"Tidak ada blacklist")
                                    kh.sendMessage(msg.to,"Tidak ada blacklist")
                              else:
                                    ma = ""
                                    for i in wait["blacklist"]:
                                        ma = cl.getContact(i)
                                        cl.sendMessage(msg.to, None, contentMetadata={'mid': i}, contentType=13)

                        elif cmd == "clearban" or text.lower() == 'clearban':
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              wait["blacklist"] = {}
                              ragets = cl.getContacts(wait["blacklist"])
                              mc = "「%i」User Blacklist" % len(ragets)
                              cl.sendMessage(msg.to,"Sukses membersihkan " +mc)
                              ki.sendMessage(msg.to,"Sukses membersihkan " +mc)
                              kk.sendMessage(msg.to,"Sukses membersihkan " +mc)
                              kc.sendMessage(msg.to,"Sukses membersihkan " +mc)
                              kb.sendMessage(msg.to,"Sukses membersihkan " +mc)
                              kd.sendMessage(msg.to,"Sukses membersihkan " +mc)
                              ke.sendMessage(msg.to,"Sukses membersihkan " +mc)
                              kf.sendMessage(msg.to,"Sukses membersihkan " +mc)
                              kg.sendMessage(msg.to,"Sukses membersihkan " +mc)
                              kh.sendMessage(msg.to,"Sukses membersihkan " +mc)
                              cl.sendMessage(msg.to,"Sukses membersihkan buron")
                                 
#===========COMMAND SET============#
                        elif 'Set pesan: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set pesan: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Pesan Msg")
                              else:
                                  wait["message"] = spl
                                  cl.sendMessage(msg.to, "Pesan Msg\nPesan Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set welcome: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set welcome: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Welcome Msg")
                              else:
                                  wait["welcome"] = spl
                                  cl.sendMessage(msg.to, "Welcome Msg\nWelcome Msg diganti jadi :\n\n「{}」".format(str(spl)))
                        
                        elif 'Set left: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set left: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Lefr Msg")
                              else:
                                  wait["welcome"] = spl
                                  cl.sendMessage(msg.to, "Left Msg\nLeft Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set respon: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set respon: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Respon Msg")
                              else:
                                  wait["Respontag"] = spl
                                  cl.sendMessage(msg.to, "Respon Msg\nRespon Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set spam: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set spam: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Spam")
                              else:
                                  Setmain["RAmessage1"] = spl
                                  cl.sendMessage(msg.to, "Spam Msg\nSpam Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif 'Set sider: ' in msg.text:
                           if msg._from in admin:
                              spl = msg.text.replace('Set sider: ','')
                              if spl in [""," ","\n",None]:
                                  cl.sendMessage(msg.to, "Gagal mengganti Sider Msg")
                              else:
                                  wait["mention"] = spl
                                  cl.sendMessage(msg.to, "Sider Msg\nSider Msg diganti jadi :\n\n「{}」".format(str(spl)))

                        elif text.lower() == "cek pesan":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "Pesan Msg\nPesan Msg mu :\n\n「 " + str(wait["message"]) + " 」")

                        elif text.lower() == "cek welcome":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "Welcome Msg\nWelcome Msg mu :\n\n「 " + str(wait["welcome"]) + " 」")
                               
                        elif text.lower() == "cek left":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "Left Msg\nLeft Msg mu :\n\n「 " + str(wait["left"]) + " 」")      

                        elif text.lower() == "cek respon":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "「Respon Msg」\nRespon Msg mu :\n\n「 " + str(wait["Respontag"]) + " 」")

                        elif text.lower() == "cek spam":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "Spam Msg\nSpam Msg mu :\n\n「 " + str(Setmain["RAmessage1"]) + " 」")

                        elif text.lower() == "cek sider":
                            if msg._from in admin:
                               cl.sendMessage(msg.to, "Sider Msg\nSider Msg mu :\n\n「 " + str(wait["mention"]) + " 」")

#===========JOIN TICKET============#
                        elif "/ti/g/" in msg.text.lower():
                          if wait["selfbot"] == True:
                            if msg._from in admin:
                              if settings["autoJoinTicket"] == True:
                                 link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                                 links = link_re.findall(text)
                                 n_links = []
                                 for l in links:
                                     if l not in n_links:
                                        n_links.append(l)
                                 for ticket_id in n_links:
                                     group = cl.findGroupByTicket(ticket_id)
                                     cl.acceptGroupInvitationByTicket(group.id,ticket_id)
                                     cl.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group1 = ki.findGroupByTicket(ticket_id)
                                     ki.acceptGroupInvitationByTicket(group1.id,ticket_id)
                                     ki.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group2 = kk.findGroupByTicket(ticket_id)
                                     kk.acceptGroupInvitationByTicket(group2.id,ticket_id)
                                     kk.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group3 = kc.findGroupByTicket(ticket_id)
                                     kc.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     kc.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group4 = kb.findGroupByTicket(ticket_id)
                                     kb.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     kb.sendMessage(msg.to, "Masuk : %s" % str(group.name))
                                     group5 = ke.findGroupByTicket(ticket_id)
                                     ke.acceptGroupInvitationByTicket(group3.id,ticket_id)
                                     ke.sendMessage(msg.to, "Masuk : %s" % str(group.name))

    except Exception as error:
        print (error)


while True:
    try:
        ops = poll.singleTrace(count=50)
        if ops is not None:
            for op in ops:
               # bot(op)
                # Don't remove this line, if you wan't get error soon!
                poll.setRevision(op.revision)
                thread1 = threading.Thread(target=bot, args=(op,))#self.OpInterrupt[op.type], args=(op,)
                #thread1.daemon = True
                thread1.start()
                thread1.join()
    except Exception as e:
        pass
