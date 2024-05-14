from Alfred import live_audio,structured_out_oa, process_audio,utils
import uuid
import os


api_key = utils.read_key('.keyfile')
filename = str(uuid.uuid4())

filepath = os.path.join("Alfred","media",filename+".wav")

print(filepath)
audio_proc = process_audio.AudioProc()

live_audio.record_audio(filepath)
command = audio_proc.process_audio(filepath)[0]

print(command)

api_key = utils.read_key('.keyfile')
print(repr(api_key))
json_generator = structured_out_oa.LLMProc("gpt-3.5-turbo-0125",api_key)
print(json_generator.generate_json(command))


