# fastapi-desc-cargo

# 🚀 **Orientações para executar a API**

## 🔧 **Requisitos**
- **Python**: Versão recomendada **>= 3.10**
- **Gerenciador de Pacotes**: `pip` instalado

## 🏗️ **Configuração do Ambiente**
### 📌 **Criar um ambiente virtual**
- **Windows**:
  ```sh
  python -m venv .venv
  ```
- **Mac/Linux**:
  ```sh
  python3 -m venv .venv
  ```

### ✅ **Ativar o ambiente virtual**
- **Windows**:
  ```sh
  .\.venv\Scripts\activate
  ```
- **Mac/Linux**:
  ```sh
  source .venv/bin/activate
  ```

## 📦 **Instalar dependências**
```sh
pip install -r requirements.txt
```

## ⚙️ **Configurar variáveis de ambiente**
```sh
cp .env.example .env  # Para Mac/Linux
copy .env.example .env  # Para Windows
```
🔹 **Edite o arquivo `.env` e preencha as variáveis necessárias.**

## 🚀 **Executar a FastAPI**
### 🔹 **Modo Desenvolvimento**
```sh
fastapi dev main.py
```
### 🔹 **Modo Produção**
```sh
fastapi run main.py
```

🎉 **Pronto! Agora sua API está rodando!** 🔥
