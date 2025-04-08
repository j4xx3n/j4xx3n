# Finding Leaked Google Maps API Keys in Mass

## Summary
During my reconnaissance fase, I discovered several exposed Google Maps API keys by scanning a large list of subdomains for secrets in their HTTP response bodies. The process was entirely passive, and no interaction beyond simple GET requests was used to obtain this information.


## Steps to reporoduce
1. I used `ProjectDiscovery's Chaos` dataset to download a large set of public subdomains associated with bug bounty programs.
```bash
choas -dL domains.txt -o subs.txt
```
This yeided over 10,000 subdomains.

2. I ran `httpx-toolkit` with a custom regex filter pattern to search for Google Maps API keys in the HTTP responses of these subdomains.
```bash
httpx -l subs.txt -mr 'AIza[0-9A-Za-z\-_]{35}'
```

3. To confirm whether the exposed keys were valid and determine their access levels, I used a tool `gmapsapiscanner`.
```bash
python3 maps_api_scanner.py --api-key AIzaSyD***********************nOpw
```


## Impact
- Leaked Google Maps API keys can potentially be abused for:

- Free quota exhaustion leading to billing abuse

- Unauthorized access to Maps, Geocoding, or Places API

- Leaking internal information via autocomplete or reverse geocoding
