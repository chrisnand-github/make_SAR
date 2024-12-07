import streamlit as st
import re
from steamlit_SAR_template import make_route_base, increment_last_octet
USERNAME = "chris"
PASSWORD = "chris123"

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False


# Function to validate IP address
def is_valid_ip(ip):
    pattern = r"^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\." \
              r"(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\." \
              r"(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\." \
              r"(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$"
    return re.match(pattern, ip) is not None

# Function to compute result from inputs
def generate_paragraph(*inputs):
    return " ".join(inputs)
def login():
    st.title("Login")

    # Username and Password Input
    username = st.text_input("Username:")
    password = st.text_input("Password:", type="password")

    # Login Button
    if st.button("Login"):
        if username == USERNAME and password == PASSWORD:
            st.session_state["logged_in"] = True
            st.success("Login successful!")
        else:
            st.error("Invalid username or password. Please try again.")

# Streamlit App
def main_app():
    st.title("Config Generator")

    # Collect inputs in a compact grid layout
    inputs = []  # List to hold all 20 inputs
    data=["","hostname",
            "Site",
            "system",
            "loopback",
            "far-end-1",
            "network-1",
            "port-source-1",
            "port-far-end-1",
            "far-end-2",
            "network-2",
            "port-source-2",
            "port-far-end-2",
            "port-1-type",
            "port-2-type",
            "isis-instance-1",
            "isis-instance-2",
            "POC2-BGP-1",
            "POC2-BGP-2",
            "POC3-BGP-1",
            "POC3-BGP-2"]
    example=["","MBHQAMUN1170",
            "1170",
            "172.16.1.1",
            "192.168.1.1",
            "MBHQAWAB1171",
            "172.16.18.202",
            "1/2/7",
            "1/4/1",
            "MBHQAWAB1171",
            "172.16.18.202",
            "1/2/7",
            "1/4/1",
            "LR",
            "LR",
            "7",
            "7",
            "172.16.240.2",
            "172.16.240.1",
            "192.168.64.2",
            "192.168.64.2"]
    default_inputs = ["","MBHQAMUN1170",
            "1170",
            "172.16.1.1",
            "192.168.1.1",
            "MBHQAWAB1171",
            "172.16.18.202",
            "1/2/7",
            "1/4/1",
            "MBHQAWAB1171",
            "172.16.18.202",
            "1/2/7",
            "1/4/1",
            "LR",
            "LR",
            "7",
            "7",
            "172.16.240.2",
            "172.16.240.1",
            "192.168.64.2",
            "192.168.64.2"]
    # Create 4 rows, each with 5 inputs
    for row in range(5):
        cols = st.columns(4)
        for col_index in range(4):
            input_number = row * 4 + col_index + 1  # Input number (1-20)
            default_value = default_inputs[input_number]  # Pre-filled default value
            if input_number in [1, 6, 11, 16]:  # IP fields (1st of each row)
                ip_input = cols[col_index].text_input(f"{data[input_number]}:",value=default_value, max_chars=15, placeholder=f"{example[input_number]}")
                inputs.append(ip_input)
            else:
                text_input = cols[col_index].text_input(f"{data[input_number]}:",value=default_value, max_chars=50, placeholder=f" {example[input_number]}")
                inputs.append(text_input)

    # Ensure all fields are filled and validate IP inputs
    button_cols = st.columns([1, 0.1, 1])  # Adjust column width for spacing
    with button_cols[0]:
        if st.button("Generate SAR Config"):
            ip_fields = [inputs[2], inputs[3], inputs[5], inputs[9], inputs[16], inputs[17], inputs[18], inputs[19]]  # IP fields
            non_ip_fields = inputs[0],inputs[1], inputs[4],inputs[6],inputs[7],inputs[8],inputs[10],inputs[11],inputs[12],inputs[13],inputs[14],inputs[15]  # Other fields
            data = {
                "hostname":inputs[0],
                "Site":inputs[1],
                "system":inputs[2],
                "loopback":inputs[3],
                "far-end-a":inputs[4],
                "network-a":inputs[5],
                "port-a1":inputs[6],
                "port-a2":inputs[7],
                "far-end-b":inputs[8],
                "network-b":inputs[9],
                "port-b1":inputs[10],
                "port-b2":inputs[11],
                "port-a-type":inputs[12],
                "port-b-type":inputs[13],
                "isis-a-area":inputs[14],
                "isis-b-area":inputs[15],
                "POC2-1":inputs[16],
                "POC2-2":inputs[17],
                "POC3-1":inputs[18],
                "POC3-2":inputs[19]
                }
            if not all(ip.strip() for ip in ip_fields):
                st.error("All IP fields must be filled!")
            elif not all(is_valid_ip(ip) for ip in ip_fields):
                st.error("All IP fields must contain valid IPv4 addresses!")
            elif not all(field.strip() for field in non_ip_fields):
                st.error("All text fields must be filled!")
            else:
                result = make_route_base(data)
                filename = data["hostname"]+".cfg"
                with open(filename, "w") as file:
                    file.write(result)
                st.success(f"Text successfully saved to `{filename}`!")
                st.download_button(
                    label="Download Text File",
                    data=result,
                    file_name=filename,
                    mime="text/plain"
                )
        if st.button("Generate Far-end Config"):
            result3="abc"
            with open("test", "w") as file:
                file.write(result3)

            st.success(f"Text successfully saved to `test`!")
        if st.button("Generate Far-end 2 Config"):
            result4="abc"
            with open("test", "w") as file:
                file.write(result4)

            st.success(f"Text successfully saved to `test`!")
        if st.button("Generate POC2 config"):
            result4="abc"
            with open("test", "w") as file:
                file.write(result4)

            st.success(f"Text successfully saved to `test`!")
        if st.button("Generate POC3 config"):
            result4="abc"
            with open("test", "w") as file:
                file.write(result4)

            st.success(f"Text successfully saved to `test`!")
    with button_cols[2]:
        if st.button("Generate IXR-e small Config"):
            result2="abc"
            with open("test", "w") as file:
                file.write(result2)

            st.success(f"Text successfully saved to `test`!")
        if st.button("Generate IXR-e big Config"):
            result2="abc"
            with open("test", "w") as file:
                file.write(result2)

            st.success(f"Text successfully saved to `test`!")
        if st.button("Generate IXR-e R6 Config"):
            result2="abc"
            with open("test", "w") as file:
                file.write(result2)

            st.success(f"Text successfully saved to `test`!")
    if st.button("Logout"):
        st.session_state["logged_in"] = False
        st.write("You have been logged out. Please reload the page.")

# App Logic
if st.session_state["logged_in"]:
    main_app()
else:
    login()
