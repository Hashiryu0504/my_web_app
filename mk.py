import os
import csv

def write_image_filenames_to_csv(directory, csv_filename):
    # Get a list of image files in the directory
    image_files = [f for f in os.listdir(directory) if f.endswith('.png')]
    
    # Open the CSV file for writing
    with open(csv_filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
        csv_writer = csv.writer(csvfile)
        
        # Write header
        csv_writer.writerow(['名前', 'ファイル名', 'なし'])
        
        # Write image file information
        for image_file in image_files:
            name = os.path.splitext(image_file)[0]
            csv_writer.writerow([name, directory+image_file, 'なし'])

# Usage example
directory = 'static/火属性'  # Replace with the path to your image folder
csv_filename = 'characters.csv'
write_image_filenames_to_csv(directory, csv_filename)
print(4)