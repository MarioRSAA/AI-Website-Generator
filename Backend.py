from openai import OpenAI
import re

client = OpenAI(
    api_key="",
    base_url="https://openrouter.ai/api/v1"
)

SYSTEM_PROMPT = r"""
You are a frontend website code generator.

STRICT RULES — NO EXCEPTIONS:

1) Output EXACTLY three fenced code blocks and NOTHING ELSE.

2) The order MUST be:
   - First block: ```html   (contents of main.html)
   - Second block: ```css    (contents of main.css)
   - Third block: ```javascript  (contents of javascript.js)

3) Do NOT include any text, explanations, headings, labels, comments, or markdown outside the code blocks.

4) Each code block must contain ONLY valid code for its language.

5) Build a clean, modern, professional UI suitable for a paid product.

6) Use responsive design.

7) Account for different screen sizes.

If these rules are violated, the response is INVALID.
"""

def get_openai_response(user_input: str) -> str | None:
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            temperature=0.3,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input},
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        print("API error:", e)
        return None


def extract_and_save_files(text: str) -> bool:
    html_match = re.search(r"```html\s*(.*?)```", text, re.S | re.I)
    css_match = re.search(r"```css\s*(.*?)```", text, re.S | re.I)
    js_match = re.search(r"```(?:javascript|js)\s*(.*?)```", text, re.S | re.I)

    if not html_match or not css_match or not js_match:
        print("❌ Failed to extract one or more files")
        return False

    with open("main.html", "w", encoding="utf-8") as f:
        f.write(html_match.group(1).strip())

    with open("main.css", "w", encoding="utf-8") as f:
        f.write(css_match.group(1).strip())

    with open("javascript.js", "w", encoding="utf-8") as f:
        f.write(js_match.group(1).strip())

    return True


def generate_website(description: str, retries: int = 3) -> bool:
    for _ in range(retries):
        response = get_openai_response(description)
        if response and all([
            re.search(r"```html", response, re.I),
            re.search(r"```css", response, re.I),
            re.search(r"```(?:javascript|js)", response, re.I)
        ]):
            return extract_and_save_files(response)

    print("❌ Failed to generate valid website code")
    return False
