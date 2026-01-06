"""
THE APP:
Text to image generator web app using Streamlit and Stability AI API
that converts text descriptions into AI-generated images.

WHAT TO FIGURE OUT:
- How do you create a Streamlit web interface?
- How do you make API requests with authentication headers?
- How do you decode base64 image data?
- How do you convert binary data to images?
- How do you create download buttons for images?

START HERE:
First, create a basic Streamlit interface with text input.
Then work on making the API request with proper authentication.
Finally, decode and display the generated image.

KEY CONCEPT:
Use st.text_area() for multi-line text input.
API requires Bearer token authentication in headers.
Response contains base64-encoded image data.
Use base64.b64decode() to convert base64 to binary.
BytesIO creates in-memory file from binary data.
"""

#---------------------------------------------
# THE CODE SKELETON

# Import necessary libraries
# (streamlit, requests, PIL, BytesIO, os, dotenv)
import streamlit as st





# Load environment variables


# Set page config


# Header
st.header("Text to Image Generator")
st.divider()


# Get API key from environment


# Text input for image description
st.text_area("Enter your image description:", "")



# Example prompts
st.text("Example prompts:")
st.text("- Cute robot")
st.text("- Futuristic city")



# Generate button
st.button("Generate Image", type="primary")
    
        
            # API endpoint
            
            
            # Request headers
            
            
            
            
            # Request body
            
            
            
            
            
            
            
            # Make API request
            
            
            # Check if request was successful
            
                
                
                # Get image data from response
                
                
                
                # Convert to PIL Image
                
                
                # Display image
                
                
                
                # Download button