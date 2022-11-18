DIR=/home/alek/Desktop/art/skyspace
feed_name=$(date +'%m-%d-%y')-feed
echo "making $DIR/$feed_name"
mkdir $DIR/$feed_name
touch $DIR/$feed_name/toc.txt
touch $DIR/$feed_name/readme.md
touch $DIR/$feed_name/description.md

