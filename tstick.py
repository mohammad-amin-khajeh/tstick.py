#!/usr/bin/env python

from PIL import Image
import argparse
from os import makedirs, path, getenv
import filetype

home = getenv("HOME")

parser = argparse.ArgumentParser(
    description="Convert images to telegram stickers on the fly.",
    usage="tstick.py [images]",
)

parser.add_argument(
    "-o",
    "--output",
    metavar="",
    default=f"{home}/Pictures/tstickers",
    help="specify the output directory(default is ~/Pictures/tstickers).",
)

parser.add_argument(
    "images",
    metavar="",
    nargs="+",
)

args = parser.parse_args()


def requirements():
    if not path.exists(args.output):
        makedirs(args.output, exist_ok=True)


def check(file: str) -> bool:
    is_image = filetype.is_image(file)
    if is_image:
        return True
    else:
        return False


def convert(image: str, file_name: str) -> None:
    extension = file_name.split(".")[1]
    output_file = file_name.removesuffix(extension)
    img = Image.open(image)
    img.thumbnail((512, 512))
    img.save(f"{args.output}/{output_file}webp")
    print(f"{file_name} has been converted")


def main():
    for image in args.images:
        image_file = image.split("/")[-1]
        if not check(image):
            continue
        requirements()
        convert(image, image_file)


if __name__ == "__main__":
    main()
