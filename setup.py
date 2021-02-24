from setuptools import setup, find_packages

# @see: https://stackoverflow.com/questions/58533084/what-keyword-arguments-does-setuptools-setup-accept
# @see: https://docs.python.org/3.7/distutils/setupscript.html#additional-meta-data
setup(
    name="Funplot",
    version="1.1.0",
    author="mastro-elfo",
    author_email="francesco.209@gmail.com",
    maintainer="mastro-elfo",
    maintainer_email="francesco.209@gmail.com",
    description="Plot simple function graphs",
    long_description="file: README.md, LICENSE",
    classifiers="Environment :: Console",
    keywords="cli, graph, plot",
    license="MIT",
    platform="any",
    provides="funplot",
    packages=find_packages(),
    install_requires=[
        "click==7.1.2",
        "cycler==0.10.0",
        "kiwisolver==1.3.1",
        "matplotlib==3.3.4",
        "numpy==1.20.1",
        "pandas==1.2.2",
        "Pillow==8.1.0",
        "pyparsing==2.4.7",
        "python-dateutil==2.8.1",
        "pytz==2021.1",
        "six==1.15.0",
    ],
    entry_points={"console_scripts": ["funplot=funplot.main:cli"]},
)
