from setuptools import setup, find_packages

setup(
    name='discordus',
    version='0.2.0',
    author='Ryan Salem',
    author_email='Ryansalem2013@gmail.com',
    description='A simpler version of discord.py',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
