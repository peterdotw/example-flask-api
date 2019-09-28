from setuptools import setup

setup(
    name='music_flask_api',
    packages=['music_flask_api'],
    include_package_data=True,
    install_requires=[
        'flask',
        'python-dotenv',
        'mongoengine',
        'dnspython'
    ],
)
