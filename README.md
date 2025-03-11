# MouseThing for [Bog](https://www.youtube.com/@bogxd)

This is a MacOS app for [Bog's video](https://www.youtube.com/watch?v=vlXdUU5pd_0). Hotkey is `cmd + shift + A`.

### Install

```zsh
python3 -m venv venv
source ./venv/bin/activate
pip install -r requirements.txt
```

## Run from command line

```zsh
python main.py
```

## Build .app

```zsh
pyinstaller --onefile --windowed --name MouseThing --icon icon.png --add-data "icon.png:." --osx-bundle-identifier com.seriousm4x.mouse-thing  main.py
```

The .app will be in `./dist/`. Next, do the following:

- Open system settings
- Open "Privacy & Security" / "Accessibility"
- Drag and drop the `MouseThing.app` into the list

Launch the app and give it a couple seconds. It will disappear and appear again. You will see the icon in your tray.

## Issues

When you've build the app again and the shortcut won't work anymore, you probably need to remove the app and re-add it to the accessibilities list.
