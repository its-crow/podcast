from setuptools import setup

setup(
    name="podcast",
    version="0.4",
    packages=["podcast"],
    install_requires=[
        "yt-dlp",
    ],
    entry_points={
        "console_scripts": [
            "podcast=podcast.podcast:main",
        ],
    },
    include_package_data=True,
)