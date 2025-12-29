# scripts/build_playlist.py

INPUT_FILE = "data/all.m3u"
OUTPUT_FILE = "output/playlist_final.m3u"
SON_EKLENEN_LIMIT = 20

def read_entries(lines):
    entries = []
    temp = []
    for line in lines:
        if line.startswith("#EXTINF"):
            temp = [line]
        elif line.startswith("http"):
            temp.append(line)
            entries.append(temp)
            temp = []
    return entries

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    lines = f.readlines()

entries = read_entries(lines)

son_eklenenler = entries[-SON_EKLENEN_LIMIT:]

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n\n")

    # 🔥 SON EKLENENLER
    f.write("#========================================\n")
    f.write("# 🔥 SON EKLENENLER\n")
    f.write("#========================================\n\n")

    for entry in reversed(son_eklenenler):
        f.write(entry[0])
        f.write(entry[1])

    f.write("\n")

    # TÜM ARŞİV
    f.write("#========================================\n")
    f.write("# 📦 TÜM İÇERİKLER\n")
    f.write("#========================================\n\n")

    for entry in entries:
        f.write(entry[0])
        f.write(entry[1])
