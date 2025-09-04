# Weather Scraper API

Uma aplicação que recolhe dados de previsão meteorológica a partir do site oficial do IPMA (Instituto Português do Mar e da Atmosfera) e disponibiliza esses dados através de uma REST API simples.


##  Instalação

### Pré-requisitos

- Docker instalado no sistema
- Git para clonar o repositório

### 1. Clonar o Repositório

### HTTPS
```bash
git clone https://github.com/Joaf03/WeatherScraperAPI.git
cd weather-scraper-api
```

### SSH
```bash
git clone git@github.com:Joaf03/WeatherScraperAPI.git
cd weather-scraper-api
```

### 2. Construir a Imagem Docker

```bash
docker build -t weather-scraper-api .
```

##  Como Executar a Aplicação

### Executar com Docker

```bash
docker run -p 8000:8000 weather-scraper-api
```

A aplicação estará disponível em: `http://localhost:8000`

##  Como Utilizar a API

### Documentação Interativa

Aceda a `http://localhost:8000/docs` para ver a documentação interativa da API (Swagger UI).

### Endpoint Principal

**GET /** - Obter previsão meteorológica

#### Parâmetros Obrigatórios:

- `date` (int): Dia para consultar (ex: 13 para o dia 13 do presente mês)
- `city` (string): Nome da cidade/distrito (ex: Porto)
- `region` (string): Nome da localidade (ex: Valongo")

###  Exemplos de Chamadas

#### Exemplo 1: Previsão para Porto, Valongo no dia 13

```bash
curl "http://localhost:8000/?date=13&city=Porto&region=Valongo"
```

#### Exemplo 2: Previsão para Lisboa, Lisboa no dia 12

```bash
curl "http://localhost:8000/?date=12&city=Lisboa&region=Lisboa"
```

#### Exemplo 3: Usando o navegador

```
http://localhost:8000/?date=5&city=Braga&region=Braga
```

###  Exemplo de Resposta

```json
{
  "Data": 13,
  "Localização": "Porto, Valongo",
  "Temperatura Mínima": "12°",
  "Temperatura Máxima": "26°",
  "Direção do Vento": "Noroeste",
  "Probabilidade de Precipitação": "10%"
}
```

###  Tratamento de Erros

#### Parâmetros Inválidos

Se a localização for inválida ou a data estiver fora do intervalo de 9 dias:

```json
{
  "error": "Parâmetros inválidos: a data deve estar dentro dos próximos 9 dias e a localização tem de ser válida."
}
```

##  Estrutura do Projeto

```
weather-scraper-api/
├── app/
│   ├── main.py          # Aplicação FastAPI
│   └── scraper.py       # Lógica de web scraping
├── Dockerfile           # Configuração Docker
├── requirements.txt     # Dependências Python
├── README.md           # Este ficheiro
└── .gitignore          # Ficheiros ignorados pelo Git
```

##  Tecnologias Utilizadas

- **FastAPI**: Framework web moderno para Python
- **Selenium**: Automação de browser para JavaScript
- **BeautifulSoup**: Parsing de HTML
- **Docker**: Containerização da aplicação
- **Chrome/ChromeDriver**: Browser headless para scraping

##  Limitações

- A aplicação depende da estrutura HTML do site do IPMA
- As previsões estão limitadas aos próximos 9 dias
- Requer conexão à internet para aceder ao IPMA
- As localidades devem existir no site do IPMA

##  Contribuições

Este projeto foi desenvolvido como exercício prático para demonstrar conhecimentos de Python, web scraping e desenvolvimento de APIs.

##  Licença

Este projeto é apenas para fins educacionais e demonstração técnica.