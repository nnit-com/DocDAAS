<h1 align="center">
📖KnowledgeGPT
</h1>

Accurate answers and instant citations for your documents.

## 🔧 Features

- Upload documents 📁(PDF, DOCX, TXT) and answer questions about them.
- Cite sources📚 for the answers, with excerpts from the text.

## 💻 Running Locally

1. Clone the repository📂

```bash
git clone https://github.com/nnit-com/DocDAAS
cd DocDAAS
```

2. Install dependencies with [Poetry](https://python-poetry.org/) and activate virtual environment🔨


pip install poetry -i https://pypi.mirrors.ustc.edu.cn/simple


pip install -r requirements.txt



```bash
poetry install
poetry shell
```

3. Run the Streamlit server🚀

```bash
cd DocDAAS
streamlit run main.py
```

## 🚀 Upcoming Features

- Add support for more formats (e.g. webpages 🕸️, PPTX 📊, etc.)
- Highlight relevant phrases in citations 🔦
- Support scanned documents with OCR 📝
- More customization options (e.g. chain type 🔗, chunk size📏, etc.)


conda activate DocDAAS-py310
streamlit run main.py
git reset HEAD
cd /home/adminsiyu/code/DocDAAS01/knowledge_gpt
