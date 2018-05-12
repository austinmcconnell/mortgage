from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

setup(
    name='mortgage',
    version='1.0.1',
    description='Mortgage Calculator',
    long_description=README,
    author='Austin McConnell',
    author_email='austin.s.mcconnell@gmail.com',
    url='https://github.com/austinmcconnell/mortgage',
    packages=find_packages(exclude='tests'),
    install_requires=[],
    extras_require={
        'develop': ['bumpversion>=0.5.3,<1.0.0',
                    'pytest>=3.2.1,<4.0.0',
                    'pytest-cov>=2.5.1,<3.0.0',
                    'twine>=1.11.0,<2.0.0']
    },
    license='MIT license',
    zip_safe=False,
    keywords='mortgage',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
    test_suite='tests'
)
