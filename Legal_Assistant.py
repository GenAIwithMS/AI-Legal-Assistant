import streamlit as st
import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyCv86uC98jkzdzO6eCR4Tjav1AcGxIT2gQ"  

st.title("AI Legal Assistant (Pakistan Law)")

tab = st.sidebar.selectbox("Choose Feature", [
    "Explain Legal Term",
    "Ask a Legal Question",
    "Summarize Legal Text",
    "Generate Legal Template",
    "Translate Legal Document"
])

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

if tab == "Explain Legal Term":
    term = st.text_input("Enter a legal term (Urdu or English)")
    lang = st.radio("Output Language", ["Urdu", "English"])
    if st.button("Explain"):
        prompt = (
            f"Explain the following legal term in simple {lang} for a layperson (Pakistan law context):\n\n{term}"
        )
        with st.spinner("Explaining..."):
            response = model.generate_content(prompt)
            st.write(response.text.strip())

elif tab == "Ask a Legal Question":
    question = st.text_area("Ask your law-related question (Urdu or English)")
    if st.button("Get Answer"):
        prompt = (
            f"Answer this law-related question for Pakistan law in a clear, simple way:\n\n{question}"
        )
        with st.spinner("Answering..."):
            response = model.generate_content(prompt)
            st.write(response.text.strip())

elif tab == "Summarize Legal Text":
    legal_text = st.text_area("Paste court judgment or legal paper (Urdu or English)", height=200)
    lang = st.radio("Summary Language", ["Urdu", "English"])
    if st.button("Summarize"):
        prompt = (
            f"Summarize the following legal text in {lang} for a layperson (Pakistan law context):\n\n{legal_text}"
        )
        with st.spinner("Summarizing..."):
            response = model.generate_content(prompt)
            st.write(response.text.strip())

elif tab == "Generate Legal Template":
    template_type = st.selectbox("Select template type", [
        "Affidavit", "Agreement", "Power of Attorney", "Legal Notice", "Other"
    ])
    details = st.text_area("Enter details")
    lang = st.radio("Template Language", ["Urdu", "English"])
    if st.button("Generate Template"):
        prompt = (
            f"Draft a {template_type} in {lang} for Pakistan, using the following details:\n{details}\n"
            "Format it as a legal document."
        )
        with st.spinner("Generating template..."):
            response = model.generate_content(prompt)
            st.write(response.text.strip())

elif tab == "Translate Legal Document":
    doc = st.text_area("Paste legal document to translate", height=200)
    direction = st.radio("Translation Direction", ["Urdu → English", "English → Urdu"])
    if st.button("Translate & Explain"):
        if direction == "Urdu → English":
            prompt = (
                f"Translate the following legal document from Urdu to English and explain any complex terms in simple English:\n\n{doc}"
            )
        else:
            prompt = (
                f"Translate the following legal document from English to Urdu and explain any complex terms in simple Urdu:\n\n{doc}"
            )
        with st.spinner("Translating and explaining..."):
            response = model.generate_content(prompt)
            st.write(response.text.strip())