from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('requirements.txt') as file:
    REQUIREMENTS = file.read()

setup(
    name='mortgage',
    version='1.0.1',
    description='Mortgage Calculator',
    long_description=README,
    author='Austin McConnell',
    author_email='austin.s.mcconnell@gmail.com',
    url='https://github.com/austinmcconnell/mortgage',
    packages=find_packages(exclude='tests'),
    install_requires=REQUIREMENTS,
    license='MIT license',
    zip_safe=False,
    keywords='mortgage',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests'
)
