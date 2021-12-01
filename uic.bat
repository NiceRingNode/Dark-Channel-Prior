echo off

pyuic5 -o ui_DeHazing.py .\DeHazing\DeHazing.ui

pyrcc5 .\DeHazing\res.qrc -o res_rc.py