from setuptools import setup, find_packages

setup(
    name='nlp_preprocess',
    version='0.1',
    packages=find_packages(),
    install_requires=['nltk'],
    description='Basic NLP text cleaning tool: stopword removal, stemming, lemmatization.',
    author='Rayyan Ahmed',
    author_email='your.email@example.com',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)

