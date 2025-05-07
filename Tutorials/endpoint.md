# How to Enumerate Endpoints

## Crawling/Spidering the Site

Katana
```bash
katana -list subs.txt | anew urls.txt
```

Wayback Machine
```bash
cat subs.txt | while read url; do curl 'https://web.archive.org/cdx/search/cdx?url=*.$url/*&output=text&fl=original&collapse=urlkey' | anew urls.txt; done
```

## Directory Brute Force

Dirb
```bash
cat subs.txt | while read sub; do dirb $sub | anew dirb.txt; done

grep -Eo 'https?://[^ ]+' dirb.txt | sed 's/^+ //' | anew urls.txt
```

Ffuf
```bash
ffuf -u https://sub.example.com/FUZZ -w wordlist.txt -mc 200 -recursion | anew ffuf.txt

cat subs.txt | while read url; do ffuf -u $url/FUZZ -w wordlist.txt -mc 200 -recursion | anew ffuf.txt; done

grep -Eo 'https?://[^ ]+' ffuf.txt | sed 's/^+ //' | anew urls.txt
```

Fuzzing Directories with Custom Wordlist
```bash
cat wordlist.txt | anew customPaths.txt

cat urls.txt | unfurl paths | anew customPaths.txt

cewl urls.txt --with-numbers | anew customPaths.txt

cat subs.txt | while read url; do ffuf -u $url/FUZZ -w customPaths.txt -mc 200 -recursion | anew ffuf.txt; done
```

## Hidden Parameter Discovery

Arjun
```bash
cat urls.txt | grep '?' | cut -d '?' -f 1 | sort -u > baseurls.txt

cat baseurls.txt | while read url; do arjun -u $url -m post; done
cat baseurls.txt | while read url; do arjun -u $url -m get; done
```

Fuzzing Parameters with Custom Wordlist
```bash
cat urls.txt | unfurl keys | anew customParams.txt
```
