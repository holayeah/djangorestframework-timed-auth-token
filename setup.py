from setuptools import setup


def read(filename):
    with open(filename) as f:
        return f.read()


setup(
    name='djangorestframework-timed-auth-token',
    version='0.1.0',
    description=('An authentication token for djangorestframework that has an expiration date.'),
    long_description=read('README.rst'),
    author='Ryan Pineo',
    author_email='ryanpineo@gmail.com',
    license='MIT',
    url='https://github.com/RyanPineo/djangorestframework-timed-auth-token',
    packages=['timed_auth_token'],
    install_requires=['djangorestframework>=3.1'],
    classifiers=[
        'Framework :: Django',
        'Programming Language :: Python :: 3'
    ]
)