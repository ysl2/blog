# mlx-audio

# Installation

```bash
uv tool install --force "mlx-audio[all]"
```

## Usage

```bash
# NOTE: auto detect language
# mlx_audio.stt.generate  \
#     --model mlx-community/Qwen3-ASR-1.7B-bf16  \
#     --audio IMG_9300.flac  \
#     --output-path IMG_9300.flac  \
#     --format txt  \
#     --gen-kwargs '{"language":null}'  \
#     --verbose
# NOTE: or, specify language and prompt (dont know how to use, this below cannot work)
# mlx_audio.stt.generate \
#     --model mlx-community/Qwen3-ASR-1.7B-bf16 \
#     --audio IMG_9300.flac \
#     --output-path IMG_9300.flac \
#     --format txt \
#     --language Chinese \
#     --gen-kwargs '{"system_prompt":"Vocabulary: abstract, topic model, llm, related work, graph propagation."}' \
#     --verbose
# NOTE: or, specify language
mlx_audio.stt.generate \
    --model mlx-community/Qwen3-ASR-1.7B-bf16 \
    --audio IMG_9300.flac \
    --output-path IMG_9300.flac \
    --format txt \
    --language Chinese \
    --verbose

# NOTE: Optional: Force alignment to single word level
mlx_audio.stt.generate \
    --model mlx-community/Qwen3-ForcedAligner-0.6B-bf16 \
    --audio IMG_9300.flac \
    --text "$(cat IMG_9300.flac.txt)" \
    --language Chinese \
    --output-path IMG_9300-aligned \
    --format json \
    --verbose
```
