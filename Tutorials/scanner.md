# How to Hunt with Vulnerabiliity Scanners

## Nuclei
Scan based on tech from Wappalizer
```bahs
nuclei -l subs.txt -as -o nuclei.txt
```

Out of Band Testing
```bash
interactsh-client -v -o interactsh.txt

nuclei -list liveUrls.txt -iserver  d0jlge6074u9dv2mjus0x943akbwkxs6p.oast.live
```


## Sn1per
```bash
sniper -t <TARGET> -m webscan
```
