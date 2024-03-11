from setuptools import find_packages, setup

from pyzolocal import __version__

setup(
    name="zolocal",
    version=__version__,
    description="A Python tool kit for interacting "
    + "with the locally hosted Zotero database.",
    url="https://github.com/allispaul/pyzotero-local",
    author="Haozhe Yang",
    author_email="yyanghaozhe@outlook.com",
    maintainer="Paul VanKoughnett",
    maintainer_email="allispaul@gmail.com",
    license="GNU General Public License v3",
    include_package_data=True,
    install_requires=[
        "fire",
        "whoosh",
    ],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
    ],
    keywords="zotero sqlite",
    packages=find_packages(),
    entry_points={"console_scripts": ["zotero = pyzolocal.cli.zolocal:main"]},
)
