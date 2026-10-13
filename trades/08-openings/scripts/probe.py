import pymupdf,sys
d=pymupdf.open(sys.argv[1]); p=d[int(sys.argv[2])]
print(p.rect, 'images',len(p.get_images()), 'drawings',len(p.get_drawings()), 'annots',len(list(p.annots())))
print(p.get_text()[:500])
