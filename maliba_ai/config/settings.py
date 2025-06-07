from dataclasses import dataclass
from typing import List


MODEL_REPO = "sudoping01/bambara-tts-1-merged-16bit"
BASE_SPARK_MODEL= "unsloth/Spark-TTS-0.5B"

SPEAKER_IDS = ["SPEAKER_01", "SPEAKER_02", "SPEAKER_03", "SPEAKER_04", "SPEAKER_05"]


@dataclass
class SingleSpeaker:
    id: str
    
    def __post_init__(self):
        if self.id not in SPEAKER_IDS:
            raise ValueError(f"Speaker ID '{self.id}' is not available. Available speakers: {SPEAKER_IDS}")
    
    def __str__(self) -> str:
        return f"Speaker({self.id})"
    
    def __repr__(self) -> str:
        return f"SingleSpeaker(id='{self.id}')"


class Speakers:
    Adame: SingleSpeaker = SingleSpeaker(id="SPEAKER_1")
    Moussa: SingleSpeaker = SingleSpeaker(id="SPEAKER_2")
    Bourama: SingleSpeaker = SingleSpeaker(id="SPEAKER_3")
    Modibo: SingleSpeaker = SingleSpeaker(id="SPEAKER_4")
    Seydou: SingleSpeaker = SingleSpeaker(id="SPEAKER_5")
    
    @classmethod
    def get_all_speakers(cls) -> List[SingleSpeaker]:
        return [cls.Adame, cls.Moussa, cls.Bourama, cls.Modibo, cls.Seydou]
    
    @classmethod
    def get_speaker_by_name(cls, name: str) -> SingleSpeaker:
        if hasattr(cls, name):
            return getattr(cls, name)
        raise ValueError(f"Speaker '{name}' not found. Available: {[attr for attr in dir(cls) if not attr.startswith('_') and not callable(getattr(cls, attr))]}")


