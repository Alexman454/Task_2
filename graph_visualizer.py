import subprocess

def save_graph_as_image(graph_mermaid, visualization_tool, output_path):
    input_file = "graph.mmd"
    with open(input_file, "w", encoding="utf-8") as f:
        f.write(graph_mermaid)

    command = [visualization_tool, "-i", input_file, "-o", output_path]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Ошибка при сохранении изображения: {e}")
    finally:
        import os
        os.remove(input_file)
