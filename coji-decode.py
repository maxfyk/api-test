import io
import base64

import requests as r

in_data = {
  'type': 'photo',
  'photo': None,
  'user-id': 'asd22',
}


in_data['photo'] = base64.encodebytes(open('out.jpg', 'rb').read()).decode()

resp = r.post('http://localhost:8000/coji-code/decode', json=in_data)
print(resp.json())