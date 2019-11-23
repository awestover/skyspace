python3 /Users/alekwestover/Desktop/math/skyspace/augmd/md_envbox_augment.py "$PWD/readme.md"
pandoc --mathjax -s data/readme.aug.md metadata.yaml -o index.html --css data/pandoc.css --css data/envbox.css 
cp /Users/alekwestover/Desktop/math/skyspace/augmd/envbox.css "$PWD/data"
cp /Users/alekwestover/Desktop/math/skyspace/augmd/pandoc.css "$PWD/data"
echo "compiled augmented md file to html"
