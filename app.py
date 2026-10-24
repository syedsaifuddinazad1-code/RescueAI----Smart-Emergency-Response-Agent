# RescueAI----Smart-Emergency-Response-Agent

import streamlit as st
from datetime import datetime


# ----------------------------------
# DisasterGuard AI
# Emergency Response Planning Agent
# ----------------------------------

st.set_page_config(
    page_title="DisasterGuard AI",
    page_icon="🚨",
    layout="wide"
)


# Emergency resources configured for demonstration.
# Replace these with verified local resources before deployment.
EMERGENCY_RESOURCES = {
    "flood": [
        "Local disaster management authority",
        "Local fire and rescue service",
        "Verified local emergency shelter"
    ],
    "lightning": [
        "Local emergency medical service",
        "Local disaster management authority"
    ],
    "earthquake": [
        "Local fire and rescue service",
        "Local disaster management authority",
        "Verified local emergency shelter"
    ],
    "cyclone": [
        "Local disaster management authority",
        "Local emergency shelter",
        "Local fire and rescue service"
    ],
    "fire": [
        "Local fire and rescue service",
        "Local emergency medical service"
    ],
    "other": [
        "Local emergency services",
        "Local disaster management authority"
    ]
}


def analyze_emergency(report):
    """
    Analyze a report using basic keyword matching.

    This is a demonstration classifier, not a trained AI model.
    """

    text = report.lower()

    if any(word in text for word in [
        "flood", "flooding", "water entering", "water rising"
    ]):
        disaster = "Flood"

    elif any(word in text for word in [
        "lightning", "thunderstorm", "thunder"
    ]):
        disaster = "Lightning / Thunderstorm"

    elif any(word in text for word in [
        "earthquake", "tremor", "building shaking"
    ]):
        disaster = "Earthquake"

    elif any(word in text for word in [
        "cyclone", "hurricane", "strong winds"
    ]):
        disaster = "Cyclone / Severe Winds"

    elif any(word in text for word in [
        "fire", "smoke", "burning"
    ]):
        disaster = "Fire"

    else:
        disaster = "Other Emergency"

    # Look for reported immediate danger.
    critical_words = [
        "trapped",
        "person missing",
        "people missing",
        "collapsed",
        "collapse",
        "unconscious",
        "injured",
        "life-threatening"
    ]

    high_words = [
        "rising rapidly",
        "houses flooded",
        "house flooded",
        "power line",
        "power lines",
        "road blocked",
        "heavy flooding"
    ]

    if any(word in text for word in critical_words):
        severity = "CRITICAL — Immediate danger reported"
        priority = 1

    elif any(word in text for word in high_words):
        severity = "HIGH — Urgent assessment needed"
        priority = 2

    else:
        severity = "UNASSESSED — Human verification required"
        priority = 3

    return disaster, severity, priority


def get_resource_key(disaster):
    """Map a detected disaster to the resource directory."""

    mapping = {
        "Flood": "flood",
        "Lightning / Thunderstorm": "lightning",
        "Earthquake": "earthquake",
        "Cyclone / Severe Winds": "cyclone",
        "Fire": "fire"
    }

    return mapping.get(disaster, "other")


