"""用 Camoufox 打开一个网页，并读取标题。"""

import argparse
import os
from pathlib import Path

os.environ.setdefault(
    "XDG_CACHE_HOME",
    str(Path(__file__).resolve().parent / ".camoufox" / "cache"),
)

from camoufox.sync_api import Camoufox


def main() -> None:
    parser = argparse.ArgumentParser(description="用 Camoufox 打开网页")
    parser.add_argument("url", nargs="?", default="about:blank", help="要打开的网址")
    args = parser.parse_args()

    with Camoufox(headless=True) as browser:
        page = browser.new_page()
        page.goto(args.url)
        print(f"页面标题：{page.title()}")
        print(f"当前网址：{page.url}")


if __name__ == "__main__":
    main()
