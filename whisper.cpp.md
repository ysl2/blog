# whisper.cpp

## Installation

```bash
brew install whisper-cpp
HTTP_PROXY=127.0.0.1:7892 HTTPS_PROXY=127.0.0.1:7892 curl -L --fail --progress-bar -o "$HOME/.vocal/whisper.cpp/models/ggml-large-v3.bin" "https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-large-v3.bin"
HTTP_PROXY=127.0.0.1:7892 HTTPS_PROXY=127.0.0.1:7892 curl -L --fail --progress-bar -o "$HOME/.vocal/whisper.cpp/models/ggml-silero-v6.2.0.bin" "https://huggingface.co/ggml-org/whisper-vad/resolve/main/ggml-silero-v6.2.0.bin"
```

## Usage

```bash
whisper-cli -m "$HOME/.vocal/whisper.cpp/models/ggml-large-v3.bin" -l zh -mc 0 --vad -vm "$HOME/.vocal/whisper.cpp/models/ggml-silero-v6.2.0.bin" -osrt "IMG_9300.flac"
whisper-cli -m "$HOME/.vocal/whisper.cpp/models/ggml-large-v3.bin" -l zh -mc 32 --vad -vm "$HOME/.vocal/whisper.cpp/models/ggml-silero-v6.2.0.bin" --prompt "abstract, topic model, llm, related work" --carry-initial-prompt -osrt "IMG_9300.flac"
```
