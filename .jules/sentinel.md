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

## 2024-05-24 - [Quarto Shortcode Injection]
**Vulnerability:** Remote Code Execution / Data Exfiltration via Quarto Shortcode Injection
**Learning:** `src/update_readme.py` writes external RSS data directly into `_dashboard_content.qmd`. Because Quarto processes `.qmd` files, an attacker could potentially execute arbitrary code or exfiltrate data by injecting malicious Quarto shortcodes (e.g., using `{{{< ... >}}}`). The previous sanitization only escaped HTML and Markdown characters but missed the curly braces used by Quarto.
**Prevention:** Sanitize `{` and `}` in any untrusted data rendered by Quarto. Use HTML entities (`&#123;` and `&#125;`) for text fields and URL-encoded equivalents (`%7B` and `%7D`) for links to prevent shortcode execution.

## 2026-04-10 - [Markdown Link Breakout and XSS]
**Vulnerability:** Markdown Link Breakout and Cross-Site Scripting (XSS)
**Learning:** `src/update_readme.py` generated Markdown links from untrusted RSS feeds using `f"- [{title}]({link})"`. While it enforced `http://` or `https://`, it did not encode characters with special meaning in Markdown links, such as parentheses `(`, `)`, spaces, or quotes `"`. An attacker could inject a URL like `https://example.com/) <script>alert(1)</script>`, which prematurely closes the Markdown link and renders the trailing HTML script tag in the dashboard (Markdown Injection/XSS).
**Prevention:** In addition to validating URL protocols, untrusted inputs injected into Markdown link URIs must have spaces, parentheses, and quote characters properly URL-encoded (e.g., `link.replace(' ', '%20').replace('(', '%28').replace(')', '%29')`).

## 2026-04-13 - [Markdown Table and Block Breakout]
**Vulnerability:** Markdown Block Breakout and Table Structure Corruption
**Learning:** `src/update_readme.py` injects untrusted RSS data into Markdown documents (`README.md`, `_dashboard_content.qmd`). Even with HTML escaping and basic character replacement, an attacker could include newline (`\n`, `\r`) or pipe (`|`) characters in the RSS feed. Newlines can cause a single link to span multiple lines, breaking out of lists or blocks and creating new Markdown blocks (like headers or code blocks). Pipe characters can corrupt Markdown tables if the injected text is rendered inside or near a table.
**Prevention:** Always strip or encode newline characters (`\n`, `\r`) and pipe characters (`|`) when injecting untrusted content into Markdown, especially when the content is expected to stay on a single line or is near table structures.

## 2024-04-14 - Markdown Breakout Vulnerability in Quarto
**Vulnerability:** Untrusted inputs (like RSS feed titles and URLs) rendered inside Quarto Markdown tables or links lacked sanitization for newlines (`\n`, `\r`) and pipe characters (`|`).
**Learning:** Malicious or malformed inputs containing these characters can cause Markdown Block Breakouts, corrupting table structures or injecting unintended formatting and links directly into the rendered document.
**Prevention:** Always strip or encode newline and pipe characters (e.g., using `.replace('\n', ' ').replace('\r', '').replace('|', '&#124;')`) when injecting untrusted content into Markdown contexts, especially within `.qmd` documents.

## 2026-04-15 - [SSRF / Arbitrary File Read Risk via urllib.request]
**Vulnerability:** Server-Side Request Forgery (SSRF) and Arbitrary File Read via `urllib.request.urlopen`
**Learning:** `src/update_readme.py` fetched Google News RSS feeds using `urllib.request.urlopen`. `urllib.request` natively supports resolving `file://` schemes. If the target URL is ever dynamically generated or manipulated to point to a local file, it could lead to arbitrary local file read. Bandit raises a B310 warning for this.
**Prevention:** Prefer using the `requests` library (e.g., `requests.get()`) instead of `urllib.request.urlopen` for HTTP requests, as it does not resolve `file://` schemas by default.

## 2026-04-17 - [Unhandled RSS Exceptions leading to DoS]
**Vulnerability:** Application Crash and Denial of Service (DoS) due to Unhandled Exceptions
**Learning:** `src/update_readme.py` previously accessed `entry.title`, `entry.link`, and `entry.published` from the parsed RSS feed using direct attribute access. If the external RSS feed is malformed or missing these fields, `feedparser` throws an `AttributeError`, causing the script to crash and the automated pipeline to fail. Furthermore, the `except Exception as e:` block itself threw an `AttributeError` by referencing `entry.title`.
**Prevention:** Never trust external payloads to conform perfectly to expected schemas. Use safe accessor methods with default fallbacks (e.g., `entry.get('title', 'Unknown')`) to handle missing data gracefully and prevent unhandled exceptions. Always ensure exception logging doesn't introduce new exceptions.

## 2026-04-19 - [Missing JSON Payload Type Validation]
**Vulnerability:** Denial of Service (DoS) due to unhandled exceptions when parsing JSON.
**Learning:** `src/fetch_daily_data.py` parsed an HTML attribute (`data-analytics-event-properties`) via `json.loads(props_str)` and immediately called `.get("coin_name")` assuming it was a dictionary. If the payload is unexpectedly parsed as a `list` or a `string`, or if the returned `slug` is not a string, the subsequent type-specific methods (like `slug.replace`) or dictionary accesses (`props.get`) cause `AttributeError` or `TypeError` crashes, halting the entire pipeline.
**Prevention:** Always validate the structure and type of data parsed from untrusted JSON strings before accessing their properties (e.g., `isinstance(props, dict)`). Additionally, use explicit exception handling (like `json.JSONDecodeError`) to avoid masking true implementation flaws.
