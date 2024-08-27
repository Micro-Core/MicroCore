import click
import os

from .content import NODE_MAIN_CONTENT, CONFIG_CONTENT

__DEFAULT_NAME = "node_1"
__DEFAULT_PATH = "."

@click.command()
@click.option('--name', default = str(__DEFAULT_NAME), prompt='App Name', help='The name of the micro-app.')
@click.option('--path', default=str(__DEFAULT_PATH), help='The path where the project will be created.')

def create_project(name: str, path: str) -> None:
    #add 'node' prefix for node name
    name = name.replace("node", "") if name.find("node") >= 1 else name
    name = "node-" + name.lower()
    project_path = os.path.join(path, name)
    if name == str(__DEFAULT_NAME):
        path = __DEFAULT_PATH

    try:
        os.makedirs(project_path)
        os.makedirs(os.path.join(project_path, name))
        os.makedirs(os.path.join(project_path, name, f"{name}.py"))
        with open(os.path.join(project_path, f"{name}.py", "w")) as f:
            f.write(str(NODE_MAIN_CONTENT))        

        with open(os.path.join(project_path, name,'config.py'), 'w') as f:
            f.write(str(CONFIG_CONTENT))

        click.echo(f"NIDE:: '{name}' created successfully -> {project_path}.")

    except OSError as e:
        click.echo(f"Error: {e}")

if __name__ == '__main__':
    create_project()
