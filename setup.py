import setuptools

with open("readme.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name='geov',
    version='0.0.1',
    author="Better Planet Investments and labml.ai",
    author_email="contact@labml.ai",
    description="The GeoV model is a large langauge model designed by Georges Harik and uses Rotary Positional Embeddings with Relative distances (RoPER). We have shared a pretrained 9B parameter model.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/geov-ai/geov",
    packages=setuptools.find_packages(exclude=(
        'labml', 'labml.*',
        'labml_samples', 'labml_samples.*',
        'labml_helpers', 'labml_helpers.*',
        'test',
        'test.*',
    )),
    install_requires=[
        'transformers',
        'torch',
        'sentencepiece',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    keywords='machine learning',
)
