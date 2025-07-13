# [lazyvim] Localhost configs

```diff
```diff
diff --git a/init.lua b/init.lua
index d62b291..4b94e92 100644
--- a/init.lua
+++ b/init.lua
@@ -3,3 +3,13 @@ _G.localhost = {}
 pcall(require, "localhost.pre")  -- For setting up the _G.localhost
 require("config.lazy")
 pcall(require, "localhost.post")
+
+vim.cmd([[
+  " filetype off
+  syntax off
+  set laststatus=0
+  colorscheme vscode
+  set nocursorline
+  set guicursor=a:blinkon0
+  set timeoutlen=1000
+]])
diff --git a/lua/plugins/init.lua b/lua/plugins/init.lua
index a1ef14f..21d6d69 100644
--- a/lua/plugins/init.lua
+++ b/lua/plugins/init.lua
@@ -358,6 +358,7 @@ return {
   {
     "lewis6991/gitsigns.nvim",
     opts = {
+      signcolumn = false,
       current_line_blame_opts = {
         delay = 0,
       },
@@ -540,6 +541,13 @@ return {
       plugins = {
           non_standalone = true,
       },
+      console = {
+        open_on_runcode = false,
+      },
+      description = {
+        position = "bottom",
+        width = "0%",
+      },
     },
   },
   {
@@ -937,4 +945,15 @@ return {
       { "<leader>tm", "<Plug>TableModeToggle", desc = "Toggle table mode" },
     },
   },
+  { "neovim/nvim-lspconfig", enabled = false },
+  { "Saghen/blink.cmp", enabled = false },
+  { "nvim-treesitter/nvim-treesitter", enabled = false },
+  { "nvim-treesitter/nvim-treesitter-textobjects", enabled = false },
+  { "nvim-lualine/lualine.nvim", enabled = false },
+  { "folke/snacks.nvim", opts = { words = { enabled = false } } },
+  { import = "lazyvim.plugins.extras.ai.copilot", enabled = false },
+  { import = "lazyvim.plugins.extras.ai.tabnine", enabled = false },
+  { "Mofiqul/vscode.nvim", cond = true },
+  { "folke/which-key.nvim", enabled = false },
+  { "echasnovski/mini.hipatterns", enabled = false },
 }
```

---

`./lua/localhost/pre.lua`

```lua
_G.localhost.OPENAI_API_KEY = "sk-xxxxx"
_G.localhost.OPENAI_API_URL = "https://api.siliconflow.cn/v1"
_G.localhost.OPENAI_MODEL = "moonshotai/Kimi-K2-Instruct"
_G.localhost.OPENAI_MODEL_EMBED = "Qwen/Qwen3-Embedding-0.6B"
```

---

`./lua/localhost/post.lua`

```lua
-- Ref: https://github.com/neovide/neovide/issues/2050#issuecomment-2571258610
if vim.g.neovide then
  vim.g.terminal_color_0 = "#45475a"
  vim.g.terminal_color_1 = "#f38ba8"
  vim.g.terminal_color_2 = "#a6e3a1"
  vim.g.terminal_color_3 = "#f9e2af"
  vim.g.terminal_color_4 = "#89b4fa"
  vim.g.terminal_color_5 = "#f5c2e7"
  vim.g.terminal_color_6 = "#94e2d5"
  vim.g.terminal_color_7 = "#bac2de"
  vim.g.terminal_color_8 = "#585b70"
  vim.g.terminal_color_9 = "#f38ba8"
  vim.g.terminal_color_10 = "#a6e3a1"
  vim.g.terminal_color_11 = "#f9e2af"
  vim.g.terminal_color_12 = "#89b4fa"
  vim.g.terminal_color_13 = "#f5c2e7"
  vim.g.terminal_color_14 = "#94e2d5"
  vim.g.terminal_color_15 = "#a6adc8"
end
```
