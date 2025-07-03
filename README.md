# MALIBA-AI Bambara TTS SDK

Welcome to the MALIBA-AI Bambara Text-to-Speech! This is the **first open-source TTS system** specifically designed for the Bambara language. Whether you're building educational platforms, creating voice interfaces, or developing accessibility tools, this SDK provides professional grade Bambara speech synthesis with multiple authentic speakers.

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
with uv (faster)

```bash
    uv pip install maliba_ai
```

```bash
    uv pip install git+https://github.com/MALIBA-AI/bambara-tts.git
```
Note : if you are in colab  please install those additional dependencies : 

```
    !pip install --no-deps bitsandbytes accelerate xformers==0.0.29.post3 peft trl triton cut_cross_entropy unsloth_zoo
    !pip install sentencepiece protobuf "datasets>=3.4.1" huggingface_hub hf_transfer
    !pip install --no-deps unsloth
```

---

## Quick Start

Get started with Bambara TTS in under a minute:

```python
from maliba_ai.tts.inference import BambaraTTSInference
from maliba_ai.config.settings import Speakers
import soundfile as sf

# Initialize the TTS system
tts = BambaraTTSInference()

# Generate speech from Bambara text
text = "Aw ni ce. Sedu bɛ aw fo wa aw ka yafa a ma, ka da a kan tuma dɔw la kow ka can."  

audio = tts.generate_speech(text, speaker_id=Speakers.Seydou)

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

# With custom model path and sequence length
tts = BambaraTTSInference(
    model_path="your-custom-model-path",  # Optional: custom model: local or huggingface repo id (make sure you login in huggingface)
    max_seq_length=4096                   # Optional: longer sequences
)
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
from maliba_ai.config.settings import Speakers

# Basic synthesis with default speaker (Adama)
text = "Bamanankan ye kan ɲuman ye"  # "Bambara is a beautiful language"
audio = tts.generate_speech(text)
```

### Speaker Selection

Choose from our ten authentic Bambara speakers:
```
Speaker recommendations:

  - Bourama: Most stable and accurate 
  - Adama: Natural conversational tone
  - Moussa: Clear pronunciation  
  - Modibo: Expressive delivery
  - Seydou: Balanced characteristics
  - Amadou: Warm and friendly voice
  - Bakary: Deep, authoritative tone
  - Ngolo: Youthful and energetic
  - Ibrahima: Calm and measured
  - Amara: Melodic and smooth
```

```python
from maliba_ai.config.settings import Speakers

text = "Aw ni ce. Ne tɔgɔ ye Adama. Awɔ,  ne ye maliden de ye. Aw Sanbɛ Sanbɛ. San min tɛ ɲinan ye, an bɛɛ ka jɛ ka o seli ɲɔgɔn fɛ,  hɛɛrɛ  ni lafiya la. Ala ka Mali suma. Ala ka Mali yiriwa. Ala ka Mali taa ɲɛ. Ala ka an ka seliw caya. Ala ka yafa an bɛɛ ma."

#let's try Adama
tts.generate_speech(
    text = text, 
    speaker_id = Speakers.Adama,
    output_filename = "adama.wav"
)



#let's try Seydou
tts.generate_speech(
    text = text, 
    speaker_id = Speakers.Seydou,
    output_filename = "seydou.wav"
)


# let's try Bourama
tts.generate_speech(
    text = text, 
    speaker_id = Speakers.Bourama,
    output_filename = "Bourama.wav"
)

```


**Note**: Try all speakers and chose your favorite for your use case

### Advanced Configuration

Fine-tune synthesis with custom parameters:

```python
audio = tts.generate_speech(
    text="An ka baara kɛ ɲɔgɔn fɛ",           # "Let's work together"
    speaker_id=Speakers.Bourama,
    temperature=0.8,                          # Sampling temperature
    top_k=50,                                # Vocabulary sampling
    top_p=0.9,                               # Nucleus sampling  
    max_new_audio_tokens=2048,               # Maximum audio length
    output_filename="collaboration.wav"       # Auto-save option
)
```

---


## Generation Parameters

The SDK comes with optimized default parameters that provide the best quality:

### Default Configuration
```python

temperature=0.8              # Optimal balance between consistency and naturalness
top_k=50                    # Vocabulary selection size
top_p=1.0                   # Nucleus sampling threshold (default)
max_new_audio_tokens=2048   # Maximum audio sequence length
```

### Parameter Guidelines
- **Temperature**: Keep at 0.8. Lower values (0.1-0.6) may sound robotic, higher values (1.0+) can introduce artifacts
- **Top-k**: Range 1-100. Default of 50 provides best quality
- **Top-p**: Range 0.1-1.0. Values like 0.9 can improve quality for some speakers
- **Max tokens**: Increase only for very long texts (splits recommended instead)

### Advanced Parameter Control
```python
# Conservative settings for maximum stability
audio = tts.generate_speech(
    "Ce!",  # "Hello!"
    speaker_id=Speakers.Bourama,
    temperature=0.6,              # More conservative
    top_k=30,                     # More focused vocabulary
    top_p=0.8,                    # Nucleus sampling
    max_new_audio_tokens=1024     # Shorter for efficiency
)

# Creative settings for experimental use
audio = tts.generate_speech(
    text,
    speaker_id=Speakers.Ngolo,
    temperature=1.0,              # More varied
    top_k=70,                     # Broader vocabulary
    top_p=0.95,                   # Slight nucleus sampling
    max_new_audio_tokens=2048
)
```

