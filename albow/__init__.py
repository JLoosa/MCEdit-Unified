"""ALBOW - A Little Bit of Widgetry for PyGameby Gregory Ewinggreg.ewing@canterbury.ac.nz"""update_translation = False# Register unparented widgets in this to track them.unparented = {}from albow.controls import Label, Button, Image, AttrRef, ItemRef, \    RadioButton, ValueDisplay, SmallLabel, SmallValueDisplay, CheckBox, ValueButton, ButtonBasefrom albow.dialogs import alert, ask, input_text, input_text_buttonsfrom albow.extended_widgets import ChoiceButton, HotkeyColumn, MenuButton, CheckBoxLabel, FloatInputRow, IntInputRow, showProgress, TextInputRowfrom albow.fields import TextField, FloatField, IntField, TimeField, TextFieldWrapped, Fieldfrom albow.file_dialogs import \    request_old_filename, request_new_filename, look_for_file_or_directory# -# Remove the folowing line when file_opener.py is movedfrom albow.file_opener import FileOpenerfrom albow.grid_view import GridViewfrom albow.image_array import get_image_arrayfrom albow.layout import Row, Column, Grid, Framefrom albow.menu import Menufrom albow.palette_view import PaletteViewfrom albow.resource import get_font, get_imagefrom albow.screen import Screenfrom albow.scrollpanel import ScrollPanelfrom albow.shell import Shellfrom albow.tab_panel import TabPanelfrom albow.table_view import TableView, TableColumnfrom albow.text_screen import TextScreenfrom albow.tree import Treefrom albow.version import versionfrom albow.widget import Widget