# -*- coding: utf-8 -*-
"""job_offer_comparison_app.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1li_TpgIQF4Fty09rqmkIVCAKKjcXhwt9
"""

# Commented out IPython magic to ensure Python compatibility.
# %%writefile job_offer_comparison_app.py
# 
#



import streamlit as st
import pandas as pd

# Set up the page configuration
st.set_page_config(page_title="Job Offer Comparison App", layout="wide")
st.title("📊 Job Offer Comparison Tool")

# Description of the app
st.markdown("""
Compare two job offers side-by-side across important career factors to make a confident, data-driven decision.
""")

# Define the comparison factors with emoji badges
factors = [
    "💰 Salary",
    "🏠 Flexibility (Remote/Onsite)",
    "🎁 Benefits (Insurance, PTO)",
    "🚚 Relocation Support",
    "💸 Bonus & Stock Options",
    "📈 Promotion Path",
    "🎓 Education Support",
    "🏢 Work Culture",
    "👀 Micromanagement",
    "📉 Employment Gap Tolerance",
    "🧭 Experience Level Fit",
    "⏳ Decision Deadline",
    "🌍 Company Brand & Industry"
]

# Function to set background color based on scores
def set_background_color(score):
    if score == 1:
        return "background-color: #f0a0a0;"  # Red for low scores
    elif score == 2:
        return "background-color: #f4d03f;"  # Yellow for below average
    elif score == 3:
        return "background-color: #f7dc6f;"  # Light yellow for average
    elif score == 4:
        return "background-color: #7dce76;"  # Green for good scores
    else:
        return "background-color: #2ecc71;"  # Dark green for excellent

# Step 1: Collect ratings for each job offer
st.subheader("Step 1: Rate each job offer on a scale of 1 (poor) to 5 (excellent)")

job_offer_a_scores = []
job_offer_b_scores = []

# Loop through each factor and get scores for both job offers
for factor in factors:
    st.markdown(f"### {factor}")
    col1, col2 = st.columns(2)
    with col1:
        score_a = st.slider(f"Job Offer A - {factor}", 1, 5, 3, key=f"A_{factor}")
        job_offer_a_scores.append(score_a)
    with col2:
        score_b = st.slider(f"Job Offer B - {factor}", 1, 5, 3, key=f"B_{factor}")
        job_offer_b_scores.append(score_b)

# Step 2: Show the results
st.subheader("Step 2: Results")
total_a = sum(job_offer_a_scores)
total_b = sum(job_offer_b_scores)

st.write(f"Total Score for Job Offer A: **{total_a}**")
st.write(f"Total Score for Job Offer B: **{total_b}**")

# Create a DataFrame to display the comparison
df = pd.DataFrame({
    "Factor": factors,
    "Job Offer A": job_offer_a_scores,
    "Job Offer B": job_offer_b_scores
})

# Apply background colors to the scores based on rating
df_style = df.style.applymap(lambda score: set_background_color(score), subset=["Job Offer A", "Job Offer B"])

st.dataframe(df_style, use_container_width=True)

# Provide a download button for the comparison data as a CSV file
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Download Comparison as CSV",
    data=csv,
    file_name='job_offer_comparison.csv',
    mime='text/csv'
)

# Future improvement tip
st.info("✨ Tip: You can enhance this app by adding PDF export, login authentication, or factor weighting in future versions!")
