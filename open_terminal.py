import os
import subprocess

# Obtener el directorio del archivo actual desde Sublime Text
file_path = os.path.dirname(sublime.active_window().active_view().file_name())

# Comando para abrir gnome-terminal en el directorio actual
subprocess.Popen(['gnome-terminal', '--working-directory', file_path])
