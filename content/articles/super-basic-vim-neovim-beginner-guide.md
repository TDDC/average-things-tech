Title: Super Basic Vim and Neovim Setup Guide for Beginners
Date: 2026-07-05 16:45
Category: Neovim
Tags: vim, neovim, beginner, terminal, linux, setup
Slug: super-basic-vim-neovim-beginner-guide
Summary: A very beginner-friendly guide to installing, opening, editing, saving, and most importantly quitting Vim and Neovim.

So you want to learn Vim or Neovim.

Good.

But before learning fancy commands, plugins, themes, and keyboard magic, let us do the boring and important things first:

- install it
- open it
- type something
- save a file
- quit safely
- know the emergency exit

Because the first rule of Vim is not speed.

The first rule of Vim is survival.

## Official links

Here are the official places to know:

- [Neovim GitHub repository](https://github.com/neovim/neovim)
- [Neovim install guide](https://neovim.io/doc/install/)
- [Vim GitHub repository](https://github.com/vim/vim)
- [Vim official download page](https://www.vim.org/download.php)
- [Vim Windows installer repository](https://github.com/vim/vim-win32-installer)

Do not download random Vim or Neovim installers from unknown websites.

For beginners, official sources are safer.

Boring source, peaceful life.

## Vim or Neovim: which one should a beginner choose?

Both are good.

Vim is the classic editor.

Neovim is the modern version inspired by Vim, with better support for modern plugins and Lua configuration.

For beginner-level editing, both work almost the same.

You can learn the basics in either one.

My simple recommendation:

Use Neovim if you are starting fresh.

Learn the basic Vim commands because they work in both Vim and Neovim.

## Step 1: Check if Vim or Neovim is already installed

Open your terminal or PowerShell and run `nvim --version`:

```powershell
nvim --version
```

Then check Vim with `vim --version`:

```powershell
vim --version
```

If one of them shows a version number, it is installed.

If the command is not found, then you need to install it.

## Step 2: Install Neovim on Windows

On Windows, there are several ways to install Neovim.

## Which Windows install method should you choose?

My recommendation:

| Method | Best for |
|---|---|
| Scoop | Terminal/dev-tool users |
| Winget | Simplest built-in Windows option |
| Chocolatey | Users already using Chocolatey |
| Manual | When package managers are not allowed |

For Average Things Tech beginners, I recommend **Scoop** if you are slowly building a proper terminal/dev-tool setup.

Reasons:

- clean terminal workflow
- easy updates
- good for developer tools
- works nicely with tools like Git, ripgrep, fzf, lazygit, and Neovim

But if you are a complete beginner and do not want to install another package manager, use **Winget**.

The most important rule:

- Pick one method.
- Do not mix install methods for the same app.

## Recommended option: Install Neovim using Scoop

For people who like terminal tools, Scoop is a very clean option.

Scoop is a command-line installer for Windows. It installs tools with minimal friction, and its installer normally sets it up inside your user folder instead of scattering files everywhere. Scoop's installer documentation shows the typical non-admin install command and notes that PowerShell execution policy may need to be set to `RemoteSigned`.

First, allow local PowerShell scripts for your user account:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then install Scoop:

```powershell
irm get.scoop.sh | iex
```

After Scoop is installed, install Neovim:

```powershell
scoop bucket add main
scoop install neovim
```

Check the installation with `nvim --version`:

```powershell
nvim --version
```

To start Neovim, run `nvim`:

```powershell
nvim
```

Important:

The command is `nvim`, not `neovim`.

Scoop is my preferred option for a beginner who wants to slowly build a proper terminal setup.

## Simple built-in option: Install Neovim using Winget

Winget is Microsoft's Windows package manager and is available on many modern Windows systems.

To install Neovim using Winget:

```powershell
winget install Neovim.Neovim
```

After installation, close and reopen PowerShell.

Then check with `nvim --version`:

```powershell
nvim --version
```

Start Neovim with `nvim`:

```powershell
nvim
```

Winget is a good choice if you want the simplest built-in Windows method.

## Alternative option: Install Neovim using Chocolatey

Chocolatey is another popular Windows package manager.

If you already use Chocolatey, you can install Neovim with:

```powershell
choco install neovim
```

If you want to skip confirmation prompts:

```powershell
choco install neovim -y
```

After installation, close and reopen PowerShell.

Then check with `nvim --version`:

```powershell
nvim --version
```

Chocolatey is fine, but I would not install Chocolatey only for Neovim if you already have Scoop or Winget.

## Manual option: MSI or Zip from GitHub Releases

You can also install Neovim manually from the official GitHub releases page.

Official repository:

[https://github.com/neovim/neovim](https://github.com/neovim/neovim)

Manual installation is useful if you do not want to use a package manager.

But for beginners, Scoop or Winget is usually easier.

## Step 3: Install Vim on Windows

If you also want classic Vim, you can install it using Winget:

```powershell
winget install -e --id vim.vim
```

After installation, close and reopen PowerShell.

Then check with `vim --version`:

```powershell
vim --version
```

If it shows a version, Vim is ready.

## Step 4: Install on Ubuntu or Debian Linux

On Ubuntu or Debian-based Linux systems:

```bash
sudo apt update
sudo apt install neovim vim
```

Then check:

```bash
nvim --version
vim --version
```

The version from the default Linux package manager may not always be the newest version, but for learning the basics, it is perfectly fine.

Do not compile from source on day one.

Day one is for learning, not summoning dragons.

## Step 5: Install on macOS

If Homebrew is installed, use:

```bash
brew install neovim vim
```

Then check:

```bash
nvim --version
vim --version
```

## Step 6: Create a very basic Neovim config

You can use Neovim without any config.

But a tiny beginner config makes it more comfortable.

On Windows PowerShell, create the Neovim config folder:

```powershell
New-Item -ItemType Directory -Path $env:LOCALAPPDATA\nvim -Force
```

Now open the config file:

```powershell
notepad $env:LOCALAPPDATA\nvim\init.lua
```

Paste this into `init.lua`:

```lua
vim.opt.number = true
vim.opt.wrap = true
vim.opt.linebreak = true
vim.opt.tabstop = 4
vim.opt.shiftwidth = 4
vim.opt.expandtab = true
vim.opt.scrolloff = 5
```

Save and close Notepad.

Now open Neovim:

```powershell
nvim
```

This config does a few simple things:

- shows line numbers
- wraps long lines nicely
- uses 4 spaces for indentation
- keeps a little space above and below the cursor while scrolling

No plugins.

No fancy theme.

No drama.

## Step 7: Create a very basic Vim config

For Vim on Windows, open:

```powershell
notepad $HOME\_vimrc
```

Paste this into `_vimrc`:

```vim
set number
set wrap
set linebreak
set tabstop=4
set shiftwidth=4
set expandtab
syntax on
filetype plugin indent on
```

Save and close Notepad.

For Linux or macOS, the Vim config file is usually `~/.vimrc`.

For beginners, do not over-configure Vim.

A small config is better than a huge config you do not understand.

## Step 8: Open your first file

Create or open a file with Neovim:

```powershell
nvim practice.txt
```

Or with Vim:

```powershell
vim practice.txt
```

If the file does not exist, it will be created when you save.

Now you are inside Vim or Neovim.

The screen may look strange.

Relax.

This is normal.

## The most important thing: how to quit Vim

The most important command in this entire guide is `:q`.

That means quit.

But before typing `:q`, press `Esc`.

Then type `:q`.

Then press `Enter`.

Full sequence:

```text
Esc
:q
Enter
```

That is how you quit Vim or Neovim.

Congratulations. You now know more than many people who got trapped and restarted their computer.

## Why quitting is confusing

Vim is a modal editor.

That means the keyboard behaves differently depending on which mode you are in.

The two beginner modes are:

- Normal mode
- Insert mode

## Normal mode

Normal mode is for commands.

In Normal mode, letters do not simply type text.

For example:

| Key or command | What it does |
|---|---|
| `i` | enter Insert mode |
| `x` | delete one character |
| `dd` | delete a full line |
| `u` | undo |
| `:q` | quit |

To return to Normal mode, press `Esc`.

Beginner rule:

When confused, press `Esc`.

Esc is the seatbelt.

## Insert mode

Insert mode is for typing text.

To enter Insert mode, press `i`.

Now you can type normally.

To leave Insert mode, press `Esc`.

Basic flow:

```text
i
type your text
Esc
```

## How to type text

After opening a file:

```powershell
nvim practice.txt
```

Press `i`.

Now type:

```text
Hello, this is my first Vim file.
```

Then press `Esc`.

Now you are back in Normal mode.

## How to save

First press `Esc`.

Then type `:w`.

Then press `Enter`.

Meaning:

` :w ` = write/save the file

Command sequence:

```text
Esc
:w
Enter
```

## How to quit

First press `Esc`.

Then type `:q`.

Then press `Enter`.

Meaning:

` :q ` = quit

Command sequence:

```text
Esc
:q
Enter
```

## How to save and quit

First press `Esc`.

Then type `:wq`.

Then press `Enter`.

Meaning:

` :wq ` = write and quit

Command sequence:

```text
Esc
:wq
Enter
```

This is one of the most useful beginner commands.

## How to quit without saving

This is the emergency exit.

First press `Esc`.

Then type `:q!`.

Then press `Enter`.

Meaning:

` :q! ` = quit forcefully without saving

Command sequence:

```text
Esc
:q!
Enter
```

The `!` means force.

Use this when you made a mess and want to escape without saving.

Very useful. Very powerful. Handle like a pressure cooker whistle.

## Beginner rescue commands

Remember only these first:

| Command | Meaning |
|---|---|
| `Esc` | return to Normal mode |
| `i` | enter Insert mode |
| `:w` | save |
| `:q` | quit |
| `:wq` | save and quit |
| `:q!` | quit without saving |

That is enough for day one.

Do not try to learn everything at once.

## Basic movement

In Normal mode, you can move using arrow keys.

That is allowed.

The classic Vim movement keys are:

| Key | Direction |
|---|---|
| `h` | left |
| `j` | down |
| `k` | up |
| `l` | right |

At first, use arrow keys if needed.

No shame.

Later, slowly practice `h`, `j`, `k`, and `l`.

The old Vim masters may raise one eyebrow, but they will survive.

## Deleting text

In Normal mode, `x` deletes the character under the cursor.

To delete a full line, use `dd`.

Be careful. `dd` deletes the entire line.

If you delete something by mistake, press `u`.

That means undo.

## Undo and redo

In Normal mode, `u` means undo.

Redo is `Ctrl + r`.

Beginner version:

| Command | Meaning |
|---|---|
| `u` | undo |
| `Ctrl+r` | redo |

## Searching inside a file

First press `Esc`.

Then type `/searchword`.

Then press `Enter`.

Example:

```text
/linux
```

This searches for the word `linux`.

To jump to the next match, press `n`.

To jump to the previous match, press `N`.

## Built-in practice: Vim tutor

Vim has a built-in beginner tutorial called Vim tutor.

Try:

```powershell
vimtutor
```

For Neovim, try:

```powershell
nvim +Tutor
```

If it opens, follow the instructions slowly.

If it does not open on your system, do not worry. Continue with this guide first.

## Beginner practice mission

Open a test file:

```powershell
nvim practice.txt
```

Then do this:

1. Press `i`
2. Type three lines of text
3. Press `Esc`
4. Type `:w`
5. Press `Enter`
6. Move around using arrow keys
7. Press `i` again and add one more line
8. Press `Esc`
9. Type `:wq`
10. Press `Enter`

You have now created, edited, saved, and exited a file in Neovim.

That is a proper first victory.

## Common beginner panic situations

### I cannot type

You are probably in Normal mode.

Press `i`.

Now you can type.

### I cannot quit

Press `Esc`.

Then type `:q`.

Then press `Enter`.

### Vim says there are unsaved changes

Use `:wq` to save and quit.

Use `:q!` to quit without saving.

### I typed random commands and everything is weird

Press `Esc`.

Then type `:q!`.

Then press `Enter`.

Escape first. Escape always.

## What not to do on day one

Do not start with:

- huge plugin managers
- complicated themes
- copying random config files
- trying to build an IDE immediately
- installing 25 plugins before learning how to quit

First learn the editor.

Then slowly add power.

A boring setup that you understand is better than a fancy setup that controls you.

## Should a beginner learn Vim or Neovim?

Yes, but slowly.

Do not make Vim your full-time editor on day one.

Use it first for small files:

- notes
- config files
- practice text
- small scripts
- Markdown files

Once comfortable, use it more.

## Why learn Vim or Neovim?

Because it teaches you:

- keyboard confidence
- terminal confidence
- text editing discipline
- config file editing
- Linux server survival

On servers, you may not always have a graphical editor.

But Vim is often available.

Knowing how to open, edit, save, and quit a file is a genuine Linux survival skill.

## Final beginner rule

Do not memorize 100 commands.

Memorize this:

| Command | Meaning |
|---|---|
| `Esc` | return to Normal mode |
| `i` | enter Insert mode |
| `:w` | save |
| `:q` | quit |
| `:wq` | save and quit |
| `:q!` | quit without saving |

That is the beginner starter kit.

Everything else can come later.

And if nothing works, remember the sacred emergency exit:

```text
Esc
:q!
Enter
```

That is how you escape the Vim jungle alive.
