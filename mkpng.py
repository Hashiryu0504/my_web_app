import os
import csv
from PIL import Image, ImageDraw, ImageFont

def generate_character_data(attribute):
    os.makedirs(f'static/{attribute}', exist_ok=True)
    character_data = []
    for i in range(1, 31):
        image = Image.new('RGB', (200, 200), color=(73, 109, 137))
        d = ImageDraw.Draw(image)
        font = ImageFont.load_default()
        d.text((10, 10), str(i), fill=(255, 255, 0), font=font)
        image_path = f"static/{attribute}/character_{i}.png"
        image.save(image_path)
        character_data.append({"name": f"キャラ{i}", "image_path": image_path})
    
    csv_file_path = f"static/{attribute}/characters.csv"
    with open(csv_file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "image_path"])
        writer.writeheader()
        writer.writerows(character_data)
    return character_data

attributes = ["火属性", "水属性", "風属性", "光属性", "闇属性"]
all_character_data = {}

for attribute in attributes:
    all_character_data[attribute] = generate_character_data(attribute)
