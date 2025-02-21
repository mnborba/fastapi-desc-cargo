import requests


class APIClient:
    """
    APIClient é uma classe para interagir com uma API RESTful.

    Métodos:
        __init__(base_url: str, api_token: int):
            Inicializa a instância do cliente API com a URL base e o token da API.

        _get(endpoint: str, params: dict = None):
            Método privado para realizar requisições GET à API.

        _post(endpoint: str, params: dict = None, json_body: dict = None):
            Método privado para realizar requisições POST à API.

        gerar_descricao(cargo: str):
            Gera uma descrição de atividades para um determinado cargo.
    """


    def __init__(self, base_url: str, api_token: int):
        self.base_url = base_url.rstrip("/")
        self.api_token = api_token

    def _get(self, endpoint: str, params: dict = None):
        params = params or {}
        params["api_token"] = self.api_token
        response = requests.get(f"{self.base_url}{endpoint}", params=params)
        return response.json()

    def _post(self, endpoint: str, params: dict = None, json_body: dict = None):
        params = params or {}
        params["api_token"] = self.api_token
        response = requests.post(
            f"{self.base_url}{endpoint}", params=params, json=json_body
        )
        return response.json()

    def gerar_descricao(self, cargo: str):
        """Gera uma descrição de atividades para um determinado cargo."""
        return self._post("/llm/gerar_descricao", params={"cargo": cargo})

    def gerar_perfil(self, cargo: str):
        """Gera uma descrição de atividades para um determinado cargo."""
        return self._post("/llm/gerar_descricao", params={"cargo": cargo})
    
    def gerar_perfil_v2(self, cargo: str):
        """Gera uma descrição de atividades para um determinado cargo."""
        return self._post("/llm/gerar_descricao", params={"cargo": cargo})