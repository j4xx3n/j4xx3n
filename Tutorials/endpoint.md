# How to Enumerate Endpoints

Katana
```bash
katana -list subs.txt | anew urls.txt
```

Wayback Machine
```bash
cat subs.txt | while read url; do curl 'https://web.archive.org/cdx/search/cdx?url=*.$url/*&output=text&fl=original&collapse=urlkey' | anew urls.txt; done
```

Dirb
```bash
cat subs.txt | while read sub; do dirb $sub | anew dirb.txt; done

grep -Eo 'https?://[^ ]+' dirb.txt | sed 's/^+ //' | anew urls.txt
```


Arjun
```bash
cat urls.txt | grep '?' | cut -d '?' -f 1 | sort -u > baseurls.txt

cat baseurls.txt | while read url; do arjun -u $url -m post; done
cat baseurls.txt | while read url; do arjun -u $url -m get; done
```

Ffuf
```bash
ffuf -u https://sub.example.com/FUZZ -w wordlist.txt -mc 200 -recursion

cat subs.txt | while read url; do ffuf -u $url -w wordlist.txt -mc 200 -recursion; done
```
