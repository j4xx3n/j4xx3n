# Leaked and Unrestricted Google Maps API Key on `example.com`

## Summary:

A publicly accessable Google Maps API key was discovered in the response body of [example.com]. The key is not properly restricted and can be abused by an attacker to generate unauthorized Google Cloud Platform (GCP) charges by making billable API calls. 

## Affected Subdomains:
`example.com`

## Location of the Key:
The key is present directly in the HTTP response body when visiting the subdomain.

## Vulnerable API Services
- example
- example

## Steps to Reproduce
1. Leak verification:
```bash
curl -s example.com | grep -o "AIza[0-9A-Za-z_-]\{35\}"
```
This should print the exposed API key to the screen. It will look somthing like this: `AIzaSyD***********************nOpw`

2. No restriction verification
```bash
https://maps.googleapis.com/maps/api/geocode/json?latlng=40,30&key=AIzaSyD***********************nOpw
```

## Proof of Concept (Abuse)
The leaked key was tested and confirmed to have no restrictions against high-cost Google Maps services. The following request demonstrates that an attacker can make billable calls:

```bash
https://maps.googleapis.com/maps/api/geocode/json?latlng=40,30&key=AIzaSyD***********************nOpw
```

## Impact:
When Google Maps API keys are publicly exposed and not properly restricted, they can be exploited by attackers to make high-volume requests to premium APIs. This leads to:

- Unintended billing on the company’s GCP account
- Abuse of proprietary services
- Potential exhaustion of quota, which could affect production applications relying on this key



# Security Best Practices Recommendation:

Restrict Google Maps API keys in the Google Cloud Console by:

- HTTP referrer restriction (for frontend web apps)
- IP restriction (for backend services)
- Limiting usage to specific APIs
