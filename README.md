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


# 📝 **Script para instalação automática de dependência na Instância AWS Lightsail**

## Veja o arquivo - start_instance.sh

```sh
#!/bin/bash

# Install Docker Engine on Ubuntu Cloud Image - AWS EC2 and LightSail instance

# Add Docker's official GPG key:
apt-get update -y
apt-get install ca-certificates curl
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

apt-get update -y

apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
```
