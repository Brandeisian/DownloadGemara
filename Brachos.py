import requests

def download_masechet_berakhot_hebrew():
    base_url = "https://www.sefaria.org/api/texts"
    seder = "Seder Kodashim"
    tractate = "Bekhorot"
    language = "he"
    edition = "William Davidson Edition - Aramaic"
    
    url = f"{base_url}/{seder}/{tractate}/Hebrew/William Davidson Edition - Aramaic.txt"
    response = requests.get(url)
    
    if response.status_code == 200:
        with open(f"{tractate}_hebrew.txt", 'w', encoding='utf-8') as file:
            file.write(response.text)
        print(f"Downloaded and saved {tractate}_hebrew.txt")
    else:
        print(f"Failed to download. Status code: {response.status_code}")

if __name__ == "__main__":
    download_masechet_berakhot_hebrew()