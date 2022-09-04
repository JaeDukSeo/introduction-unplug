import streamlit    as st
import pandas       as pd
import gpt_2_simple as gpt2
from google_drive_downloader import GoogleDriveDownloader as gdd
import tarfile
import gdown

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

if check_password():
    st.title("AI Rich - The AI Unplugged Alpha")
    name = st.text_input("Enter the starting phrase", 'A high value male')
    sess = gpt2.start_tf_sess()
    gpt2.load_gpt2(sess, run_name='run1')

    loaded = gpt2.generate(sess,
              length=250,
              temperature=0.7,
              prefix="A high value man is",
              nsamples=5,
              batch_size=5
              )
    st.write(f"Hello {loaded}!")

    x = st.slider("Select an integer x", 0, 10, 1)
    y = st.slider("Select an integer y", 0, 10, 1)
    df = pd.DataFrame({"x": [x], "y": [y] , "x + y": [x + y]}, index = ["addition row"])
    st.write(df)