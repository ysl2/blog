# pandoc

## Installation

```bash
brew install pandoc
```

## Usage

```bash
# Convert Markdown to DOCX.
pandoc 'input.md' -o 'output.docx'

# Convert Markdown to PDF using the default PDF engine (pdflatex).
pandoc 'input.md' -o 'output.pdf'

# For Chinese characters, you need to specify a CJK font, such as 'PingFang SC'.
pandoc 'input.md' -o 'output.pdf' --pdf-engine=xelatex -V CJKmainfont='PingFang SC'
```
