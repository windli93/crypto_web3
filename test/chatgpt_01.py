import json
import unittest

import requests


class MyTestCase(unittest.TestCase):

    def test_chatgpt_01(self):
        api_endpoint = "https://api.openai.com/v1/engines/davinci-codex/completions"
        access_token = "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"

        prompt_text = "Hello, how are you today?"
        params = {
            "prompt": prompt_text,
            "temperature": 0.7,
            "max_tokens": 60,
            "top_p": 1,
            "frequency_penalty": 0.5,
            "presence_penalty": 0.0
        }

        # Send the API request
        headers = {"Content-Type": "application/json",
                   "Authorization": f"Bearer {access_token}"}
        response = requests.post(api_endpoint, headers=headers, json=params)

        # Process the API response
        if response.status_code == 200:
            print(f"ChatGPT response1: {response.text}")
            response_text = json.loads(response.text)["choices"][0]["text"]
            print(f"ChatGPT response2: {response_text}")
        else:
            print(f"Error: {response.status_code} - {response.text}")


if __name__ == '__main__':
    unittest.main()
