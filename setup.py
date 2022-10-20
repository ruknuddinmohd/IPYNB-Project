from encodings.utf_8 import encode
import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "IPYNBrender"
AUTHOR_USER_NAME = "ruknuddinmohd"
SRC_REPO = "IPYN-Project"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email="ruknuddinmohd@gmail.com",
    description="Its IPYNBrender library",
    long_description= long_description,
    long_description_content= "text/markdown",
    url=f"http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker":f"http://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"
    },
    package_dir={"","src"},
    packages=setuptools.find_packages(where="src")
)