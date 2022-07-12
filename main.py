from subprocess import PIPE, Popen
from . import *

def pip_(module):
    onemli(f"📥 installing {module} for cerceynlab")
    pip_cmd = ["pip", "install", f"{module}"]
    process = Popen(pip_cmd, stdout=PIPE, stderr=PIPE)
    stdout, stderr = process.communicate()
    return stdout
try:
    import requests
except:
    pip_("requests") 
finally:
    import requests   

try:
    import bs4
except:
    pip_("bs4") 
finally:
    import bs4   
import time

if __name__=="__main__":
      numara = soru("[?] Telefon Numaranız: ")
      try:
         rastgele = requests.post("https://my.telegram.org/auth/send_password", data={"phone": numara}).json()["random_hash"]
      except:
         hata("[!] Kod Gönderilemedi. Telefon Numaranızı Kontrol Ediniz.")
         exit(1)
      
      sifre = input("[?] Telegram'dan Gelen Kodu Yazınız: ")
      try:
         cookie = requests.post("https://my.telegram.org/auth/login", data={"phone": numara, "random_hash": rastgele, "password": sifre}).cookies.get_dict()
      except:
         hata("[!] Büyük İhtimal Kodu Yanlış Yazdınız. Lütfen Scripti Yeniden Başlatın.")
         exit(1)
      app = requests.post("https://my.telegram.org/apps", cookies=cookie).text
      soup = bs4.BeautifulSoup(app, features="html.parser")

      if soup.title.string == "Create new application":
         bilgi("[i] Uygulamanız Yok. Oluşturuluyor...")
         hashh = soup.find("input", {"name": "hash"}).get("value")
         AppInfo = {
            "hash": hashh,
            "app_title":"Cerceyn UserBot",
            "app_shortname": "CerceynLab"+ str(time.time()).replace(".", ""),
            "app_url": "",
            "app_platform": "android",
            "app_desc": ""
         }
         app = requests.post("https://my.telegram.org/apps/create", data=AppInfo, cookies=cookie).text
         print(app)
         bilgi("[i] Uygulama başarıyla oluşturuldu!")
         bilgi("[i] API ID/HASH alınıyor...")
         newapp = requests.get("https://my.telegram.org/apps", cookies=cookie).text
         newsoup = bs4.BeautifulSoup(newapp, features="html.parser")

         g_inputs = newsoup.find_all("span", {"class": "form-control input-xlarge uneditable-input"})
         app_id = g_inputs[0].string
         api_hash = g_inputs[1].string
         basarili("[i] Bilgiler Getirildi! Lütfen Bunları Not Ediniz.\n\n")
         tamamlandi(app_id,api_hash)
else:
    hata("Hata")