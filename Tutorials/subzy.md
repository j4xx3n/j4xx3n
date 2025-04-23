# How to Hunt for Subdomain Takovers

```bash
echo example.com | subfinder | httpx-toolkit > subs.txt

subzy run --targets subs.txt --hide_fails
```
