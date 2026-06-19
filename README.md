# Fact Check Agent

An AI-powered web application that automatically verifies claims found in PDF documents by comparing them against live web data.

## Problem

Marketing reports, research papers, and business documents often contain outdated statistics, incorrect figures, or hallucinated facts. Manually validating every claim is time-consuming.

Fact Check Agent acts as a "Truth Layer" by extracting factual claims from uploaded PDFs, searching the web for evidence, and identifying whether claims are accurate.

## Features

* Upload PDF documents
* Automatic claim extraction
* Detects statistics, percentages, dates, and financial figures
* Live web search for evidence
* Classifies claims as:

  * ✅ Verified
  * ⚠️ Inaccurate
  * ❌ False
* Provides corrected facts and explanations
* Interactive results dashboard

## Tech Stack

* Streamlit
* OpenAI GPT-4o-mini
* Tavily Search API
* PyMuPDF
* Python

## How It Works

1. Upload a PDF document
2. Extract text from the PDF
3. Identify factual claims
4. Search the web for supporting evidence
5. Verify each claim using an LLM
6. Generate a fact-checking report

## Project Structure

```text
fact-check-agent/
│
├── app.py
├── requirements.txt
├── src/
│   ├── pdf_parser.py
│   ├── claim_extractor.py
│   ├── web_search.py
│   ├── verifier.py
│   └── report_generator.py
│
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/fact-check-agent.git
cd fact-check-agent
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the environment:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
TAVILY_API_KEY=your_tavily_api_key
```

## Run Locally

```bash
streamlit run app.py
```

## Deployment

The application can be deployed on Streamlit Cloud by connecting the GitHub repository and adding the required API keys through Streamlit Secrets.

## Future Improvements

* Source credibility scoring
* PDF report export
* Historical fact tracking
* Multi-language support
* Batch document processing

## Author

Bikram Singh
