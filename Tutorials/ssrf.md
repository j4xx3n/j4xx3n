# How to Hunt for SSRF Vulnerabilities

```bash
echo "example.com" | katana -o katana.txt

cat katana.txt | sort -u | urldedupe > urls.txt

cat urls.txt | gf ssrf | qsreplace FUZZ > ssrf.txt

cat ssrf.txt | while read url; do ffuf -u $url -w payloads.txt -mc all; done
```
