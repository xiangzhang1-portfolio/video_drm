#!/usr/bin/env bash
# Requires: bash, ffmpeg, bento4

KID=432646294A404E635266546A576E5A72
KEY=2D4A614E645266556A586E3272357538

rm -rf dash/*

for filename in `ls source`; do
    echo converting $filename
    basename=${filename%.*}
    ffmpeg -hide_banner -loglevel panic -i source/$filename -vcodec h264 -vf scale=1024:-2 TMP1.mp4
    mp4fragment TMP1.mp4 TMP2.mp4
    mp4encrypt --method MPEG-CENC --key 1:$KEY:random --property 1:KID:$KID --key 2:$KEY:random --property 2:KID:$KID  --global-option mpeg-cenc.eme-pssh:true TMP2.mp4 TMP3.mp4
    mp4dash -o dash/$basename/ TMP3.mp4
    rm TMP*
done
