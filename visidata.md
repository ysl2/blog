# visidata

## Installation

```bash
brew install visidata
```

## Default keymaps

| sheet      | module | longname       | keystrokes | description                                                           |
| ---------- | ------ | -------------- | ---------- | --------------------------------------------------------------------- |
| BaseSheet  | help   | help-commands  | zCtrl+H    | list commands and keybindings available on current sheet              |
| BaseSheet  | sheets | quit-sheet     | q          | quit current sheet                                                    |
| TableSheet | layout | resize-col-max | \_         | toggle width of current column between full and default width         |
| TableSheet | search | search-col     | /          | search for regex forwards in current column                           |
| TableSheet | sheets | type-int       | #          | set type of current column to int                                     |
| TableSheet | sort   | sort-asc       | [          | sort ascending by current column; replace any existing sort criteria  |
| TableSheet | sort   | sort-desc      | ]          | sort descending by current column; replace any existing sort criteri… |
