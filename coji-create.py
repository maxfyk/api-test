from PIL import Image, ImageOps
import io
import base64

import requests as r

in_data = {
  'in-data': 'LOL',
  'data-type': 'text',
  'style-info': {
    'name': 'geom-original',
    # 'background-color': (255, 191, 0),
    # 'border': {
    #     'border-size': 15,
    #     'border-color': (26, 26, 26),
    # }
  },
  'user-id': 'asdasd222'
}

in_data_small = {
  'in-data': 'LOL',
  'data-type': 'text',
  'style-info': {
  	'size': 300,
    'name': 'geom-small',
    # 'background-color': (255, 191, 0),
    # 'border': {
    #     'border-size': 5,
    #     'border-color': (26, 26, 26),
    # }
  },
  'user-id': 'asdasd222'
}


resp = r.post('http://localhost:8000/coji-code/create', json=in_data)
img = base64.b64decode(resp.json()['image'])
img = Image.open(io.BytesIO(img))
img.save('out.jpg', quality=100)

resp = r.post('http://localhost:8000/coji-code/create', json=in_data_small)
img = base64.b64decode(resp.json()['image'])
img = Image.open(io.BytesIO(img))
img.save('out_small.jpg', quality=100)