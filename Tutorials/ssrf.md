# How to Hunt for SSRF Vulnerabilities

```bash
echo "example.com" | katana -o katana.txt

cat katana.txt | sort -u | urldedupe > urls.txt
```

## Attacking GET Requests
```bash
cat urls.txt | gf ssrf | qsreplace FUZZ >> ssrf.txt

cat ssrf.txt | while read url; do ffuf -u $url -w payloads.txt -mc all; done

```

## Attacking POST Requests

Manullay crawl website with burp and find any POST requests with parameters

```bash
 ffuf -w payloads.txt -u "https://example.com" -d 'parameter=FUZZ' -mc 200
```
