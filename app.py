import streamlit    as st
import pandas       as pd
import torch
from simpletransformers.language_generation import LanguageGenerationModel, LanguageGenerationArgs

global model
model = None

def check_password():
    """Returns `True` if the user had the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == "RockstarEntrupures":
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True

def load_model():
    global model
    model = LanguageGenerationModel("gpt2", "General/my-awesome-model-unplugged",use_cuda=False)
    return True

if check_password() and load_model():
    st.title("AI Rich - The AI Unplugged Alpha")
    name = st.text_input("Enter the starting phrase", 'A high value male')
    generated = model.generate("A high value male")

    st.write(f"Hello {generated}!")

    x = st.slider("Select an integer x", 0, 10, 1)
    y = st.slider("Select an integer y", 0, 10, 1)
    df = pd.DataFrame({"x": [x], "y": [y] , "x + y": [x + y]}, index = ["addition row"])
    st.write(df)