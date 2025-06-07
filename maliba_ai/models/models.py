import os
import torch
from unsloth import FastModel
from huggingface_hub import snapshot_download
from maliba_ai.config.settings import MODEL_REPO, BASE_SPARK_MODEL
from maliba_ai.sparktts.models.audio_tokenizer import BiCodecTokenizer

def load_tts_model(hf_token):
    """
    Load the TTS model and tokenizer from the specified repository.
    
    Args:
        hf_token (str): Hugging Face token for authentication.
    
    Returns:
        tuple: (model, tokenizer) - Loaded TTS model and tokenizer.
    """
    model, tokenizer = FastModel.from_pretrained(
        model_name=MODEL_REPO,
        max_seq_length=2048,
        dtype=torch.float32,
        load_in_4bit=False,
        token=hf_token,
    )
    FastModel.for_inference(model)
    return model, tokenizer


def load_audio_tokenizer(device):
    """
    Load the audio tokenizer, downloading the base model if necessary.
    
    Args:
        device (torch.device): Device to load the tokenizer on (e.g., 'cuda' or 'cpu').
    
    Returns:
        BiCodecTokenizer: Loaded audio tokenizer instance.
    """
    if not os.path.exists("Spark-TTS-0.5B"):
        snapshot_download(BASE_SPARK_MODEL, local_dir="Spark-TTS-0.5B")
    audio_tokenizer = BiCodecTokenizer("Spark-TTS-0.5B", device)
    return audio_tokenizer