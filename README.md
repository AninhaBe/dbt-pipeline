# Projeto DBT Weather API

Este é um projeto de pipeline de dados ponta a ponta que extrai informações meteorológicas da **OpenWeather API** e as transforma utilizando o **dbt (data build tool)**, tendo o **PostgreSQL** como nosso Data Warehouse local.

## Estrutura do Projeto

O ecossistema está dividido em dois componentes principais:
- **Data Pipeline**: Scripts Python responsáveis pela extração (E) e carga (L) dos dados crus.
- **dbt Transformations**: Modelagem e transformação dos dados (T) seguindo as melhores práticas de engenharia de software aplicada a dados.

---

## 🛠️ Pré-requisitos

* **Python 3.12+**
* **Banco de Dados PostgreSQL**
* **Chave de API do OpenWeather** (gratuita)

## 🚀 Configuração Inicial

### 1. Ambiente Virtual e Dependências
Recomenda-se o uso do `uv` pela velocidade, mas você também pode usar o `pip`:

```bash
# Usando uv (recomendado)
uv sync

# Ou usando pip tradicional
pip install -r requirements.txt