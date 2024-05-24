import streamlit as st
import os
import requests
import json
import glob
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def create_tmp_folder():
    os.makedirs('rocket', exist_ok=True)

def download_launches():
    url = 'https://ll.thespacedevs.com/2.0.0/launch/upcoming'
    response = requests.get(url)
    with open("rocket/launches.json", "wb") as f:
        f.write(response.content)

def get_pictures():
    os.makedirs('images', exist_ok=True)
    with open("rocket/launches.json") as f:
        launches = json.load(f)

    image_urls = [launch["image"] for launch in launches["results"] if "image" in launch]

    for image_url in image_urls:
        try:
            response = requests.get(image_url)
            image_filename = image_url.split("/")[-1]
            target_file = f"images/{image_filename}"

            with open(target_file, "wb") as f:
                f.write(response.content)

        except requests.exceptions.RequestException as e:
            st.error(f"Failed to download {image_url}: {str(e)}")

def display_images():
    image_files = glob.glob('images/*')
    if image_files:
        cols = st.columns(5)
        for i, file in enumerate(image_files):
            with cols[i % 5]:
                img = mpimg.imread(file)
                st.image(img, caption=file.split('/')[-1], use_column_width=True)

def main():
    st.title("Rocket Launch Image Fetcher")
    
    if st.button("Create Temporary Folder"):
        create_tmp_folder()
        st.success("Temporary folder created.")
    
    if st.button("Download Launch Data"):
        download_launches()
        st.success("Launch data downloaded.")
    
    if st.button("Fetch Images"):
        get_pictures()
        st.success("Images fetched.")
    
    if st.button("Display Images"):
        display_images()

    images_count = len(glob.glob('images/*'))
    st.write(f"Total images downloaded: {images_count}")

if __name__ == "__main__":
    main()

# Save this as a Python script named 'rocket_launch_app.py' to run it using Streamlit.
# streamlit run rocket_launch_app.py
