import streamlit as st
st.write('testes')

if st.button('testes'):
    import os
    from google import genai
    from google.genai import types
    from google.genai.errors import ClientError



    GEMINI_API_KEY = st.secrets['GEMINI_API_KEY']

    def generate(input_text: str = "What is the capital of France?",):
        client = genai.Client(
            api_key=GEMINI_API_KEY,
        )

        model = "gemini-3-flash-preview"
        contents = [
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(text=input_text),
                ],
            ),
        ]
            
        generate_content_config = types.GenerateContentConfig(
            # Set thinking to MINIMAL or LOW to save thousands of background tokens
            thinking_config=types.ThinkingConfig(
                thinking_level="MINIMAL",
            ),
            # Hard ceiling on combined thinking + output tokens to prevent quota drainage
            max_output_tokens=1024, 
            tools= None,
        )

        resultado = []

        try:
            for chunk in client.models.generate_content_stream(
                model=model,
                contents=contents,
                config=generate_content_config,
            ):
                if text := chunk.text:
                    resultado.append(text)
            print() 
            
        except ClientError as e:
            print(f"\n[API Error]: {e}")

        return resultado 

    resultado = generate("Quem ganhou o jogo da argentina e austria? nessa copa ")
    st.write(resultado)
    