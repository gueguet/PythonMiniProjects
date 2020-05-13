import pyaudio

# instanciate pyaudio
p = pyaudio.PyAudio()

# determine number of usable device
num_available_device = p.get_device_count()
print("Num device available : ", num_available_device, '\n')

# index 0 --> Microphone
# index 1 --> Speakers
by_index = p.get_device_info_by_index(0)
print("Microphone : ", by_index, '\n')


print(p.get_default_host_api_info())
print(p.get_host_api_info_by_index(0))
print(p.get_default_host_api_info())
