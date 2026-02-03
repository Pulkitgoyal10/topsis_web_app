import streamlit as st
import pandas as pd
import tempfile
import os
import re
import smtplib
from email.message import EmailMessage
from topsis_pulkit_102303800.topsis import topsis

st.set_page_config(page_title="TOPSIS Decision Tool", layout="centered")
st.title("TOPSIS Decision Making Web App")

uploaded_file = st.file_uploader("Upload CSV or Excel file", type=["csv", "xlsx"])
weights = st.text_input("Enter Weights (comma separated)", "1,1,1")
impacts = st.text_input("Enter Impacts (+ or - comma separated)", "+,+,+")
email = st.text_input("Enter Email to receive result")

# ---------------- EMAIL VALIDATION ----------------
def is_valid_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email)

# ---------------- EMAIL SENDING ----------------
def send_email(file_path, receiver_email):
    sender_email = os.environ.get("EMAIL")
    app_password = os.environ.get("PASSWORD")

    if not sender_email or not app_password:
        st.error("Email credentials not configured in Streamlit Secrets.")
        return

    msg = EmailMessage()
    msg["Subject"] = "Your TOPSIS Result File"
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg.set_content("Please find attached the TOPSIS result file.")

    with open(file_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename="result.csv"
        )

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.send_message(msg)
    except smtplib.SMTPAuthenticationError:
        st.error("Gmail login failed. Check App Password in Streamlit Secrets.")
    except Exception as e:
        st.error(f"Email sending failed: {e}")

# ---------------- MAIN PROCESS ----------------
if uploaded_file:
    st.success("File uploaded successfully!")

    if st.button("Run TOPSIS"):
        try:
            suffix = os.path.splitext(uploaded_file.name)[1]
            with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
                tmp.write(uploaded_file.read())
                input_path = tmp.name

            output_path = input_path.replace(suffix, "_result.csv")

            topsis(input_path, weights, impacts, output_path)

            result_df = pd.read_csv(output_path)
            st.dataframe(result_df)

            with open(output_path, "rb") as f:
                st.download_button("Download Result File", f, "topsis_result.csv")

            if email:
                if is_valid_email(email):
                    send_email(output_path, email)
                    st.success("Result sent to email successfully!")
                else:
                    st.error("Invalid email format")

        except Exception as e:
            st.error(f"Error: {e}")
