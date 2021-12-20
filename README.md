TPA Image Cropper

===========
This script uses imagemagick to crop the viewer frame on Concentriq screenshots from Lambdatest for TPA testing.

## Lambdatest Image Specs
-Windows 10
-1920 x 1080 resolution 
-Chrome 86, latest, Edge 86, latest

## Directions
-Install imagemagick, python, and wand
https://www.pythonpool.com/imagemagick-python/
-Add desired images from Lambdatest to the Images folder
-Run script
-512x512px cropped images will be saved to the CroppedImages folder

### Warning
This script is only verified to crop images that will match those taken with the Phillips Viewer. If/when this script is needed for TPA testing with another viewer, it will need to be verified and may need to be updated.