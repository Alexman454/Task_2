import subprocess

def get_commit_log(repo_path, tag_name):
    command = ["git", "-C", repo_path, "log", tag_name, "--pretty=format:%H %s"]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout.strip().split("\n")
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Ошибка при выполнении git log: {e}")

def build_commit_graph(repo_path, tag_name):
    commit_log = get_commit_log(repo_path, tag_name)
    graph_lines = ["graph TD"]
    previous_commit = None

    for commit in commit_log:
        commit_hash, commit_message = commit.split(" ", 1)
        graph_lines.append(f"{commit_hash}({commit_message})")
        if previous_commit:
            graph_lines.append(f"{previous_commit} --> {commit_hash}")
        previous_commit = commit_hash

    return "\n".join(graph_lines)
