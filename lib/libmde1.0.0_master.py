from res import resource
from tqdm import tqdm
from pathlib import Path
import requests
import math


def Drop(url):
    req = requests.get(url, stream=resource.EngineSettings.stream,
                       allow_redirects=resource.EngineSettings.allow_redirect)

    total_box_size = int(req.headers.get(resource.EngineSettings.header_type, 0))
    chunk_size = resource.EngineSettings.chunk_size
    recived = 0
    filename = Path(url).name

    with open(filename, 'wb') as file:
        for data in tqdm(req.iter_content(chunk_size):
            total = math.ceil(
                total_box_size // chunk_size), unit = resource.EngineSettings.unit, unit_scale = resource.EngineSettings.unit_scale)
        recived = recived + len(data)
        file.write(data)
    if total_box_size != 0 and recived != total_box_size:
        ErrMsg = 'Error on: [' + Path(__file__).name + ']'
        return ErrMsg
    else:
        pass
