from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='easycnn',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'tensorflow>=2.0',
        'pandas',
        'matplotlib',
        'scikit-learn'
    ],
    description='EasyCNN: A library to create, train, and use custom CNN models with ease.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Sidhant Yadav',
    author_email='supersidhant10@gmail.com',
    url='https://github.com/yadavsidhant/easycnn',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6',
    project_urls={
        'Bug Tracker': 'https://github.com/yadavsidhant/easycnn/issues',
        'Documentation': 'https://github.com/yadavsidhant/easycnn#readme',
        'Youtube': 'https://www.youtube.com/@SidhantKYadav',
    },
)