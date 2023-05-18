import openai
import dns.resolver
import argparse
import sys
import time

def generate_subdomains(subdomain, domain, api_key):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Generate 5 subdomains similar to {subdomain}."},
        ],
    )
    ai_generated_subdomains = [f"{sub}.{domain}" for sub in response['choices'][0]['message']['content'].strip().split('\n')]

    return ai_generated_subdomains

def resolve_subdomains(subdomains):
    resolved_subdomains = []
    for subdomain in subdomains:
        try:
            answers = dns.resolver.resolve(subdomain, 'A')
            for rdata in answers:
                resolved_subdomains.append(subdomain)
                print(f"\n*** {subdomain} RESOLVES to {rdata.address} ***\n")
        except dns.resolver.NXDOMAIN:
            print(f"{subdomain} does not resolve.")
        except Exception as e:
            print(f"Error resolving {subdomain}: {e}")

    return resolved_subdomains

def main():
    parser = argparse.ArgumentParser(description='AI-assisted subdomain discovery.')
    parser.add_argument('--apikey', required=True, help='OpenAI API key.')
    args = parser.parse_args()

    lines = [line.strip() for line in sys.stdin]

    for line in lines:
        if '*' in line:  # Skip wildcard domains
            continue
        subdomain, domain = line.split('.', 1)  # Split the line into subdomain and domain
        print(f"\nSubdomain = {subdomain}.{domain}")
        new_subdomains = generate_subdomains(subdomain, domain, args.apikey)
        print(f"Guesses: {', '.join([sub.split('.')[0] for sub in new_subdomains])}\n")
        resolved_subdomains = resolve_subdomains(new_subdomains)
        time.sleep(1)  # Pause for 1 second

if __name__ == "__main__":
    main()
