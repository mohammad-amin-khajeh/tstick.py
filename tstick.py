#!/usr/bin/env python

from subprocess import call
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
    "-s",
    "--start",
    metavar="",
    default="00:00:00",
    help="specify the starting time of video stickers('only works on videos').",
)

parser.add_argument(
    "-d",
    "--duration",
    metavar="",
    default="00:00:02.950",
    help="specify the duration of the video sticker.",
)

parser.add_argument(
    "files",
    metavar="",
    nargs="+",
)

args = parser.parse_args()


def check(file: str) -> bool:
    is_valid = filetype.is_image(file) or filetype.is_video(file)
    if is_valid:
        return True
    else:
        return False


def requirements():
    if not path.exists(args.output):
        makedirs(args.output, exist_ok=True)


def determine_file_type(file: str) -> str:
    if filetype.is_image(file):
        return "image"
    elif filetype.is_video(file):
        return "video"
    else:
        raise ValueError


def convert(file_type: str, file: str, base_name: str) -> None:
    extension = base_name.split(".")[-1]
    output_file = base_name.removesuffix(extension)
    if file_type == "image":
        img = Image.open(file)
        img.thumbnail((512, 512))
        img.save(f"{args.output}/{output_file}webp")
        print(f"{base_name} has been converted")
    else:
        call(
            f"ffmpeg -ss {args.start} -t {args.duration} -an -i '{file}' -c:v libvpx-vp9 -b:v 500k -vf scale=512:-2 -r 30 '{args.output}/{output_file}webm'",
            shell=True,
        )


def main():
    for file in args.files:
        base_name = file.split("/")[-1]
        if not check(file):
            continue
        requirements()
        file_type = determine_file_type(file)
        convert(file_type, file, base_name)


if __name__ == "__main__":
    main()
