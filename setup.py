from setuptools import setup, find_packages


# allows to get version via python setup.py --version
__version__ = "dev"

install_requires = [
    "pyyaml",
    "tqdm",
    "Pillow",
    "chainer",
    "numpy",
    "pandas",  # for csv dataset and eval pipeline
    "fastnumbers",  # for dict utils
]

install_full = [  # for extra functionality
    "streamlit > 0.49",  # for edexplore
    "psutil",  # for edlist
    "scipy<1.4",  # TODO pinned dependency of scikit-image; only until 1.4.1 is out and fixes https://github.com/scipy/scipy/issues/11237
    "scikit-image",  # for ssim in image_metrics.py
    "black",  # for formatting of code
    "matplotlib",  # for plot_datum
]
install_docs = [  # for building the documentation
    "sphinx >= 1.4",
    "sphinx_rtd_theme",
    "better-apidoc",
]
install_test = install_full + [  # for running the tests
    "pytest",
    "pytest-cov",
    "coveralls",
    "scipy<1.4",  # TODO pinned dependency of scikit-image; only until 1.4.1 is out and fixes https://github.com/scipy/scipy/issues/11237
    "scikit-image",  # for some tf tests (also for image_metrics.py but lets avoid heavy dependency for a single functionality)
]
extras_require = {"full": install_full, "docs": install_docs, "test": install_test}


setup(
    name="edflow",
    version=__version__,
    description="Logistics for Deep Learning",
    url="https://github.com/pesser/edflow",
    author="Mimo Tilbich et al.",
    author_email="patrick.esser@iwr.uni-heidelberg.de, johannes.haux@iwr.uni-heidelberg.de",
    license="MIT",
    packages=find_packages(),
    package_data={"": ["*.yaml"]},
    install_requires=install_requires,
    extras_require=extras_require,
    zip_safe=False,
    scripts=[
        "edflow/edflow",
        "edflow/edcache",
        "edflow/edlist",
        "edflow/edeval",
        "edflow/edsetup",
        "edflow/edexplore",
    ],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
)
