# Example of // download through FTP on Python

Here I'm using `asyncio` along with `aioftp` to download file in parallel.

Files are of different size, the download order is decreasing, but you can see that smaller files get downloaded faster, which shows that tasks were run near all together.

