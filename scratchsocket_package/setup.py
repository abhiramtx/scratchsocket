import setuptools

setuptools.setup(
    name="scratchsocket",
    url="https://github.com/abhiramtx/scratchsocket",
    version="0.0.1",
    author="Abhiram V",
    author_email="abhiram.tx@gmail.com",
    license="MIT",
    description="Establish simple cloud connections with scratch.mit.edu!",
    long_description="Establish simple cloud connections with scratch.mit.edu! Complete documentation: https://github.com/abhiramtx/scratchsocket",
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=["websocket-client", "requests", "numpy"],
    include_package_data=True
)

HomePage="https://github.com/abhiramtx/scratchsocket"