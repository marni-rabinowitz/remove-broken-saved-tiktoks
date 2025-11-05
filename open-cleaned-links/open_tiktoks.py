import webbrowser
import time

# File that contains your TikTok links (one per line)
LINKS_FILE = "tiktoks.txt"

# Delay between opening links (in seconds)
DELAY = 2

def open_tiktok_links():
    try:
        with open(LINKS_FILE, "r") as f:
            links = [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: Could not find {LINKS_FILE}. Make sure it’s in the same folder.")
        return

    print(f"Opening {len(links)} TikTok links...")
    for i, link in enumerate(links, 1):
        print(f"({i}/{len(links)}) Opening: {link}")
        webbrowser.open(link)
        time.sleep(DELAY)

if __name__ == "__main__":
    open_tiktok_links()
