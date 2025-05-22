# How to Enumerate Subdomains


## Passive
Subfinder
```bash
subfinder -d example.com -all -recursive -t 200 -silent | anew subfinder.txt

subfinder -dL domains.txt -all -recursive -t 200 -silent | anew subfinder.txt
```

Findomain
```bash
findomain --quiet -t example.com | anew findomain.txt

cat domains.txt | while read domain; do findomain --quiet -t $domain | anew findomain.txt; done
```

Assetfinder
```bash
assetfinder -subs-only example.com | anew assetfinder.txt

cat domains.txt | while read domain; do assetfinder -subs-only $domain | anew assetfinder.txt; done
```

Sublistr3r
```bash
sublist3r -d example.com -t 50 | anew sublist3r.txt

cat domains.txt | while read domain; do sublist3r -d $domain -t 50 | anew sublist3r.txt; done
```

Go-Dork
```bash
go-dork -q 'site:*.example.com' -p 100 | anew godork.txt

go-dork -q 'site:*.example.com' -e bing -p 100 | anew godork.txt
```

## Active

DNS Brute Force
```bash
gobuster dns -d example.com | anew gobuster.txt

cat domains.txt | while read domain; do gobuster dns -d $domain -w wordlist.txt | anew gobuster.txt; done
```

Virtual Host Fuzzing
```bash
ffuf -c -r -u 'https//www.example.com' -H 'Host: FUZZ.example.com' -w wordlist.txt | anew vhost.txt

cat domains.txt | while read domain; do ffuf -c -r -u 'https://$domain' -H 'Host: FUZZ.$domain' -w wordlist.txt  | anew vhost.txt; done
```

Reverse DNS Lookup
```bash
cat subs.txt | httpx-toolkit -ip | grep -oP '\[\K[^\]]+' | dnsx -ptr -resp-only | anew reverseDns.txt
```


## Filter and Probe Subdomains
Deduplicate Subdomains
```bash
cat subfinder.txt findomain.txt assetfinder.txt sublist3r.txt godork.txt gobuster.txt vhost.txt reverseDns.txt | anew subs.txt
```

Probe Subdomains
```bash
cat subs.txt | httpx-toolkit > liveSubs.txt
```

Clean Directory
```bash
rm -rf subfinder.txt findomain.txt assetfinder.txt sublist3r.txt godork.txt gobuster.txt vhost.txt reverseDns.txt
```
