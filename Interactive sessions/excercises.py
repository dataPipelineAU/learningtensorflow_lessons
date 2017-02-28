
from PIL import Image
from io import BytesIO

# read data from string
im = Image.open(BytesIO(result))
im