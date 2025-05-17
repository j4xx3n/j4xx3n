# How to Enumerate Subdomains


## Passive
Subfinder
```bash
subfinder -d example.com -all -recursive -t 200 -silent | anew subs.txt

subfinder -dL domains.txt -all -recursive -t 200 -silent | anew subs.txt
```

Findomain
```bash
findomain --quiet -t example.com | anew subs.txt

cat domains.txt | while read domain; do findomain --quiet -t $domain | anew subs.txt; done
```

Assetfinder
```bash
assetfinder -subs-only example.com | anew subs.txt

cat domains.txt | while read domain; do assetfinder -subs-only $domain | anew subs.txt; done
```

Sublistr3r
```bash
sublist3r -d example.com -t 50 | anew subs.txt

cat domains.txt | while read domain; do sublist3r -d $domain -t 50 | anew subs.txt; done
```


## Active

DNS Brute Force
```bash
gobuster dns -d example.com | anew subs.txt

cat domains.txt | while read domain; do gobuster dns -d $domain -w wordlist.txt | anew subs.txt; done
```

Virtual Host Fuzzing
```bash
ffuf -c -r -u 'https//www.example.com' -H 'Host: FUZZ.example.com' -w wordlist.txt

cat domains.txt | while read domain; do ffuf -c -r -u 'https://$domain' -H 'Host: FUZZ.$domain' -w wordlist.txt  | anew subs.txt; done
```

Reverse DNS Lookup
```bash
cat subs.txt | httpx-toolkit -ip | grep -oP '\[\K[^\]]+' | dnsx -ptr -resp-only | anew subs.txt
```


## Probe Subdomains


```bash
cat subs.txt | httpx-toolkit > live.txt
```


















