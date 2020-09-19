## Pré-requisitos
- Vs Code
- Windows 10
- Python 3.8

## Passo a Passo

### Venv
- > mkdir hypermodern_imc
- > cd hypermodern_imc
- > python3 -m venv py38hypermodern
- > . py38hypermodern/Scripts/activate
### Poetry
- > pip install poetry
- > poetry init --no-interaction
- > mkdir src
- > cd src
- > mkdir hypermodern_imc
- Crie um arquivo `__init__.py` dentro de *src/hypermodern_imc* com conteúdo `__version__ = "0.1.0"`
- > poetry install
- > poetry add click
- > poetry add requests
- Crie um arquivo `console.py`dentro de *src/hypermodern_imc* com uma função `main` usando *click* decorators e *requests*. Coloque ajuda na função `main`.
- No arquivo pyproject.toml:
    ```
    [tool.poetry.scripts]
    hypermodern_imc = "hypermodern_imc.console:main"
    ```
### Pytest
- > poetry install
- > poetry run hypermodern_imc
- > poetry run hypermodern_imc --help
- > poetry add --dev pytest
- > mkdir tests
- Crie os arquivos `__init__.py` e `test_console.py` dentro da pasta *tests*. Crie algum teste para *src.hypermodern_imc.console.main*.
- > poetry run pytest
### Coverage
- > poetry add --dev coverage[toml] pytest-cov
- No arquivo pyproject.toml:
    ```
        [tool.coverage.paths]
        source = ["/src"]

        [tool.coverage.run]
        branch = true
        source = ["/src"]

        [tool.coverage.report]
        show_missing = true
        fail_under = 100
    ```
### Nox
- > pip install nox
- Em *hypermodern_imc* (raíz) criar `noxfile.py`. Crie a configuração de testes nesse arquivo.
- > nox
- > nox -r
- > nox -- src/tests/test_console.py
### Mock
- > poetry add --dev pytest-mock
- Crie alguns mocks para seu projeto em *src/tests/test_console.py*.

## Referências
- https://python-poetry.org/
- https://cjolowicz.github.io/

