import requests
from pixoo import Pixoo, SimulatorConfig
from PIL import Image, ImageDraw, ImageFont
import time
import os
from dotenv import load_dotenv

# Load .env variables at the start of the script
load_dotenv()

def fetch_chess_stats(username):
    url = f"https://api.chess.com/pub/player/{username}/stats"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch stats. Status code: {response.status_code}")
        return None

def create_text_image(text, font_size, text_color, image_size):
    image = Image.new('RGBA', image_size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('arial.ttf', font_size)
    text_width, text_height = draw.textsize(text, font=font)

    # Adjust these values as needed for positioning
    x = 30
    y = 40

    draw.text((x, y), text, fill=text_color, font=font)
    return image

def combine_images(background, overlay, position):
    background.paste(overlay, position, overlay)
    return background

def main():
    username = os.getenv("CHESS_USERNAME")
    pixoo_ip = os.getenv("PIXOO_IP_ADDRESS")

    pixoo = Pixoo(pixoo_ip, simulated=False, simulation_config=SimulatorConfig(16))

    refresh_interval = 300  # Refresh interval in seconds
    while True:
        stats = fetch_chess_stats(username)
        if stats and 'chess_rapid' in stats and 'last' in stats['chess_rapid']:
            rating = stats['chess_rapid']['last']['rating']
            text = f"{rating}"
        else:
            text = "No rating available"

        background_image_path = os.path.join(os.path.dirname(__file__), "background.png")
        background_image = Image.open(background_image_path)

        text_color = (255, 255, 255, 255)  # White color
        font_size = 16  # Adjust font size as needed
        text_image = create_text_image(text, font_size, text_color, background_image.size)

        combined_image = combine_images(background_image, text_image, (0, 0))

        pixoo.draw_image(combined_image)
        pixoo.push()

        # Countdown for the next refresh
        for remaining in range(refresh_interval, 0, -1):
            print(f"Next rating refresh in: {remaining} seconds", end='\r')
            time.sleep(1)

if __name__ == "__main__":
    main()
