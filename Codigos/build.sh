#!/bin/bash
# É necessário criar uma variável de ambiente chamada PYPI_TOKEN a partir do comando no console: export PYPI_TOKEN=seu-token-aqui
poetry config pypi-token.pypi "${PYPI_TOKEN}"
poetry build
poetry publish