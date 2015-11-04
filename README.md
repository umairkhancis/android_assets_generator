# android_assets_generator
The script to generate android assets given in xxhdpi for other buckets xhdpi, hdpi, mdpi

# Instructions
1- Install this anywhere you want 
ImageMagick-6.8.9-3-Q16-x64-dll.exe from  http://www.imagemagick.org/script/binary-releases.php#windows

2- Run this command on the windows:
shell asset_generator.py -res [path/to/res] -im [path/to/image_magick]

# Note: 
1- res directory should be same as android res dir contaning all the buckets folder 
as res/drawable-xxhdpi, res/drawable-xhdpi, res/drawable-hdpi, res/drawable-hdpi

2- This utility only down converts images from xxhdpi to xhdpi, hdpi and mdpi
