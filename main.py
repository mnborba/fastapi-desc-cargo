from fastapi import FastAPI, Depends
from utils import common_verificacao_api_token
from routers import llm_router


descricao = """
    API desenvolvida como apresentação de trabalho da disciplina Pós UFG.

    # Rotas definidas
    - /llm: retorna uma mensagem de sucesso
"""


app = FastAPI(
    title="FastAPI Aula 4b",
    description=descricao,
    version="4.3",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "Marcelo Nunes Borba",
        "url": "http://github.com/mnborba/",
        "email": "marceloborba@discente.ufg.br",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
    dependencies=[Depends(common_verificacao_api_token)],
)


app.include_router(llm_router.router, prefix="/llm")
