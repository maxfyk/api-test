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

in_data['in-data'] = base64.encodebytes(open("C:\\Users\\maxfyk\\Downloads\\test.jpg", 'rb').read()).decode()

in_data = {
    'decode-type': 'keyboard',
    'in-data': 'bbjhodfpdefajdhi',
    'user-id': 'asd22',
    'style-info': {
        'name': 'geom-original',
    }
}

start_time = time.time()
resp = r.get('http://localhost:8000/coji-code/decode', json=in_data)
print("--- %s seconds ---" % (time.time() - start_time))
print(resp.json())
