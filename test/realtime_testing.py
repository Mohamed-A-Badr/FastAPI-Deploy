import asyncio
import httpx
import random


async def send_request():
    temperature = round(random.uniform(35.0, 37.0), 1)
    pulse_rate = round(random.uniform(80.0, 100.0), 1)
    oximeter = round(random.uniform(120.0, 130.0), 1)
    async with httpx.AsyncClient() as client:
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjU1LCJpYXQiOjE2ODkzNTM5NjMsIm5iZiI6MTY4OTM1Mzk2MywianRpIjoiMjE0ODc3ZjMtNDllMS00MzIzLThkNzAtNDZiM2QzYWNjZTU3IiwiZXhwIjoxNzIwODg5OTYzLCJ0eXBlIjoiYWNjZXNzIiwiZnJlc2giOmZhbHNlfQ.MjjtCG7ii9G9ecVCTjbxd-T4oAFAgY84y-CmaRACC-I",
        }
        payload = {
            "temperature": temperature,
            "oximeter": oximeter,
            "pulse_rate": pulse_rate,
        }
        response = await client.post(
            "http://127.0.0.1:8000/chair/data", headers=headers, json=payload
        )
        # if response.status_code == 401:
        #     login()
        print(response.text)


# async def get_request():
#     async with httpx.AsyncClient() as client:
#         response = await client.get("http://127.0.0.1:8000/chair/data/12315")
#         print(response.text)
#


async def main():
    while True:
        await send_request()
        await asyncio.sleep(5)


if __name__ == "__main__":
    asyncio.run(main())
