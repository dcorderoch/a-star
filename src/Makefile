ifeq ($(origin .RECIPEPREFIX), undefined)
  $(error This Make does not support .RECIPEPREFIX. Please use GNU Make 4.0 or later)
endif
.RECIPEPREFIX = >

all:
> mkdir -p GUI
> pyside2-uic UI/main.ui -o GUI/window.py

