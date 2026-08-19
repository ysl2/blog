# ffmpeg

## Convert video to pngs

```bash
ffmpeg -i input.mp4 output-frames/frame-%05d.png
```

## Convert pngs to video

```bash
ffmpeg -framerate 30 -pattern_type glob -i 'output-frames/*.png' -c:v libx264 -crf 1 -pix_fmt yuv420p output.mp4
```

## Crop pngs to 16:8.15 aspect ratio

```bash
mkdir output-frames-16_8.15

# NOTE: If you want to scale a single file, you can just replace the `crop` filter below with `scale`.
ffmpeg -i output-frames/frame-01935.png -vf "crop=iw:iw*8.15/16" "output-frames-16_8.15/frame-01935.png"

# Or batch process all pngs in a directory
for f in output-frames/*.png; do
    ffmpeg -i "$f" -vf "crop=iw:iw*8.15/16" "output-frames-16_8.15/$(basename "$f")"
done
```

## Convert pngs to gif

```bash
ffmpeg -framerate 30 -pattern_type glob -i '*.png' output.gif
```

## MOV to flac

```bash
ffmpeg -i IMG_9300.MOV -map 0:a:0 -vn -c:a flac IMG_9300.flac
```

## Compress video size (From H.264 to H.265)

```bash
# ffmpeg -i "input.mov" -c:v libx265 -crf 20 -c:a copy "output.mp4"

# NOTE: For more compress efficiency, use this (the default crf is 28, lower is better quality but bigger file size):
ffmpeg -i 'input.mov' -c:v libx265 -c:a copy 'output.mp4'
```
