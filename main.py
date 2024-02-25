import ffmpeg, os, shutil, requests

if "ffmpeg.exe" not in os.listdir("./"):
    print("[ERROR] ffmpeg was not found!")
    url = f"https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip"
    req = requests.get(url = url, stream = True)
    with open(f"./ffmpeg-master-latest-win64-gpl.zip", "wb") as f:
        f.write(req.content)
        f.close()
    shutil.unpack_archive('./ffmpeg-master-latest-win64-gpl.zip')
    os.rename('./ffmpeg-master-latest-win64-gpl/bin/ffmpeg.exe', './ffmpeg.exe')
    os.remove('ffmpeg-master-latest-win64-gpl.zip')
    shutil.rmtree('ffmpeg-master-latest-win64-gpl')

items = []
for item in os.listdir('./'):
    if item.endswith('.mp4'):
        items.append(item)
        stream = ffmpeg.input(item)
        filename = item.replace('.mp4', '.wav')
        stream = ffmpeg.output(stream, filename)
        ffmpeg.run(stream)

rslt = f""
for i in items:
    rslt += f"- {i} -> {i.replace('.mp4', '.wav')}\n"
print(f'Result: \n{rslt}')
input('Press Enter to exit...')