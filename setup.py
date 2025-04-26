from setuptools import setup, find_packages

setup(
    name="doc_quality",
    version="0.1.1",
    description="A Python library for evaluating documentation quality using 14 metrics.",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="Sristy Sumana Nath",
    author_email="sristy.sumana@usask.ca",
    packages=find_packages(),
    install_requires=[
        "nltk",
        "spacy",
        "textstat",
        "pandas",
        "beautifulsoup4",
        "scikit-learn"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
