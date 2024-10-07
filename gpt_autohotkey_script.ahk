; Define a hotkey (Ctrl + Shift + T) to trigger translation or definition
^+t::
    ; Send Ctrl+C to copy selected text to the clipboard
    Send, ^c

    ; Wait a bit for the clipboard to update
    Sleep, 100

    ; Get the clipboard content
    selectedText := Clipboard

    ; Specify a temporary file to store the output
    tempFile := "C:\\Users\\surre\\Desktop\\CODES\\gpt translator\\output.txt"

    ; Call the Python script with the selected text as an argument and redirect the output to a file
    RunWait, %ComSpec% /C pythonw.exe "C:\\Users\\surre\\Desktop\\CODES\\gpt translator\\gpt_python_script.py" "%selectedText%" > "%tempFile%", , Hide

    ; Read the result from the tempFile
    FileRead, OutputVar, %tempFile%

    ; Show the result from Python output in a message box
    MsgBox, %OutputVar%

return
