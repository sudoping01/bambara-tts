# MALIBA-AI Bambara TTS SDK

Welcome to the MALIBA-AI Bambara Text-to-Speech SDK! This is the **first open-source TTS system** specifically designed for the Bambara language. Whether you're building educational platforms, creating voice interfaces, or developing accessibility tools, this SDK provides professional grade Bambara speech synthesis with multiple authentic speakers.

## Table of Contents

1. [About MALIBA-AI](#about-maliba-ai)
2. [Installation](#installation)
3. [Quick Start](#quick-start)
4. [Client Initialization](#client-initialization)
5. [Basic Usage](#basic-usage)
   - 5.1 [Simple Text-to-Speech](#simple-text-to-speech)
   - 5.2 [Speaker Selection](#speaker-selection)
   - 5.3 [Advanced Configuration](#advanced-configuration)
6. [Speaker System](#speaker-system)
7. [Generation Parameters](#generation-parameters)
8. [Audio Output Options](#audio-output-options)
9. [Examples](#examples)
   - 9.1 [Educational Applications](#educational-applications)
   - 9.2 [Voice Interface Integration](#voice-interface-integration)
   - 9.3 [Batch Processing](#batch-processing)
10. [Best Practices](#best-practices)
11. [Performance Considerations](#performance-considerations)
12. [Troubleshooting](#troubleshooting)
13. [Contributing](#contributing)

---

## About MALIBA-AI

MALIBA-AI is a community driven initiative focused on developing AI solutions for Mali while ensuring no Malian is left behind by technological advances. Our mission is to break down linguistic barriers by creating AI systems that understand and speak Mali's indigenous languages.

This Bambara TTS SDK represents a breakthrough in African language technology:
- **First open-source Bambara TTS**: Pioneering accessible speech synthesis for Bambara
- **Highest accuracy available**: State-of-the-art neural architecture fine-tuned specifically for Bambara
- **Production-ready**: Built for real-world applications with optimized performance
- **Community-driven**: Developed by and for the Bambara speaking community

---

## Installation

Install the MALIBA-AI SDK using pip:

```bash
pip install maliba_ai
```

For development installations:

```bash
pip install git+https://github.com/MALIBA-AI/bambara-tts.git
```

---

## Quick Start

Get started with Bambara TTS in under a minute:

```python
from maliba_ai.tts import BambaraTTSInference
from maliba_ai.config.speakers import Bourama
import soundfile as sf

# Initialize the TTS system
tts = BambaraTTSInference()

# Generate speech from Bambara text
text = "I ni ce! N ye MALIBA-AI ye."  # "Hello! I am MALIBA-AI."
audio = tts.generate_speech(text, speaker_id=Bourama)

# Save the audio
sf.write("greeting.wav", audio, 16000)
print("Bambara speech generated successfully!")
```

---

## Client Initialization

The TTS system initializes automatically with optimal settings:

```python
from maliba_ai.tts import BambaraTTSInference

# Standard initialization
tts = BambaraTTSInference()

# With custom Hugging Face token (if needed)
tts = BambaraTTSInference(hf_token="your_token_here")
```

The system automatically:
- Detects and uses GPU acceleration when available
- Downloads required models on first use
- Loads all available speaker voices
- Optimizes memory usage for your hardware

---

## Basic Usage

### Simple Text-to-Speech

The most straightforward way to generate Bambara speech:

```python
# Basic synthesis with default speaker (Adame)
text = "Bamanankan ye kan ɲuman ye"  # "Bambara is a beautiful language"
audio = tts.generate_speech(text)
```

### Speaker Selection

Choose from our five authentic Bambara speakers:

```python
from maliba_ai.config.speakers import Adame, Moussa, Bourama, Modibo, Seydou

# Use different speakers
speakers_demo = [
    (Adame, "I ni ce, n tɔgɔ ye Adame ye"),      # "Hello, my name is Adame"
    (Moussa, "N bɛ baara kɛ sɛnɛkɛla la"),      # "I work in agriculture"
    (Bourama, "Aw ye ɲɛnɛmako"),                # "Welcome"
    (Modibo, "Kalan ka di kosɛbɛ"),             # "Learning is very good"
    (Seydou, "Aw ka se ka baara in kɛ"),        # "You can do this work"
]

for speaker, text in speakers_demo:
    audio = tts.generate_speech(text, speaker_id=speaker)
    print(f"Generated speech for {speaker.id}")
```

**Note**: Bourama is our most stable and accurate speaker, recommended for production applications.

### Advanced Configuration

Fine-tune synthesis with custom parameters (though defaults are optimized):

```python
audio = tts.generate_speech(
    text="An ka baara kɛ ɲɔgɔn fɛ",           # "Let's work together"
    speaker_id=Bourama,
    temperature=0.8,                          # Keep at 0.8 for optimal results
    top_k=50,                                # Vocabulary sampling
    top_p=1.0,                               # Nucleus sampling
    max_new_audio_tokens=2048,               # Maximum audio length
    output_filename="collaboration.wav"       # Auto-save option
)
```

---

## Speaker System

Our speaker system features five distinct Bambara voices:

```python
from maliba_ai.config.speakers import Speakers

# View all available speakers
all_speakers = Speakers.get_all_speakers()
for speaker in all_speakers:
    print(f"Speaker: {speaker.id}")

# Get specific speaker by name
bourama = Speakers.get_speaker_by_name("Bourama")

# Speaker recommendations:
# - Bourama: Most stable and accurate (recommended for production)
# - Adame: Natural conversational tone
# - Moussa: Clear pronunciation
# - Modibo: Expressive delivery
# - Seydou: Balanced characteristics
```

---

## Generation Parameters

The SDK comes with optimized default parameters that provide the best quality:

### Default Configuration
```python
# These defaults are optimized for Bambara - avoid changing unless necessary
temperature=0.8        # Optimal balance between consistency and naturalness
top_k=50              # Vocabulary selection size
top_p=1.0             # Nucleus sampling threshold
max_new_audio_tokens=2048  # Maximum audio sequence length
```

### Parameter Guidelines
- **Temperature**: Keep at 0.8. Lower values may sound robotic, higher values can introduce artifacts
- **Top-k/Top-p**: Defaults provide best quality. Experimentation often reduces accuracy
- **Max tokens**: Increase only for very long texts (splits recommended instead)

### When to Adjust Parameters
```python
# For very short texts
audio = tts.generate_speech(
    "Ce!",  # "Hello!"
    speaker_id=Bourama,
    max_new_audio_tokens=1024  # Shorter for efficiency
)

# For experimental/creative applications only
audio = tts.generate_speech(
    text,
    speaker_id=Bourama,
    temperature=0.7,  # Slightly more conservative
    top_k=40         # More focused vocabulary
)
```

---

## Audio Output Options

Handle generated audio efficiently:

```python
import numpy as np
import soundfile as sf

# Generate audio
audio = tts.generate_speech("Baara ka nɔgɔya", speaker_id=Bourama)

# Method 1: Direct file saving during generation
audio = tts.generate_speech(
    "Baara ka nɔgɔya", 
    speaker_id=Bourama,
    output_filename="work_improves.wav"
)

# Method 2: Save after generation
sf.write("output.wav", audio, 16000)

# Method 3: Audio analysis
print(f"Duration: {len(audio)/16000:.2f} seconds")
print(f"Sample rate: 16000 Hz")
print(f"Channels: 1 (mono)")

# Method 4: Audio processing
normalized_audio = audio / np.max(np.abs(audio))
```

---

## Examples

### Educational Applications

Create learning materials with consistent, high-quality pronunciation:

```python
# Bambara language lessons
lessons = [
    "Dɔrɔn kelen: I ni ce - Musow kɛlɛ",        # "Lesson one: Hello - Greetings"
    "Dɔrɔn fila: Tɔgɔ - N tɔgɔ ye ... ye",     # "Lesson two: Names - My name is ..."
    "Dɔrɔn saba: Jamu - I jamu ye mun ye?",     # "Lesson three: Family - What is your family name?"
]

for i, lesson in enumerate(lessons, 1):
    audio = tts.generate_speech(
        lesson,
        speaker_id=Bourama,  # Consistent speaker for lessons
        output_filename=f"lesson_{i:02d}.wav"
    )
    print(f"Created lesson {i}")
```

### Voice Interface Integration

Build Bambara-speaking applications:

```python
# Voice assistant responses
responses = {
    "greeting": "I ni ce! I bɛ se ka n wele min na?",      # "Hello! What can I call you?"
    "confirmation": "Awɔ, n ye a faamu",                   # "Yes, I understand"
    "error": "Hakɛto, segin ka a fɔ",                     # "Sorry, please repeat"
    "goodbye": "Kan bɛn na! I ni che!",                   # "See you later! Goodbye!"
}

def generate_assistant_voices():
    for intent, response in responses.items():
        audio = tts.generate_speech(
            response,
            speaker_id=Bourama,
            output_filename=f"assistant_{intent}.wav"
        )
        print(f"Generated response for: {intent}")

generate_assistant_voices()
```

### Batch Processing

Process multiple texts efficiently:

```python
# News headlines in Bambara
news_items = [
    "Kalan yɔrɔ kura da Bamakɔ",                         # "New school opens in Bamako"
    "Sɛnɛkɛlaw ka baara ka ɲɛ",                          # "Farmers' work improves"
    "Fɛn kura bɛ na bamanankan na",                      # "New things come to Bambara"
]

def batch_process(texts, speaker=Bourama):
    results = []
    for i, text in enumerate(texts):
        try:
            audio = tts.generate_speech(
                text,
                speaker_id=speaker,
                output_filename=f"news_{i+1:02d}.wav"
            )
            results.append(f"news_{i+1:02d}.wav")
            print(f"Processed: {text}")
        except Exception as e:
            print(f"Error processing '{text}': {e}")
    return results

batch_process(news_items)
```

---

## Best Practices

### Speaker Selection
- **Use Bourama for production**: Most stable and accurate results
- **Consistent speakers**: Use the same speaker for related content
- **Test speakers**: Try different voices for your specific use case

### Text Preparation
```python
# Good practices for input text
def prepare_bambara_text(text):
    # Remove extra whitespace
    text = " ".join(text.split())
    
    # Ensure proper sentence ending
    if not text.endswith(('.', '!', '?')):
        text += '.'
    
    return text

# Example usage
raw_text = "  I ni ce   "
clean_text = prepare_bambara_text(raw_text)  # "I ni ce."
audio = tts.generate_speech(clean_text, speaker_id=Bourama)
```

### Long Text Handling
```python
def synthesize_long_text(text, speaker_id=Bourama, max_length=100):
    """Split long texts into manageable chunks"""
    sentences = text.split('. ')
    audio_chunks = []
    
    for sentence in sentences:
        if sentence.strip():
            audio = tts.generate_speech(
                sentence.strip() + '.',
                speaker_id=speaker_id
            )
            audio_chunks.append(audio)
    
    # Combine all audio
    return np.concatenate(audio_chunks) if audio_chunks else np.array([])

# Example with long text
long_text = "Bamanankan ye kan ye min bɛ kuma Mali la. A bɛ kuma miliyɔn caman fɛ. A ka fɔcogo ka nɔgɔya don."
full_audio = synthesize_long_text(long_text)
sf.write("long_speech.wav", full_audio, 16000)
```

---

## Performance Considerations

### GPU Usage
```python
import torch

# Check GPU availability
if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name()}")
    print(f"Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.1f} GB")
else:
    print("Running on CPU (slower but functional)")
```

### Memory Optimization
```python
# For memory-constrained environments
def memory_efficient_synthesis(texts, speaker_id=Bourama):
    # Process one text at a time instead of batching
    for i, text in enumerate(texts):
        audio = tts.generate_speech(
            text,
            speaker_id=speaker_id,
            max_new_audio_tokens=1024,  # Shorter sequences
            output_filename=f"output_{i}.wav"
        )
        # Audio is saved, memory can be freed
        print(f"Processed text {i+1}/{len(texts)}")
```

### Batch Efficiency
```python
# Reuse the same TTS instance
tts = BambaraTTSInference()  # Initialize once

# Process multiple texts
texts = ["Text 1", "Text 2", "Text 3"]
for text in texts:
    audio = tts.generate_speech(text, speaker_id=Bourama)
    
# Don't create new instances unnecessarily
```

---

## Troubleshooting

### Common Issues and Solutions

**Empty audio output:**
```python
# Check text content and length
text = "I ni ce"
if not text.strip():
    print("Error: Empty text provided")
elif len(text) < 3:
    print("Warning: Very short text may not generate audio")
else:
    audio = tts.generate_speech(text, speaker_id=Bourama)
```

**CUDA memory errors:**
```python
# Reduce token limit for GPU memory issues
audio = tts.generate_speech(
    text,
    speaker_id=Bourama,
    max_new_audio_tokens=1024  # Reduced from default 2048
)
```

**Speaker validation errors:**
```python
from maliba_ai.config.settings import SPEAKER_IDS

# Verify speaker availability
def validate_speaker(speaker):
    if speaker.id not in SPEAKER_IDS:
        print(f"Invalid speaker. Available: {SPEAKER_IDS}")
        return False
    return True

# Safe speaker usage
if validate_speaker(Bourama):
    audio = tts.generate_speech(text, speaker_id=Bourama)
```

### Performance Issues
```python
# Monitor generation time
import time

start_time = time.time()
audio = tts.generate_speech(text, speaker_id=Bourama)
generation_time = time.time() - start_time

print(f"Generated {len(audio)/16000:.2f}s audio in {generation_time:.2f}s")
print(f"Real-time factor: {generation_time/(len(audio)/16000):.2f}x")
```

---

## Contributing

We welcome contributions to improve Bambara TTS! Here's how to get involved:

```bash
# Development setup
git clone https://github.com/MALIBA-AI/bambara-tts.git
cd bambara-tts
pip install -e ".[dev]"

# Run tests
pytest tests/

# Code formatting
ruff format .
isort .
```

**Ways to contribute:**
- **Training data**: Help collect diverse Bambara speech samples
- **Bug reports**: Report issues with detailed reproduction steps
- **Documentation**: Improve guides and examples
- **Testing**: Test on different hardware and use cases
- **Speaker diversity**: Contribute additional voice recordings

**Contribution guidelines:**
- Follow existing code style
- Add tests for new features
- Update documentation
- Respect speaker privacy and consent

---

## Support and Community

- **GitHub Issues**: [Report bugs and request features](https://github.com/MALIBA-AI/bambara-tts/issues)
- **Email**: contact@maliba-ai.com
- **Website**: [maliba-ai.com](https://maliba-ai.com)

---

## License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.

---

## Acknowledgments

- **Spark-TTS**: Foundation architecture for neural speech synthesis
- **Bambara speakers**: Community members who contributed voice data
- **MALIBA-AI team**: Dedicated developers and researchers
- **Mali**: Our inspiration for building inclusive technology

**MALIBA-AI ka baara kɛ ka bamanankan lakana diɲɛ kɔnɔ!** *(MALIBA-AI works to preserve Bambara language in the world!)*