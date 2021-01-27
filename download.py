import aioftp
import asyncio

files = [
    "20MB.zip",
    "10MB.zip",
    "1MB.zip",
]

async def get_data(file: str):
    async with aioftp.Client.context("speedtest.tele2.net") as client:
        print(f"Downloading file {file}...")
        await client.download(file, f"data/{file}", write_into=True)
        print(f"Finished downloading file {file} into data/{file}")

async def main():
    tasks = [
        asyncio.create_task(get_data(file)) for file in files
    ]
    await asyncio.wait(tasks)

if __name__ == "__main__":
    asyncio.run(main())

