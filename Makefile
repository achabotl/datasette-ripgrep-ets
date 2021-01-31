publish:
	datasette publish cloudrun --metadata metadata.yml \
		--static all:all \
		--install=https://github.com/simonw/datasette-ripgrep/archive/main.zip \
		--apt-get-install ripgrep \
		--service datasette-ripgrep-ets


.PHONY: publish
