import streamlit    as st
import pandas       as pd
import torch

from transformers import GPT2LMHeadModel, GPT2Tokenizer


model = None
tokenizer = None


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
    global tokenizer
    model = GPT2LMHeadModel.from_pretrained("General/my-awesome-model-unplugged-gpt2")
    tokenizer = GPT2Tokenizer.from_pretrained("General/my-awesome-model-unplugged-gpt2")

    return True

def generate_idea(industry_input,creativity_input):
    global model
    global tokenizer
    input_ids = tokenizer.encode(industry_input, return_tensors='pt')
    sample_outputs = model.generate(
        input_ids,
        do_sample=True, 
        max_length=250, 
        temperature = creativity_input,
        top_k=50, 
        top_p=0.95, 
        num_return_sequences=1
    )
    return tokenizer.decode(sample_outputs[0], skip_special_tokens=True)

if check_password() and load_model():
    st.title("🚀 AI Rich - The AI Unplugged Alpha 💪💪🏻💪🏽💪🏿")

    form = st.form(key="user_settings")
    with form:
        st.write("Example 1: A high value man is")
        st.write("Example 2: Complicate life justify why")
        st.write("Example 3: Vitamin d and k are important because")

        industry_input = st.text_input("Starting phrase...", value="A high value man is",key = "user_input")

        # Create a two-column view
        col1, col2 = st.columns(2)

        with col1:
            # User input - The number of ideas to generate
            num_input = st.slider("Number of ideas", value = 3, key = "num_input", min_value=1, max_value=10)

        with col2:
            # User input - The 'temperature' value representing the level of creativity
            creativity_input = st.slider("Creativity", value = 0.5, key = "creativity_input", min_value=0.1, max_value=0.9)

        generate_button = form.form_submit_button("Generate paragraph")

        if generate_button:
            if industry_input == "":
                st.error("Starting phrase field cannot be blank")
            else:
                my_bar = st.progress(0.05)
                for i in range(num_input):
                    st.markdown("""---""")
                    startup_idea = generate_idea(industry_input,creativity_input)
                    st.write(startup_idea)
                    my_bar.progress((i+1)/num_input)

    # name = st.text_input("Enter the starting phrase", 'A high value male')
    # generated = model.generate("A high value male")

    # st.write(f"Hello {generated}!")

    # x = st.slider("Select an integer x", 0, 10, 1)
    # y = st.slider("Select an integer y", 0, 10, 1)
    # df = pd.DataFrame({"x": [x], "y": [y] , "x + y": [x + y]}, index = ["addition row"])
    # st.write(df)