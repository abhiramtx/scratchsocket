import setuptools

setuptools.setup(
    name="scratchsocket",
    url="none",
    version="0.1.0",
    author="Abhiram V",
    license="MIT",
    description="Establish cloud connections with scratch.mit.edu!",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["websocket-client", "requests", "numpy"]
)