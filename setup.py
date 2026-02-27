from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dais10mini",
    version="1.1.7",
    description="DAIS-10 Mini - Lightweight data quality analysis library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Dr. Usman Zafar",
    author_email="usman19zafar@gmail.com",
    url="https://github.com/usman19zafar/DAIS10_Pyton_Library_Project",
    project_urls={
        "Bug Tracker": "https://github.com/usman19zafar/DAIS10_Pyton_Library_Project/issues",
        "Documentation": "https://github.com/usman19zafar/DAIS10_Pyton_Library_Project#readme",
        "Source Code": "https://github.com/usman19zafar/DAIS10_Pyton_Library_Project",
    },
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[],
    extras_require={
        "dev": ["pytest", "black", "flake8"],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Financial and Insurance Industry",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Office/Business",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    keywords="data-quality governance semantic-analysis dais10 completeness",
    license="Apache License 2.0",
)
