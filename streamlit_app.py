import streamlit as st
from collections import defaultdict
import re
import math
import os
import glob


def main():
    # Title of the app
    st.title("MAKE SAR CONFIG_INI")

    # Create a textbox for input text
    st.write("PUT IP SYTEM")
    input_text = st.text_area("Input Text")

    # Create a button to trigger the conversion
    if st.button("MAKE SERVICE"):
        if input_text:
            # Call the conversion function
            #output_text = final_service(input_text)
            output_text = final_service(input_text)
            # Display the output on the right side
            st.write("### Converted Text:")
            st.text_area("Output Text", output_text, height=200)
            st.download_button(
                label="Save Result",
                data=output_text,
                file_name="converted_text.txt",
                mime="text/plain"
            )
        else:
            st.write("Please paste some text to convert.")

# Run the Streamlit app
if __name__ == "__main__":
    main()
