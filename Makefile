include make.env

.PHONY: clean playback_guy

playback_guy: dist/playback_guy-$(Version)-py3-none-any.whl

dist/playback_guy-$(Version)-py3-none-any.whl:

	VERSION=$(Version) python -m build
	pip install $@

clean:
	-rm dist/*
	pip uninstall --yes playback_guy
