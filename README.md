# SubreconGPT

This (VERY BETA) Python script performs AI-assisted subdomain discovery. It takes a list of subdomains as input, generates similar subdomains using the OpenAI GPT-3 model, and attempts to resolve these subdomains.

## Prerequisites
Before you begin, you need to have the following:

- Python 3.6 or later.
- The OpenAI Python client. You can install this using pip:

```bash
pip install openai
```

- An OpenAI API key. You can obtain this from the OpenAI website.

## Usage

You can run the script from the command line like this:

```bash
chaos -d yourdomain.com | python subrecongpt.py --apikey YOUR_OPENAI_API_KEY
```
Replace yourdomain.com with the domain you're investigating and YOUR_OPENAI_API_KEY with your actual OpenAI API key.

This command will run Chaos on yourdomain.com, and then pipe the output into the Python script. The script will generate similar subdomains for each subdomain output by Chaos, and then attempt to resolve these new subdomains.

## Output
For each input subdomain, the script will print out the AI's guesses for similar subdomains and whether each guess resolves:

```
Subdomain = admin.kroger.com
Guesses: dev, qa, test, prod, secure

dev.kroger.com does not resolve.
qa.kroger.com does not resolve.

*** test.kroger.com RESOLVES to 192.0.2.123 ***

prod.kroger.com does not resolve.
secure.kroger.com does not resolve.
```

Resolved subdomains are printed with a clear message and their IP address. The IP address 192.0.2.123 is a placeholder used for illustrative purposes.

## Notes

- The script will pause for 1 second between each set of subdomains to prevent over-requesting the OpenAI API.
- The script will skip wildcard domains. If an input subdomain contains a '', the script will skip it.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
