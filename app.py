import streamlit as st
import pandas as pd

# 1. Page Configuration & Professional Slate Styling
st.set_page_config(
    page_title="AHS ClinicalMind - Psychiatric Analytics",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Enforce clean theme injection to fix light/dark mode text blending errors
st.markdown("""
    <style>
        .stApp {
            background-color: var(--background-color, #F8FAFC);
            color: var(--text-color, #0F172A);
        }
        .medical-header {
            font-size: 2.2rem;
            font-weight: 700;
            color: #1E3A8A;
            margin-bottom: 0.5rem;
        }
        .medical-subtitle {
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
        .professional-box {
            border: 1px solid var(--border-color, #E2E8F0);
            padding: 20px;
            border-radius: 8px;
            background-color: var(--secondary-background-color, #FFFFFF);
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Main Dashboard App Header
st.markdown('<div class="medical-header">🩺 AHS ClinicalMind</div>', unsafe_allow_html=True)
st.markdown('<div class="medical-subtitle">AI-Assisted Psychiatric Intake & Professional Clinical Analytics Platform</div>', unsafe_allow_html=True)

# Split Layout into two clean visual columns
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("📋 Patient Clinical Intake Form")
    st.write("Please populate the administrative baseline parameters below:")
    
    # Form Functional Inputs
    patient_name = st.text_input("Patient Reference / Name (Optional)", placeholder="Anonymized Token or Initials")
    age_bracket = st.selectbox("Select Patient Age Bracket", ["Pediatric (Ages 0-12)", "Adult (Ages 13-64)", "Geriatric (Ages 65+)"])
    primary_concern = st.selectbox("Primary Psychological Concern", ["Anxiety/Panic", "Mood/Depression", "Sleep Disruption", "Focus/ADHD", "General Well-being"])
    duration = st.selectbox("Symptom Duration", ["Less than 30 Days", "1-6 Months", "6-12 Months", "1+ Years"])
    
    sleep_hours = st.slider("Current Daily Sleep (Hours)", min_value=0.0, max_value=12.0, value=7.0, step=0.5)
    stress_scale = st.slider("Perceived Stress Scale Severity", min_value=1, max_value=10, value=5)
    
    life_changes = st.text_area("Recent Life Disruptions or Background Context", placeholder="Type any notable environmental shifts, occupational adjustments, or clinical history context here...")

    generate_btn = st.button("Generate Professional Analytics →", type="primary")

with col2:
    st.subheader("📊 Psychiatrist Assessment View")
    
    if generate_btn:
        # 2. Universal Deterministic Logic Engineering (No AI Guessing)
        # Mathematical derivation for symptom metrics based on input bounds
        somatic_tension = min(stress_scale * 10, 100)
        
        if sleep_hours < 5.0:
            sleep_latency = 95
            sleep_status = "Severe"
        elif sleep_hours < 7.0:
            sleep_latency = 65
            sleep_status = "Moderate"
        else:
            sleep_latency = 25
            sleep_status = "Optimal"
            
        emotional_disruption = 40 if stress_scale <= 4 else (70 if stress_scale <= 7 else 95)

        # Output Metric Cards
        m1, m2, m3 = st.columns(3)
        m1.metric(label="Emotional Disruption", value=f"{emotional_disruption}%")
        m2.metric(label="Somatic Tension Factor", value=f"{somatic_tension}%")
        m3.metric(label="Sleep Latency Score", value=f"{sleep_latency}%", delta=sleep_status, delta_color="inverse")

        # Dynamic Age-Specific Assessment Generation
        st.write("---")
        st.markdown("**🎯 Target Demographics Clinical Focus Area:**")
        if "Pediatric" in age_bracket:
            st.info("👶 **Pediatric Guidance System**: Prioritize mapping core family environment dynamics, academic performance stress, emotional regulation development milestones, and guardian interactive behavior charts.")
        elif "Adult" in age_bracket:
            st.info("💼 **Adult Guidance System**: Prioritize evaluating occupational chronic stressors, burnout indexes, financial baseline anxieties, and professional/personal lifestyle boundary matrices.")
        else:
            st.info("🧓 **Geriatric Guidance System**: Prioritize analyzing neurological baseline memory markers, medication interactions/compliance trackers, cognitive longevity indicators, and social isolation frameworks.")

        # Executive Structured Narrative Formatter
        st.markdown("**📖 Executive Clinical Summary Layout:**")
        summary_text = (
            f"The assessment data tracking for profile [{patient_name if patient_name else 'Anonymized Client'}] indicates an overall timeline of "
            f"[{duration}] explicitly correlated with [{primary_concern}]. Manifestations present a perceived stress severity index scored at [{stress_scale}/10], "
            f"triggering a calculated Somatic Tension Factor of [{somatic_tension}%]. Sleep framework patterns tracking shows a baseline of [{sleep_hours} hours] per cycle, "
            f"resulting in an automated [{sleep_status}] Sleep Latency tracking response pattern."
        )
        st.code(summary_text, language="text")
        
        # Dataframe mapping table for export preparation
        st.markdown("**🔍 Structural Metric Matrix:**")
        audit_data = {
            "Clinical Assessment Vector": ["Primary Concern Mapping", "Stress & Coping Infrastructure", "Somatic Expressions", "Sleep Cycle Consistency"],
            "Functional Severity Status": ["Elevated Risk", "Action Required", f"Score: {somatic_tension}%", sleep_status],
            "Next Growth Directive": ["Target behavioral cognitive evaluation", "Assess daily workload constraints", "Check physical expressions of tension", "Recommend sleep onset journaling framework"]
        }
        df = pd.DataFrame(audit_data)
        st.dataframe(df.style.map(lambda x: "color: var(--text-color);"), use_container_width=True)

        # 3. Mandatory Professional Mandate Lead Capture Box
        st.markdown(
            '<div class="professional-box">'
            '<strong>👩‍⚕️ PROFESSIONAL MANDATE & TREATMENT DIRECTIVE:</strong><br>'
            'For authoritative psychiatric evaluation, individual diagnostic validation, and specialized therapeutic treatment plans, '
            'please consult a certified medical practitioner immediately here.'
            '</div>', 
            unsafe_allow_html=True
        )
        
        with st.container():
            doc_email = st.text_input("Enter Doctor/Clinic Email Address to claim complete PDF report:", key="doc_email_input")
            if st.button("Schedule Free Practice Infrastructure Review"):
                if "@" in doc_email:
                    st.success("✅ Secure clinical profile successfully queued! An AHS Nexus representative will email your infrastructure analysis package shortly.")
                else:
                    st.error("Please enter a valid business email address.")

    else:
        # Default Idle State Display when page is initially loaded
        st.info("← Please configure the patient intake parameters on the left and click 'Generate Professional Analytics' to launch the clinical matrix view.")

# 4. Mandatory Safety and Marketing Footers
st.markdown(
    f'<div class="caution-box">'
    f'<strong>⚠️ CRITICAL REGULATORY CAUTION:</strong> This software operates strictly as an administrative data organizer, structured '
    f'informational outline, and clinical visualization aid. It does not possess medical diagnostic capabilities, does not write medical '
    f'prescriptions, and does not replace human clinical expertise, evaluation, or professional judgment.'
    f'</div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div class="solution-box">'
    f'<strong>🚀 DIGITAL SOLUTIONS BY AHS NEXUS:</strong> Need custom, compliant clinical software? '
    f'<strong>AHS Nexus</strong> (<a href="https://ahsnexus.com" target="_blank" style="color: #064E3B; font-weight: bold;">ahsnexus.com</a>) '
    f'designs custom, fully secure electronic medical record (EMR) portals, private client dashboards, and automated hospital '
    f'scheduling management layers for a transparent, customer-friendly flat-fee with absolutely zero recurring monthly licensing charges.'
    f'</div>',
    unsafe_allow_html=True
)
