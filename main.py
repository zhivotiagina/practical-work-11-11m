import requests

class LLMClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.url = "https://openrouter.ai/api/v1/chat/completions"

    def ask(self, prompt: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost",
            "X-Title": "PracticalWork11"
        }

        data = {
            "model": "openrouter/free",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        try:
            response = requests.post(self.url, headers=headers, json=data)
            result = response.json()

            if "error" in result:
                return f"Ошибка API: {result['error']}"

            return result["choices"][0]["message"]["content"]

        except Exception as e:
            return f"Ошибка: {e}"

        try:
            response = requests.post(self.url, headers=headers, json=data)
            result = response.json()

            # 👉 ВАЖНО: сначала смотрим, есть ли ошибка
            if "error" in result:
                return f"Ошибка API: {result['error']}"

            # 👉 безопасно достаём ответ
            return result.get("choices", [{}])[0].get("message", {}).get("content", "Нет ответа")

        except Exception as e:
            return f"Ошибка: {e}"

        try:
            response = requests.post(self.url, headers=headers, json=data)
            result = response.json()

            return result["choices"][0]["message"]["content"]

        except Exception as e:
            return f"Ошибка: {e}"

def main():
    api_key = input("Введите API ключ OpenRouter: ")

    llm = LLMClient(api_key)

    while True:
        user_input = input("\nВаш вопрос: ")

        if user_input.lower() == "выход":
            break

        answer = llm.ask(user_input)
        print("\nОтвет:", answer)

if __name__ == "__main__":
    main()