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

2. Install dependencies with [Conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html) and activate virtual environment🔨

```bash
conda create --name DocDAAS-py310 python=3.10
conda activate DocDAAS-py310
pip install -r requirements.txt
```

3. Run the Streamlit server🚀

```bash
cd knowledge_gpt
streamlit run main.py
```

## 🚀 Upcoming Features

- Add support for more formats (e.g. webpages 🕸️, PPTX 📊, etc.)
- Highlight relevant phrases in citations 🔦
- Support scanned documents with OCR 📝
- More customization options (e.g. chain type 🔗, chunk size📏, etc.)
