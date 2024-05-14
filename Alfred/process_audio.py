import librosa
from transformers import WhisperProcessor, WhisperForConditionalGeneration


class AudioProc():
    def __init__(self) -> None:
        self.processor = WhisperProcessor.from_pretrained("openai/whisper-tiny.en")
        self.model = WhisperForConditionalGeneration.from_pretrained("openai/whisper-tiny.en")

    def process_audio(self,filepath):
        
        audio_file_path = filepath
        audio_samples, sample_rate = librosa.load(audio_file_path, sr=None, mono=True)

        normalized_audio_samples = librosa.util.normalize(audio_samples)

        target_sample_rate = 16000 
        if sample_rate != target_sample_rate:
            normalized_audio_samples = librosa.resample(normalized_audio_samples, orig_sr=sample_rate, target_sr=target_sample_rate)

        

        sample = normalized_audio_samples
        input_features = self.processor(sample, sampling_rate=16000, return_tensors="pt").input_features

        predicted_ids = self.model.generate(input_features)

        transcription = self.processor.batch_decode(predicted_ids, skip_special_tokens=True)

        return transcription

if __name__ == '__main__':
    ap = AudioProc()
    print(ap.process_audio("temp.wav"))