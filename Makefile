.PHONY: build clean install

build:
	@./scripts/build.sh

clean:
	@rm -rf dist
	@echo "✓ Cleaned dist directory"

install: build
	@if [ ! -f "dist/qbobsidian.qbtheme" ]; then \
		echo "✗ Theme not built. Run 'make build' first."; \
		exit 1; \
	fi
	@echo "Installing theme..."
	@if [ "$$(uname)" = "Darwin" ]; then \
		mkdir -p "$$HOME/Library/Application Support/qBittorrent"; \
		cp dist/qbobsidian.qbtheme "$$HOME/Library/Application Support/qBittorrent/"; \
		echo "✓ Installed to: ~/Library/Application Support/qBittorrent/qbobsidian.qbtheme"; \
	elif [ "$$(uname)" = "Linux" ]; then \
		mkdir -p "$$HOME/.config/qBittorrent"; \
		cp dist/qbobsidian.qbtheme "$$HOME/.config/qBittorrent/"; \
		echo "✓ Installed to: ~/.config/qBittorrent/qbobsidian.qbtheme"; \
	else \
		echo "✗ Unsupported OS. Please copy dist/qbobsidian.qbtheme manually."; \
		exit 1; \
	fi
	@echo ""
	@echo "Next steps:"
	@echo "1. Open qBittorrent"
	@echo "2. Go to Tools → Options → Behavior"
	@echo "3. Enable 'Use custom UI Theme'"
	@echo "4. Select qbobsidian.qbtheme"
	@echo "5. Restart qBittorrent"
