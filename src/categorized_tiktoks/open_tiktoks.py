import webbrowser
import time
import random

# --- CONFIGURATION ---
BATCH_SIZE = 10
LINKS_FILE = "relationships_and_dating_formatted.txt"

# Human-like delay settings (seconds)
MIN_DELAY = .1
MAX_DELAY = .9
# ----------------------

def open_links_in_batches(file_path):
    # Read links bottom-to-top
    with open(file_path, 'r', encoding='utf-8') as f:
        links = [line.strip() for line in f if line.strip()][::-1]

    total = len(links)
    print(f"Loaded {total} TikTok links.\n")

    for i in range(0, total, BATCH_SIZE):
        batch = links[i:i + BATCH_SIZE]
        batch_num = (i // BATCH_SIZE) + 1

        input(f"\nPress ENTER to open batch {batch_num} ({len(batch)} links)...")

        for link in batch:
            print(f"Opening: {link}")
            webbrowser.open_new_tab(link)

            delay = random.uniform(MIN_DELAY, MAX_DELAY)
            print(f"  waiting {delay:.1f} seconds")
            time.sleep(delay)

        remaining = total - (i + BATCH_SIZE)
        print(f"\nBatch {batch_num} complete. {max(0, remaining)} links remaining.")

    print("\nAll links opened!")

if __name__ == "__main__":
    open_links_in_batches(LINKS_FILE)
