import os

def generate_markdown(image_folder='textures', output_file='textures_display.md', img_width=400):
    # Define a list of filenames to exclude
    excluded_files = {'gui_arrow_blank.png', 'mobs_npc_shop_icon.png'}

    # Open the markdown file for writing
    with open(output_file, 'w') as md_file:
        # Write the table header
        md_file.write('# 💁‍♀️ NPC Skins\n\n')
        md_file.write('| Skin | Dateiname |\n')
        md_file.write('| ------- | -------- |\n')

        # Loop through each file in the image folder
        for img_file in sorted(os.listdir(image_folder)):
            # Check if the file is an image and is not in the excluded list
            if img_file.lower().endswith(('.png')) and img_file not in excluded_files:
                img_path = os.path.join(image_folder, img_file)

                # HTML <img> tag for the image with specified width
                img_html = f'<img src="{img_path}" alt="{img_file}" width="{img_width}"/>'

                # Write a row in the markdown table with HTML for the image
                md_file.write(f'| {img_html} | {img_file} |\n')

    print(f"Markdown file '{output_file}' generated successfully with images from '{image_folder}', excluding: {excluded_files}")

# Run the function
generate_markdown()
