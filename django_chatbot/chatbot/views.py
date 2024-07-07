from django.shortcuts import render
from django.http import JsonResponse
from openai import OpenAI
import os

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

def ask_openai(message):
    try:
        response = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": message,
                }
            ],
            model="",
            max_tokens=150,
            temperature=0.7,
        )
        print(response)  # Print the response to the terminal for debugging
        answer = response['choices'][0]['message']['content'].strip()
        return answer
    except Exception as e:
        print(f"Error fetching response from OpenAI: {e}")
        return "Sorry, I couldn't process your request at the moment."

def chatbot(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html')
