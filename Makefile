.PHONY: clean

DOCKER?=docker
NO_CACHE?=false

build: Dockerfile
	$(DOCKER) build --no-cache=$(NO_CACHE) -t taccsciapps/base .
	touch build

slim: build
	$(eval ID=$(shell $(DOCKER) run -d taccsciapps/base true))
	$(DOCKER) export $(ID) | docker import - taccsciapps/base
	$(DOCKER) rm -f $(ID)
	touch slim

push: build
	$(DOCKER) push taccsciapps/base
	touch push

clean:
	rm build slim push
