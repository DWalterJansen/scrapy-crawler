run-crawler:  ## Inicia execução do crawler
	@cd desafio_xkcd/desafio_xkcd && scrapy crawl xkcd

help:  ## Mostra comandos disponíveis.
	@echo "Comandos disponíveis:"
	@echo
	@sed -n -E -e 's|^([a-z-]+):.+## (.+)|\1@\2|p' $(MAKEFILE_LIST) | column -s '@' -t