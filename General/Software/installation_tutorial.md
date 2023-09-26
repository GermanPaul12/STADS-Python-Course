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

1. `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"` execute this line in terminal
2. After that go on the mac symbol in the top left corner and click on "About this Mac" under macOS you can see which OS version you have.
3. If the version is 10.12 or smaller then add `export PATH=/usr/local/bin:/usr/local/sbin:$PATH` this line to your `~/.profile`
4. Else add `export PATH="/usr/local/opt/python/libexec/bin:$PATH"` this line to your `~/.profile`
5. You can open the `~/.profile` with `nano ~/.profile` in the terminal
6. After you have added the line press `command + o` followed by `enter` and then `commmand + x`
7. Check that everything has worked with `brew --version`
8. Execute `brew install python` to install python
9. For git you can use `brew install git`
10. For vs code you can use `brew install --cask visual-studio-code`
11. Check your installation with `python3 --version` and `pip --version` you should see version numbers
12. Also `git --version` and `code --version` should show version numbers
