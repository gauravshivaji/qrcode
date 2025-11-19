import streamlit as st

st.set_page_config(
    page_title="Sandeep Ramchandra Gavali",
    page_icon="🕴️",
    layout="centered"
)

# ---------------- HEADER ----------------
st.title("🕴️ Business Tycoon Profile")
st.header("Sandeep Ramchandra Gavali")

st.markdown(
    """
    <h4 style="text-align:center; color:#555;">
        Visionary entrepreneur • Strategic investor • Business tycoon
    </h4>
    """,
    unsafe_allow_html=True
)

st.write("")

# ---------------- PROFILE SECTION ----------------
col1, col2 = st.columns([1, 2])

with col1:
    st.image(
        "WhatsApp Image 2025-11-19 at 1.31.07 PM.jpeg",
        caption="Sandeep Ramchandra Gavali",
        use_column_width=True
    )

with col2:
    st.subheader("💼 About Sandeep")
    st.write(
        """
        Sandeep Ramchandra Gavali is a dynamic business tycoon known for his
        sharp decision-making, fearless execution, and long-term vision.

        He builds businesses the way others build dreams — with clarity,
        courage, and consistency.
        """
    )

    st.markdown("### 🔥 Why he stands out:")
    st.markdown(
        """
        - 🚀 Turns ideas into profitable businesses with speed and precision  
        - 🧠 Strong strategic mindset with a focus on growth and innovation  
        - 🤝 Builds powerful networks and long-term partnerships  
        - 📈 Loves scaling businesses, not just starting them  
        """
    )

# ---------------- INTERACTIVE PRAISE ----------------
st.markdown("---")
st.subheader("💬 Show Some Appreciation")

praise_option = st.selectbox(
    "Choose what you admire most about Sandeep:",
    [
        "His business mindset",
        "His leadership style",
        "His risk-taking ability",
        "His vision for the future"
    ]
)

if praise_option:
    st.success(f"✅ You admire Sandeep's **{praise_option}**. Great choice!")

if st.button("👏 Send a virtual applause"):
    st.balloons()
    st.success("Sandeep deserves this applause! 👏👏👏")

# ---------------- BUSINESS METRICS ----------------
st.markdown("---")
st.subheader("📊 Business Snapshot (Demo)")

m1, m2, m3 = st.columns(3)
with m1:
    st.metric("Years of Experience", "10+", "Growing")
with m2:
    st.metric("Businesses Handled", "5+", "Expanding")
with m3:
    st.metric("Vision", "Global Entrepreneur", "On Track")

# ---------------- CARS / LUXURY SECTION ----------------
st.markdown("---")
st.subheader("🚗 Signature Cars & Lifestyle")

st.write(
    """
    A tycoon deserves machines that match his personality — powerful, bold, and dominant.
    These cars reflect Sandeep’s presence and mindset.
    """
)

car_col1, car_col2 = st.columns(2)
car_col3, car_col4 = st.columns(2)

with car_col1:
    st.image(
        "https://images.pexels.com/photos/356830/pexels-photo-356830.jpeg",
        caption="Mahindra XUV700 – Power & Presence",
        use_column_width=True
    )

with car_col2:
    st.image(
        "https://images.pexels.com/photos/358070/pexels-photo-358070.jpeg",
        caption="Toyota Fortuner – Dominance on Road",
        use_column_width=True
    )

with car_col3:
    st.image(
        "https://images.pexels.com/photos/170811/pexels-photo-170811.jpeg",
        caption="Luxury SUV – Class & Comfort",
        use_column_width=True
    )

with car_col4:
    st.image(
        "https://images.pexels.com/photos/210019/pexels-photo-210019.jpeg",
        caption="Premium Ride – Statement of Success",
        use_column_width=True
    )

st.markdown("### ✅ Highlights:")
st.markdown(
    """
    - 💪 Bold SUVs that match his strong personality  
    - 🛣️ Built for long drives, business trips, and luxury travel  
    - 🎯 Represents power, stability, and growth  
    """
)

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("Profile powered by Streamlit – QR-ready personal brand page.")
