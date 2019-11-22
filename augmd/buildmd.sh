python3 /Users/alekwestover/Desktop/math/skyspace/augmd/md_envbox_augment.py "$PWD/index.md"
pandoc --mathjax -s index.aug.md metadata.yaml -o index.html --css pandoc.css --css envbox.css 
cp /Users/alekwestover/Desktop/math/skyspace/augmd/envbox.css $PWD
cp /Users/alekwestover/Desktop/math/skyspace/augmd/pandoc.css $PWD
