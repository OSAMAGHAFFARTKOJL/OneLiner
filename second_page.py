import streamlit as st
from ai71 import AI71
import traceback

AI71_API_KEY = "api71-api-2fcb29da-a589-4632-9e26-47a71786cd25"


def get_ai_response(prompt, option):
    try:
        response = ""
        for chunk in AI71(AI71_API_KEY).chat.completions.create(
            model="tiiuae/falcon-180b-chat",
            messages=[
                {
                    "role": "system",
                    "content": f"You are a helpful assistant for {option} problems."
                },
                {
                    "role": "user",
                    "content": prompt + '''First, judge whether the person is a beginner or advanced based on the way they ask questions. If the person is a beginner, give more detailed hints, and if advanced, give less concise hints. The answer you give must have the following sections:

                    1. Give hints to solve the question but do not give the coding solution. After it, give a two-line space.

                    2. Provide some real-world examples. Give only one example to explain it. Don't give the code. After it, give a two-line space.

                    3. Give some more hints that enhance the self-learning of the user. After it, give a two-line space.

                    4. Provide the code solution to the question. After it, give a two-line space.

                    5. Mention the topic name to study to understand the question.
                    '''
                },
            ],
            stream=True,
        ):
            if chunk.choices[0].delta.content:
                response += chunk.choices[0].delta.content
        return response
    except Exception as e:
        st.error(f"An error occurred while fetching the AI response: {str(e)}")
        return None

def display_hint(title, content):
    st.markdown(f'<div class="hint-box"><h4>{title}</h4><p>{content}</p></div>', unsafe_allow_html=True)
    st.write(" ")
    st.write(" ")

def main():
    try:
        with open("second_style.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

        st.title("Explore the World of AI")
        st.write(" ")
        st.write(" ")
        st.write(" ")
        st.subheader("Put your queries here:")

        col1, col2 = st.columns([3, 1])

        with col1:
            answer = st.text_input("", key="user_query")

        with col2:
            option = st.selectbox("", ("Coding", "Math"), index=0, key="option")

        if st.button("Submit"):
            if answer:
                st.session_state.ai_response = get_ai_response(answer, option)
                st.session_state.show_hints = True
                st.session_state.hints = st.session_state.ai_response.split("\n\n")
            else:
                st.warning("Please enter a query.")

        if st.session_state.get('show_hints', False):
            st.subheader("Solution:")
            if st.session_state.ai_response:
                hints = st.session_state.hints if len(st.session_state.hints) >= 5 else st.session_state.hints + [""] * (5 - len(st.session_state.hints))

                hint_titles = ["Hints", "Example", "Self Learning", "Solution", "Topics"]
                for i, (title, hint) in enumerate(zip(hint_titles, hints), 1):
                    if i == 4:
                        hint = "\n\n".join(hints[3:-1]) if len(hints) > 3 else ""
                    elif i == 5:
                        hint = hints[-1] if hints else ""
                    
                    if st.button(f"Level {i}: {title:<20}", key=f"hint_button_{i}"):
                        st.session_state[f'show_hint_{i}'] = not st.session_state.get(f'show_hint_{i}', False)
                    if st.session_state.get(f'show_hint_{i}', False):
                        display_hint(title, hint)

        

    except Exception as e:
        st.error(f"An unexpected error occurred: {str(e)}")
        st.error(traceback.format_exc())

if __name__ == "__main__":
        main()