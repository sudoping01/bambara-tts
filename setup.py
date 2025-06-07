import os
from setuptools import find_packages, setup

this_directory = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="maliba_ai",
    version="0.1.0",
    author="Maliba-AI Engineering Team",  
    author_email="contact@maliba-ai.com",  
    description="Bambara Text-to-Speech system using Maliba-AI models",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MALIBA-AI/bambara-tts",  
    project_urls={
        "Bug Tracker": "https://github.com/MALIBA-AI/bambara-tts/issues",
        "Documentation": "https://github.com/MALIBA-AI/bambara-tts/wiki",
        "Source Code": "https://github.com/MALIBA-AI/bambara-tts",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Multimedia :: Sound/Audio :: Speech",
        "License :: OSI Approved :: MIT License",  
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    
    install_requires=[
        "unsloth==2025.5.9",  
        "bitsandbytes==0.46.0",
        "einops==0.8.1",
        "einx==0.3.0",
        "numpy==2.2.3",
        "omegaconf==2.3.0",
        "packaging==24.2",
        "safetensors==0.5.2",
        "soundfile==0.12.1",
        "soxr==0.5.0.post1",
        "torch==2.5.1",
        "torchaudio==2.5.1",
        "transformers", 
        "huggingface_hub==0.20.0"
       
    ],

    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.950",
            "isort>=5.10.0",
            "pre-commit>=2.17.0",
        ],
        "docs": [
            "sphinx>=4.0.0",
            "sphinx-rtd-theme>=0.5.0",
        ],
    },
    keywords=[
        "bambara",
        "tts",
        "text-to-speech",
        "speech synthesis",
        "maliba-ai",
        "artificial intelligence",
        "machine learning",
        "natural language processing",
    ],
    include_package_data=True,
    zip_safe=False,
)


