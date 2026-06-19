import streamlit as st

from src.pdf_parser import extract_text
from src.claim_extractor import extract_claims
from src.web_search import search_claim
from src.verifier import verify_claim

st.title("📄 Fact Check Agent")

pdf = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if pdf:

    with st.spinner("Processing..."):

        text = extract_text(pdf)

        claims = extract_claims(text)

        results = []

        for item in claims['factual_claims']:

            claim = item["claim"]

            evidence = search_claim(claim)
            st.write("Evidence length:", len(str(evidence)))

            verification = verify_claim(
                claim,
                evidence
            )

            results.append({
                "Claim": claim,
                "Status": verification["status"],
                "Correct Fact": verification["correct_fact"],
                "Confidence": verification["confidence"]
            })

        st.dataframe(results)