def create_response_plan(report, disaster, priority):
    """Generate practical safety recommendations and tasks."""

    text = report.lower()

    actions = [
        {
            "task": "Notify emergency services",
            "details": (
                "Contact the verified local emergency service "
                "and report the exact location and danger."
            )
        },
        {
            "task": "Protect people",
            "details": (
                "Move away from immediate danger if safe. "
                "Do not enter hazardous areas to attempt a rescue."
            )
        },
        {
            "task": "Share verified information",
            "details": (
                "Record the location, number of people affected, "
                "and immediate hazards. Avoid spreading rumors."
            )
        }
    ]

    if disaster == "Flood":
        actions.insert(0, {
            "task": "Flood safety",
            "details": (
                "Stay out of floodwater. Move to higher ground "
                "if safe, and never walk or drive through floodwater."
            )
        })

    elif disaster == "Lightning / Thunderstorm":
        actions.insert(0, {
            "task": "Lightning safety",
            "details": (
                "Get inside a substantial enclosed building or "
                "hard-topped vehicle. Avoid open areas and isolated trees."
            )
        })

    elif disaster == "Earthquake":
        actions.insert(0, {
            "task": "Earthquake safety",
            "details": (
                "During shaking, drop, cover, and hold on. "
                "After shaking stops, watch for damage and follow "
                "official evacuation instructions."
            )
        })

    elif disaster == "Cyclone / Severe Winds":
        actions.insert(0, {
            "task": "Severe weather safety",
            "details": (
                "Stay indoors, away from windows, and follow "
                "official weather warnings and evacuation orders."
            )
        })

    elif disaster == "Fire":
        actions.insert(0, {
            "task": "Fire safety",
            "details": (
                "Leave the affected building using a safe exit, "
                "avoid smoke, and do not re-enter."
            )
        })

    if any(word in text for word in [
        "trapped", "unconscious", "injured", "person missing"
    ]):
        actions.insert(0, {
            "task": "URGENT: Report people in danger",
            "details": (
                "Tell emergency dispatchers the exact location "
                "and the number of people believed to be at risk. "
                "Do not attempt a dangerous rescue yourself."
            )
        })

    if priority == 1:
        priority_label = "Priority 1 — Immediate escalation"
    elif priority == 2:
        priority_label = "Priority 2 — Urgent assessment"
    else:
        priority_label = "Priority 3 — Verify and assess"

    return priority_label, actions


def main():
    st.title("🚨 DisasterGuard AI")
    st.subheader("Emergency Response Planning & Coordination")

    st.write(
        "Report an emergency to generate a preliminary safety plan "
        "and an organized list of response tasks."
    )

    st.warning(
        "This is a demonstration tool. Its severity labels are "
        "keyword-based, not professional risk assessments. "
        "Contact verified emergency services immediately when "
        "someone may be in danger."
    )

    with st.form("emergency_form"):
        location = st.text_input(
            "Emergency location",
            placeholder="Enter town, street, or landmark"
        )

        report = st.text_area(
            "Describe the emergency",
            placeholder=(
                "Example: Heavy rain has flooded our street "
                "and water is entering houses."
            ),
            height=150
        )

        submitted = st.form_submit_button(
            "Analyze Emergency"
        )

    if submitted:
        if not location.strip() or not report.strip():
            st.error(
                "Please provide both the location and emergency report."
            )
            return

        disaster, severity, priority = analyze_emergency(report)

        resource_key = get_resource_key(disaster)

        priority_label, actions = create_response_plan(
            report,
            disaster,
            priority
        )

        st.divider()
        st.header("📋 Emergency Assessment")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Detected Incident", disaster)

        with col2:
            st.metric("Preliminary Priority", priority)

        with col3:
            st.metric("Response Tasks", len(actions))

        st.write("**Reported location:**", location)
        st.write("**Assessment:**", severity)
        st.write("**Coordination status:** Plan generated; no tasks dispatched.")

        st.subheader("🛡️ Recommended Response Plan")

        for index, action in enumerate(actions, start=1):
            st.markdown(
                f"**{index}. {action['task']}**"
            )
            st.write(action["details"])

        st.subheader("🤝 Suggested Coordination Resources")

        for resource in EMERGENCY_RESOURCES[resource_key]:
            st.write(f"• {resource}")

        st.subheader("📝 Responder Task Checklist")

        for index, action in enumerate(actions, start=1):
            st.checkbox(
                f"{index}. {action['task']}",
                key=f"task_{index}"
            )

        st.caption(
            "Resources are suggestions, not verified live contacts. "
            "Confirm availability and suitability before use."
        )

        st.caption(
            "Generated at: "
            + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )

        st.success(
            "Response plan generated. Share it with authorized "
            "responders for human review and coordination."
        )


if __name__ == "__main__":
    main()
