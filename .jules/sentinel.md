## 2024-05-24 - [RSS Feed Injection]
**Vulnerability:** Markdown Injection & XSS via RSS feed data
**Learning:** `src/update_readme.py` fetches data from Google News RSS using `feedparser`. By directly injecting fields like `title`, `link`, and `published` into Markdown (`README.md`, `_dashboard_content.qmd`), the pipeline implicitly trusts external content, making it vulnerable to XSS and Markdown injection.
**Prevention:** Sanitize untrusted input by escaping HTML (`html.escape()`), replacing Markdown-sensitive characters (e.g., `[` and `]`), and enforcing safe link protocols (`http://` or `https://`).

## 2026-03-28 - [CSV Injection in Data Scraper]
**Vulnerability:** CSV Injection (Formula Injection)
**Learning:** `src/fetch_daily_data.py` and `src/update_readme.py` retrieve unvalidated external strings (CoinGecko slugs, Google News RSS titles) and write them directly into pandas DataFrames saved as CSVs. This introduces a vulnerability where malicious strings starting with formula indicators (like `=cmd|' /C calc'!A0`) could execute arbitrary macros or code if users open the CSV files in spreadsheet tools like Excel.
**Prevention:** Always validate and sanitize strings meant for CSV files. Ensure any string starting with `=`, `+`, `-`, `@`, `\t`, or `\r` is escaped, commonly by prepending it with a single quote (`'`).
