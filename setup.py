import setuptools
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ ="0.0.0"

REPO_Name = "textSummerizer"
AUTHOR_USER_NAME = "piyushtwri"
SRC_REPO = "text_summerizer"
AUTHOR_email = "piyush.hyd@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_email,
    description="Text Summarizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_Name}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_Name}/issues",
    },
package_dir={"":"src"},
packages=setuptools.find_packages(where="src")
)
