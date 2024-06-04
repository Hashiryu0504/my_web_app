from flask import Flask, render_template, jsonify
import os
import csv

app = Flask(__name__)

def load_character_data(attribute):
    character_data = []
    csv_file_path = f"static/{attribute}/characters.csv"
    try:
        with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row)
                character_data.append(row)
    except UnicodeDecodeError:
        with open(csv_file_path, mode='r', newline='', encoding='shift_jis') as file:
            reader = csv.DictReader(file)
            for row in reader:
                character_data.append(row)
    print(f"Loaded {len(character_data)} characters for attribute {attribute}")  # デバッグ用ログ
    return character_data


attributes = ["火属性", "水属性", "風属性", "光属性", "闇属性"]
all_character_data = {attribute: load_character_data(attribute) for attribute in attributes}

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/team')
def team():
    return render_template('team.html', characters=all_character_data["火属性"], attributes=attributes)

@app.route('/characters/<attribute>')
def get_characters(attribute):
    return jsonify(all_character_data[attribute])

if __name__ == '__main__':
    app.run(debug=True)
