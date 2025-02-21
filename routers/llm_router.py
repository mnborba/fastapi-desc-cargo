from fastapi import APIRouter
from utils import obter_logger_e_configuracao, executar_prompt_cargo, executar_prompt_perfil


logger = obter_logger_e_configuracao()

router = APIRouter()


@router.post(
    "/gerar_descricao",
    summary="Gera uma descrição de cargo, com as atividades a serem realizadas, por cada cargo - LLM Groq",
    description="Gera esta descrição curta utilizando a API Groq",
)
def gerar_descricao(cargo: str):
    logger.info(f"Cargo informado: {cargo}")

    descricao_cargo = executar_prompt_cargo(cargo)
    logger.info(f"Descrição gerada: {descricao_cargo}")

    return {"Descrição do Cargo": descricao_cargo}

@router.post(
    "/gerar_perfil",
    summary="Gera o perfil comportamental indicado para um determinado cargo - LLM OpenAI 4o-mini",
    description="Gera o perfil utilizando a API da OpenAI",
)
def gerar_perfil(cargo: str):
    logger.info(f"Cargo informado: {cargo}")

    perfil_cargo = executar_prompt_perfil(cargo)
    logger.info(f"Perfil gerado: {perfil_cargo}")

    return {"Perfil do Cargo": perfil_cargo}

@router.post(
    "/gerar_perfil/v2",
    summary="Gera o perfil comportamental indicado para um determinado cargo, em um arquivo markdown - LLM OpenAI 4o-mini",
    description="Gera o perfil utilizando a API da OpenAI e salva em um arquivo markdown",
)
def gerar_perfil_v2(cargo: str):
    logger.info(f"Cargo informado: {cargo}")

    perfil_cargo = executar_prompt_perfil(cargo)
    logger.info(f"Perfil gerado: {perfil_cargo}")

    # Create a markdown file with the profile description
    file_path = f"./perfil_{cargo}.md"
    with open(file_path, "w") as file:
        file.write(f"# Perfil do Cargo: {cargo}\n\n{perfil_cargo}")

    return {"file_path": file_path}