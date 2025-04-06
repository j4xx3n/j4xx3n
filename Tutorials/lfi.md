# How to Hunt for LFI Vulnerabilities

```bash 
echo "example.com" | katana -o katana.txt

cat katana.txt | sort -u | urldedupe > urls.txt

cat urls.txt | gf lfi > lfi.txt

ffuf -u FUZZ -w lfi-urls.txt:FUZZ -w lfi-payloads.txt:PAYLOAD

```




