from setuptools import setup, find_packages

setup(
    name="poc",
    version="1.0.0",
    author="Vinicius",
    description="Prova de Conceito com arquitetura Cliente-Servidor",
    packages=find_packages(),
    python_requires='>=3.7',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'start-server=server:iniciar_servidor',
            'start-client=client:conectar_servidor'
        ]
    },
)
