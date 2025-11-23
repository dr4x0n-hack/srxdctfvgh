import requests
import socket
import exifread

# ============================
# 1) PORT SCANNER (safe)
# ============================
def port_scan(target, ports=[21,22,80,443,8080]):
    print("\n=== PORT SCAN RESULT ===")
    for port in ports:
        s = socket.socket()
        s.settimeout(0.5)
        try:
            s.connect((target, port))
            print(f"[OPEN] {port}")
        except:
            pass
    print("=========================")


# ============================
# 2) SUBDOMAIN FINDER (public API)
# ============================
def subfinder(domain):
    print("\n=== SUBDOMAIN FINDER ===")
    api = f"https://dns.bufferover.run/dns?q=.{domain}"
    try:
        res = requests.get(api).json()
        subdomains = res.get("FDNS_A", [])
        for sub in subdomains:
            print(sub.split(",")[0])
    except:
        print("Error fetching data")
    print("=========================")


# ============================
# 3) USERNAME OSINT (public only)
# ============================
def username_osint(username):
    print("\n=== USERNAME OSINT ===")
    sites = {
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://x.com/{username}",
        "TikTok": f"https://www.tiktok.com/@{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
    }
    for site, url in sites.items():
        try:
            r = requests.get(url)
            if r.status_code == 200:
                print(f"[FOUND] {site}: {url}")
        except:
            pass
    print("=========================")


# ============================
# 4) EXIF READER (image metadata)
# ============================
def exif_reader(image_path):
    print("\n=== EXIF INFO ===")
    try:
        with open(image_path, "rb") as img:
            tags = exifread.process_file(img)
            for tag in tags.keys():
                print(f"{tag}: {tags[tag]}")
    except:
        print("Could not read EXIF data")
    print("=========================")


# ============================
# 5) WEBSITE TECHNOLOGY INFO
# ============================
def tech_lookup(domain):
    print("\n=== WEBSITE TECH ANALYSIS ===")
    url = f"https://api.wappalyzer.com/lookup/v1/?urls={domain}"
    headers = {"x-api-key": "YOUR_API_KEY"}   # API key qo‘shsang ishlaydi
    try:
        r = requests.get(url, headers=headers).json()
        print(r)
    except:
        print("Error getting technology data")
    print("=========================")


# ============================
# MAIN DEMO
# ============================
if __name__ == "__main__":
    print("OSINT HUB — Safe Edition")

    # Misollar:
    # port_scan("127.0.0.1")
    # subfinder("example.com")
    # username_osint("example")
    # exif_reader("test.jpg")
    # tech_lookup("example.com")

    print("\nReady to use!")
