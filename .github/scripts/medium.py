"""Rewrite the "Lately on Medium" block in README.md from the Medium RSS feed.

Standard library only. Leaves the README untouched if the feed can't be read,
so a Medium outage never wipes the list.
"""
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
from pathlib import Path

FEED = "https://hashimmohamedta.medium.com/feed"
README = Path(__file__).resolve().parents[2] / "README.md"
LIMIT = 5
START, END = "<!-- medium:start -->", "<!-- medium:end -->"


def fetch():
    req = urllib.request.Request(FEED, headers={"User-Agent": "Mozilla/5.0 (profile-readme)"})
    with urllib.request.urlopen(req, timeout=20) as res:
        return res.read()


def posts(xml):
    for item in ET.fromstring(xml).iter("item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or "").split("?")[0]
        date = parsedate_to_datetime(item.findtext("pubDate")).strftime("%b %Y")
        if title and link:
            yield f"- [{title.replace(']', '').replace('[', '')}]({link}) ({date})"


def main():
    try:
        lines = list(posts(fetch()))[:LIMIT]
    except Exception as err:  # network, Cloudflare, bad XML
        print(f"skipping: {err}", file=sys.stderr)
        return
    if not lines:
        print("skipping: feed had no posts", file=sys.stderr)
        return
    text = README.read_text()
    block = f"{START}\n" + "\n".join(lines) + f"\n{END}"
    new = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: block, text, flags=re.S)
    if new != text:
        README.write_text(new)
        print("README updated")
    else:
        print("no change")


if __name__ == "__main__":
    main()
