@app.route('/generate-blog', methods=['POST'])
def generate_blog_post():
    data = request.json
    keyword = data.get("keyword")
    article_url = data.get("article_url")

    if not keyword or not article_url:
        return jsonify({"error": "Missing required fields"}), 400

    article_content = requests.get(article_url).text[:4000]
    prompt = f"{keyword} 기사 요약: {article_content}\n이 정보를 바탕으로 블로그 글을 써줘."

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=600
    )

    blog_content = response.choices[0].text.strip()
    return jsonify({"result": blog_content})
