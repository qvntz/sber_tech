from setuptools import setup, find_packages

setup(
    name="service",
    platforms="all",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "aiohttp",
        "pydantic",
        "aiomisc",
        "python-dotenv",
        "docker-compose",
        "ansible",
        ],

    entry_points={
        'console_scripts': [
            'sber-zvuk-api = service:main',
        ]
    },
    include_package_data=True,
)

