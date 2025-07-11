# [mac] Known issues & New features

## System Settings

- [ ] 通知显示超时时间设置
  - Ref: <https://www.cnblogs.com/itcomputer/p/6613230.html>
  - `defaults read com.apple.notificationcenterui bannerTime`
  - `defaults write com.apple.notificationcenterui bannerTime #` 在`#`里面设置秒数
  - `defaults delete com.apple.notificationcenterui bannerTime`
  - `killall NotificationCenter`
- [x] 多次空格会生成英文句号 (已经记录到installation中了)

## Aerospace & Sketchybar

- [x] 拼音 / ABC，内置输入法和搜狗输入法适配
- [x] 高版本aerospace，关闭window切换工作区切回的问题 (通过alias暂时规避)
- [x] 快捷键close功能的适配，避免直接kill进程
- [x] resize的问题，考虑关联enable norm问题

## Nvim

- [x] 全功能适配

## dotfiles

- [x] yazi无法显示当前目录下的文件/文件夹内容

## Hardwere

- [ ] trackpad: cmd + tap to click, sometimes not work: <https://github.com/lcomplete/hammerspoon_mbp14_tap_to_click_fix>
  - <https://www.hammerspoon.org/docs/hs.eventtap.html>
  - <https://www.hammerspoon.org/docs/hs.eventtap.event.html>
  - <https://www.hammerspoon.org/docs/hs.html#loadSpoon>
  - <https://github.com/Hammerspoon/Spoons/blob/master/Source/ForceTouchMapper.spoon/init.lua>
  - Add into .dotfiles
