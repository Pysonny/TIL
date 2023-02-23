import requests 
import pprint
URL = 'https://api.bithumb.com/public/ticker /ALL KRW'
while True:
    response = requests.get (URL)
    # print (response)
    # print (type(response))
    # print(dir(response))
    data = response. json ()
    print (data.get ('data').get('BTC').get ('closing_price'))


# 5명 반복해서 알아보기

import requests
students = ['gunhee", 'mingi', 'hyunyoung', 'minji', 'yuyoung ]
for name in students:
    URL = fhttps://api.nationalize. io/?name={name}
    response = requests.get (URL) • json)
    # print(response)
    # print (response.get ('country'))
    # print (response. get ('country') [01)
    print (response.get ('country")[0].get ('country_id')))



# ex

import requests
# https://api.themoviedb.org/3/movie/2846?api key=8854669b886a6c07c12ea947bcc2311d
BASE_URL = "https://api. themoviedb.org/3'
Bath ='/movie/popular' # API 문서에서 적절하게 구성
parans ={ # 그 문서에서 필요한 parans 정의
    'api_key': '8854669b886a6c07c12ea947bcc2311d',
    'language': 'Ko-KR'
    'region': 'KR'
}

response = requests. get (BASE_URL+path, params-params) • json ()
print(response)
print (response.get ('results')[0])