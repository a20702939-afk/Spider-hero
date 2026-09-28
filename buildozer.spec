[app]
android.accept_sdk_license = True
title = MANCH
package.name = manch
package.domain = org.amirreza

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,wav,ogg,ttf

version = 1.0

requirements = python3,pygame

orientation = portrait

fullscreen = 1

android.permissions = INTERNET

android.api = 35
android.minapi = 23

android.archs = arm64-v8a

[buildozer]

log_level = 2
warn_on_root = 1
