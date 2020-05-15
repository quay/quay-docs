
build:
	@podman run -it --rm --name asciidoctor --detach -v $(CURDIR):/documents/:z asciidoctor/docker-asciidoctor
	@-podman exec -it asciidoctor bash -c "source build_docs"
	@podman kill asciidoctor

view:
	xdg-open file://$(CURDIR)/dist/welcome.html

all: build view

