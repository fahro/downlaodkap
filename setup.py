from setuptools import setup

setup(
    name='downloadkap',
    description="A library to download pdf attachemnts from announcments about Turkish companies as pdf files",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
       "Programming Language :: Python",
    ],
    packages=['downloadkap',],
    keywords='pdf scraping Turkish companies',
    author='Fahrudin Halilovic',
    author_email='fahrudin.halilovic@gmail.com',
    url='http://github.com/fahro/downloadkap',
    license='MIT',
    namespace_packages=[],
    test_suite='nose.collector',
    install_requires=[
        'click',
        'requests',
        'lxml',
    ],
    entry_points='''
        [console_scripts]
        start_download_kap = downloadkap.cli:enter
    ''',

)
