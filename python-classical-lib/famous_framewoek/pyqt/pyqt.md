## PyQt5

[官方文档](https://www.riverbankcomputing.com/static/Docs/PyQt5/)
### install
`$: python3 -m pip install PyQt5`
`$: sudo apt-get install qt5-default qttools5-dev-tools`
>> not support python2

### open editor 
`$: designer`


### transform
`python3 -m PyQt5.uic.pyuic ~/xiaoao/untitled.ui -o ~/xiaoao/pyqt_ui.py`

### bugs
1. >> This application failed to start because no Qt platform plugin could be initialized. Reinstalling the application may fix this problem.
`sudo apt-get install libxkbcommon-x11-0`
you can see details by `export QT_DEBUG_PLUGINS=1`
2. 


### key notes
1. ![base](.//imgs/pyqt_1.png)
