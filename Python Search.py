import translator as translator #import translator
from bs4 import BeautifulSoup   #import BeautifulSoup
import requests #.
import pyttsx3 #import pyttsx3 if you want python doing speech automatically for you
from translate import Translator #Warning: Translation has limitation
# get info using pyreptile
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
translator = Translator(from_lang="English", to_lang="Chinese") #translate English to Chinese
def google(query):
    translator = Translator(from_lang="English", to_lang="Chinese") #translate English to Chinese
    query = query.replace(" ","+")
    try:
        url = f'https://www.google.com/search?q={query}&oq={query}&aqs=chrome..69i57j46j69i59j35i39j0j46j0l2.4948j0j7&sourceid=chrome&ie=UTF-8'
        res = requests.get(url,headers=headers)
        bsoup = BeautifulSoup(res.text,'html.parser')
    except:
        print("please check if you have a internet connection,thanks.")
    try:
        try:
            ans = bsoup.select('.RqBzHd')[0].getText().strip()

        except:
            try:
                title=bsoup.select('.AZCkJd')[0].getText().strip()
                try:
                    ans=bsoup.select('.e24Kjd')[0].getText().strip()
                except:
                    ans=""
                ans=f'{title}\n{ans}'

            except:
                try:
                    ans=bsoup.select('.hgKElc')[0].getText().strip()
                except:
                    ans=bsoup.select('.kno-rdesc span')[0].getText().strip()

    except:
        ans = "can't find on google,please try again!"
        translator = Translator(from_lang="English", to_lang="Chinese")
    #trt12 = translator.translate(ans)
    return ans+"\n"
#translator = Translator(from_lang="English", to_lang="Chinese")
#trt11 = translator.translate("Please enter your query thanks")
#translator = Translator(from_lang="English", to_lang="Chinese")
result = google(str(input("Please enter your query thanks\n")))
print(result)

def weather(city):
    translator = Translator(from_lang="English", to_lang="Chinese")
    city=city.replace(" ","+")
    trt8 = translator.translate("Searching in google,please wait a second......")
    res = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
    print("Searching in google,please wait a second...... "+trt8+"\n")

    soup = BeautifulSoup(res.text,'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()

    time = soup.select('#wob_dts')[0].getText().strip()

    information = soup.select('#wob_dc')[0].getText().strip()

    weather = soup.select('#wob_tm')[0].getText().strip()


    trt = translator.translate(location)
    trt1 = translator.translate(time)
    trt2 = translator.translate(information)
    print(location+" "+"city ("+trt+")")
    print("Today is "+time+" ("+trt1+")")
    print(information+" ("+trt2+")")
    print(weather+"¡ãC")
    wtr = int(weather)
    if wtr>27:
        trt3 = translator.translate("Very hot,stay away from sun!")
        print("It is hot!"+" ("+trt3+")")
    elif (wtr<24 and wtr>21):
        trt4 = translator.translate("comfy weather,go out for play!")
        print("Comfortable weather!"+" ("+trt4+")")
    elif (wtr<21 and wtr>=14):
        trt5 = translator.translate("comfy weather,go out for play!")
        print("Nice and cool weather!"+" ("+trt5+")")
    elif (wtr<14 and wtr>0):
        trt6 = translator.translate("Very cold!")
        print("It is cold!"+" ("+trt6+")")
    else:
        trt7 = translator.translate("Cold to death!")
        print("Freeze!"+" ("+trt7+")")

remind = "No matter upper or lower case."
trt9 = translator.translate(remind)
trt10 = translator.translate("Please enter the city name")
print("Please enter the city name "+"("+remind+") "+trt10+"("+trt9+")")
city=input()
city=city+" weather"
weather(city)
# trt represents translation variable.
# Each trt only for one sentence.
# you can use gooletranlator as well.
# program has two functions and each function implements translator.
# translator works inside the function also outside one.
# 并不是所有的信息都有自动翻译的功能
# 会继续更新
# aomeng causes error
