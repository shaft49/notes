# Tutorial

- [freecodecamp](https://www.youtube.com/watch?v=WPqXP_kLzpo)

# VSCODE Shortcuts

> Move lines of code down <b>ALT/OPT + DOWN</b> <br>
> Move lines of code up <b>ALT/OPT + UP</b> <br>

> Duplicate lines of code up <b>SHIFT + ALT/OPT + UP</b> <br>
> Duplicate lines of code down <b>SHIFT + ALT/OPT + DOWN</b> <br>

> Move words by words <b>ALT/OPT + LEFT/RIGHT</b> <br>

> Select the current line <b>COMMAND + L</b>, keep pressing for multiple lines</b> <br>

> Delete the current line <b>COMMAND + SHIFT + K</b> <br>

> Insert a line above the current line <b>COMMAND + SHIFT + ENTER</b> <br>

> Indent the line, <b>COMMAND + ]</b> <br>
> Outdent the line, <b>COMMAND + [</b> <br>

> Traversal Shortcuts

    Jump to the top of the file, COMMAND + UP
    Jump to the down of the file, COMMAND + DOWN
    Traverse word by word in line, OPT + ARROW[Left or Right]
    Traverse to start or end of a lin, CMD + ARROW[Left or Right]

> Go to a specific line <b>CTRL + G</b>, and wirte the line number <br>

> Delete everything of a line from specific point, <b>COMMAND + DELETE</b> <br>

## Sidebar Shortcuts

| Key              | Option          |
| ---------------- | --------------- |
| CMD + B          | Toggle Sidebar  |
| CMD + SHIFT + B  | Search Bar      |
| CMD + SHIFT + F  | Version Control |
| CTRl + SHIFT + G | Git             |
| CMD + SHIFT + D  | Debug           |

> Terminal show/hide <b>CMD+J</b><br>

> Command Pallette -> CMD + SHIFT + P

> Close a file -> CMD + W
> Switch Between Files -> CTRL + TAB
> To open a file in new tab -> CMD + P

## Switch Between terminal and editor<br>

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

## Python Extensions

    python
    python docstring generator
    python indent
    code runner
    pylint or flake8, install using pip

## Generic Extension

    prettier
    better comments
    liveserver: for basic html css stuff cmd + l cmd + o
    polacode: beautiful snippet of codes

## JS Extensions

    quokka: js playground
    bracket pair colorizer
    VS Code ES7 React/Redux/React-Native/JS snippets

## HTML CSS Extensions

    auto rename tag

## Settings Sync

If you wanna use the same settings in multiple devices
Turn on the setting sync by going to the command pallette an type

> Settings Sync: Turn On

## Debugging

Choose the file that you wanna debug then open Debuggger in the sidebar. And start debugging.

## Source Control Integration

To see the differences visually open the source control in the sidebar and select the file.
You can create a new github repo from the vscode. From command pallette select `Publish to Github`

    gitlens extension
