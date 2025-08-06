#------------------------------------------------------------------------------#
from pathlib import Path

publish_dir = Path("_publish")
provas_dir  = publish_dir / "provas"
aulas_dir   = publish_dir / "aulas"
index_file  = publish_dir / "index.html"

title = 'Materiais de CFVVI'
discipline = 'Cálculo de Funções de Várias Variáveis I'

add_book = True

#------------------------------------------------------------------------------#
def write_header(f, title: str, discipline: str):
    f.write(f"""<!DOCTYPE html>
      <html lang="pt-BR">
      <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1" />
        <title>{title}</title>
        <link rel="stylesheet" href="styles.css">
      </head>
      <body>
      <h1>{title}</h1>
      <p>Materiais para a disciplina {discipline}</p>
      <a href="/">Home</a>
      """)

#------------------------------------------------------------------------------#
def open_section(f, title):
    f.write(f"""<details close>
    <summary>{title}</summary>
    """)

#------------------------------------------------------------------------------#
def close_section(f):
    f.write("</details>")

#------------------------------------------------------------------------------#
def open_sub_section(f, path: Path):
    f.write(f"""<details close>
    <summary>{path.name.replace('_', ' ')}</summary>
    """)

#------------------------------------------------------------------------------#
def close_sub_section(f):
    f.write("</details>")

#------------------------------------------------------------------------------#
# def write_folder(f, path: Path):
#     f.write(f"<li>{path.name.replace('_', ' ')}\n")

#------------------------------------------------------------------------------#
def write_pdf_link(f, file: Path):
    text = file.name.replace('_', ' ').replace('.pdf', '')
    f.write(f"<li><a href=\"{file}\" download>{text}</a></li>\n")

#------------------------------------------------------------------------------#
def write_footer(f):
    f.write("""  <footer>
      &copy; 2025 Luis Alberto D'Afonseca. Licenciado sob
      <a href="https://creativecommons.org/licenses/by-sa/4.0">CC BY-SA 4.0</a>
      </footer>
      </body>
      </html>
      """)

#------------------------------------------------------------------------------#
with index_file.open("w", encoding="utf-8") as f:

    write_header(f, title, discipline)

    # Apostila
    if add_book:
        open_section(f, "Apostila")
        f.write("<ul>\n")
        for file in sorted(publish_dir.glob("*.pdf")):
            write_pdf_link(f, file)
        f.write("</ul>\n")
        f.write("</div>\n")
        close_section(f)

    # Aulas
    open_section(f, "Apresentações das Aulas")
    f.write("<ul>\n")
    for folder in sorted(aulas_dir.glob("*")):
        open_sub_section(f, folder)
        f.write("<ul>\n")
        for file in sorted(folder.glob("*.pdf")):
            write_pdf_link(f, file.relative_to(publish_dir))
        close_sub_section(f)
    f.write("</ul>\n")
    close_section(f)

    # Provas
    open_section(f, "Provas Anteriores")
    f.write("<ul>\n")
    for folder in sorted(provas_dir.glob("*")):
        open_sub_section(f, folder)
        f.write("<ul>\n")
        for file in sorted(folder.glob("*.pdf")):
            write_pdf_link(f, file.relative_to(publish_dir))
        close_sub_section(f)
    f.write("</ul>\n")
    close_section(f)

    write_footer(f)

#------------------------------------------------------------------------------#