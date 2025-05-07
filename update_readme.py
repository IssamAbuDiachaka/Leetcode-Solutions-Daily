def add_to_table(problem_num, problem_name, problem_url, difficulty, solution_path, approach):
    new_row = f"| {problem_num} | [{problem_name}]({problem_url}) | {difficulty} | [Python]({solution_path}) | {datetime.now().strftime('%Y-%m-%d')} | {approach} |\n"
    with open("README.md", "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if line.startswith("|----"):  # Find the separator line
            lines.insert(i + 1, new_row)
            break
    with open("README.md", "w") as f:
        f.writelines(lines)
