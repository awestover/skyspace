DIR=/home/alek/Desktop/art/skyspace/formatting
[ ! -d "data" ] && mkdir data
[ ! -f "toc.txt" ] && touch toc.txt
[ ! -f "description.md" ] && touch description.md
python3 "$DIR/md_envbox_augment.py" "$PWD/readme.md"
python3 "$DIR/siteToc.py" "$PWD/toc.txt"
pandoc --mathjax data/readme.aug.md -o data/content.html 
cp "$DIR/index.html" "$PWD/index.html"
echo "$PWD/readme.md compiled from augmented markdown to html"
