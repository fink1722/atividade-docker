# Alunos: Cauã Evaristo da Cruz e Ana Dantas

# Django com Docker 

Aplicação simples com upload de arquivos e três containers:

- **django**: imagem própria, criada pelo `Dockerfile`, com Django e Gunicorn.
- **nginx**: proxy reverso e download dos arquivos enviados.
- **db**: PostgreSQL, que guarda os registros dos arquivos.

## Executar

Com o Docker Desktop instalado e iniciado (containers Linux), execute nesta pasta:

```sh
docker compose up --build -d
```

Abra http://localhost:8080, selecione um arquivo e clique em **Enviar**.
Clique no nome de um arquivo enviado para baixá-lo.
As tabelas do banco são criadas automaticamente na inicialização.
O nginx aceita requisições de até 20 MB, incluindo os dados do formulário.

## Persistência

O volume `uploads` guarda os arquivos em `/app/media`. Django grava nesse
volume e nginx o acessa somente para leitura. O volume `postgres_data`
guarda os dados do PostgreSQL.

Para verificar a persistência, envie um arquivo e recrie os containers:

```sh
docker compose down
docker compose up -d
```

O arquivo continuará listado e disponível para download.
`docker compose down` mantém os volumes; adicionar `-v` apaga os volumes e os dados.

Para acompanhar a inicialização ou investigar erros:

```sh
docker compose logs
```

As credenciais no Compose são apenas para esta atividade local.
