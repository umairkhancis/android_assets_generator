
# !/usr/bin/python


import os
import argparse

# ==================================================================================================================================================

class AssetsGenerator:
	def __init__(self, resPath, image_magic_path):
		self.mResPath = resPath
		self.image_magic_path = image_magic_path;

	def __getFileListing(self):
		assetsPath = self.mResPath + '\\drawable-xxhdpi'
		return os.listdir(assetsPath)

	def generate(self):
		for fileName in self.__getFileListing():
			cmd = u'drawable_convert.py -i {0} -d {1}\drawable-mdpi -d {1}\drawable-hdpi -d {1}\drawable-xhdpi {1}\drawable-xxhdpi\{2}'.format(self.image_magic_path, self.mResPath, fileName)
			os.system(cmd)

# ================================================================================================================================================
def getWindowsPath(path):
	return path.replace("\\", '\\\\')

''' Main Entry Point '''

if __name__ == "__main__" :	
	
	''' Parse command line arguments '''
	parser = argparse.ArgumentParser(description='Generates Drawable Icons for Android Apps')
	parser.add_argument('-res', dest='res', action='append', required=True, help='resource directory')
	parser.add_argument('-im', dest='image_magic_path', action='append', required=True, help='ImageMagick directory')

	args = parser.parse_args()

	res = getWindowsPath(args.res[0])
	image_magic_path = getWindowsPath(args.image_magic_path[0])
	ag = AssetsGenerator(res, image_magic_path)
	ag.generate()


