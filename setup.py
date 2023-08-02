import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

__version__ ="0.0.0.0"
REP0_NAME = "Text-Summarizer-NLP"
AUTHOR_USERNAME = "jeanarm"
SRC_REPO = "textSummarizer"

setuptools.setup(
    name=REP0_NAME,
    version=__version__,
    author=AUTHOR_USERNAME,
    author_email="nizigiarmel2015@gmail.com",
    description="Text Summarizer packages installation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/{AUTHOR_USERNAME}/{REP0_NAME}",
    
    project_urls={
          "Bug Tracker": "https://github.com/{AUTHOR_USERNAME}/{REP0_NAME}/issues",

    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
    
)