import os

# -----------------------------
# 1️⃣ Output klasörü ve dosyası
# -----------------------------
if not os.path.exists("output"):
    os.makedirs("output")

output_file = "output/playlist_final.m3u"

# -----------------------------
# 2️⃣ Playlist verilerini hazırla
# -----------------------------
playlist_entries = [
    "#EXTM3U",
    "#EXTINF:-1 tvg-id='avatar_live_action' tvg-name='Avatar: The Last Airbender', Avatar S01E01",
    "https://vs6.pictureflix.org/v/Avatar.The.Last.Airbender.S01E01.WEB-DL.1080p.DUAL.x264-HDM/1080.m3u8",
    "#EXTINF:-1 tvg-id='avatar_live_action' tvg-name='Avatar: The Last Airbender', Avatar S01E02",
    "https://vs8.photofunia.pro/v/Avatar.The.Last.Airbender.S01E02.WEB-DL.1080p.DUAL.x264-HDM/1080.m3u8"
    # Buraya diğer bölümleri ekle
]

# -----------------------------
# 3️⃣ Playlist’i output dosyasına yaz
# -----------------------------
with open(output_file, "w", encoding="utf-8") as f:
    for line in playlist_entries:
        f.write(line + "\n")

print(f"Playlist başarıyla yazıldı: {output_file}")
