from fastapi import HTTPException
from groq import Groq
import os
import logging
from dotenv import load_dotenv
import openai


load_dotenv()


API_TOKEN = int(os.getenv("API_TOKEN"))


def obter_logger_e_configuracao():
    """
    Configura o logger padrão para o nível de informação e formato especiticado.

    Retorna:
        logging.Logger: Um objetivo de logger com as configurações padrões.
    """
    logging.basicConfig(
        level=logging.INFO, format="[%(levelname)s] %(asctime)s: %(message)s"
    )
    logger = logging.getLogger("fastapi")
    return logger


def common_verificacao_api_token(api_token: int):
    """
    Verifica se o token da API fornecido é válido.

    Args:
        api_token (int): O token da API a ser verificado.

    Raises:
        HTTPException: Se o token da API for inválido, uma exceção HTTP 401 é levantada com a mensagem "API Token inválido".
    """
    if api_token != API_TOKEN:
        raise HTTPException(status_code=401, detail="API Token inválido")


def executar_prompt_cargo(cargo: str):
    """
    Gera uma descrição de cargo, com as atividades a serem realizadas, por cada cargo.

    Args:
        cargo (str): O cargo sobre o qual a descrição será escrita.

    Returns:
        str: A descrição do cargo API Groq.
    """
    prompt = f"O método DISC é uma metodologia comportamental que ajuda gestores a tomarem decisões \
    estratégicas com base no perfil comportamental do time.  \
    Com base neste método, retorne em um parágrafo de até 5 linhas, qual os dois tipos de perfis \
    predominantes são adequados ao {cargo}?"

    client = Groq(
        api_key=os.getenv("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    return chat_completion.choices[0].message.content


def executar_prompt_perfil(cargo: str):
    """
    Gera uma descrição de cargo, com as atividades a serem realizadas, por cada cargo.

    Args:
        cargo (str): O cargo sobre o qual a descrição será escrita.

    Returns:
        str: A descrição do cargo gerada pela API OpenAI.
    """
    prompt = f"O método DISC é uma metodologia comportamental que ajuda gestores a tomarem decisões \
    estratégicas com base no perfil comportamental do time.  \
    Com base neste método, retorne em um parágrafo de até 5 linhas, qual os dois tipos de perfis \
    predominantes são adequados ao {cargo}?"

    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-4o-mini",  # Escolha um modelo da OpenAI
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content