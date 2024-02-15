import hashlib

class URLShortener:
    def __init__(self):
        self.url_mapping = {}

    def shorten_url(self, long_url):
        # Generate MD5 hash
        hash_object = hashlib.md5(long_url.encode())
        hash_hex = hash_object.hexdigest()

        # Take the first 8 characters as the short URL
        short_url = hash_hex[:8]

        # Store the mapping in a dictionary
        self.url_mapping[short_url] = long_url

        return short_url

    def expand_url(self, short_url):
        # Retrieve the long URL from the mapping
        return self.url_mapping.get(short_url, "Short URL not found")

# Example usage
url_shortener = URLShortener()

long_url = "https://www.example.com/some/long/url"
short_url = url_shortener.shorten_url(long_url)
print(f"Short URL: {short_url}")

expanded_url = url_shortener.expand_url(short_url)
print(f"Expanded URL: {expanded_url}")
