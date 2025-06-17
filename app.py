import streamlit as st
from summarizer import extract_video_id, fetch_transcript, summarize_transcript

st.set_page_config(page_title="Youtube Summarizer", page_icon=":robot:", layout = "centered" )
st.title("Youtube Summarizer")
url = st.text_input("Enter the URL of the YouTube video")

if st.button("Summarize"):
    if not url.strip():
        st.warning("Please enter a valid URL.")
    else:
        with st.spinner("Fetching transcript..."):
            video_id = extract_video_id(url)
            try:
                transcript = fetch_transcript(video_id)
                with st.spinner("Summarizing transcript..."):
                    summary = summarize_transcript(transcript)
                    st.subheader("Summary:")
                    st.write(summary)
            except Exception as e:
                st.error(f"Error: {str(e)}")