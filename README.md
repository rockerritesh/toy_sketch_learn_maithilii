# Sketch App

The Sketch App is a web application that allows users to draw on a canvas and save their sketches as images. It provides a reference image for users to draw on, and they can save their modified images with a single click.

## Features

- Display a reference image for users to draw on.
- Enable users to draw on the canvas using their mouse.
- Save the modified image as a PNG file.
- Allow users to start with a fresh canvas and reference image.

## Technologies Used

- Flask - Python web framework for building the backend server.
- HTML/CSS/JavaScript - Frontend development languages for creating the user interface and interactivity.
- Canvas API - JavaScript API for drawing on the canvas element.

## Installation

1. Clone the repository:

```
git clone <repository-url>
```

2. Navigate to the project directory:

```
cd sketch-app
```

3. Create a virtual environment (optional but recommended):

```
python -m venv venv
```

4. Activate the virtual environment:

   - For Windows:

   ```
   venv\Scripts\activate
   ```

   - For Linux/Mac:

   ```
   source venv/bin/activate
   ```

5. Install the required dependencies:

```
pip install -r requirements.txt
```

6. Start the Flask development server:

```
python app.py
```

7. Open your web browser and visit `http://localhost:5000` to access the Sketch App.

## Usage

1. Upon accessing the Sketch App, you will see a canvas with a reference image displayed on the left side.

2. Use your mouse to draw on the canvas area. Click and hold the left mouse button to start drawing, and release it to stop.

3. To save the modified image, click the "Save Image" button. The modified image will be saved as a PNG file.

4. To start with a fresh canvas and reference image, click the "New Image" button. This will reload the page.

## License

The Sketch App is licensed under the [MIT License](LICENSE).

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## Acknowledgements

This app was created as a learning project and is based on various resources and tutorials available online.
