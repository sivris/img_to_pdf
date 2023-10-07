## Python Image to PDF Converter

This Python application converts images to PDF files. It is a simple app that I created for my mother, who wanted an easy way to convert her images to PDF.

The app uses the following Python libraries:
* `img2pdf`: To convert the images to PDF
* `datetime`: To generate a timestamp for the output PDF file
* `os`: To interact with the operating system
* `tkinter`: To create the graphical user interface (GUI)
* `pillow`: To process the image files

**Usage**

1. Run the `make_PDF.py` file.
2. In the GUI window, select the image that you want to convert.

The app will then create a new PDF file containing the selected image. The output PDF file will be saved in the Desktop.

**Example**

```python
python make_PDF.py
```

**Distribution**

The repository also contains a zip file (`dist`) that contains the executable for the app. To run the executable, simply unzip the file and then double-click on the `make_PDF.exe` file.

**Contributing**

If you have any suggestions or bug reports, please feel free to create a new issue on GitHub.

**Thanks**

I would like to thank the developers of the `img2pdf`, `datetime`, `os`, `tkinter`, and `pillow` libraries for making it possible to create this app.
