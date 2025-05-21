# How to Enumerate Paths

## Crawling/Spidering the Site

Katana
```bash
katana -list subs.txt | anew katana.txt
```

Wayback Machine
```bash
cat subs.txt | waybackurls | anew waybackurls.txt; done
```

## Directory Brute Force

Dirb
```bash
cat subs.txt | while read sub; do dirb https://$sub | anew dirb.txt; done

grep -Eo 'https?://[^ ]+' dirb.txt | sed 's/^+ //' | anew dirbUrls.txt
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


## Scanning JS Files

```bash
cat urls.txt | grep '\.js$' | httpx-toolkit -mc 200 tee js.txt

cat js.txt | jsleaks -s -l -k
```
