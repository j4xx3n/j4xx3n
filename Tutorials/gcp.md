# How to Hunt for Leaked GCP API Keys


```bash
echo example.com | subfinder | httpx-toolkit > subs.txt

cat subs.txt | xargs -I@ curl -s @ | grep -oP 'AIza[0-9A-Za-z-_]{35}' | sort -u
```
