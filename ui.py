import streamlit as st

def render_input():
    """Render patient notes input panel."""
    st.subheader("📝 Patient's Notes")
    notes = st.text_area(
        "Before your appointment, please tell us what’s on your mind. You can write about anything — your ideas, worries, or what you hope to get from the consultation. There are no right or wrong answers.:",
        height=320,
        placeholder="e.g., 'I've had sharp pain in my lower back for 3 days...'",
    )
    button = st.button("✨ Generate Summary", type="primary", use_container_width=True)
    return notes, button

def render_output(default_message=True):
    """Render the summary panel."""
    st.subheader("📋 Clinician's Summary")
    placeholder = st.empty()
    if default_message:
        placeholder.markdown(
            """
            <div style="background-color:#f9fafc; padding: 20px; 
                        border: 1px solid #ddd; border-radius: 12px; 
                        height: 340px; display: flex; align-items: center; justify-content: center;">
                <p style="color: #888; font-style: italic;">The generated summary will appear here.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    return placeholder
