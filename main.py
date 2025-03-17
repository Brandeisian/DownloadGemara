import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Base URL for raw content from GitHub
base_url = "https://raw.githubusercontent.com/Sefaria/Sefaria-Export/master/txt/Talmud/Bavli"

# Define the seders and their tractates
seders = {
    "Seder Kodashim": ["Arakhin", "Bekhorot", "Chullin", "Keritot", "Meilah", "Menachot", "Tamid", "Temurah", "Zevachim"],
    "Seder Moed": ["Beitzah", "Chagigah", "Eruvin", "Megillah", "Moed Katan", "Pesachim", "Rosh Hashanah", "Shabbat", "Sukkah", "Taanit", "Yoma"],
    "Seder Nashim": ["Gittin", "Ketubot", "Kiddushin", "Nazir", "Nedarim", "Sotah", "Yevamot"],
    "Seder Nezikin": ["Avodah Zarah", "Bava Batra", "Bava Kamma", "Bava Metzia", "Horayot", "Makkot", "Sanhedrin", "Shevuot"],
    "Seder Tahorot": ["Niddah"],
    "Seder Zeraim": ["Berakhot"],
}

# Filename for the master text file
master_filename = "master_text_file.txt"

# Ensure the master file is empty before starting
open(master_filename, 'w').close()

# Iterate through each seder and tractate
for seder, tractates in seders.items():
    for tractate in tractates:
        # Construct the URL for the tractate's English text
        url = f"{base_url}/{seder}/{tractate}/English/William Davidson Edition - English.txt".replace(" ", "%20")
        logging.info(f"Fetching {tractate} from {seder}")

        try:
            # Fetch the tractate text with a timeout
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            text = response.text

            # Append the text to the master file
            with open(master_filename, "a") as master_file:
                master_file.write(f"---{tractate}---\n{text}\n\n")
            logging.info(f"Successfully fetched {tractate} from {seder}")

        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to fetch {tractate} from {seder}. Error: {e}")

print(f"Master text file '{master_filename}' has been created.")