# tstick.py
A simple no-nonsense script that converts images and videos to telegram stickers.
input the files as parameters(globbing is accepted as well) and viola your stickers are ready!

Please note that images must have a height or width of at least 512px and as for videos they must either be square or wide(haven't added support for tall videos yet.)

The default output directory is ```"~/Pictures/tstickers"```
however you can override it with the ```-o``` flag.
some other flags are present, feel free to have a look them using the -h/--help flag.

# dependencies
- [python-filetype](https://github.com/h2non/filetype.py)
- [pillow](https://pypi.org/project/pillow/)

# tip:
send the output images to t.me/stickers to create your own sticker pack.
