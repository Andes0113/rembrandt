from openai import OpenAI
client = OpenAI(api_key='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')

response = client.images.generate(
  model="dall-e-3",
  prompt="a white siamese cat",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)
