import streamlit as st
from invoke_lambda import invoke_lambda
from load_css import load_css

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


def clear_chat():
    st.session_state.chat_history = []


def main():
    st.set_page_config(page_title="RAG Gpt", layout="centered")

    st.markdown(load_css("style.css"), unsafe_allow_html=True)

    # Display chat history
    for message in st.session_state.chat_history:
        message_style = (
            "user-message" if message["role"] == "user" else "assistant-message"
        )
        with st.chat_message(message["role"]):
            st.markdown(
                f'<div class="{message_style}">{message["content"]}</div>',
                unsafe_allow_html=True,
            )

    # Text input for user
    if user_input := st.chat_input("Message RAG Gpt"):
        # Append user message to chat history
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        # Show user message in chat
        with st.chat_message("user"):
            st.markdown(
                f'<div class="user-message">{user_input}</div>',
                unsafe_allow_html=True,
            )

        # Create a placeholder for the bot's response
        bot_message_placeholder = st.empty()

        with st.spinner("Thinking..."):
            bot_response = invoke_lambda(user_input)

        # Update the placeholder with the bot's response within the chat message context
        with bot_message_placeholder.container():
            st.chat_message("assistant").markdown(
                f'<div class="assistant-message">{bot_response}</div>',
                unsafe_allow_html=True,
            )

        # Append bot response to chat history
        st.session_state.chat_history.append(
            {"role": "assistant", "content": bot_response}
        )

    # "Clear Chat" button when there are messages in the chat history
    if st.session_state.chat_history:
        st.button(
            "Clear Chat",
            on_click=clear_chat,
            key="clear_chat_button",
            help="Clear the chat and start a new one",
            use_container_width=False,
        )


if __name__ == "__main__":
    main()
