import os
import streamlit as st
from groq import Groq

# Set the API key for Groq
os.environ["GROQ_API_KEY"] = "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"

client = Groq()

# Title for the Streamlit app
st.title("🌍✈️ AI Travel Genie 🌟")
st.write("✨ Plan your dream trip effortlessly with the magic of AI! 🤖🌴")

with st.sidebar:

# Input fields for the user
    destination = st.text_input("Enter your destination:")
    budget = st.text_input("Enter your budget:")
    start_date = st.date_input("Start date:")
    end_date = st.date_input("End date:")
    preferences = st.text_area("Enter your preferences (e.g., sightseeing, adventure, cuisine):")

# Button to trigger the travel plan generation
if st.button("Generate Travel Plan"):
    if not (destination and budget and start_date and end_date and preferences):
        st.error("Please fill in all fields to generate your travel plan.")
    else:
        # Display a loading animation
        with st.spinner("Generating your travel plan..."):
            try:
                # Create chat messages for the API
                messages = [
                    {
                        "role": "system",
                        "content": (
                            "You are a travel planner assistant that helps create travel itineraries "
                            "based on user inputs."
                        ),
                    },
                    {
                        "role": "user",
                        "content": (
                            f"Plan a trip to {destination} with a budget of {budget}. "
                            f"Dates: {start_date} to {end_date}. Preferences: {preferences}."
                        ),
                    },
                ]

                # Call the Groq API
                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant", messages=messages
                )




                # Extract the response content
                assistant_response = response.choices[0].message.content

                # Display the generated travel plan
                st.success("Travel plan generated successfully!")
                st.write("Your Travel Plan:", assistant_response, height=300)
            except Exception as e:
                st.error(f"An error occurred: {e}")
