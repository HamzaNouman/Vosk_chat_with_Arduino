import sounddevice as sd
import queue
import json
from vosk import Model, KaldiRecognizer

class Sound:
    def __init__(self):
        self.model_path = "vosk-model-small-en-us-0.15"
        self.model = Model(self.model_path)
        self.samplerate = 16000
        self.device = None  # or set to your input device ID
        self.rec = KaldiRecognizer(self.model, self.samplerate)
        self.q = queue.Queue()
        self.n = 10



    def callback(self, indata, frames, time, status):
        if status:
            print("⚠️", status)
        self.q.put(bytes(indata))

    def Open(self):
        # Start streaming from microphone
        with sd.RawInputStream(samplerate=self.samplerate, blocksize=8000, dtype='int16',
                            channels=1, callback=self.callback, device=self.device):
            print("🎙️ Listening (Press Ctrl+C to stop)...")
            try:
                while True:
                    for i in range(self.n):
                        data = self.q.get()
                        if self.rec.AcceptWaveform(data):
                            self.result = json.loads(self.rec.Result())
                            print("📝", self.result.get("text"))
                            if self.result.get("text") == None:
                                break
                            return self.result.get("text")

                        else:
                            # Partial result (can be removed if you only want final text)
                            self.partial = json.loads(self.rec.PartialResult())
                            print("⏳", self.partial.get("partial", ""))
            except KeyboardInterrupt:
                print("🛑 Stopped.")
