#------------------------------------------------------------------------------#
from pathlib import Path

publish_dir = Path("_publish")
provas_dir  = publish_dir / "provas"
aulas_dir   = publish_dir / "aulas"
index_file  = publish_dir / "index.html"

title = 'Materiais de CFVVI'
disc  = 'Cálculo de Funções de Várias Variáveis I'

#------------------------------------------------------------------------------#
def html_header() -> str:
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
<h1>{title}</h1>
<p>Arquivos em PDF disponíveis para download</p>
<p>Materiais para a disciplina {disc}</p>
"""

#------------------------------------------------------------------------------#
def html_footer() -> str:
    return """  <footer>
&copy; 2025 Luis Alberto D'Afonseca. Licenciado sob
<a href="https://creativecommons.org/licenses/by-sa/4.0">CC BY-SA 4.0</a>
</footer>
</body>
</html>
"""

#------------------------------------------------------------------------------#
with index_file.open("w", encoding="utf-8") as f:

    f.write(html_header())

    # Apostila
    f.write("""<div class="section">
      <h2>Apostila</h2>
    """)

    f.write("<ul>\n")
    for file in sorted(publish_dir.glob("*.pdf")):
        f.write(f"<li><a href=\"{file.name}\" download>{file.name}</a></li>\n")
    f.write("</ul>\n")
    f.write("</div>\n")

    # Aulas
    f.write("""<div class="section">
      <h2>Apresentações das Aulas</h2>
    """)
    f.write("<ul>\n")
    for file in sorted(aulas_dir.rglob("*.pdf")):
        relative_path = file.relative_to(publish_dir)
        f.write(f"<li><a href=\"{relative_path}\" download>{relative_path.name}</a></li>\n")
    f.write("</ul>\n")

    # Provas
    f.write("""<div class="section">
      <h2>Provas Anteriores</h2>
    """)
    f.write("<ul>\n")
    for file in sorted(provas_dir.rglob("*.pdf")):
        relative_path = file.relative_to(publish_dir)
        f.write(f"<li><a href=\"{relative_path}\" download>{relative_path.name}</a></li>\n")
    f.write("</ul>\n")

    f.write(html_footer())

#------------------------------------------------------------------------------#