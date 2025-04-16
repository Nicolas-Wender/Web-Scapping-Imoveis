# 🏠 Extrator de Dados Imobiliários

[![Python 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Selenium](https://img.shields.io/badge/Selenium-4.0+-green.svg)](https://selenium-python.readthedocs.io/)
[![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4.9+-orange.svg)](https://www.crummy.com/software/BeautifulSoup/)
[![Pandas](https://img.shields.io/badge/Pandas-1.0+-yellow.svg)](https://pandas.pydata.org/)

## O que é isso?

Este é um projeto simples que ajuda a coletar informações sobre casas à venda no site ZAP Imóveis. Se você está procurando um imóvel ou apenas curioso sobre os preços no mercado, este programa pode poupar seu tempo reunindo todas essas informações automaticamente.

## Por que isso é útil?

Imagina passar horas navegando em sites de imóveis, anotando preços, endereços e características de cada casa. Cansativo, né? Este programa faz isso para você em poucos segundos e organiza tudo em uma planilha Excel fácil de entender.

## O que ele coleta?

Para cada casa à venda, o programa captura:

- Link do anúncio
- Preço
- Bairro e cidade
- Nome da rua
- Tamanho da casa
- Número de quartos
- Número de banheiros
- Vagas de garagem
- Uma foto do imóvel

## Como usar?

1. Instale o Python (se ainda não tiver)
2. Instale os pacotes necessários:

```
pip install -r requirements.txt
```

3. Execute o programa:

```
python main.py
```

4. Abra o arquivo "casas_encontradas.xlsx" que será criado

## Características

- **Funciona nos bastidores**: Roda sem precisar abrir uma janela do navegador
- **Evita bloqueios**: Usa técnicas para não ser detectado como um robô
- **Rápido e eficiente**: Coleta apenas o que é importante
- **Pronto para análise**: Entrega tudo organizado em Excel

## Tecnologias Utilizadas

- **Selenium**: Para navegação e interação com páginas dinâmicas em JavaScript
- **BeautifulSoup**: Para parsing de HTML e extração estruturada de dados
- **Pandas**: Para processamento e exportação de dados
- **WebDriver Manager**: Para gerenciamento automático dos drivers de navegador

## Lembretes importantes

- Use com moderação para não sobrecarregar o site
- Este projeto foi criado apenas para fins educacionais e pessoais
- Respeite sempre os termos de uso dos sites

## Quer melhorar o código?

Fique à vontade para modificar e adaptar o código para suas necessidades. Você pode facilmente mudar a url para buscar apartamentos em vez de casas, ou até mesmo adaptar para outros sites imobiliários.
