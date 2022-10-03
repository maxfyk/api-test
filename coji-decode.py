import io
import time
import base64

import requests as r

in_data = {
    'decode-type': 'image',
    'in-data': None,
    'user-id': 'asd22',
    'style-info': {
        'name': 'geom-original',
    }
}

in_data['in-data'] = base64.b64encode(open('C:\\Users\\maxfyk\\Downloads\\photo_2022-08-12_16-24-41.jpg', 'rb').read()).decode('utf-8')
#
# in_data = {
#     'decode-type': 'keyboard',
#     'in-data': 'bbjhodfpdefajdhi',
#     'user-id': 'asd22',
#     'style-info': {
#         'name': 'geom-original',
#     }
# }

start_time = time.time()
resp = r.post('http://138.2.132.121/coji-code/decode', json=in_data)
print("--- %s seconds ---" % (time.time() - start_time))
print(resp)
print(resp.text)
print(resp.json())
