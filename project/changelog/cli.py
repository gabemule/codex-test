"""
Core implementation of the changelog generator.
"""

def get_paths(mode: str = "prod") -> tuple[str, str, str]:
    """
    Get the correct paths based on whether we're running in production or development mode.
    
    Args:
        mode (str): Running mode, either "prod" or "dev" (default: "prod")
            - "prod": Running from .nexus/project in another repository
            - "dev": Running locally from codex-test repository
    
    Returns:
        tuple[str, str, str]: Template path, prompt path, and log path
    """
    base = ".nexus/project" if mode == "prod" else "project"
    template_path = f"{base}/changelog/template.md"
    prompt_path = f"{base}/changelog/prompt.md"
    log_path = ".tmp/commit_full_log.txt"
    return template_path, prompt_path, log_path

def run(mode: str = "prod") -> None:
    """
    Runs the aider command to generate changelog documentation.
    
    Args:
        mode (str): Running mode, either "prod" or "dev" (default: "prod")
            - "prod": Running from .nexus/project in another repository
            - "dev": Running locally from codex-test repository
    """
    template_path, prompt_path, log_path = get_paths(mode)
    
    command = f"""aider \\
  --subtree-only \\
  --no-git \\
  --yes \\
  --sonnet \\
  --cache-prompts \\
  --no-stream \\
  --read {template_path} \\
  --message-file {prompt_path} \\
  {log_path}"""
    
    print()
    print(command)
    print()
