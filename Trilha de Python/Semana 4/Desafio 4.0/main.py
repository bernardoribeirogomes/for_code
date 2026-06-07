from __future__ import annotations

import json
import os
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


GITKEEP_FILE = ".gitkeep"
LOGS_DIR = "logs"
LOG_FILE = "log.json"
IGNORED_DIRS = {LOGS_DIR, ".git"}


def get_relative_path(path: Path, repo_path: Path) -> str:
    """Retorna o caminho relativo ao repositório no formato padrão."""
    return path.relative_to(repo_path).as_posix()


def should_ignore_directory(directory: Path, repo_path: Path) -> bool:
    """Verifica se o diretório deve ser ignorado pelo algoritmo."""
    relative_parts = directory.relative_to(repo_path).parts
    return any(part in IGNORED_DIRS for part in relative_parts)


def ensure_logs_directory(repo_path: Path) -> Path:
    """Cria o diretório logs, caso ele não exista, e retorna o caminho do log."""
    logs_path = repo_path / LOGS_DIR
    logs_path.mkdir(exist_ok=True)
    return logs_path / LOG_FILE


def is_empty_directory(directory: Path) -> bool:
    """
    Verifica se um diretório está vazio para fins de versionamento.

    O arquivo .gitkeep é ignorado nessa verificação, pois sua função é justamente
    representar diretórios vazios no Git.
    """
    items = [item for item in directory.iterdir() if item.name != GITKEEP_FILE]
    return len(items) == 0


def collect_directories(repo_path: Path) -> list[Path]:
    """
    Percorre o repositório e coleta os diretórios que devem ser processados.

    Os diretórios logs e .git são ignorados.
    """
    directories = []

    for current_root, dirnames, _ in os.walk(repo_path):
        dirnames[:] = [
            dirname for dirname in dirnames if dirname not in IGNORED_DIRS
        ]

        current_directory = Path(current_root)

        if not should_ignore_directory(current_directory, repo_path):
            directories.append(current_directory)

    return directories


def process_directory(directory: Path, repo_path: Path) -> tuple[list[str], list[str]]:
    """
    Aplica as regras de criação ou remoção do .gitkeep em um diretório.
    """
    created_files = []
    removed_files = []

    gitkeep_path = directory / GITKEEP_FILE

    if is_empty_directory(directory):
        if not gitkeep_path.exists():
            gitkeep_path.touch()
            created_files.append(get_relative_path(gitkeep_path, repo_path))
    else:
        if gitkeep_path.is_file():
            gitkeep_path.unlink()
            removed_files.append(get_relative_path(gitkeep_path, repo_path))

    return created_files, removed_files


def load_log_file(log_path: Path) -> dict[str, Any]:
    """Carrega o arquivo de log existente ou cria uma estrutura inicial."""
    if not log_path.exists():
        return {"execucoes": []}

    try:
        with log_path.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if isinstance(data, dict) and isinstance(data.get("execucoes"), list):
            return data

    except json.JSONDecodeError:
        pass

    return {"execucoes": []}


def update_log(
    log_path: Path,
    created_files: list[str],
    removed_files: list[str],
) -> None:
    """Atualiza o arquivo logs/log.json com os dados da execução atual."""
    log_data = load_log_file(log_path)

    execution_data = {
        "data_hora": datetime.now().isoformat(timespec="seconds"),
        "arquivos_gitkeep_criados": created_files,
        "arquivos_gitkeep_removidos": removed_files,
    }

    log_data["execucoes"].append(execution_data)

    with log_path.open("w", encoding="utf-8") as file:
        json.dump(log_data, file, indent=4, ensure_ascii=False)


def process_repository(repo_path: Path) -> tuple[list[str], list[str]]:
    """
    Processa todos os diretórios do repositório.

    Diretórios vazios recebem .gitkeep.
    Diretórios não vazios têm .gitkeep removido, caso exista.
    """
    repo_path = repo_path.resolve()

    if not repo_path.exists() or not repo_path.is_dir():
        raise NotADirectoryError("O caminho informado não é um diretório válido.")

    log_path = ensure_logs_directory(repo_path)

    all_created_files = []
    all_removed_files = []

    directories = collect_directories(repo_path)

    directories.sort(key=lambda path: len(path.parts), reverse=True)

    for directory in directories:
        created_files, removed_files = process_directory(directory, repo_path)
        all_created_files.extend(created_files)
        all_removed_files.extend(removed_files)

    update_log(log_path, all_created_files, all_removed_files)

    return all_created_files, all_removed_files


def main() -> None:
    """Função principal do programa."""
    repo_path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path.cwd()

    try:
        created_files, removed_files = process_repository(repo_path)

        print("Processamento concluído com sucesso!")
        print(f"Arquivos .gitkeep criados: {len(created_files)}")
        print(f"Arquivos .gitkeep removidos: {len(removed_files)}")

        if created_files:
            print("\nCriados:")
            for file_path in created_files:
                print(f"- {file_path}")

        if removed_files:
            print("\nRemovidos:")
            for file_path in removed_files:
                print(f"- {file_path}")

    except NotADirectoryError as error:
        print(f"Erro: {error}")


if __name__ == "__main__":
    main()
