python3 "../formatting/md_envbox_augment.py" "$PWD/readme.md"
python3 "../formatting/siteToc.py" "$PWD/toc.txt"
pandoc --mathjax data/readme.aug.md -o data/content.html 
cp "../formatting/index.html" "$PWD/index.html"
echo "$PWD/readme.md compiled from augmented markdown to html"
