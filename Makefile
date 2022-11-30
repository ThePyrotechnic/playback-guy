include make.env

.PHONY: clean playback_guy docker

Wheel=playback_guy-$(Version)-py3-none-any.whl

playback_guy: dist/$(Wheel)

dist/$(Wheel):

	VERSION=$(Version) python -m build
	pip install $@

docker: playback_guy
	sudo docker build . -t thepyrotechnic/playback-guy:$(Version) --build-arg VERSION=$(Version) --build-arg WHEEL=$(Wheel)

clean:
	-rm dist/*
	pip uninstall --yes playback_guy
