import requests

url = "http://challenge.ctf.games:31879"
user_agent = ["Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
"Mozilla/5.0 (X11; U; Linux x86_64; en-us) AppleWebKit/531.2+ (KHTML, like Gecko) Version/5.0 Safari/531.2+",
"Mozilla/5.0 (compatible; Konqueror/2.2.2)",
"Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
"Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0"]

rest = ["/M7p.txt",
"/gJZz.txt",
"/Me7p.txt",
"/9RJteo26Y.txt",
"/sHiv78lb.txt",
"/I2MejD.txt",
"/pI9aCdcw.txt",
"/hftZI6pP6Z.txt",
"/bczOH0.txt",
"/OeXfK.txt",
"/tP11S.txt",
"/pg7vTotvNO.txt",
"/xV5.txt",
"/PcFy.txt",
"/QabcMr.txt",
"/ptJYDt_Ca.txt",
"/vWZIAzKAK.txt",
"/944P7izIWE.txt",
"/cRW.txt",
"/EGPyJ4.txt",
"/ptJYDtCa.txt",
"/rYp.txt",
"/aE09.txt",
"/4Pqa6xS.txt",
"/bdr99.txt",
"/mBqcCYVC.txt",
"/lOLP1y.txt",
"/7H6aX3.txt",
"/oBHCz1yC.txt",
"/5IZGzF.txt",
"/pv68EGE.txt",
"/hiW75Wrn.txt",
"/6CQFfJOpe.txt",]

for part in rest:
    for ug in user_agent:
        headers = {
            "User-Agent": ug
        }
        response = requests.get(f"{url}{part}", headers=headers)
        if 'HELLO' in response.text:
            r = {
                "file": part,
                "user-agent": ug,
                "response": response.text
            }
            print(r)

        if 'REJOICE' in response.text:
            r = {
                "file": part,
                "user-agent": ug,
                "response": response.text
            }
            print(r)
        
        # print(response.content)

# flag[7] = 'e'
# flag[13] = 'p'
# flag[24] = '_'
# REJOICE, ROBOT. THE CHARACTER OF THE FLAG AT INDEX 13 IS THE SAME CHARACTER AT INDEX 0 IN THIS FILENAME.
#Mozilla/5.0 (X11; U; Linux x86_64; en-us) AppleWebKit/531.2+ (KHTML, like Gecko) Version/5.0 Safari/531.2+
