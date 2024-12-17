import os
import toml
from graph_builder import build_commit_graph
from graph_visualizer import save_graph_as_image

def main():
    config = toml.load("config.toml")
    repo_path = config["paths"]["repository_path"]
    output_path = config["paths"]["output_path"]
    visualization_tool = config["paths"]["visualization_tool"]
    tag_name = config["git"]["tag_name"]

    if not os.path.exists(repo_path):
        raise FileNotFoundError(f"Путь к репозиторию не найден: {repo_path}")

    print("Строим граф коммитов...")
    graph_mermaid = build_commit_graph(repo_path, tag_name)
    print("Граф коммитов построен:\n", graph_mermaid)

    print("Сохраняем граф как изображение...")
    save_graph_as_image(graph_mermaid, visualization_tool, output_path)
    print(f"Граф успешно сохранен в файл: {output_path}")

if __name__ == "__main__":
    main()
