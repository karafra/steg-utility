import setuptools

with open('README.md', 'r', encoding='utf-8') as readme:
    long_description = readme.read()

setuptools.setup(
    name='simple-steganography',
    author='Karafra',
    author_email='dariusKralovic@protonmail.com',
    description='Simple steganography command line utility',
    keywords='steganography, cli, utility',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/karafra/steg-utility/settings',
    project_urls={
        'Documentation': 'https://github.com/tomchen/example_pypi_package',
        'Bug Reports':
        'https://github.com/karafra/steg-utility/issues',
        'Source Code': 'https://github.com/karafra/steg-utility/settings',
        # 'Funding': '',
        # 'Say Thanks!': '',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    extras_require={
        'dev': ['check-manifest'],
    },
)

