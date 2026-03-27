## 2024-05-24 - [RSS Feed Injection]
**Vulnerability:** Markdown Injection & XSS via RSS feed data
**Learning:** `src/update_readme.py` fetches data from Google News RSS using `feedparser`. By directly injecting fields like `title`, `link`, and `published` into Markdown (`README.md`, `_dashboard_content.qmd`), the pipeline implicitly trusts external content, making it vulnerable to XSS and Markdown injection.
**Prevention:** Sanitize untrusted input by escaping HTML (`html.escape()`), replacing Markdown-sensitive characters (e.g., `[` and `]`), and enforcing safe link protocols (`http://` or `https://`).
