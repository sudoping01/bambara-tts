from setuptools import setup, find_packages

setup(
    name='maliba_ai',
    version='0.1.0',
    description='Bambara Text-to-Speech system using Maliba-AI models',
    packages=find_packages(),
    install_requires=[
        'einops==0.8.1',
        'einx==0.3.0',
        'numpy==2.2.3',
        'omegaconf==2.3.0',
        'packaging==24.2',
        'safetensors==0.5.2',
        'soundfile==0.12.1',
        'soxr==0.5.0.post1',
        'torch==2.5.1',
        'torchaudio==2.5.1',
        'tqdm==4.66.5',
        'transformers==4.46.2',
        'gradio==5.18.0',
        'unsloth',
    ],
    python_requires='>=3.8',
)