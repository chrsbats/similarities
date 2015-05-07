from distutils.core import setup

setup(
    name='similarities',
    version='0.1',
    author='C Bates',
    author_email='chrsbats@gmail.com',
    packages=['similarities'],
    scripts=[],
    url='https://github.com/chrsbats/similarities',
    license='LICENSE.TXT',
    description='A collection of similarity metrics and hashes',
    long_description='A utility library containing hashes and distance metrics used in information retrieval.',
    install_requires=[
        "scurve==0.2",
        "xxhash==0.3.2"
    ],
)
