import streamlit as st
from PIL import Image


def resize_image(image, width, height):
    resized_image = image.resize((width, height))
    return resized_image


def convert_to_grayscale(image):
    grayscale_image = image.convert("L")
    return grayscale_image


def crop_image(image, left, top, right, bottom):
    cropped_image = image.crop((left, top, right, bottom))
    return cropped_image


def rotate_image(image, angle):
    rotated_image = image.rotate(angle)
    return rotated_image


def main():
    st.title("Image Processing App")

    uploaded_file = st.file_uploader(
        "Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:

        image = Image.open(uploaded_file)

        st.image(image, caption="Original Image", width=500)

        options = st.multiselect("Select image processing techniques",
                                 ["Resize", "Grayscale Conversion", "Image Cropping", "Image Rotation"])

        processed_image = image

        if "Resize" in options:
            width = st.number_input(
                "Enter width", value=image.width, min_value=1)
            height = st.number_input(
                "Enter height", value=image.height, min_value=1)
            processed_image = resize_image(processed_image, width, height)

        if "Grayscale Conversion" in options:
            processed_image = convert_to_grayscale(processed_image)

        if "Image Cropping" in options:
            left = st.number_input(
                "Enter left coordinate", value=0, min_value=0, max_value=image.width-1)
            top = st.number_input("Enter top coordinate",
                                  value=0, min_value=0, max_value=image.height-1)
            right = st.number_input(
                "Enter right coordinate", value=image.width, min_value=left+1, max_value=image.width)
            bottom = st.number_input(
                "Enter bottom coordinate", value=image.height, min_value=top+1, max_value=image.height)
            processed_image = crop_image(
                processed_image, left, top, right, bottom)

        if "Image Rotation" in options:
            angle = st.number_input(
                "Enter rotation angle", value=0, min_value=-360, max_value=360)
            processed_image = rotate_image(processed_image, angle)

        st.image(processed_image, caption="Processed Image", width=500)


if __name__ == "__main__":
    main()
