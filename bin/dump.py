#!/usr/bin/env python3
from pathlib import Path
from subprocess import run
from textwrap import dedent


def nord_improved() -> None:
    filename = (
        Path(__file__).resolve().parent.parent
        / "autoload/lightline/colorscheme/nord_improved.vim"
    )
    filename.write_text(
        dedent(
            """
            " DO NOT EDIT THIS FILE
            " generated by bin/dump.py
            let g:lightline#colorscheme#nord_improved#palette="""
        ).strip()
    )
    func = "lightline#delphinus#colorscheme#nord_improved#palette"
    script = f'call writefile([{func}()], "{filename}", "a")'
    run(f"vim +'{script}' +q", shell=True)
    print("write successfully nord_improved")


def solarized_improved() -> None:
    filename = (
        Path(__file__).resolve().parent.parent
        / "autoload/lightline/colorscheme/solarized_improved.vim"
    )
    func = "lightline#delphinus#colorscheme#solarized_improved#palette"
    script = f'call writefile([{func}()], "{filename}", "a")'
    filename.write_text(
        dedent(
            """
            " DO NOT EDIT THIS FILE
            " generated by bin/dump.py
            if &background ==# 'dark'
              let g:lightline#colorscheme#solarized_improved#palette="""
        ).strip()
    )
    run(f"vim +'set bg=dark' +'{script}' +q", shell=True)
    with open(filename, "a", encoding="utf-8") as f:
        f.write(
            dedent(
                """
                else
                  let g:lightline#colorscheme#solarized_improved#palette="""
            ).strip()
        )
    run(f"vim +'set bg=light' +'{script}' +q", shell=True)
    with open(filename, "a", encoding="utf-8") as f:
        f.write("endif")
    print("write successfully solarized_improved")


if __name__ == "__main__":
    nord_improved()
    solarized_improved()
