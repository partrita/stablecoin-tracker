## 2024-05-24 - [RSS Feed Injection]
**Vulnerability:** Markdown Injection & XSS via RSS feed data
**Learning:** `src/update_readme.py` fetches data from Google News RSS using `feedparser`. By directly injecting fields like `title`, `link`, and `published` into Markdown (`README.md`, `_dashboard_content.qmd`), the pipeline implicitly trusts external content, making it vulnerable to XSS and Markdown injection.
**Prevention:** Sanitize untrusted input by escaping HTML (`html.escape()`), replacing Markdown-sensitive characters (e.g., `[` and `]`), and enforcing safe link protocols (`http://` or `https://`).

## 2024-03-30 - [Missing Timeout and Silent Error Swallowing]
**Vulnerability:** Denial of Service (DoS) risk from missing API timeout and silent exception swallowing.
**Learning:** `src/fetch_daily_data.py` previously fetched data from CoinGecko without a configured `timeout`. This is a classic DoS vector where the application could hang indefinitely if the external service stops responding. Additionally, bare `except:` blocks silently swallowed errors, effectively masking potentially critical parsing failures or API structure changes.
**Prevention:** Always set explicit timeouts on network requests (e.g., `scraper.get(URL, timeout=15)`). Never use bare `except:` blocks; explicitly catch expected exceptions and log them to provide visibility into failures.

## 2024-05-24 - [CSV Formula Injection]
**Vulnerability:** CSV Formula Injection via un-sanitized external input written to CSV.
**Learning:** `src/fetch_daily_data.py` and `src/update_readme.py` were writing scraped/fetched strings (`coin_name`, `title`, etc.) directly into CSV files. If these inputs begin with characters like `=`, `+`, `-`, or `@`, spreadsheet applications like Excel could interpret them as executable formulas upon opening, leading to a command execution vulnerability on the user's machine.
**Prevention:** Always sanitize data bound for CSV files. Iterate over strings and prepend a single quote (`'`) to any string starting with `=`, `+`, `-`, or `@`.
