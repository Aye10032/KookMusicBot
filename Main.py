import json
import zlib
import uvicorn
from fastapi import FastAPI, Request

app = FastAPI()


@app.post('/')
async def process_json(request: Request):
    compressed_data = await request.body()
    uncompressed_data = zlib.decompress(compressed_data)
    parsed_message = json.loads(uncompressed_data.decode('utf-8'))

    if parsed_message['d']['channel_type'] == 'WEBHOOK_CHALLENGE':
        challenge = parsed_message['d']['challenge']
        return {'challenge': challenge}


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=9500)
