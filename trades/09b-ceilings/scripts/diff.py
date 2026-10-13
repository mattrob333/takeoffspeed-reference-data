import pymupdf, glob, collections, sys
f=glob.glob('/home/user/takeoffspeed-reference-data/source/markups/*_p01-10.pdf')[0]
mp=pymupdf.open(f)[4]
sp=pymupdf.open('/home/user/takeoffspeed-reference-data/source/drawings/Architectural/A-130-REFLECTED-CEILING-PLAN-Rev.0.pdf')[0]
print(mp.rect, sp.rect, sp.rotation)
# images in markup page
for im in mp.get_images(full=True): print(im)
print(mp.get_image_info())
