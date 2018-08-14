Scripts contained in ~/bin

Some scripts might depend on external dependencies (figlet, lolcat, etc.)

# My setup

Create a folder ~/bin

Add it to your path by editing your .bashrc / .profile / .zshrc / whatever:

```bash
export PATH="$PATH:~/bin"
```

Clone the repository into that folder:

```bash
cd ~/bin
git clone git@github.com:bschuedzig/bin.git ~/bin
```

Reopen your terminal to apply changes

# Meta helpers

## List available scripts

```bash
bin 
```

## List available help topics

```bash
help
```