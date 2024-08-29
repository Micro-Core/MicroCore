import typer
import os
from microcore.cli.content import NODE_MAIN_CONTENT, CONFIG_CONTENT

app = typer.Typer()

DEFAULT_NAME = "default_node"
DEFAULT_PATH = "."

@app.command()
def create_project(
    name: str = typer.Option(DEFAULT_NAME, prompt='Node Name', help='Name of node to init.'),
    path: str = typer.Option(DEFAULT_PATH, help='The path where the node confs will be created.')
) -> None:
    name = name.replace("node", "") if "node" in name[1:] else name
    name = "node-" + name.lower()
    project_path = os.path.join(path, name)

    try:
        os.makedirs(project_path)
        os.makedirs(os.path.join(project_path, name))
        with open(os.path.join(project_path, f"{name}.py"), "w") as f:
            f.write(str(NODE_MAIN_CONTENT))

        with open(os.path.join(project_path, name, 'config.py'), 'w') as f:
            f.write(str(CONFIG_CONTENT))

        typer.echo(f"Node '{name}' created successfully -> {project_path}.")

    except OSError as e:
        typer.echo(f"Error: {e}")
