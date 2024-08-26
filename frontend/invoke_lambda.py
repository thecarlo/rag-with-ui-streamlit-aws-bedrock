import json
import logging

import requests
import streamlit as st

logging.basicConfig(level=logging.INFO)


def invoke_lambda(user_input):
    lambda_endpoint = st.secrets["lambda_endpoint"]

    try:
        logging.debug("invoking API with query '%s'", user_input)

        headers = {
            "Content-Type": "application/json",
        }

        prompt_template = "%s. Format results in markdown format." % user_input

        response = requests.post(
            lambda_endpoint,
            headers=headers,
            data=json.dumps({"prompt": prompt_template}),
        )

        logging.debug("response status = %s", response.status_code)

        response.raise_for_status()

        response_body = json.loads(response.text)

        logging.debug(f"response_body: {response_body}")

        text_response = response_body.get(
            "text", "No response text received from AWS Lambda"
        )

        logging.debug(f"text_response: {text_response}")

        return text_response
    except Exception as e:
        logging.error("Lambda error: %s", e)

        return f"Error invoking Lambda: {e}"
