# How to Hunt for Leaked GCP API Keys


```bash
echo example.com | subfinder | httpx-toolkit > subs.txt

httpx-toolkit -l subs.txt -mr 'AIza[0-9A-Za-z\-_]{35}'
```
