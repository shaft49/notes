# VSCODE Basics
Move lines of code down <b>ALT/OPT + DOWN</b> <br>
Move lines of code up <b>ALT/OPT + UP</b> <br>
Duplicate lines of code up <b>SHIFT + ALT/OPT + UP</b> <br>
Duplicate lines of code down <b>SHIFT + ALT/OPT + DOWN</b> <br>
Move words by words <b>ALT/OPT + LEFT/RIGHT</b> <br>
Select the current line <b>COMMAND + L</b>, keep pressing for multiple lines</b> <br>
Delete the current line <b>COMMAND + SHIFT + K</b> <br>
Insert a line above the current line <b>COMMAND + SHIFT + ENTER</b> <br>
Indent the line, <b>COMMAND + ]</b> <br>
Outdent the line, <b>COMMAND + [</b> <br>
Jump to the top of the file, <b>COMMAND + UP</b> <br>
Jump to the down of the file, <b>COMMAND + DOWN</b> <br>
Go to a specific line <b>CTRL + G</b>, and wirte the line number <br>
Delete everything of a line from specific point, <b>COMMAND + DELETE</b> <br>

Sidebar show/hide <b>CMD+B</b><br>
Terminal show/hide <b>CMD+J</b><br>

Switch Between terminal and editor<br>
Put this in <b>Preferences: Open Keyboard Shortcuts (JSON)</b> <br>
```json
{
        "key": "ctrl+=",
        "command": "workbench.action.terminal.focus",
    },
    {
        "key": "ctrl+=",
        "command": "workbench.action.focusActiveEditorGroup",
        "when": "terminalFocus"
    }
}
```

# Python Extensions for vscode

    python
    python docstring generator
    python indent
    code runner
    pylint or flake8, install using pip