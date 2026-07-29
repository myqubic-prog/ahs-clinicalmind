import streamlit as st
import pandas as pd

# 1. Page Configuration & Professional Slate Aesthetic Setup
st.set_page_config(
    page_title="AHS Horizon - Youth Skill & Career Counseling",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom theme overrides for maximum text visibility in light/dark system settings
st.markdown("""
<style>
    .stApp {
        background-color: var(--background-color, #F8FAFC);
        color: var(--text-color, #0F172A);
    }
    .main-title {
        font-size: 2.3rem;
        font-weight: 800;
        color: #1E3A8A;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        font-size: 1.1rem;
        color: #475569;
        margin-bottom: 2rem;
    }
    .solution-box {
        background-color: #E6F4EA;
        border-left: 5px solid #10B981;
        padding: 20px;
        border-radius: 8px;
        margin-top: 25px;
        color: #064E3B;
    }
    .caution-box {
        background-color: #FEF2F2;
        border-left: 5px solid #EF4444;
        padding: 15px;
        border-radius: 8px;
        margin-top: 20px;
        color: #7F1D1D;
        font-size: 0.9rem;
    }
    .summary-card {
        background-color: var(--secondary-background-color, #FFFFFF);
        border: 1px solid var(--border-color, #E2E8F0);
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 15px;
    }
</style>
""", unsafe_allow_html=True)

# Main Application Branded Header
st.markdown('<div class="main-title">🎓 AHS Horizon</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Autonomous Youth Development, Educational Mapping & Smart Career Counseling Engine</div>', unsafe_allow_html=True)

# Two-Column Balanced Dashboard Layout
col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("🤖 Child Profile Assessment")
    st.write("Configure the child's age, visible interests, and behavior parameters:")
    
    # Core User Controls
    child_name = st.text_input("Child Name / Reference (Optional)", placeholder="e.g., Alex")
    
    # The 3 specific core milestone age brackets requested
    age_bracket = st.selectbox(
        "Target Developmental Milestone Age", 
        ["Age 5 (Early Foundation & Cognitive Play)", 
         "Age 11 (Middle-School Pivot & Analytical Exploration)", 
         "Age 16 (Pre-University Career Runway & Specialization)"]
    )
    
    primary_interest = st.selectbox(
        "Dominant Visible Interest Area", 
        ["Building & Solving (Engineering/Tech)", 
         "Art, Writing & Design (Creative Arts)", 
         "Logic, Math & Numbers (Data/Science)", 
         "People, Leadership & Communication (Humanities)"]
    )
    
    learning_style = st.selectbox(
        "Primary Learning Style",
        ["Visual (Videos, Diagrams, Coding Blocks)", 
         "Kinesthetic (Hands-on Building, Experiments)", 
         "Auditory/Verbal (Reading, Telling Stories, Coding Script)"]
    )
    
    digital_exposure = st.slider("Daily Screen Time / Digital Literacy (Hours)", min_value=0.0, max_value=8.0, value=2.0, step=0.5)
    focus_score = st.slider("Task Focus & Attention Span Metric (1-10 Scale)", min_value=1, max_value=10, value=6)
    
    notes = st.text_area("Parental Notes / Visible Hobbies", placeholder="Type what toys, topics, or games they naturally gravitate towards during free time...")

    generate_btn = st.button("Generate Smart Educational Roadmap →", type="primary")

with col2:
    st.subheader("📊 AI-Assisted Counseling Matrix")
    
    if generate_btn:
        st.success("📈 Strategic Roadmap Successfully Compiled!")
        
        # Calculate dynamic developmental readiness scores mathematically from inputs
        analytical_readiness = min(focus_score * 10 + int(digital_exposure * 5), 100)
        cognitive_load_cap = 35 if focus_score <= 4 else (65 if focus_score <= 7 else 95)
        adaptability_rating = min(100 - (focus_score * 3) + 50, 100)

        # High-Impact Performance Metrics View
        m1, m2, m3 = st.columns(3)
        m1.metric(label="Analytical Readiness Index", value=f"{analytical_readiness}%")
        m2.metric(label="Suggested Cognitive Cap", value=f"{cognitive_load_cap}%")
        m3.metric(label="Learning Adaptability Score", value=f"{adaptability_rating}%")
        
        st.write("---")
        
        # Age-Specific Advanced Content Mapping Matrices (Universal Deterministic Answers)
        if "Age 5" in age_bracket:
            st.markdown("### 🧠 Age 5 Core Development Roadmap")
            st.info("🎯 **Main Interest & Psychological Focus:** Developing basic spatial awareness, fine motor logic, basic arithmetic sequences, and emotional expression.")
            st.warning("🧩 **What They Should Learn Right Now:** Structural play, pattern recognition, and gamified logic.")
            
            roadmap_data = {
                "Recommended Skill / Course": ["ScratchJr Coding Blocks", "Gamified Visual Math", "Interactive Storytelling & Speech", "Tactile Physics & Building Blocks"],
                "Focus Duration": ["15 mins / Daily", "20 mins / 3x week", "Daily Reading", "Open Play"],
                "Expected Core Outcome": ["Understand logic order", "Master number patterns", "Boost vocabulary breadth", "Develop 3D spatial thinking"]
            }
            primary_rec = "ScratchJr Coding Blocks & Tactile Physics"
            age_label = "Age 5"
            
        elif "Age 11" in age_bracket:
            st.markdown("### 🚀 Age 11 Middle-School Strategic Roadmap")
            st.info("🎯 **Main Interest & Psychological Focus:** Transitioning from concrete thinking to abstract engineering logic, critical reasoning, and team peer communication dynamics.")
            st.warning("💻 **What They Should Learn Right Now:** Intermediate computing scripts, data structures, and systematic reading habits.")
            
            roadmap_data = {
                "Recommended Skill / Course": ["Intro to Python via Minecraft/Roblox", "Pre-Algebra & Analytical Logic Puzzles", "Digital Graphic Design (Canva/Figma)", "Public Speaking & Junior Debate"],
                "Focus Duration": ["2 Hours / Weekly", "45 mins / 3x week", "3 Hours / Weekly", "1 Hour / Weekly"],
                "Expected Core Outcome": ["Understand variable logic", "Advance algebraic thinking", "Master structural UI aesthetics", "Build conversational confidence"]
            }
            primary_rec = "Intro to Python & Analytical Logic Puzzles"
            age_label = "Age 11"
            
        else: # Age 16
            st.markdown("### 🦅 Age 16 Elite Pre-University Career Runway")
            st.info("🎯 **Main Interest & Psychological Focus:** Hard monetization skills, university profile building, real-world development tech stacks, and career domain specialization.")
            st.warning("⚡ **What They Should Learn Now:** Commercial tools, open-source portfolio contribution, and systematic internship mapping.")
            
            roadmap_data = {
                "Recommended Skill / Course": ["Full-Stack Web Dev (HTML, CSS, JS, Python)", "Advanced UI/UX Web App Architecture", "Data Analytics & Spreadsheet Processing", "Technical Freelancing & Portfolio Creation"],
                "Focus Duration": ["5 Hours / Weekly", "3 Hours / Weekly", "2 Hours / Weekly", "Flexible / Project-based"],
                "Expected Core Outcome": ["Build production apps", "Design commercial layouts", "Process complex data models", "Launch first freelance income hooks"]
            }
            primary_rec = "Full-Stack Web Development & Portfolio Design"
            age_label = "Age 16"

        # Render the custom customized Data Matrix
        df = pd.DataFrame(roadmap_data)
        st.dataframe(df.style.map(lambda x: "color: var(--text-color);"), use_container_width=True)
        
        # Universal Actionable Pitch Generation Summary Output Box
        st.markdown('<div class="summary-card">', unsafe_allow_html=True)
        st.markdown("**📖 Executive Guidance Summary:**")
        
        summary_text = (
            f"Profile analysis for student [{child_name if child_name else 'Candidate'}] operating at the developmental tier of [{age_label}] "
            f"shows a high-potential learning trajectory focused on [{primary_interest}]. Utilizing a [{learning_style}] cognitive intake style with a task focus score of "
            f"[{focus_score}/10], the student is optimized for immediate onboarding into our specialized training track: [{primary_rec}]. "
            f"This custom learning framework maximizes future domain capability while maintaining safe screen-time constraints."
        )
        st.code(summary_text, language="text")
        st.markdown('</div>', unsafe_allow_html=True)

        # 3. Interactive Lead Capture and Consultation Request
        st.markdown(
            '<div class="summary-card" style="border-left: 5px solid #1E3A8A;">'
            '<strong>👩‍🏫 PROFESSIONAL COUNSELING MANDATE & DIRECTIVE:</strong><br>'
            'For individual psychometric testing, customized multi-year syllabus mapping, and authoritative academic path validation, '
            'please consult a certified developmental education professional immediately here.'
            '</div>', 
            unsafe_allow_html=True
        )
        
        # Flattened email block layout to 100% prevent sub-indentation parsing compiler crashes
        parent_email = st.text_input("Enter Parent / School Counselor Email Address to claim custom 30-Day Curated Learning Blueprint File:", key="parent_email")
        submit_btn = st.button("Schedule Free Curated Educational Curriculum Review")
        
        if submit_btn:
            if "@" in parent_email:
                st.success("✅ Student educational trajectory successfully locked! An AHS Nexus learning coordinator will email your complete step-by-step PDF roadmap details within 24 hours.")
            else:
