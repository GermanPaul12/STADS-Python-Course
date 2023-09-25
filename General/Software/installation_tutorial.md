# Installation Tutorial for Windows and Mac OS

## Windows

1. `Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))` execute this line of code in the admin powershell
2. Execute this line to check that chocolatey was installed successfully `choco --version`
3. Next this one to not be asked to type in "y" for a hundred times while downloading software `choco feature enable -n=allowGlobalConfirmation` at a later stage you can also disable it again with `choco feature disable -n=allowGlobalConfirmation`
4. Install python with `choco install python311`
5. Check that everything worked with `python --version` and `pip --version` you should see version numbers
6. Type in `choco install git` to get git which is a version control software
7. Execute `choco install vscode` to get vs code

## Mac OS
