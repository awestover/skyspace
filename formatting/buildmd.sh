python3 "/Users/alekwestover/Desktop/math/skyspace/formatting/md_envbox_augment.py" "$PWD/readme.md"
pandoc --mathjax data/readme.aug.md -o content.html 
cp "/Users/alekwestover/Desktop/math/skyspace/formatting/index.html" "$PWD/index.html"
echo "$PWD/readme.md compiled from augmented markdown to html"
