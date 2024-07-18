from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Google Generative AI client
api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=api_key)

# Example function to interact with Gemini API
def ask_google_genai(message):
    try:
        # Initialize the GenerativeModel with your desired model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Generate content based on the message
        response = model.generate_content(message)
        
        return response.text.strip()  # Extract the text response
    except Exception as e:
        print(f"Error fetching response from Google Generative AI: {e}")
        return "Sorry, I couldn't process your request at the moment."

# Example Django view function
def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_google_genai(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')
