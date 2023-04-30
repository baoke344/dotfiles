local opt = vim.opt  --for conciseness

--Line numbers
opt.relativenumber = true
opt.number = true

--tabs & indentation
opt.tabstop = 2
opt.shiftwidth = 2
opt.expandtab = true
opt.autoindent = true

--line wrapping
opt.wrap = false

--search
opt.ignorecase = true
opt.smartcase = true

--cursor line
opt.cursorline = true

--color
opt.termguicolors = true
opt.background = "dark"
opt.signcolumn = "yes"

--backspace
opt.backspace = "indent,eol,start"

--clipboard
opt.clipboard:append("unnamedplus")

--split window
opt.splitright = true
opt.splitbelow = true
--make word contain - become single word
opt.iskeyword:append("-")
