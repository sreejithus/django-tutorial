from google import genai


api_key="AIzaSyC04p986dY9YsWCxfCJBE0QM0UsOU7wpCw"

client = genai.Client(api_key=api_key)

prompt = "ai projects react-django "





response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents=prompt
)

print(response.text)