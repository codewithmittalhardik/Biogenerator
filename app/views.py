import json
import os
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from groq import Groq # <--- NEW LIBRARY
from dotenv import load_dotenv
load_dotenv()


# --- PASTE YOUR GROQ API KEY HERE ---
# Get it for free at: https://console.groq.com/keys
GROQ_API_KEY = os.getenv("API_KEY")

@csrf_exempt
def generate_ai_content(request):
    if request.method == 'POST':
        try:
            client = Groq(api_key=GROQ_API_KEY)

            data = json.loads(request.body)
            user_text = data.get('text', '')
            request_type = data.get('type')

            # Define Prompts
            if request_type == 'bio':
                prompt = f"Write a professional Instagram bio for: '{user_text}'. Keep it under 150 chars, use emojis."
            elif request_type == 'post':
                prompt = f"Write an engaging caption for a post about: '{user_text}'. Include a hook and call to action."
            elif request_type == 'hashtag':
                prompt = f"Generate 30 trending hashtags for: '{user_text}'. Output ONLY hashtags."
            else:
                return JsonResponse({'error': 'Unknown request type'}, status=400)

            # Generate Content (UPDATED MODEL NAME)
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                # ✅ UPDATED to the newest working model
                model="llama-3.1-8b-instant", 
            )

            result = chat_completion.choices[0].message.content
            return JsonResponse({'result': result})

        except Exception as e:
            print(f"SERVER ERROR: {e}") 
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=400)

# --- YOUR PAGE VIEWS ---
def home(request): return render(request, 'home.html')
def why(request): return render(request, 'why.html')
def about(request): return render(request, 'about.html')
def privacy(request): return render(request, 'privacy.html')
def terms(request): return render(request, 'terms.html')
def bio(request): return render(request, 'bio.html')
def hashtags(request): return render(request, 'hashtag.html')
def posts(request): return render(request, 'posts.html')