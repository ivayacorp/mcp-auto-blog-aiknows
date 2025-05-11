from flask import Flask, request, jsonify
import requests
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")  # 환경변수로 키 처리

@app.route('/mcp', methods=['POST'])
def generate_blog_post():
    data = request.json
    keyword = data.get("keyword")
    article_url = data.get("article_url")

    article_content = requests.get(article_url).text[:4000]

    prompt = f"키워드: {keyword}\n기사 요약: {article_content}\n이 정보를 바탕으로 블로그 글을 써줘."

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=600
    )

    blog_content = response.choices[0].text.strip()
    return jsonify({"blog_content": blog_content})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
