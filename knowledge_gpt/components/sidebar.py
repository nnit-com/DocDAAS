import streamlit as st

from knowledge_gpt.components.faq import faq


# def set_openai_api_key(api_key: str):
    # st.session_state["OPENAI_API_KEY"] = api_key

def set_openai__key():
    st.session_state["AZURE_OPENAI_API_KEY"] = "e111e1b9b44641a880e5331a4617354d"
    st.session_state["AZURE_OPENAI_ENDPOINT"] = "https://nnitkitn.openai.azure.com/"
    st.session_state["MODEL_ENGINE_35"] = "OpenAITest01"
    st.session_state["OPENAI_API_VERSION"] = "2023-09-01-preview"
    st.session_state["MODEL_NAME_EMDEDDING_ADA2"] = "NNIT-Ada2-tst1"


def sidebar():
    with st.sidebar:
        st.markdown(
            "## How to use\n"
#            "1. Enter your [OpenAI API key](https://platform.openai.com/account/api-keys) below🔑\n"  # noqa: E501
            "1. Upload a pdf, docx, or txt file📄 (Currently we don't support scanned PDF)\n"
            "2. Ask a question about the document💬\n"
            "   Or you can ask DocGPT to give you some questions about the document💬\n"
        )
#        api_key_input = st.text_input(
#            "OpenAI API Key",
#            type="password",
#            placeholder="Paste your OpenAI API key here (sk-...)",
#            help="You can get your API key from https://platform.openai.com/account/api-keys.",  # noqa: E501
#            value=st.session_state.get("OPENAI_API_KEY", ""),
#        )

#        if api_key_input:
#            set_openai_api_key(api_key_input)
        # set_openai_api_key(st.secrets["OPENAI_API_KEY"])
        set_openai__key()
        
        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "📖DocGPT allows you to ask questions about your "
            "documents and get accurate answers with instant citations. "
            "You can use it to research a paper or practice your exam. "
        )
        st.markdown(
            "This tool is a work in progress. "
        )

        faq()
