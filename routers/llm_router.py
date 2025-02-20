from fastapi import APIRouter
from utils import obter_logger_e_configuracao, executar_prompt


logger = obter_logger_e_configuracao()

router = APIRouter()


@router.post(
    "/gerar_descricao",
    summary="Gera uma descrição de cargo, com as atividades a serem realizadas, por cada cargo",
    description="Gera esta descrição curta utilizando a API Groq",
)
def gerar_descricao(cargo: str):
    logger.info(f"Cargo informado: {cargo}")

    descricao_cargo = executar_prompt(cargo)
    logger.info(f"Descrição gerada: {descricao_cargo}")

    return {"Descrição do Cargo": descricao_cargo}
