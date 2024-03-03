# Bulbasaur Counter

This code is designed to count the number of Bulbasaurs in images where other Pokémon might be present, excluding those other Pokémon from the count. The counting is based on image processing techniques, particularly contour detection and morphological operations.

## How it Works

1. **Image Brightness Check**: Initially, the brightness of the image is checked. If the image is too dark, it is lightened.
2. **Thresholding and Pre-processing**: Adaptive Gaussian thresholding is applied to the grayscale image to obtain binary images. This helps in identifying the dots representing Bulbasaurs.
3. **Morphological Operations**: Morphological operations like erosion and dilation are performed to merge the dots into Bulbasaur shapes, eliminating noise and separating merged Bulbasaurs.
4. **Contour Detection**: Contours are detected on the processed image.
5. **Counting Bulbasaurs**: The number of contours is counted, excluding the largest contour (which usually corresponds to the image edge) and small contours (which may represent other Pokémon).
6. **Visualization**: The contours of identified Bulbasaurs are drawn on the original image for visual verification.

## Code Components

- **`calculate_brightness(image)`**: Calculates the brightness of an image.
- **`is_dark(image, threshold)`**: Checks if the image is dark based on a threshold.
- **`lighten_image(image, factor)`**: Lightens the image.
- **`erode_dilate(img)`**: Performs erosion and dilation operations.
- **`count_contours(contours)`**: Counts the number of contours representing Bulbasaurs.
- **Main Loop**: Iterates over a set of images, applies the above operations, and counts Bulbasaurs in each image.

## Mean Absolute Error (MAE)

Mean Absolute Error (MAE) is a metric used to evaluate the performance of a prediction model. It measures the average absolute difference between the predicted values and the actual values. In the context of this code, MAE is used to quantify how accurate the Bulbasaur counting algorithm is across a set of images. In this implementation, the MAE is calculated to be 0, indicating perfect accuracy.

## Usage

To use this code:

1. Ensure you have Python installed along with required packages (`numpy`, `opencv-python`, `matplotlib`).
2. Clone the repository.
3. Place the images you want to analyze in a folder named `pictures` within the cloned repository.
4. Run the script. The output will display the number of Bulbasaurs counted in each image and the Mean Absolute Error (MAE) across all images.

## Results

![picture_6](https://github.com/lara-petkovic/BulbasaurCounter/assets/116621727/56910cac-7fe5-49e7-b363-7bf819e27a2e)

![picture_10](https://github.com/lara-petkovic/BulbasaurCounter/assets/116621727/68034c8b-596a-4275-aa3c-8177c914b6b7)
