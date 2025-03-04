import streamlit as st
from pathlib import Path
import random

# Set page config
st.set_page_config(
    page_title="BMI Calculator Python",
    page_icon="./static/favicon.ico",
    layout="centered"
)

def calculate_bmi(weight, height):
    """Calculate BMI given weight (kg) and height (m)"""
    return round(weight / (height ** 2), 1)

def get_bmi_category(bmi):
    """Return BMI category with fancy styling"""
    categories = [
        ("Underweight", "#4ecdc4", "#96c93d", "🌟"),
        ("Normal", "#45b7d1", "#feca57", "✨"),
        ("Overweight", "#ff6b6b", "#ff9f1c", "⚡"),
        ("Obese", "#ff4757", "#d63031", "🔥")
    ]
    for cat, color1, color2, emoji in categories:
        if (bmi < 18.5 and cat == "Underweight") or \
           (18.5 <= bmi < 25 and cat == "Normal") or \
           (25 <= bmi < 30 and cat == "Overweight") or \
           (bmi >= 30 and cat == "Obese"):
            return cat, color1, color2, emoji
    return "Normal", "#45b7d1", "#feca57", "✨"

# Custom CSS
def load_css():
    css_path = Path("./static/style.css")
    if css_path.exists():
        with open(css_path) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Load CSS
load_css()

# Main app
def main():
    # Fancy header with centered logo and left margin
    # Use columns with an empty left column to create margin effect
    col1, col2, col3, col4 = st.columns([0.2, 1.1, 0.9, 1])  # 0.2 creates roughly 2vmin-like spacing
    with col3:
        # Wrap the logo image with a div that will be styled in CSS for centering
        st.markdown('<div class="logo-container">', unsafe_allow_html=True)
        st.image("./static/logo.png", width=100)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
        <div class="header">
            <div class="head1">BMI Calculator Streamlit Python Web App</div>
            <div class="head2">Project 8: Create a Python Streamlit BMI Calculator Web App in Just 6 Minutes</div>
            <div class="head3">FOR GIAIC Q3 - ROLL # 00037391 BY MERCHANTSONS</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Input form with colorful containers
    with st.form(key='bmi_form'):
        col1, col2 = st.columns(2)
        
        with col1:
            weight = st.number_input("Weight (kg)", min_value=20.0, max_value=300.0, value=70.0, step=0.1)
        
        with col2:
            height = st.number_input("Height (m)", min_value=0.5, max_value=2.5, value=1.7, step=0.01)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Fancy submit button
        submit_button = st.form_submit_button(label="Calculate Your BMI! 🌈")
    
    # Calculate and display results with flair
    if submit_button:
        bmi = calculate_bmi(weight, height)
        category, color1, color2, emoji = get_bmi_category(bmi)
        
        # Random sparkle effect position
        sparkle_pos = random.randint(0, 80)
        
        st.markdown(
            f"""
            <div class="result-card" style="background: linear-gradient(135deg, {color1}, {color2})">
                <div class="sparkle" style="left: {sparkle_pos}%;"></div>
                <h2>{emoji} Your BMI: {bmi} {emoji}</h2>
                <p class="category pulse">Category: {category}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    # Add footer with copyright
    st.markdown(
        """
        <div class="footer">
            <p>© Copyright 2025 Merchantsons. All rights reserved.</p>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()