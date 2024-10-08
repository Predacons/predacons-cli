from setuptools import find_packages, setup
import pathlib
with open("README.md", "r") as f:
    long_description = f.read()

HERE = pathlib.Path(__file__).parent

setup(
    name="predacons_cli",
    version="0.0.100",
    description="comand line interface for Predacons",
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    # scripts=['bin/predacons-gui'],
    entry_points ={ 
        'console_scripts': [ 
            'predacons = predacons_cli.src.predacons_cli:launch'
        ]
    },
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shouryashashank/predacons-gui",
    author="shouryashashank",
    author_email="shouryashashank@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["predacons >= 0.0.125"]
,
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    python_requires=">=3.10",
)