---

## Audio Output Options

Handle generated audio efficiently:

```python
import numpy as np
import soundfile as sf

# Generate audio
audio = tts.generate_speech("Baara ka nɔgɔya", speaker_id=Speakers.Bourama)

# Method 1: Direct file saving during generation
audio = tts.generate_speech(
    "Baara ka nɔgɔya", 
    speaker_id=Speakers.Bourama,
    output_filename="work_improves.wav"
)

# Method 2: Save after generation
sf.write("output.wav", audio, 16000)

# Method 3: Audio analysis
print(f"Duration: {len(audio)/16000:.2f} seconds")
print(f"Sample rate: 16000 Hz")
print(f"Channels: 1 (mono)")
print(f"Data type: {audio.dtype}")

# Method 4: Audio processing
normalized_audio = audio / np.max(np.abs(audio))

# Method 5: Check if audio was generated successfully
if audio.size > 0:
    print("Audio generated successfully!")
else:
    print("No audio generated - check input text")
```

---

## Examples

### Educational Applications

Create learning materials with consistent, high-quality pronunciation:

```python
# Bambara language lessons with different speakers
lessons = [
    ("Walanda fɔlɔ: foli - I ni ce.", Speakers.Adama),             
    ("Walanda filanan : Tɔgɔ - N tɔgɔ ye Sedu", Speakers.Seydou),     
    ("Walanda sabanan: Jamu - I jamu ye mun ye?", Speakers.Bourama),  
    ("Walanda  naaninan: Baara - N bɛ baara kɛ", Speakers.Modibo),   
]

for i, (lesson, speaker) in enumerate(lessons, 1):
    audio = tts.generate_speech(
        lesson,
        speaker_id=speaker,
        output_filename=f"lesson_{i:02d}_{speaker.id.lower()}.wav"
    )
    print(f"Created lesson {i} with speaker {speaker.id}")
```

 **Test speakers**: Try different voices for your specific use case and audience

---


## License

⚠️ **Important License Information**

This project is built upon Spark-TTS architecture and is subject to **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 (CC BY-NC-SA 4.0)** license due to the licensing terms of underlying training data and model architecture.

### Key License Terms:

- **Non-Commercial Use Only**: This model can only be used for non-commercial purposes including:
  - Academic research and education
  - Personal projects and learning
  - Open-source community development
  - Linguistic and cultural preservation research

- **Share-Alike**: Any modifications, derivatives, or improvements must also be released under CC BY-NC-SA 4.0

- **Attribution Required**: Proper attribution must be provided when using or modifying the model


### Commercial Use

For commercial licensing options, please contact the MALIBA-AI team at ml.maliba.ai@gmail.com

### Compliance Requirements

When using this model, you must:

1. **Provide Attribution**: Credit MALIBA-AI and the Spark-TTS foundation
2. **Respect Non-Commercial Terms**: Ensure your use case qualifies as non-commercial
3. **Share Derivatives**: Release any modifications under the same license
4. **Include License Notice**: Include license information in your distributions

### Example Attribution

```
This work uses MALIBA-AI Bambara TTS, built on Spark-TTS architecture.
Licensed under CC BY-NC-SA 4.0.
Original work: https://github.com/MALIBA-AI/bambara-tts
Spark-TTS: https://github.com/SparkAudio/Spark-TTS
```

For full license text, see [LICENSE](LICENSE) file.

## Usage Disclaimer & Ethical Guidelines

⚠️ **Important Usage Guidelines**

This Bambara TTS model is intended for legitimate applications that benefit the Bambara-speaking community and support language preservation efforts.

### Authorized Uses:
- **Educational purposes**: Language learning, pronunciation training, literacy programs
- **Accessibility tools**: Screen readers, communication aids for people with disabilities
- **Cultural preservation**: Documenting oral traditions, creating audio archives
- **Research**: Academic studies on Bambara linguistics and speech technology
- **Community applications**: Local radio, public announcements, community services

### Prohibited Uses:
- **Unauthorized voice cloning** or impersonation without explicit consent
- **Fraud or scams** using generated Bambara speech
- **Deepfakes or misleading content** that could harm individuals or communities
- **Any illegal activities** under local or international law
- **Harassment or discrimination** targeting any group or individual

### Ethical Responsibilities:
- Always obtain proper consent when using someone's voice characteristics
- Clearly disclose when audio content is AI-generated
- Respect the cultural significance of the Bambara language
- Support the Bambara-speaking community's digital inclusion
- Report any misuse of the technology to the MALIBA-AI team

### Community Standards:
The MALIBA-AI project is committed to responsible AI development that empowers communities rather than exploiting them. We encourage users to:
- Engage with Bambara speakers and communities respectfully
- Contribute to the preservation and promotion of Bambara language
- Use this technology to bridge digital divides, not create them
- Share improvements back with the community when possible

**The developers assume no liability for any misuse of this model. Users are responsible for ensuring their applications comply with applicable laws and ethical standards.**

If you have concerns about potential misuse or need guidance on ethical applications, please contact us at ml.maliba.ai@gmail.com

- **Spark-TTS**: Foundation architecture for neural speech synthesis

- **MALIBA-AI team**: Dedicated developers, researchers, and linguists
- **Mali**: Our inspiration for building inclusive technology that serves all communities
- **Open source community**: Contributors and users who help improve the system

---
