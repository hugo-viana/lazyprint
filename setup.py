import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("VERSION", "r", encoding="utf-8") as fh:
    version = fh.read()

setuptools.setup(
    name="lazyprint",
    version=version,
    author="Hugo Viana",
    author_email="hugosemianoviana@gmail.com",
    description="Lazy python print utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hugo-viana/lazyprint",
    project_urls={
        "Bug Tracker": "https://github.com/hugo-viana/lazyprint/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)