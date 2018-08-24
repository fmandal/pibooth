#! /bin/sh

#convert $1 -bordercolor "#FFFFFF" -border 10x10 new1.jpg
#convert $2 -bordercolor "#FFFFFF" -border 10x10 new2.jpg
#convert $3 -bordercolor "#FFFFFF" -border 10x10 new3.jpg
#convert $4 -bordercolor "#FFFFFF" -border 10x10 new4.jpg

#convert /home/pi/pibooth/pics/new1.jpg /home/pi/pibooth/pics/new2.jpg -append temp.jpg
#convert /home/pi/pibooth/pics/new3.jpg /home/pi/pibooth/pics/new5.jpg -append temp2.jpg
#convert temp.jpg temp2.jpg +append final.jpg

dt=$(date '+%y%m%d%H%M%S');
new="/home/pi/pibooth/pics/$dt.jpg"
real="/home/pi/pibooth/pics/$5"
montage $1 $2 $3 $4 -geometry 956x536+2+2 $5
echo $5

