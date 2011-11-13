Python Image Cropper
===================

This image cropper provides a primitive command line interface to the crop function of the Python Image Library (PIL).

Example Usage:
-------------

```Shell
cd ~/Images
for f in *.jpg; do ~/Code/Scripts/crop.py "$f" 0 0 430 300; done
```

Crops each jpg image file in the ~/Images directory and adds a new file with '_cropped' appended to the original filename.

Requirements:
------------

* Python 2.7 (Only version I have tested)
* Python Image Library http://www.pythonware.com/products/pil/

I also had some trouble getting PIL working in my environment (OSX Lion).  I narrowed the problem down to an issue with libjpeg and solved it by doing the follow:

```Shell
# Get libjpeg v 8
curl -O http://www.ijg.org/files/jpegsrc.v8c.tar.gz
tar -zxf jpegsrc.v8c.tar.gz
cd jpeg-8c
./configure
make
sudo make install

# Re-Install PIL
curl -O http://effbot.org/downloads/Imaging-1.1.7.tar.gz
tar -zxf Imaging-1.1.7.tar.gz
cd Imaging-1.1.7
# Point to libjpeg library in setup.py
sed -i -e 's/JPEG_ROOT = None/JPEG_ROOT = \"\/usr\/local\/bin\"/g' setup.py
sudo python setup.py install
```