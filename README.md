# dbt-weather (OpenWeather → Postgres → dbt)

Projeto didático de uma **pipeline de dados** que:
1. **Extrai** dados de clima da API **OpenWeather** (Python)
2. **Carrega** no **PostgreSQL** (tabela “bruta”)
3. **Transforma/modela** com **dbt** em camadas (staging → marts)
4. **Documenta** o projeto com `dbt docs`

![Print](architecture.png)

---

A intenção com o projeto é intensificar e solidificar o conhecimento em relação a ferramenta dbt, praticando:
- **Sources**: declarar a tabela de entrada como fonte confiável
- **Models**: criar models em camadas (staging e marts)
- **Materializações**: views em staging e modelo final (ex.: incremental)
- **Macros**: reutilizar lógica (ex.: schema por camada, conversão de horário)
- **dbt docs**: gerar e navegar na documentação do projeto

## Como o projeto funciona (visão rápida)

### 1. Ingestão (Python → Postgres)
Os scripts em `scripts/`:
- Buscam clima de uma cidade (OpenWeather)
- Conectam no Postgres
- Criam schema/tabela se não existir
- Inserem um registro com os dados retornados pela API

Isso vira a “camada bruta” que o dbt vai consumir.

### 2. Transformação (dbt)
No dbt:
- `models/sources/` define a tabela bruta como `source`
- `models/staging/` padroniza e organiza os campos (staging)
- `models/marts/` cria a tabela final pronta para consumo (marts)

---

## Comandos úteis (dbt)

Dentro da pasta do projeto dbt (`weather/`):

```bash
dbt debug
dbt run
dbt test
dbt docs generate
dbt docs serve --port 8081 (ou 8080, usei a 8081 pois era a que estava disponível para uso)
```
----

## Pré-requisitos

- Python (rodando via `uv`)
- PostgreSQL rodando local (host/porta configurados)
- Chave da OpenWeather API
- dbt instalado no ambiente

## Variáveis de ambiente (.env)

Para gerar sua api key: **https://openweathermap.org/**

Crie/edite `weather/scripts/.env`:

```env
OPENWEATHER_API_KEY=sua_api_key
POSTGRES_HOST=localhost
POSTGRES_PORT=5432 (geralmente)
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
```

# opcional (pode ser passado tanto como uma variável de ambiente ou como parâmetro da função principal)
CITY=São Paulo

---


## Ordem de execução
1. Rodar ingestão (Python → Postgres):
```bash
uv run python scripts/main.py
```

2. Rodar transformações (dbt):
```bash
dbt run
dbt test
```

3. Gerar docs:
```bash
dbt docs generate
dbt docs serve --port 8081
```
