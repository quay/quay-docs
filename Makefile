
build:
	@docker run -it --rm --name asciidoctor --detach -v $(CURDIR):/documents/ asciidoctor/docker-asciidoctor
	@-docker exec -it asciidoctor bash -c "source build_docs"
	@docker kill asciidoctor

view:
	xdg-open file://$(CURDIR)/dist/welcome.html

all: build view

